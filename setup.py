"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['haxe.py']
DATA_FILES = []
OPTIONS = dict(
#	iconfile="path/to/my/icon/my_icon_file.icns",
 includes=["importlib",
#  			"string",
#  			"argparse"
#               'PyQt5',
#               'numpy',
#               'sys',
#               'os',
		'construct'
              'time'],


)

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
