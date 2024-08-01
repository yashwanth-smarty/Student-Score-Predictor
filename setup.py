from setuptools import find_packages, setup
from typing import List

END='-e .'

def get_req(file_path:str)->List[str]:
    reqs=[]
    with open(file_path) as fp:
        reqs=fp.readlines()
        reqs=[req.replace("\n","") for req in reqs]

        if END in reqs:
            reqs.remove(END)
    
    return reqs

setup(
    name='etemlproject',
    version='0.0.1',
    author='Yashwanth',
    author_email='kumaryashwanth198@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)