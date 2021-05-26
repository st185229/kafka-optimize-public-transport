class Constants:
    station_topic_name = "com.chicago.transport.arrival.stations."
    station_faust_out_topic_name = "org.chicago.transport.stations.table.out"
    station_faust_out_table_name = "com.chicago.transport.stations.faust.out"
    num_partitions = 2
    num_replicas = 1
    turnstiles_topic_name = "com.chicago.transport.station.turnstiles"
    weather_topic_name = "com.chicago.transport.weather"
    KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
    KAFKA_CONNECTOR_NAME = "stations"
    rest_proxy_url = "http://localhost:8082/"
    bootstrap_server = "localhost:9092"
    KSQL_URL = "http://ksql:8088"
    schema_registry_url = "http://localhost:8081"
    consumer_group_id = "com.chicago.transport.consumer.group.1"
    turnstile_summary_topic = "turnstile_summary"
