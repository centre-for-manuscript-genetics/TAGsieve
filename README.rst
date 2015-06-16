========
TAGsieve
========

TAGsieve is a small HTML/XML stripper GUI application, written in Python and based on the HTML sanitizer bleach_. It strips or batch strips tags from .html, .htm, or .xml files, ignoring specified tags and attributes through whitelisting.

Basic use
=========
TAGsieve is a simple GUI application that strips tags of a single file or a directory of files.

.. image:: tagsievegui.png
	:height: 200
	:width: 200
	:scale: 50%

It follows bleach_ and works with tag and attribute whitelists: these tags and attributes will not be stripped. Click the "Clean" button to clean a file or directory of files.

Installation
============
Install Python on your machine, using the Anaconda_ distribution. This includes the PyQt package needed for the GUI.

After installing the distribution, check if PyQt is there::

	$ conda install pyqt

Then run::

	$ pip install TAGsieve

This should install the requirements used for TAGsieve. Start the program in terminal by running::

	$ python -m TAGsieve

.. _bleach: https://github.com/jsocol/bleach
.. _Anaconda: http://continuum.io/downloads
