import os


def get_resource_path(resource_file_name):
    """
    Used to safely get the full path of resource by its name
    :param resource_file_name:
    :return: abs path of the resource file (str)
    """
    abs_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(abs_path, resource_file_name)


