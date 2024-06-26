@patch.object(TSC.TableauDataExtractor, 'get_signin_info')
@patch.object(TSC.TableauDataExtractor, 'dashboard_analysis')
@patch.object(TSC.TableauDataExtractor, 'setOptions')
# @patch.object(TSC, 'pd')
@patch.object(TSC.logging, 'exception')
def test_download_baseline(self, MockLoggingException, MockPandas, MockSetOptions, MockDashboardAnalysis, MockGetSigninInfo):
    MockGetSigninInfo.return_value = None
    MockDashboardAnalysis.return_value = None
    mock_csv_data = 'test,csv,data\n'
    MockSetOptions.return_value = mock_csv_data
    MockPandas.read_csv.return_value = pd.DataFrame()
    self.instance.tableau_server = MagicMock()
    self.instance.tableau_auth = MagicMock()
    self.instance.tableau_server.auth.sign_in.return_value = None
    self.instance.version = '2023.1'
    result = self.instance.download_baseline({'viewId': 'view123'})
    MockGetSigninInfo.assert_called_once()
    MockDashboardAnalysis.assert_called_once_with(self.baselineDetails)
    self.instance.tableau_server.auth.sign_in.assert_called_once_with(self.instance.tableau_auth)
    MockSetOptions.assert_called_once_with(self.baselineDetails['viewId'])
    MockPandas.read_csv.assert_called_once_with(data_io.StringIO(mock_csv_data))
    self.assertEqual(result, mock_df)
    MockLoggingException.assert_not_called()