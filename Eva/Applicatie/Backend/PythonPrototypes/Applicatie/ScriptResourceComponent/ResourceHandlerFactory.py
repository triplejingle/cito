from ResourceHandlerGithub import ResourceHandlerGithub


class ResourceHandlerFactory(object):
    @staticmethod
    def get_resource_handler(file_extension):
        if file_extension == "git":
            return ResourceHandlerGithub()
        else:
            raise ValueError(format)
