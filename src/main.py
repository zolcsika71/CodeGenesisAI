"""
This is the main file to run the Project Creator.   
"""
from project_creator import ProjectCreator


def main():
    """
    This is the main function to run the Project Creator.   
    :return: 
    """
    print("1. Create a project")
    print("2. Change a project")
    print("3. Delete a project")
    print("4. Exit")
    action = input("Select an option: ")

    if action == '1':
        creator = options(
            "Enter the project name: ",
            "Enter the Python version: ",
            "Enter the necessary modules (comma separated): ",
        )
        creator.create_project()
    elif action == '2':
        creator = options(
            "Enter the project name: ",
            "Enter the Python version: ",
            "Enter the necessary modules (comma separated): ",
        )
        creator.change_project()
    elif action == '3':
        creator = options(
            "Enter the project name: ",
            "Enter the Python version: ",
            "Enter the necessary modules (comma separated): ",
        )
        creator.delete_project()
    elif action == '4':
        return
    else:
        print("Invalid option. Please select from 1 to 4.")


def options(arg0, arg1, arg2):
    """
    :param arg0:
    :param arg1:
    :param arg2:
    :return:
    """
    project_name = input(arg0)
    python_version = input(arg1)
    modules = input(arg2).split(',')
    return ProjectCreator(project_name, python_version, modules)


if __name__ == "__main__":
    main()
