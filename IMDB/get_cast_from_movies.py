# modified from https://raw.githubusercontent.com/5harad/datascience/master/webscraping/01-bs/get_cast_from_movie.py

from bs4 import BeautifulSoup
import requests


def clean_text(text):
    """ Removes white-spaces before, after, and between characters

    :param text: the string to remove clean
    :return: a "cleaned" string with no more than one white space between
    characters
    """
    return ' '.join(text.split())


""" Go to the IMDb Movie page in link, and find the cast overview list.
    Prints tab-separated movie_title, actor_name, and character_played to
    stdout as a result.
"""
link = 'http://www.imdb.com/title/tt0111161/?ref_=nv_sr_1'
movie_page = requests.get(link)

# Strain the cast_list table from the movie_page
soup = BeautifulSoup(movie_page.content, 'html.parser')

# Iterate through rows and extract the name and character
# Remember that some rows might not be a row of interest (e.g., a blank
# row for spacing the layout). Therefore, we need to use a try-except
# block to make sure we capture only the rows we want, without python
# complaining.

cast_list = soup.find('table', {'class': 'cast_list'})
for row in cast_list.find_all('tr'):
    try:
        td = row.find_all('td')
        if len(td) == 4:
            actor = clean_text(td[1].find('a').text)
            character = clean_text(td[3].find('a').text)
            print('{:20} {:10}'.format(actor, character))
    except AttributeError:
        pass
