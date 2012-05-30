from setuptools import setup

setup(name='python-filetype',
      description='Expansion of python-magic for certain types and extensions',
      author='Mike Jensen',
      author_email='jjensen.mike@gmail.com',
      url='https://github.com/jjensenmike/python-filetype',
      version='0.1',
      py_modules=['filetype'],
      license='PSF',
      install_requires=["python-magic >= 0.4.1"],
      )
