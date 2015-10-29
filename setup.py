import glob
from distutils.core import setup

# get all of the scripts
scripts = glob.glob("bin/*")

setup(
  name='docx2txt',
  packages=['docx2txt'],
  version='0.3',
  description='A pure python-based utility to extract text from docx files.',
  author='Ankush Shah',
  author_email='ankush.shah.nitk@gmail.com',
  url='https://github.com/ankushshah89/python-docx2txt',
  download_url='https://github.com/ankushshah89/python-docx2txt/tarball/0.3',
  keywords=['python', 'docx', 'text'],
  scripts=scripts,
  classifiers=[],
)