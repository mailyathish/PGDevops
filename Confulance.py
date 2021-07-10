
from atlassian import Confluence
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conf_site = 'https://wiki.jcpenney.com/#popular'
conf_user = 'yningapp'
conf_pass = 'Bangalore660$$'

page_title = 'Release Validations | Production Performance run | 2021' 
page_space = 'Performance Engineering 2021'

# connect to Confluence 
conf = Confluence(url=conf_site, username=conf_user, password=conf_pass)
# resolve page ID
#page_id = conf.get_page_id(page_space, page_title)

# Check page exists
#confluence.page_exists(page_space,page_title)

print(conf.page_exists(page_space,page_title)).encode('utf-8').strip()


