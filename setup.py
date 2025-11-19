# setup.py is responsible for creating my ML application as a package. 
# With the help of setup.py I will be able to build my entire ML application as a package and even deploy in pypi.

from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #inside this requirement.txt when we go to the next line there will be "\n" that will get added, whenever we try to use readlines that \n will also get recorded over there
                                                                    # read the object in requirements.txt and replace the \n by blank
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
setup(
name='mlproject',
version='0.0.1',
author='Ramith',
author_email='ramithpesala123@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')



)