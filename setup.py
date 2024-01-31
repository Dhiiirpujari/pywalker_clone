from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in library_department/__init__.py
from library_department import __version__ as version

setup(
	name="library_department",
	version=version,
	description="librabry management system",
	author="NEW INDIA",
	author_email="new.india@lib.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
