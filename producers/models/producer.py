"""Producer base-class providing common utilities and functionality"""
import logging
import time

from confluent_kafka.admin import AdminClient, NewTopic

logger = logging.getLogger(__name__)


def topic_exists(client, topic_name):
    """Checks if the given topic exists"""
    topic_metadata = client.list_topics(timeout=5)
    return topic_name in set(t.topic for t in iter(topic_metadata.topics.values()))


def create_topic(client, topic_name):
    """Creates the topic with the given topic name"""
    futures = client.create_topics(
        [
            NewTopic(
                topic=topic_name,
                num_partitions=10,
                replication_factor=1,
                config={
                    "cleanup.policy": "delete",
                    "compression.type": "lz4",
                    "delete.retention.ms": "2000",
                    "file.delete.delay.ms": "2000",
                },
            )
        ]
    )

    for topic, future in futures.items():
        try:
            future.result()
            print("topic created")
        except Exception as e:
            print(f"failed to create topic {topic_name}: {e}")


def time_millis():
    return int(round(time.time() * 1000))


class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
            self,
            topic_name,
            key_schema,
            value_schema=None,
            num_partitions=1,
            num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        #
        #
        # TODO: Configure the broker properties below. Make sure to reference the project README
        # and use the Host URL for Kafka and Schema Registry!
        #
        #
        self.broker_properties = {
            "bootstrap.servers": "PLAINTEXT://localhost:9092"
            # TODO
            # TODO
            # TODO
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # TODO: Configure the AvroProducer
        # self.producer = AvroProducer(
        # )

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        client = AdminClient(self.broker_properties)
        exists = topic_exists(client, self.topic_name)
        logger.info(f"Topic {self.topic_name} exists: {exists}")
        if exists is False:
            create_topic(client, self.topic_name)
        else:
            logger.info(f"Topic {self.topic_name} already exists")
        #
        #
        # TODO: Write code that creates the topic for this producer if it does not already exist on
        # the Kafka Broker.
        #
        #

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        logger.info("producer close ")
        Producer.existing_topics.discard(self.topic_name)
        #
        #
        # TODO: Write cleanup code for the Producer here
        #
        #

    @property
    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
