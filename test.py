def setUp(self):
        self.handler = BaseHandler()
        self.handler.runSpec = {"baselineDetails": {"viewName": "TestView"}}
        self.handler.store = MagicMock()

    @patch('TableauRegressionConfigManager')
    def test_run(self, MockTableauRegressionConfigManager):
        mock_taskobj = MagicMock()
        MockTableauRegressionConfigManager.return_value = mock_taskobj
        mock_zipped_data = MagicMock()
        mock_taskobj.download_view.return_value = mock_zipped_data

        self.handler.run()

        mock_taskobj.download_view.assert_called_once_with(self.handler.runSpec["baselineDetails"])
        self.handler.store.persistObject.assert_called_once_with(mock_zipped_data, 'TestView.zip', skipValidation=True)