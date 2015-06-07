========
TAGsieve
========

TAGsieve is a small HTML/XML stripper GUI application, written in Python and based on the HTML sanitizer .. _bleach: https://github.com/jsocol/bleach. It strips or batch strips tags from .html, .htm, or .xml files, ignoring specified tags and attributes via whitelists.

## Basic use
TAGsieve is a simple GUI application, so usage should be fairly straightforward. However, in order to avoid some errors, some simple rules should be followed.

 files can be specified based on their extension. 'Clean HTML' will only clean .html/.htm files and 'Clean XML' does the according job.	
It is possible to clean both a single file and a complete directory of files, based on the path information.

Both tag and attribute whitelist should be entered according to a couple of rules.
The tag whitelist must be a comma-separated list:

.. code-block:: python
	x₁,..., xₙ

The attribute whitelist must be entered according to the following pattern:

.. code-block:: python
	x₁:[a₁,..., aₙ,]/.../xₙ:[a₁,..., aₙ,] for each tag x₁-xₙ and attributes a₁-aₙ.


Installation
============
Via 'dist' folder
-----------------
Installation is not required. Save the 'dist' folder to your computer, open the folder location, and double click the TAGsieve executable.

A dist folder has been build for Linux. Other platforms will be supported soon.

Via source code
---------------
If the executable does not work, try installing the prerequisites on your machine and subsequently call the program.

1) Have Python and pip installed on your machine.
2) Install the requirements via pip:

	.. code-block:: python
		$ pip install -r requirements.txt

	Or install BeautifulSoup and bleach via pip:

	.. code-block:: python
		$ pip install beautifulsoup4
		$ pip install bleach

3) Install PyQt:

	.. code-block:: python
		$ apt-get install pyqt4

The program can then be called by opening TAGsieve/ and executing TAGsieve.pyw or via terminal:

.. code-block:: python
	$ cd path/to/TAGsieve/ && ./TAGsieve.pyw
