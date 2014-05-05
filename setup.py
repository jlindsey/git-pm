from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as readme:
    LONG_DESCRIPTION = readme.read()

setup(name="git-pm",
      version="0.1.0",
      description="Git Project Management",
      long_description=LONG_DESCRIPTION,
      author="Josh Lindsey",
      author_email="joshua.s.lindsey@gmail.com",
      url="https://github.com/jlindsey/git-pm",
      license="MIT",
      provides=["gitpm"],
      packages=find_packages(),
      namespace_packages=["gitpm"],
      entry_points={
          'console_scripts': [
              'gitpm = gitpm.core.command:run',
              ]
          },
      install_requires=[
          "pycrypto >=2.6.1",
          "argh >=0.24.1",
          "gitpython >=0.1.7",
          "markdown >=2.4",
          "flask >=0.10.1",
          ],
      )

