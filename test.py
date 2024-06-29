class TestTableauServerPassword(unittest.TestCase):
    @patch('lib.epv.get_credential')
    def test_get_password_success(self, mock_get_credential):
        # Arrange
        mock_get_credential.return_value.Password.return_value = 'correct_password'
        
        obj = TableauRegressionShell()
        obj._env = 'test_env'
        obj.userName = 'test_user'
        
        # Act
        password = obj.get_password()
        
        # Assert
        mock_get_credential.assert_called_once_with(f'/idanywhere/{obj._env}/{obj.userName}')
        self.assertEquals(password, 'correct_password')
        
    @patch('lib.epv.get_credential')
    def test_get_password_failure(self, mock_get_credential):
        # Arrange
        mock_get_credential.side_effect = Exception('Credential Error')
        
        obj = TableauRegressionShell()
        obj._env = 'test_env'
        obj.userName = 'test_user'
        
        # Act
        password = obj.get_password()
        
        # Assert
        mock_get_credential.assert_called_once_with(f'/idanywhere/{obj._env}/{obj.userName}')
        self.assertEquals(password, "s6ry6UezhnoS9V4U")