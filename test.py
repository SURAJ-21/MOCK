def setUp(self):
        self.handler = RegressionServiceHandler()
        self.handler._paramsDict = {
            'dashboardParams': ['param1', 'param2', 'param3'],
            'env': 'test_env',
            'SID': 'test_sid'
        }
        self.handler.env = 'test_env'

    @patch('your_module.RegressionServiceHandler.sendResponse')
    @patch('your_module.RegressionServiceHandler.setRegression')
    @patch('your_module.run')
    @patch('your_module.RegressionServiceHandler.tableauRegressionConfigurer')
    @patch('your_module.RegressionServiceHandler.tableau')
    def test_configRegression(self, mock_tableau, mock_tableauRegressionConfigurer, mock_run, mock_setRegression, mock_sendResponse):
        # Setup the tableau mock
        mock_tableau._dict_ = {
            '_sa_instance_state': 'state',
            'other_key': 'other_value'
        }
        baseline_details = mock_tableau._dict_
        baseline_details.pop('_sa_instance_state')

        # Setup the return values for the mock methods
        mock_run.return_value.taskId = 'test_task_id'
        mock_run.return_value.getOutputs.return_value = [['', {'uri': 'test_uri'}]]
        mock_setRegression.return_value = 'regression_result'
        
        self.handler.configRegression()

        # Assertions
        mock_run.assert_called_once_with(
            {'other_key': 'other_value', 'dashboardParams': ['param1', 'param2', 'param3']},
            'test_env',
            'test_env',
            unittest.mock.ANY,  # We can't predict the exact time value
            unittest.mock.ANY   # We can't predict the exact date value
        )
        self.assertEqual(self.handler.baselineTaskId, 'test_task_id')
        self.assertEqual(self.handler.baselineEnv, 'test_env')

        mock_setRegression.assert_called_once_with({'other_key': 'other_value', 'dashboardParams': ['param1', 'param2', 'param3']})
        self.assertEqual(self.handler._paramsDict['actor'], 'test_sid')

        mock_tableauRegressionConfigurer.regressionconfig_table_insert.assert_called_once_with(
            'test_task_id', 
            {'other_key': 'other_value', 'dashboardParams': ['param1', 'param2', 'param3']},
            'test_env'
        )
        mock_sendResponse.assert_called_once_with('test_uri')