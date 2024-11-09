from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' 
    this function will return the list o requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
           
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Yash Shivankar',
    author_email='yashshivankar1998@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    # there are many time we need to install 100 of libraries in that case we cannot write all here, 
    # so for that we create one function with name get_requirement and in that function we pass requirements.txt file as paramater
)