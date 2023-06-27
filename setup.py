from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in e_invoice/__init__.py
from e_invoice import __version__ as version

setup(
	name="e_invoice",
	version=version,
	description="Electronic Invocie For Tax Auth",
	author="Beshoy Atef",
	author_email="beshoyatef31@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
