class Constants:
    # station_topic_name = "com.chicago.transport.arrival.stations."
    # turnstiles_topic_name = "com.chicago.transport.station.turnstiles"
    #
    # station_faust_out_topic_name = "org.chicago.cta.stations.table.v1"
    # station_faust_out_table_name = "com.cta.faust.stntbl"

    TRAIN_ARRIVAL_TOPIC_PREFIX = "org.chicago.cta.station.arrivals.t001"
    STATION_TURNSTILE_TOPIC_PREFIX = "com.cta.stations.turnstile.entry"
    STATION_TURNSTILE_SUMMARY = "TURNSTILE_SUMMARY"
    STATION_TRANSFORMED_TOPIC = "org.chicago.cta.stations.table.v1t001"
    STATION_DATA_TOPIC_PREFIX = "com.cta.stations.data.rawt001."
    FAUST_STATION_TRANSFORMED_TABLE_NAME = "com.cta.faust.stntbl"

    weather_topic_name = "org.chicago.cta.weather.v1"
    num_partitions = 2
    num_replicas = 1
    KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
    KAFKA_CONNECTOR_NAME = "stations"
    rest_proxy_url = "http://localhost:8082/"
    bootstrap_server = "localhost:9092"
    schema_registry_url = "http://localhost:8081"
    consumer_group_id = "com.chicago.transport.consumer.group.1"
