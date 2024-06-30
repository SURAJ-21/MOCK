mock_session = MagicMock()
        mock_openDbTransaction.return_value.__enter__.return_value = mock_session
        
        mock_inventory = MagicMock()
        mock_inventory.actor = 'owner'
        mock_inventory.workbookName = 'workbook'
        mock_inventory.viewName = 'view'
        mock_inventory.baselineTaskId = 'task_id'
        mock_inventory.baselineParams = 'params'
        
        mock_session.query.return_value.all.return_value = [mock_inventory]

        obj = TableauRegressionShell()
        result = obj.get_regression_config()

        expected_result = [{
            'owner': 'owner',
            'workbookName': 'workbook',
            'viewName': 'view',
            'baseline TaskId': 'task_id',
            'params': 'params'
        }]
        
        self.assertEqual(result, expected_result)

        mock_openDbTransaction.assert_called_once()
        mock_session.query.assert_called_once_with(TableauRegressionConfig)
        mock_session.query.return_value.all.assert_called_once()