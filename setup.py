from distutils.core import setup
setup(
  name = 'Verilog',
  packages = ['Verilog'],
  version = '0.1',
  description = 'Python Verilog File Parser',
  long_description='''Python Verilog File Parser''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/Verilog',
  download_url = 'https://github.com/sepandhaghighi/Verilog/tarball/v0.1',
  keywords = ["Verilog","python","HDL","ISCAS","script","parser","simulation"],
  install_requires=[
      'art',
	  'codecov',
      ],
  classifiers = [],
  license='MIT',
)
