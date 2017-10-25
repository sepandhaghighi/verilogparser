from distutils.core import setup
setup(
  name = 'verilog',
  packages = ['verilog'],
  version = '0.1',
  description = 'Python Verilog File Parser',
  long_description='''Python Verilog File Parser''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/verilog',
  download_url = 'https://github.com/sepandhaghighi/verilog/tarball/v0.1',
  keywords = ["Verilog","python","HDL","ISCAS","script","parser","simulation"],
  install_requires=[
      'art',
	  'codecov',
      ],
  classifiers = [],
  license='MIT',
)
