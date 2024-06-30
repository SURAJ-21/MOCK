 @patch('path.to.your.module.TableauRegressionShell.set_inventory')
    @patch('path.to.your.module.TableauRegressionShell._openDbTransaction')
    @patch('path.to.your.module.getTableauConfig')
    def test_update_inventory(self, mock_getTableauConfig, mock_openDbTransaction, mock_set_inventory):
        mock_getTableauConfig.return_value.get.return_value = 'test_table'
        mock_session = MagicMock()
        mock_openDbTransaction.return_value.__enter__.return_value = mock_session

        obj = TableauRegressionShell()
        obj._env = 'test_env'
        obj.update_inventory()

        mock_getTableauConfig.assert_called_once_with('test_env')
        mock_openDbTransaction.assert_called_once()
        mock_session.execute.assert_called_once_with(text("TRUNCATE TABLE test_table"))
        mock_set_inventory.assert_called_once()