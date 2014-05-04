from distutils.core import setup

with open('README.rst') as readme:
  long_description = readme.read()

setup(name="git-pm",
      version="0.1.0",
      description="Git Project Management",
      long_description=long_description,
      author="Josh Lindsey",
      author_email="joshua.s.lindsey@gmail.com",
      url="https://github.com/jlindsey/git-pm",
      provides=["gitpm"],
      packages=[
        "gitpm.flask",
        "gitpm.core",
        "gitpm.users",
        "gitpm.issues",
        "gitpm.pull_requests",
        "gitpm.wiki",
        ],
      requires=[
        "pycrypto (>=2.6.1)",
        "argh (>=0.24.1)",
        "gitpython (>=0.1.7)",
        "markdown (>=2.4)",
        "flask (>=0.10.1)",
        ],
      package_dir={'gitpm': 'lib'},
      scripts=["bin/gitpm"],
)
