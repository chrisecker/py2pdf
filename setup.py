#from distutils.core
from setuptools import setup


with open('README') as file:
    readme = file.read()

    
setup(name='py2pdf',
      version='0.1.2',
      description='Python source to pdf conversion library.',
      long_description=readme,
      author='C. Ecker',
      author_email='textmodelview@gmail.com',
      url='https://github.com/chrisecker/py2pdf',
      python_requires="<3.0",
      license='BSD',
      py_modules = ['py2pdf'],
      platforms = ['any'],
     )
