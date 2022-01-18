from setuptools import setup


setup(
    name="rubiks_cube_check",
    version="1.0.0",
    description="Resolve rubiks cube RGB values to the six cube colors",
    keywords="rubik's cube check",
    url="https://github.com/lidacity/rubiks-cube-check",
    author="lidacity",
    author_email="dzmitry@lidacity.by",
    license="GPLv3",
    scripts=["usr/bin/example.py"],
    packages=["rubiks_cube_check"],
)
