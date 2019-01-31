import selenium.webdriver as web_driver
from bs4 import BeautifulSoup
import re

url = input('gimme dat url ').strip() or 'https://www.youtube.com/channel/UC78cxCAcp7JfQPgKxYdyGrg' # get url
print('scrapping {url}'.format(url=url))

driver = web_driver.Firefox() # open firefox
driver.get(url) # go to url with firefox

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.close()

# get amount of subscribers
sub_divs = soup.findAll(id='subscriber-count')
n_subscribers = sub_divs[len(sub_divs)-1].text
subscribers = int(re.sub('\D', '', n_subscribers)) #only get the number from e.g. 10,943,836 subscribers

# get username
title_divs = soup.findAll(id='channel-title')
username = title_divs[len(title_divs)-1].text

print('\n{name} has {subscribers} subscribers!!!!!'.format(name=username, subscribers='{:,}'.format(subscribers)))
