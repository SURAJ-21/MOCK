@patch.object(TSC, 'CSVRequestOptions')
def test_setOptions(self, MockCSVRequestOptions):
    mock_csv_data = b'test,csv,data\n'
    mock_view = MagicMock()
    mock_view.csv = [mock_csv_data]
    
    # Mocking self.instance.tableau_server.get_by_id
    self.instance.tableau_server = MagicMock()
    self.instance.tableau_server.get_by_id.return_value = mock_view
    
    mock_options_instance = MagicMock()
    MockCSVRequestOptions.return_value = mock_options_instance
    
    self.instance.setOptions(self.viewId)
    
    # Assertions
    self.instance.tableau_server.get_by_id.assert_called_once_with(self.viewId.strip())
    self.assertEqual(self.instance.tableau_server.views.populate_csv.call_count, 1)
    self.assertEqual(MockCSVRequestOptions.call_count, 1)