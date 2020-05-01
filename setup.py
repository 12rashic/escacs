import os

from setuptools import setup

_dir = os.path.dirname(os.path.realpath(__file__))

with open("VERSION", "r") as f:
    VERSION = f.read().strip("\n")

setup(
    name="escacs",
    version=VERSION,
    description="Fun with chess",
    long_description_content_type="text/markdown",
    long_description=open(os.path.join(_dir, "README.md")).read(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/lferran/escacs",
    license="GNU General Public License V3",
    author="Ferran Llamas",
    author_email="llamas.arroniz@gmail.com",
    keywords=[],
    zip_safe=True,
    include_package_data=True,
    packages=["escacs"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
)
