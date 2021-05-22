"""Defines trends calculations for stations"""
import logging
from dataclasses import dataclass

import faust


logger = logging.getLogger(__name__)


# Faust will ingest records from Kafka in this format
class Station(faust.Record):
    stop_id: int
    direction_id: str
    stop_name: str
    station_name: str
    station_descriptive_name: str
    station_id: int
    order: int
    red: bool
    blue: bool
    green: bool


# Faust will produce records to Kafka in this format
@dataclass
class TransformedStation(faust.Record):
    station_id: int
    station_name: str
    order: int
    line: str


# TODO: Define a Faust Stream that ingests data from the Kafka Connect stations topic and
#   places it into a new topic with only the necessary information.
app = faust.App("stations-stream", broker="kafka://localhost:9092", store="memory://")
# TODO: Define the input Kafka Topic. Hint: What topic did Kafka Connect output to?
topic = app.topic("com.cta.stations.data.1.stations", value_type=Station)
# TODO: Define the output Kafka Topic
out_topic = app.topic("org.udacity.chicago.cta.stations.table.1", partitions=1, value_type=TransformedStation)
# TODO: Define a Faust Table
#table = app.Table(
#    # "TODO",
#    # default=TODO,
#    partitions=1,
#    changelog_topic=out_topic,
#)
table = app.Table(
   "com.udacity.faust.station.table.1",
   default=TransformedStation,
   partitions=1,
   changelog_topic=out_topic,
   value_type=TransformedStation
)


#
#
# TODO: Using Faust, transform input `Station` records into `TransformedStation` records. Note that
# "line" is the color of the station. So if the `Station` record has the field `red` set to true,
# then you would set the `line` of the `TransformedStation` record to the string `"red"`
#
#

@app.agent(topic)
async def transform_stations(in_stations):
    async for sn in in_stations:

        t = TransformedStation(sn.station_id, sn.station_name, sn.order, "na")
        if sn.red:
            t.line = "red"
        elif sn.blue:
            t.line = "blue"
        elif sn.green:
            t.line = "green"
        else:
            continue

        table[sn.station_id] = t


if __name__ == "__main__":
    app.main()
