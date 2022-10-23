import ntpath

from PDF import PDF


class Controller:

    file_to_path_dict = {}

    def __init__(self):
        self.pdf = PDF()

    def addFiles(self, path_list):
        """
        Add files to local dictionary and split them into simple name an path

        Args:
            path_list (list): A list of paths to the selected files

        Returns:
            set(): A list of file names
        """
        simple_file_name_list = []

        for path in path_list:
            simple_file_name = ntpath.basename(path)
            simple_file_name_list.append(simple_file_name)
            self.file_to_path_dict[simple_file_name] = path

        return set(simple_file_name_list)

    """
    call pdf to set merge requested files
    """

    def mergeFiles(self, files_to_merge, path):
        paths_of_files = []
        for file in files_to_merge:
            paths_of_files.append(self.file_to_path_dict.get(file))

        self.pdf.merge(paths_of_files, path)
