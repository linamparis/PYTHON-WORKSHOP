from setuptools import find_packages, setup


def read_file(file_name):
   with open(file_name, 'r') as f:
      return f.read()


def read_requirements(file_name):
   return read_file(file_name).splitlines()


setup(
   name='school api',
   version='1.0.0',
   description='Something different',
   author='lparis',
   author_email='linamparis@gmail.com',
   packages_dir={"": "."},
   packages=find_packages(where="."),
   install_requires=read_requirements('requirements.txt')
)