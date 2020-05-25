from unittest import TestCase

from Applicatie.UsecaseControllers.VisualizeVariablesController import VisualizeVariablesController
from Tool.Test.Excel_Library import Excel


class TestController(TestCase):
    base_path = "./sources/"

    def test_filter(self):
        criteria = "[{\"name\":\"Plaats\",\"variables\":[\"Apeldoorn\",\"Arnhem\"]},{\"name\":\"Niveau\",\"variables\":[\"HBO\"]}]"

        excel = Excel()
        file_name = "test_filter_criteria.xlsx"
        excel.create_document(self.base_path + file_name)
        excel.add_worksheet()
        niveaus = ["Plaats", "School", "Niveau", "Leerling", "Score", "Label", "Response"]
        data = [
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Arnhem", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Nijmegen", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Doetinchem", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."]
        ]
        test = [niveaus]
        for x in range(0, 200):
            for rowset in data:
                test.append(rowset)
        excel.add_data_to_document(test)
        excel.save_document()
        controller = VisualizeVariablesController()

        controller.load(self.base_path + file_name)

        expectedResult = {'Plaats': ['Apeldoorn', 'Arnhem', 'Nijmegen', 'Doetinchem'], 'School': ['HAN'],
                          'Niveau': ['HBO'], 'Leerling': ['563631'], 'Score': ['15'], 'Label': ['test1'], 'Response': [
                'Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis.']}
        criteriaResult = controller.get_criteria()
        self.assertEqual(expectedResult, criteriaResult)
        print(controller.filter(criteria))

    def test_filter_criteria(self):
        excel = Excel()
        file_name = "test_filter_criteria.xlsx"
        excel.create_document(self.base_path + file_name)
        excel.add_worksheet()
        niveaus = ["Plaats", "School", "Niveau", "Leerling", "Score", "Label", "Response"]
        data = [
            ["Apeldoorn", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Arnhem", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Nijmegen", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Amsterdam", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."],
            ["Zutphen", "HAN", "HBO", "563631", "15", "test1",
             "Litora fringilla turpis hymenaeos tempor interdum pede dapibus ac, dui magna fermentum Habitasse ad sed justo enim placerat sagittis per sagittis in sed adipiscing proin diam duis facilisi adipiscing varius dignissim eu fringilla porta tempor. Pellentesque lorem convallis.Condimentum mus ultrices nostra quis ut commodo diam integer nibh hac. Sociosqu egestas nisl aliquam purus nisl mattis laoreet massa venenatis. Fringilla nisi elementum vehicula. Iaculis sem laoreet lacinia. Interdum Nec augue et aliquam euismod massa hac praesent, mus nec maecenas sollicitudin ante leo metus imperdiet semper vehicula fames interdum sociosqu pretium sit. Duis mi parturient, dignissim platea arcu magnis quis mattis."]
        ]
        test = [niveaus]
        for x in range(0, 200):
            for rowset in data:
                test.append(rowset)
        excel.add_data_to_document(test)
        excel.save_document()
        controller = VisualizeVariablesController()

        controller.load(self.base_path + file_name)

        controller.get_criteria()

    def runTest(self):
        self.test_filter()
        self.test_filter_criteria()
