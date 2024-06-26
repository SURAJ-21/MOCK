class TestMyClass(unittest.TestCase):
    @patch('requests.get')
    @patch.object(MyClass, 'sign_in_token', return_value='dummy_token')
    @patch.object(MyClass, 'request_header', return_value={'Authorization': 'Bearer dummy_token'})
    def test_get_request(self, mock_request_header, mock_sign_in_token, mock_get):
        instance = MyClass()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        page_number = 1
        response = instance.get_request(page_number)

        self.assertEqual(response.status_code, 200)
        mock_sign_in_token.assert_called_once()
        mock_request_header.assert_called_once_with('dummy_token')
        mock_get.assert_called_once_with(
            url=f'{instance.baseUrl}/sites/{instance.siteId}/views?fields=_all_&includeUsageStatistics=True&pageNumber={page_number}&pageSize={instance.getConfig("MAX_PAGE_SIZE")}',
            headers={'Authorization': 'Bearer dummy_token'},
            verify=False
        )