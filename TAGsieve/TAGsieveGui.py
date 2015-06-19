#!/usr/bin/env python

import sys, os, glob, re
from PyQt4 import QtCore, QtGui
from CleanDirtySoup import CleanDirtySoup

__version__ = "0.2.0"

class StripUi(QtGui.QDialog):
	'''
	Class for the TAGsieve GUI.
	'''
	def __init__(self, parent=None):
		super(StripUi, self).__init__(parent)

		df_label = QtGui.QLabel('Enter path to file or directory:')
		self.dirty_file = QtGui.QLineEdit('')

		self.htmlcheck = QtGui.QCheckBox('Clean HTML')
		self.htmlcheck.toggle()
		self.xmlcheck = QtGui.QCheckBox('Clean XML')

		at_label = QtGui.QLabel('Enter allowed tags (comma separated):')
		self.allowed_tags = QtGui.QLineEdit('a, div')
		aa_label = QtGui.QLabel('Enter allowed attributes (slash "/" separated):')
		self.allowed_attrs = QtGui.QLineEdit('a:[href, target,]/*:[class,]')
		as_label = QtGui.QLabel('Enter allowed styles (comma separated):')
		self.allowed_styles = QtGui.QLineEdit('')

		self.browser = QtGui.QTextBrowser()
		self.browser.setFixedSize(QtCore.QSize(500,100))

		self.scbutton = QtGui.QPushButton('Clean')

		layout = QtGui.QVBoxLayout()
		layout.addWidget(df_label)
		layout.addWidget(self.dirty_file)
		layout.addWidget(self.htmlcheck)
		layout.addWidget(self.xmlcheck)
		layout.addWidget(at_label)	
		layout.addWidget(self.allowed_tags)
		layout.addWidget(aa_label)
		layout.addWidget(self.allowed_attrs)
		layout.addWidget(as_label)
		layout.addWidget(self.allowed_styles)
		layout.addWidget(self.scbutton)
		layout.addWidget(self.browser)

		self.setLayout(layout)
		self.dirty_file.setFocus()

		self.connect(self.scbutton, QtCore.SIGNAL('clicked()'), self.clean_path)

		self.setWindowTitle('TAGsieve v'+__version__)

	def extension_check(self):
		'''Check which extension boxes have been ticked, and if at least one has been ticked.'''
		targetextension = []

		if self.htmlcheck.isChecked():
			targetextension.append('.html')
			targetextension.append('.htm')
		if self.xmlcheck.isChecked():
			targetextension.append('.xml')
		if not (self.htmlcheck.isChecked() or self.xmlcheck.isChecked()):
			raise IOError

		return targetextension

	def make_attrs_dict(self, attrs_text):
		'''Check on typos and create attribute dictionary'''

		attrs_dict = {}
		target_attrs = attrs_text.split('/')

		for tag in target_attrs:

			if bool(re.match(r'(.*\:\[.*\]){2}', tag)) or not bool(re.match(r'(.*\:\[.*\])', tag)):
				raise SyntaxError
			else:
				dictkey = str(tag.split(':')[0])
				dictvalue = re.sub('[\[\]]', '', str(tag.split(':')[1]))

				attrs_dict[dictkey] = [x.strip() for x in dictvalue.split(',')]

		return attrs_dict

	def check_styleattr_present(self, styles_text):
		'''Check if style attribute has been added.'''
		if 'style' in self.allowed_attrs.text():
			return [x.strip().lower() for x in unicode(styles_text).split(',')]
		else:
			raise EOFError

	def file_clean(self, dirt_text):
		'''Create tag list; check and create attribute dictionary; then pass this information to clean.'''

		tags = [x.strip().lower() for x in unicode(self.allowed_tags.text()).split(',')]

		try:
			attrs = self.make_attrs_dict(self.allowed_attrs.text()) if len(self.allowed_attrs.text()) else {}
			styles = self.check_styleattr_present(self.allowed_styles.text()) if len(self.allowed_styles.text()) else []

		except SyntaxError:
			self.browser.append(
				u'''E: Discovered mistake in your attribute entry. Be sure to input an attribute pattern x\u2081:[a\u2081,..., a\u2099,]/.../x\u2099:[a\u2081,..., a\u2099,] for each tag x\u2081-x\u2099 and attributes a\u2081-a\u2099.'''
			)
			raise
		except EOFError:
			self.browser.append(
				u'''E: Style attribute not allowed. To add style attribute for all tags, enter *:[style] in allowed attributes.'''
			)
			raise
		else:
			soup = CleanDirtySoup(dirt_text, tags, attrs, styles)
			self.browser.append('Successfully cleaned %s' % (dirt_text.replace('\\', '/').split('/')[-1]))

	def check_is_file_cleaned(self, dirfile, extensions):
		if any(ext in dirfile for ext in extensions):
			# The requested path is a file with extension in list of chosen extensions (i.e. .html, .htm, or .xml).
			

			fileName, fileExtension = os.path.splitext(dirfile)
			neighbfiles = glob.glob(os.path.join(os.path.dirname(dirfile), '*'+fileExtension))

			if (fileName+'_cleaned'+fileExtension in neighbfiles) or ('_cleaned' in dirfile):
				self.browser.append("I: %s already clean." % (dirfile.replace('\\', '/').split('/')[-1]))
			else:
				return self.file_clean(dirfile)

		else:
			# The extensions have been wrongly matched.
			self.browser.append('E: Extensions do not match.')

	def batch_clean(self, dirfile, extensions):
		'''
		Check if path is file or directory.
		If file, check if file has not been cleaned, then clean.
		If directory, then loop through its files via recursion.
		'''

		if os.path.isfile(dirfile):
			self.check_is_file_cleaned(dirfile, extensions)

		else:
			# The requested path is a directory.

			files_set = []
			for ext in extensions:
				files_set.extend(glob.glob(os.path.join(dirfile, '*'+ext)))

			message = 'Are you sure to batch clean %s?' % (dirfile)
			reply = QtGui.QMessageBox.question(self, 'Warning', message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

			if reply == QtGui.QMessageBox.Yes:
				for filename in files_set:
					self.batch_clean(filename, extensions)

	def clean_path(self):
		'''Check if path is file or directory, then pass each file to file_clean()'''

		targetextension = []
		targetfd = unicode(self.dirty_file.text())

		try:
			targetextension = self.extension_check()
		except IOError:
			self.browser.append('E: No extension check detected.')
		else:
			if os.path.exists(targetfd):
				self.batch_clean(targetfd, targetextension)
			else:
				self.browser.append('E: Path was not found.')

def main():
	app = QtGui.QApplication(sys.argv)
	strip = StripUi()
	strip.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
