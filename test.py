def setUp(self):
        self.serviceName = MagicMock()
        self.reportType = 'reportType'
        self.handler = BaseHandler()
    
    @patch('BaseHandler.getEnvConfig')
    def test_initialize(self, MockGetEnvConfig):
        mock_env = MagicMock()
        self.serviceName._env = mock_env
        mock_wcap_config = MagicMock()
        MockGetEnvConfig.return_value = mock_wcap_config
        
        self.handler.initialize(self.serviceName, self.reportType)
        
        self.assertEqual(self.handler.regressionService, self.serviceName)
        self.assertEqual(self.handler.reportType, self.reportType)
        self.assertEqual(self.handler.entitlementsService, self.serviceName.getEntitlementsService())
        self.assertEqual(self.handler._env, mock_env)
        self.assertEqual(self.handler._wcapConfig, mock_wcap_config)
        self.assertEqual(MockGetEnvConfig.call_count, 1)