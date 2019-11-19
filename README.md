# search-engine-dorking
script to automate extraction of search results with query dorks

# usage
git clone https://github.com/offensivesubversion/search-engine-dorking.git\
pip3 install -r requirements.txt\
python3 dork.py\

# misc
the default dorks.txt file contains no real dorks
set the 'pages' variable to however many pages you want to scrape for each query. the default is 1
set the 'verbose' boolean to True to see the dorks printed as theyre executed
results are printed to stdout
