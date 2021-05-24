station_topic_name = "com.chicago.cta.arrival.stations"
station_faust_out_topic_name = "org.chicago.cta.stations.table.out"
station_faust_out_table_name = "com.chicago.cta.stations.faust.out"

num_partitions = 2
num_replicas = 1
turnstiles_topic_name = "com.chicago.train.turnstiles"
weather_topic_name = "com.udacity.transport.weather"
KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
KAFKA_CONNECTOR_NAME = "stations"
rest_proxy_url = "http://localhost:8082"
bootstrap_server = "localhost:9092"

KSQL_URL = "http://localhost:8088"