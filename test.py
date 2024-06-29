class TestTableauRegressionShell(unittest.TestCase):
    @patch('TableauRegressionShell.TableauRegressionConfigManager')
    @patch('TableauRegressionShell.CalculatorShell.store')
    def test_run(self, mock_store, MockTableauRegressionConfigManager):
        mock_taskobj = MockTableauRegressionConfigManager.return_value
        mock_taskobj.download_view.return_value = b'fake_zipped_data'
        
        baseline_details = {'viewName': 'test_view'}
        run_spec = {'baselineDetails': baseline_details}
        
        shell = TableauRegressionShell()
        shell.runSpec = run_spec
        
        shell.run()
        
        MockTableauRegressionConfigManager.assert_called_once()
        mock_taskobj.download_view.assert_called_once_with(baseline_details)
        mock_store.persistObject.assert_called_once_with(b'fake_zipped_data', filename='test_view.zip', skipValidation=True)