from setuptools import setup, find_namespace_packages

setup(name='lori',
      packages=find_namespace_packages(include=["lori", "lori.*"]),
      version='0.0.1',
      install_requires=[
            "tensorboard",
            "einops",
            "timm",
            "matplotlib",
            ]
      )
