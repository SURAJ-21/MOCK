def setUp(self):
        self.baselineDetails = MagicMock()
        self.baselineDetails.workbookName = "Workbook Name"
        self.baselineDetails.viewName = "View Name"
        self.instance = YourClass()

        self.instance.baselineTaskId = "123"
        self.instance._paramsDict = {"SID": "456"}
        self.instance.env = "test_env"
        self.instance.get_current_user = MagicMock(return_value="test_user")
        self.instance.postBaselineBatch = MagicMock()

        self.patcher = patch('path.to.YourClass.getConfig')
        self.MockGetConfig = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_setRegression(self):
        self.MockGetConfig.side_effect = lambda key: f"test_{key}"
        
        result = self.instance.setRegression(self.baselineDetails)

        self.instance.postBaselineBatch.assert_called_once_with({
            "batchId": "123",
            "testName": "F_Test__456__Workbook-Name__View-Name",
            "baselineEnv": "test_env",
            "owner": "test_user",
            "teamOwnerAddress": "test_teamOwnerAddress",
            "escalationOwner": "test_escalationOwner",
        })
        self.assertEqual(result, self.instance.postBaselineBatch.return_value)