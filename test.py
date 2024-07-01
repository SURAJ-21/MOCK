def setUp(self):
        self.handler = RegressionServiceHandler()
        self.handler._paramsDict = {
            'some_key': 'some_value'
        }
        
        # Mock objects
        self.obj_write = MagicMock()
        self.obj_finish = MagicMock()
        self.obj_set_status = MagicMock()
        
        # Patch methods with mock objects
        patch('your_module.RegressionServiceHandler.write', self.obj_write).start()
        patch('your_module.RegressionServiceHandler.finish', self.obj_finish).start()
        patch('your_module.RegressionServiceHandler.set_status', self.obj_set_status).start()
        
        # Add cleanup to stop patching
        self.addCleanup(patch.stopall)

    @patch('your_module.RegressionServiceHandler.removeRegressionConfig')
    @patch('your_module.queryRegressionConfigTable')
    def test_deleteRegression_baseline_configured(self, mock_queryTable, mock_removeConfig):
        # Mock is_baseline_configured to return a non-None value
        mock_config_row = MagicMock()
        mock_config_row.baselineTaskId = 'test_task_id'
        mock_config_row.env = 'test_env'
        mock_queryTable.is_baseline_configured.return_value = mock_config_row

        # Mock removeRegressionConfig to return a response
        mock_removeConfig.return_value = 'test_response'

        self.handler.deleteRegression()

        # Assertions
        mock_queryTable.is_baseline_configured.assert_called_once_with(self.handler._paramsDict)
        mock_removeConfig.assert_called_once_with('test_task_id')
        mock_queryTable.deleteBaseline.assert_called_once_with('test_task_id', 'test_env')
        self.obj_set_status.assert_called_once_with(200)
        self.obj_write.assert_called_once_with('test_response')
        self.obj_finish.assert_called_once()
