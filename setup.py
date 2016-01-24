from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "C:\\Users\mattf\Desktop\Personal\slic3rToXYZ\slic3rToXYZ.py"}],
    zipfile = None,
)