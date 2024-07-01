import unittest
from unittest.mock import Mock
from your_module import TableauHandler

class TestTableauHandler(unittest.TestCase):
    def setUp(self):
        self.handler = TableauHandler()
        self.handler.request = Mock()
        self.handler.request.path = "/path/to/getInventory"
        self.handler.getInventory = Mock(return_value="inventory_result")
        self.handler.getRegressionConfig = Mock(return_value="regression_config_result")
    
    def test_get_inventory(self):
        result = self.handler.get()
        self.assertEqual(result, "inventory_result")
        self.assertEqual(self.handler.getInventory.call_count, 1)
    
    def test_get_regression_config(self):
        self.handler.request.path = "/path/to/getRegressionConfig"
        result = self.handler.get()
        self.assertEqual(result, "regression_config_result")
        self.assertEqual(self.handler.getRegressionConfig.call_count, 1)