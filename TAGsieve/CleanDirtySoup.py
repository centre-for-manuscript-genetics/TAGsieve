'''
Class that removes HTML/XML tags based on the Python modules BeautifulSoup and bleach.
The class ignores a set of allowed tags and attributes, and writing the results into a new '_cleaned' file.
'''

from bs4 import BeautifulSoup
import bleach
import sys, os

class CleanDirtySoup(object):
	unclean_file = ''
	new_file = ''

	allowed_tags = []
	allowed_attrs = {}

	def __init__(self, unclean_file, allowed_tags, allowed_attrs):
		self.unclean_file = unclean_file
		self.allowed_tags = allowed_tags
		self.allowed_attrs = allowed_attrs

		uncleanFile, uncleanExtension = os.path.splitext(unclean_file)

		self.new_file = uncleanFile+'_cleaned'+uncleanExtension

		self.make_cleansoup()
		
	def clean_dirtysoup(self):
		dirtysoup = BeautifulSoup(open(self.unclean_file).read())

		clean_soup =  bleach.clean(dirtysoup, self.allowed_tags, self.allowed_attrs, strip=True)
		clean_soup = clean_soup.encode('ascii', 'ignore')

		return clean_soup

	def make_cleansoup(self):
		f = open(self.new_file, 'w')
		f.write(self.clean_dirtysoup())

		sys.stdout.write('Finished cleaning: ' + f.name + '\n')
		f.close()
