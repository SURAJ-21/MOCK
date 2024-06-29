def test_get_auth_token(self):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {'credentials': {'token': 'expected_token'}}
        
        obj = TableauRegressionShell()  # Replace with the actual class name
        
        # Act
        token = obj.get_auth_token(mock_response)
        
        # Assert
        mock_response.json.assert_called_once()
        self.assertEquals(token, 'expected_token')