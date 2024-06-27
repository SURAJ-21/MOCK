@patch.object(TSC.TableauDataExtractor, 'get_signin_info')
    @patch.object(TSC.TableauDataExtractor, 'dashboard_analysis')
    @patch.object(TSC.TableauDataExtractor, 'setOptions')
    @patch('io.StringIO')
    @patch.object(TSC, 'pd')
    @patch.object(TSC.logging, 'exception')
    def test_download_baseline(self, MockLoggingException, MockPandas, MockStringIO, MockSetOptions, MockDashboardAnalysis, MockGetSigninInfo):
        MockGetSigninInfo.return_value = None
        MockDashboardAnalysis.return_value = None
        mock_csv_data = 'test,csv,data\n'
        MockSetOptions.return_value = mock_csv_data
        
        mock_df = MagicMock(spec=pd.DataFrame)
        MockPandas.read_csv.return_value = mock_df
        
        self.instance.tableau_server = MagicMock()
        self.instance.tableau_auth = MagicMock()
        self.instance.tableau_server.auth.sign_in.return_value = None
        self.instance.version = '2023.1'
        
        result = self.instance.download_baseline(self.baselineDetails)
        
        MockGetSigninInfo.assert_called_once()
        MockDashboardAnalysis.assert_called_once_with(self.baselineDetails)
        self.instance.tableau_server.auth.sign_in.assert_called_once_with(self.instance.tableau_auth)
        MockSetOptions.assert_called_once_with(self.baselineDetails['viewId'])
        MockStringIO.assert_called_once_with(mock_csv_data)
        MockPandas.read_csv.assert_called_once_with(MockStringIO(mock_csv_data))
        self.assertEqual(result, mock_df)
        MockLoggingException.assert_not_called()