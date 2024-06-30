@patch('path.to.your.module.TableauRegressionShell._openDbTransaction')
    def test_is_baseline_configured(self, mock_openDbTransaction):
        mock_session = MagicMock()
        mock_openDbTransaction.return_value.__enter__.return_value = mock_session
        
        mock_query_result = MagicMock()
        mock_session.query.return_value.filter.return_value.one_or_none.return_value = mock_query_result

        obj = TableauRegressionShell()
        paramsDict = {
            'SID': 'test_sid',
            'workbookName': 'test_workbook',
            'viewName': 'test_view',
            'env': 'test_env'
        }
        result = obj.is_baseline_configured(paramsDict)

        self.assertEqual(result, mock_query_result)
        mock_openDbTransaction.assert_called_once()
        mock_session.query.assert_called_once_with(TableauRegressionConfig)

        expected_filters = and_(
            func.trim(TableauRegressionConfig.actor) == paramsDict.get('SID').strip(),
            func.trim(TableauRegressionConfig.workbookName) == paramsDict.get('workbookName').strip(),
            func.trim(TableauRegressionConfig.viewName) == paramsDict.get('viewName').strip(),
            func.trim(TableauRegressionConfig.env) == paramsDict.get('env').strip()
        )

        mock_session.query.return_value.filter.assert_called_once_with(expected_filters)
        mock_session.query.return_value.filter.return_value.one_or_none.assert_called_once()