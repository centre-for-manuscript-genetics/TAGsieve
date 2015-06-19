from bs4 import BeautifulSoup
import bleach
import sys, os

class CleanDirtySoup(object):
	'''
	Class that removes HTML/XML tags based on the
	Python modules BeautifulSoup and bleach.
	The class ignores a set of allowed tags and attributes,
	and writing the results into a new '_cleaned' file.
	'''

	unclean_file = ''
	new_file = ''

	allowed_tags = []
	allowed_attrs = {}
	allowed_styles = []

	def __init__(self, unclean_file, allowed_tags, allowed_attrs, allowed_styles):
		self.unclean_file = unclean_file
		self.allowed_tags = allowed_tags
		self.allowed_attrs = allowed_attrs
		self.allowed_styles = allowed_styles

		uncleanFile, uncleanExtension = os.path.splitext(unclean_file)

		self.new_file = uncleanFile+'_cleaned'+uncleanExtension

		self.make_cleansoup()
		
	def clean_dirtysoup(self):
		'''
		Sends the unclean file to BeautifulSoup parser.
			The parsing unescapes HTML ascii characters.

		The parsed HTML is then sent to bleach for cleaning. Unescaped HTML is correctly ignored.
			The result has then to be re-encoded,
			replacing unescaped ascii characters with their raw HTML string variants.
			e.g. &ldquo; --> &#8220;
		'''
		dirtysoup = BeautifulSoup(open(self.unclean_file).read())

		clean_soup =  bleach.clean(dirtysoup, self.allowed_tags, self.allowed_attrs, self.allowed_styles, strip=True)
		clean_soup = clean_soup.encode('ascii', 'xmlcharrefreplace')

		return clean_soup

	def make_cleansoup(self):
		f = open(self.new_file, 'w')
		f.write(self.clean_dirtysoup())

		sys.stdout.write('Finished cleaning: ' + f.name + '\n')
		f.close()
