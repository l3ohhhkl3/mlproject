from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path)->List[str]:
    '''
    This function will return the list of requirements

    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Vishal',
    author_email='vishalpachpande831@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    )
