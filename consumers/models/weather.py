"""Contains functionality related to Weather"""
import logging
import constants



logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        if constants.Constants.weather_topic_name in message.topic():
            self.temperature = message.value["temperature"]
            self.status = message.value["status"]
        else:
            logger.warning("Some error with weather topic")

