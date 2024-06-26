@patch.object(MyClass, 'get_request')
    def test_get_all_views(self, mock_get_request):
        instance = MyClass()
        mock_response_1 = MagicMock()
        mock_response_1.json.return_value = {
            'views': {'view': [{'id': 1}, {'id': 2}]},
            'pagination': {'totalAvailable': 4}
        }
        mock_response_2 = MagicMock()
        mock_response_2.json.return_value = {
            'views': {'view': [{'id': 3}, {'id': 4}]},
            'pagination': {'totalAvailable': 4}
        }
        mock_get_request.side_effect = [mock_response_1, mock_response_2]

        total_views = instance.get_all_views()

        self.assertEqual(len(total_views), 4)
        self.assertEqual(total_views, [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}])
        self.assertEqual(mock_get_request.call_count, 2)
        mock_get_request.assert_any_call(1)
        mock_get_request.assert_any_call(2)
