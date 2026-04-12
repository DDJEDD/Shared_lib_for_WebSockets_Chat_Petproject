from setuptools import setup, find_packages


setup(name="petproject_shared",
      version="1.1.4",
      packages=find_packages(),
      install_requires=["PyJWT","sqlalchemy", "redis" ],
      python_requires=">=3.12")