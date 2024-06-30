@patch('path.to.your.module.TableauDataExtractor')
    @patch('path.to.your.module.TableauDashboardInventoryAllDAO')
    @patch('path.to.your.module.TableauRegressionShell._openDbTransaction')
    def test_set_inventory(self, mock_openDbTransaction, mock_TableauDashboardInventoryAllDAO, mock_TableauDataExtractor):
        # Arrange
        mock_dataObj = MagicMock()
        mock_dataObj.get_all_views.return_value = [
            {
                'owner': {'name': 'John Doe', 'fullName': 'Johnathan Doe', 'id': 'user-123', 'siteRole': 'Admin'},
                'workbook': {'id': 'workbook-456', 'name': 'Sales Report'},
                'id': 'view-789',
                'name': 'Quarterly Sales',
                'project': {'id': 'project-101'},
                'ownerEmail': 'john.doe@example.com'
            }
        ]
        mock_TableauDataExtractor.return_value = mock_dataObj
        
        mock_DAO = MagicMock()
        mock_TableauDashboardInventoryAllDAO.return_value = mock_DAO
        
        mock_session = MagicMock()
        mock_openDbTransaction.return_value.__enter__.return_value = mock_session
        
        obj = TableauRegressionShell()  # Replace with the actual class name
        
        # Act
        obj.set_inventory()
        
        # Assert
        mock_TableauDataExtractor.assert_called_once()
        mock_dataObj.get_all_views.assert_called_once()
        
        mock_TableauDashboardInventoryAllDAO.assert_called_once()
        mock_DAO.build.assert_called_once_with({
            'actor': 'John Doe',
            'ownerName': 'Johnathan Doe',
            'ownerId': 'user-123',
            'ownerSiteRole': 'Admin',
            'workbookId': 'workbook-456',
            'workbookName': 'Sales Report',
            'viewId': 'view-789',
            'viewName': 'Quarterly Sales',
            'projectId': 'project-101',
            'ownerEmail': 'john.doe@example.com'
        })
        
        mock_session.add.assert_called_once()
        mock_openDbTransaction.return_value.__enter__.assert_called_once()
        mock_openDbTransaction.return_value.__exit__.assert_called_once()