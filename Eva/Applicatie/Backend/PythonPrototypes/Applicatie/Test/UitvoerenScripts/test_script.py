from unittest import TestCase

from Script import Script


class TestScript(TestCase):

    def test_getTotalRows(self):
        data = self.getData()
        script = Script()
        expectedResult = 1
        result = script.get_total_rows(data)

        self.assertEqual(expectedResult, result)

    def test_getEigenschap(self):
        data = self.getData()
        script = Script()
        expectedResult="Tokenize.py"

        result = script.get_property_from_data(data)

        self.assertEqual(expectedResult, result)

    def test_getFileExtension(self):
        data = self.getData()
        script = Script()
        expectedResult = "py"

        result = script.get_file_extension(data)

        self.assertEqual(expectedResult, result)

    def getData(self):
        return "{\"Totalrows\":1,\"PropertyExtractionScript\":\"Tokenize.py\",\"Data\":{\"row\":{\"Label\":[\"test1\"],\"Leerling\":[\"563631\"],\"Niveau\":[\"HBO\"],\"Plaats\":[\"Apeldoorn\"],\"Response\":[\"Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis.\"],\"School\":[\"HAN\"],\"Score\":[\"15\"]}}}"
    def runTest(self):
        self.test_getEigenschap()
        self.test_getFileExtension()
        self.test_getTotalRows()
