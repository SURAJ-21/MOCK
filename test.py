@patch('TSC.TableauAuth')
    @patch('TSC.Server')
    def test_get_signin_info(self, mock_server, mock_tableau_auth):
        instance = TableauDataExtractor()
        instance.userName = 'username'
        instance.get_password = MagicMock(return_value='password')
        instance.siteUrl = 'siteUrl'
        instance.server = 'server'
        instance.get_signin_info()
        mock_tableau_auth.assert_called_once_with('username', 'password', 'siteUrl')
        mock_server.assert_called_once_with('server')