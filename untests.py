import re
from Class_for_bot import Bot
import unittest


class TestBot(unittest.TestCase):

    def test_get_the_weather(self):
        self.assertTrue(re.search("^The minimum .* day!$", Bot().get_the_weather()))

    def test_get_the_weather_from_api(self):
        self.assertTrue(re.search("^Current .*°.$", Bot().get_the_weather_from_api()))


if __name__ == '__main__':
    unittest.main()

