"""
    This class is responsible for creating/change/deleting a project folder
"""


class ProjectCreator:
    """
    This class is responsible for creating/change/deleting a project folder
    """
    def __init__(self, project_name, python_version, modules):
        self.project_name = project_name
        self.python_version = python_version
        self.modules = modules

    def create_folder(self):
        """Creates the project folder one level up"""
        try:
            os.mkdir(os.path.join("..", self.project_name))
        except FileExistsError as err:
            print(f"Folder {self.project_name} already exists in the parent directory.")

    def create_project(self):
        """
        This method creates a new project folder with the given name and installs the required modules.
        :return: If the project generated successfully, true is returned, else false.
        """
        """Creates a new project folder with the given name and installs the required modules."""
        print(f"Creating project {self.project_name}...")
        self.create_folder()  # Call the new method
        print(f"Project name: {self.project_name}")
        print(f"Python version: {self.python_version}")
        print(f"Modules: {self.modules}")

    def change_project(self):
        """
        This method changes the project modules.
         :return: If the project modules changed successfully, true is returned, else false.
        """
        # Logic to change the project goes here
        print("Changing project...")
        print(f"Modules: {self.modules}")

    def delete_project(self):
        """
        This method deletes the project folder.
        """
        # Logic to delete the project goes here
        print("Deleting project...")
        print(f"Project name: {self.project_name}")
