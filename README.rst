========
TAGsieve
========

TAGsieve is a small HTML/XML stripper GUI application, written in Python and based on the HTML sanitizer bleach_. It strips or batch strips tags from .html, .htm, or .xml files, ignoring specified tags and attributes via whitelists.

Basic use
=========
TAGsieve is a simple GUI application that strips tags of a single file or a directory of files.

.. image:: tagsieveim.png
	:height: 300
	:width: 300
	:align: center

It follows bleach_ and works with tag and attribute whitelists: these tags and attributes will not be stripped. The tag whitelist must be a comma-separated list:

.. code-block:: python

	x₁,..., xₙ

The attribute whitelist must be entered according to the following pattern::

	x₁:[a₁,..., aₙ,]/.../xₙ:[a₁,..., aₙ,] for each tag x₁-xₙ and attributes a₁-aₙ.

Installation
============
Via 'dist' folder
-----------------
Installation is not required. Save the 'dist' folder to your computer, open the folder location, and double click the TAGsieve executable.

A dist folder has been build for Linux. Other platforms will be supported soon.

Via source code
---------------
If the executable does not work, try installing the prerequisites on your machine and subsequently install TAGsieve by running::

	$ python setup.py install

TAGsieve works with PyQt, so only installing the prerequisites may not be enough. Install PyQt by running::

	$ apt-get install pyqt4

Do not hesitate to contact me on any issues involving the use and installation of the application.

.. _bleach: https://github.com/jsocol/bleach
