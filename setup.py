from distutils.core import setup
setup(
  name = 'pyVerilog',
  packages = ['pyVerilog'],
  version = '0.1',
  description = 'Python Random Graph Generator',
  long_description='''Python Verilog File Parser''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/pyVerilog',
  download_url = 'https://github.com/sepandhaghighi/pyrgg/tarball/v0.1',
  keywords = ['random', 'graph', 'python3','python','generator',"graph-process","generator",
              "moduland","DIMACS","JSON","YAML","Pickle","CSV","WEL","ASP","TGF","UCINET",
              ],
  install_requires=[
      'pyyaml',
	  'codecov',
      ],
  classifiers = [],
  license='MIT',
)
