# TAGsieve

## What is TAGsieve?
TAGsieve is a small HTML/XML stripper GUI application, written in Python and based on the HTML sanitizer [bleach](https://github.com/jsocol/bleach). It strips or batch strips tags from .html, .htm, or .xml files, ignoring specified tags and attributes via whitelists.

## Basic use
TAGsieve is a simple GUI application, so usage should be fairly straightforward. However, in order to avoid some errors, some simple rules should be followed.

 files can be specified based on their extension. 'Clean HTML' will only clean .html/.htm files and 'Clean XML' does the according job.	
It is possible to clean both a single file and a complete directory of files, based on the path information.

Both tag and attribute whitelist should be entered according to a couple of rules.
The tag whitelist must be a comma-separated list:
'''
x₁,..., xₙ
'''
The attribute whitelist must be entered according to the following pattern:
'''
x₁:[a₁,..., aₙ,]/.../xₙ:[a₁,..., aₙ,] for each tag x₁-xₙ and attributes a₁-aₙ.
'''

## Installation
###Via 'dist' folder
Installation is not required. Save the 'dist' folder to your computer, open the folder location, and double click the TAGsieve executable.

*Note:* Up until now, the executable has only been tested for Ubuntu 14.04.

###Via source code 
If the executable does not work, try installing the prerequisites on your machine and subsequently call the program.

1. Have Python and pip installed on your machine.
2. Install BeautifulSoup and bleach via pip:
	'''
	$ pip install beautifulsoup4
	$ pip install bleach
	'''
3. Install PyQt:
	'''
	$ apt-get install pyqt4
	'''

The program can then be called by opening TAGsieve/ and executing TAGsieve.pyw or via terminal:
'''
$ cd path/to/TAGsieve/ && ./TAGsieve.pyw
'''
