@patch('io.BytesIO')
    @patch('zipfile.ZipFile')
    def test_convert_and_create_zip(self, mock_zipfile, mock_bytesio):
        instance = TableauDataExtractor()
        viewDf = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        viewName = 'test_view'
        mock_io_instance = MagicMock()
        mock_bytesio.return_value = mock_io_instance
        mock_zipfile_instance = MagicMock()
        mock_zipfile.return_value.__enter__.return_value = mock_zipfile_instance
        mock_csv_string = "col1,col2\n1,3\n2,4\n"
        viewDf.to_csv = MagicMock(return_value=mock_csv_string)
        data = instance.convert_and_create_zip(viewDf, viewName)
        viewDf.to_csv.assert_called_once()
        mock_zipfile_instance.writestr.assert_called_once_with(f"{viewName.strip()}.csv", mock_csv_string)
        mock_io_instance.getvalue.assert_called_once()
        mock_io_instance.close.assert_called_once()