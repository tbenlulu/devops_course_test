from setuptools import setup, find_packages
from portscan import __version__
 
requires = ['argparse', 'socket']
dist = setup(
 name='scanner',
 version=__version__,
 description="A system for controlling process state under UNIX",
 author="Chris McDonough",
 author_email="chrism@plope.com",
 packages=find_packages(),
 include_package_data=True,
 zip_safe=False,
 test_suite="supervisor.tests",
 entry_points={
     'console_scripts': [
         'scanner = portscan.portscan:main'
     ],
 },
)
