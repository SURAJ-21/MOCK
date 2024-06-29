class TestTableauSignInHeader(unittest.TestCase):
    @patch('path.to.your.module.TableauRegressionShell.getConfig', {'signin_header': 'expected_signin_header'})
    def test_get_signin_header(self, mock_getConfig):
        obj = TableauRegressionShell()  # Replace with the actual class name
        
        signin_header = obj.get_signin_header()
        
        self.assertEqual(signin_header, 'expected_signin_header')