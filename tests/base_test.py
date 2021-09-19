import unittest
import pytest

from src.utils.log import logger

@pytest.mark.usefixtures("setup_environment")
class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        logger.info("Start each test case")

    def tearDown(self) -> None:
        logger.info("End each test case")
