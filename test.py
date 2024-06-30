@patch('path.to.your.module.TableauRegressionShell._openDbTransaction')
    def test_get_workbook_inventory(self, mock_openDbTransaction):
        mock_session = MagicMock()
        mock_openDbTransaction.return_value.__enter__.return_value = mock_session
        
        mock_query_result = [
            MagicMock(actor='actor1', ownerName='owner1', workbookName='workbook1', viewName='view1'),
            MagicMock(actor='actor2', ownerName='owner2', workbookName='workbook2', viewName='view2')
        ]
        
        mock_session.query.return_value.filter.return_value.all.return_value = mock_query_result

        obj = TableauRegressionShell()
        inventoryDetailDict = {'SID': 'test_sid'}
        result = obj.get_workbook_inventory(inventoryDetailDict)

        expected_result = [
            {'owner': 'actor1', 'ownerName': 'owner1', 'workbookName': 'workbook1', 'viewName': 'view1'},
            {'owner': 'actor2', 'ownerName': 'owner2', 'workbookName': 'workbook2', 'viewName': 'view2'}
        ]
        
        self.assertEqual(result, expected_result)
        mock_openDbTransaction.assert_called_once()
        mock_session.query.assert_called_once_with(TableauDashboardInventoryAll)
        mock_session.query.return_value.filter.assert_called_once_with(TableauDashboardInventoryAll.actor == 'test_sid')
        mock_session.query.return_value.filter.return_value.all.assert_called_once()