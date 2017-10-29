from distutils.core import setup
setup(
  name = 'verilogparser',
  packages = ['verilogparser'],
  version = '0.1',
  description = 'Python Verilog File Parser',
  long_description='''Python Verilog File Parser''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/verilogparser',
  download_url = 'https://github.com/sepandhaghighi/verilogparser/tarball/v0.1',
  keywords = ["Verilog","python","HDL","ISCAS","script","parser","simulation"],
  install_requires=[
      'art',
	  'codecov',
      ],
  classifiers = [],
  license='MIT',
)
