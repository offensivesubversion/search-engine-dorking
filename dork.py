import requests, re
from bs4 import BeautifulSoup

# config/setup
verbose = False # set this to True if you want to see the banner, and dorks as theyre processed
url = "https://bing.com/search?q=" # using Bing to allow connections through TOR
pages = 1 # number of search engine pages to crawl for each query
seen = [] # to avoid dupes
dorks = open( "dorks.txt", "r+" ).readlines() # get dorks

# print banner
if verbose:
	print
	print( "###########################" )
	print( "#  Search Engine Dorking  #" )
	print( "# by Offensive Subversion #" )
	print( "###########################" )
	print

# loop through each dork
for dork in dorks:

	# print to stdout
	if verbose:
		print( url + dork )

	# get the source code of the results page
	source = requests.get( url + dork ).text

	# get up to n pages of results
	for i in range( pages ):
		source = source + requests.get( url + dork + "&first=" + str( i ) + "1" ).text

	# create BS4 object
	soup = BeautifulSoup( source, 'html.parser' )

	# loop through all URLs in source
	tags = soup.find_all( 'a' )
	for tag in tags:

		try:

			# grab URL as string
			curr = tag.get( 'href' )

			# skip relative links
			if curr[0] != "h":
				continue
			# skip dupes
			elif curr in seen:
				continue

			# only grab those containing our dork
			elif dork[1:-1] in curr:
				# print to stdout regardless of verbosity settings
				print( curr )
				seen.append( curr )

		# catch exceptions
		except Exception as e:
			continue
