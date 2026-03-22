'''
The setup.py file is an essential part of any Python project. It is used to specify the metadata and dependencies of the project, making it easier for others to install and use the package. The setup.py file typically includes information such as the package name, version, author, description, and a list of required dependencies.
'''


from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    # this function return list of requirements from the requirements.txt file
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()
            # process each line 
            for line in lines:
                # remove leading and trailing whitespace
                requirement = line.strip()
                # ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("Requirements file not found. Please ensure that requirements.txt is present in the same directory as setup.py.")
    return requirement_lst
# print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Iti singh',
    description='A package for network security analysis and tools.',
    packages=find_packages(),
    install_requires=get_requirements()
)