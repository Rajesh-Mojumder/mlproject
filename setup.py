from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from a file.
    It strips newlines and removes '-e .' so install_requires works.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # remove whitespace and newline characters
        requirements = [req.strip() for req in requirements]
        # remove '-e .' if present
        requirements = [req for req in requirements if req != HYPEN_E_DOT]

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author="Rajesh Mojumder",
    author_email="rajesh.mojumder@g.bracu.ac.bd",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)