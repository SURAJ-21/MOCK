@patch.object(tableau_api_lib.TSC, 'TableauAuth')
@patch.object(tableau_api_lib.TSC, 'Server')
def test_get_signin_info(self, MockServer, MockAuth):
    mock_auth = MagicMock()
    MockAuth.return_value = mock_auth
    mock_server = MagicMock()
    MockServer.return_value = mock_server
    
    self.instance.get_signin_info()
    
    MockAuth.assert_called_once_with(self.userName, self.instance.get_password(), self.siteUrl)
    MockServer.assert_called_once()
    
    # Additional verification: Check the arguments passed to Server
    actual_server_args, _ = mock_server.call_args
    self.assertEqual(actual_server_args[0], self.server)