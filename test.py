self.handler.get_query_argument = MagicMock(side_effect=lambda x, y: f"value_of_{x}")

        expectedParams = ['param1', 'param2']
        self.handler.readParams(expectedParams)

        self.handler.get_query_argument.assert_any_call('param1', '')
        self.handler.get_query_argument.assert_any_call('param2', '')
        self.assertEqual(self.handler.param1, 'value_of_param1')
        self.assertEqual(self.handler.param2, 'value_of_param2')