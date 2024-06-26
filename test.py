@patch.object(TSC.Server, 'views')
@patch.object(TSC.Server, 'get_by_id')
@patch.object(TSC, 'CSVRequestOptions')
def test_setOptions(self, MockCSVRequestOptions, MockGetById, MockViews):
    mock_csv_data = b'test,csv,data\n'
    mock_view = MagicMock()
    instance = TSC()
    mock_view.csv = [mock_csv_data]
    MockGetById.return_value = mock_view
    mock_options_instance = MagicMock()
    MockCSVRequestOptions.return_value = mock_options_instance
    instance.setOptions("view123")
    self.assertEqual(MockGetById.call_count, 1)
    self.assertEqual(MockViews.populate_csv.call_count, 1)
    self.assertEqual(MockCSVRequestOptions.call_count, 1)