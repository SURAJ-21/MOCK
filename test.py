@patch('path.to.your.module.TableauRegressionShell._openDbTransaction')
    def test_delete_baseline(self, mock_openDbTransaction):
        mock_session = MagicMock()
        mock_openDbTransaction.return_value.__enter__.return_value = mock_session
        
        mock_query_result = MagicMock()
        mock_session.query.return_value.filter.return_value.one_or_none.return_value = mock_query_result

        obj = TableauRegressionShell()
        batchId = 'test_batch_id'
        env = 'test_env'
        obj.deleteBaseline(batchId, env)

        mock_openDbTransaction.assert_called_once()
        mock_session.query.assert_called_once_with(TableauRegressionConfig)

        expected_filters = and_(
            func.trim(TableauRegressionConfig.baselineTaskId) == batchId.strip(),
            func.trim(TableauRegressionConfig.env) == env.strip()
        )

        mock_session.query.return_value.filter.assert_called_once_with(expected_filters)
        mock_session.query.return_value.filter.return_value.one_or_none.assert_called_once()
        mock_session.delete.assert_called_once_with(mock_query_result)