def setUp(self):
        self.handler = RegressionServiceHandler()
        self.handler.readParams = MagicMock()
        self.handler.request = MagicMock()
        self.handler.request.path = "/some/path/getInventory"
        self.handler.getInventory = MagicMock(return_value="inventory_result")
        self.handler.getRegressionConfig = MagicMock(return_value="regression_config_result")

    @patch('your_module.RegressionServiceHandler.getInventory')
    @patch('your_module.RegressionServiceHandler.getRegressionConfig')
    def test_get_inventory(self, mock_get_regression_config, mock_get_inventory):
        self.handler.request.path = "/some/path/getInventory"
        result = self.handler.get()
        mock_get_inventory.assert_called_once()
        mock_get_regression_config.assert_not_called()
        self.assertEqual(result, "inventory_result")

    @patch('your_module.RegressionServiceHandler.getInventory')
    @patch('your_module.RegressionServiceHandler.getRegressionConfig')
    def test_get_regression_config(self, mock_get_regression_config, mock_get_inventory):
        self.handler.request.path = "/some/path/getRegressionConfig"
        result = self.handler.get()
        mock_get_inventory.assert_not_called()
        mock_get_regression_config.assert_called_once()
        self.assertEqual(result, "regression_config_result")