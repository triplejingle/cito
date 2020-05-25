from Reader import ExcelReader


class ReaderFactory(object):
    @staticmethod
    def get_file_reader(file_extension):
        if file_extension == "xlsx":
            return ExcelReader()
        else:
            raise ValueError(format)
