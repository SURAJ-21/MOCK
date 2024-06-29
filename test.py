@patch('path.to.your.module.TableauRegressionShell.get_auth_token')
    @patch('path.to.your.module.TableauRegressionShell.get_credentials')
    @patch('path.to.your.module.TableauRegressionShell.get_signin_header')
    @patch('path.to.your.module.requests.post')
    def test_sign_in_token(self, mock_post, mock_get_signin_header, mock_get_credentials, mock_get_auth_token):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {'credentials': {'token': 'expected_token'}}
        mock_post.return_value = mock_response
        mock_get_signin_header.return_value = {'header_key': 'header_value'}
        mock_get_credentials.return_value = {'username': 'test_user', 'password': 'test_pass'}
        mock_get_auth_token.return_value = 'expected_token'
        
        obj = TableauRegressionShell()  # Replace with the actual class name
        obj.baseUrl = 'http://example.com'
        
        # Act
        token = obj.sign_in_token()
        
        # Assert
        mock_post.assert_called_once_with(
            url='http://example.com/auth/signin',
            headers={'header_key': 'header_value'},
            verify=False,
            json={'username': 'test_user', 'password': 'test_pass'}
        )
        mock_get_signin_header.assert_called_once()
        mock_get_credentials.assert_called_once()
        mock_get_auth_token.assert_called_once_with(mock_response)
        self.assertEqual(token, 'expected_token')