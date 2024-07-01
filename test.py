def setUp(self):
        self.instance = TableauRegressionShell()
        self.instance._paramsDict = {'dashboardParams': ['param1', 'param2', 'param3']}
        self.instance.tableauRegressionConfigurer = MagicMock()
        self.instance.setResponse = MagicMock()

    def test_downloadBatchAnalysisView_success(self):
        baselineDetails = {'viewName': 'TestView', '_sa_instance_state': 'to_remove'}
        expected_baselineDetails = {
            'viewName': 'TestView',
            'dashboardParams': ['param1', 'param2', 'param3'],
            'dashboardType': 'BatchAnalysis'
        }
        
        self.instance.tableauRegressionConfigurer.is_view_in_inventory.return_value = baselineDetails
        self.instance.tableauRegressionConfigurer.download_view.return_value = 'zippedFile'

        self.instance.downloadBatchAnalysisView()

        self.assertEqual(self.instance.tableauRegressionConfigurer.is_view_in_inventory.call_count, 1)
        self.assertEqual(self.instance.tableauRegressionConfigurer.download_view.call_count, 1)
        self.instance.tableauRegressionConfigurer.download_view.assert_called_with(expected_baselineDetails)
        self.assertEqual(self.instance.setResponse.call_count, 1)
        self.instance.setResponse.assert_called_with('zippedFile')

    def test_downloadBatchAnalysisView_invalid_params(self):
        self.instance._paramsDict = {'dashboardParams': ['param1', 'param2']}

        with self.assertRaises(Exception) as context:
            self.instance.downloadBatchAnalysisView()
        self.assertEqual(str(context.exception), "Item in the dashBoardParams has to be of length 3. Received: ['param1', 'param2']")

if __name__ == '__main__':
    unittest.main()