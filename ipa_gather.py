import ipa_page_scan as pg
from urllib.request import urlopen

std_url = "https://en.wikipedia.org/wiki/Help:IPA/Standard_German"
page = urlopen(std_url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

ipa_pages_index = html.find('navbox-styles')
html = html[ipa_pages_index:len(html)] # Cut off all text before ipa language pages
start = html.find('<li>') + len('<li>') # Starting index

if html[start + 1] == "<": # Skipping closing statements
    start += 1 # TODO: Deal with multi-dialect pages

print(pg.url)

stock_url = 'https://en.wikipedia.org/wiki/'
url_scans = [std_url]
url_titles = ["Standard German"]

def link_scan(index):
    global url_scans
    global url_titles
    
    data = []
    scanning = True

    record = False

    if html[index] == 't':
        title_check = ""
        for i in range(6):
            title_check += html[index + i]
        if title_check == "title=":
            index += 7 # skip quotation mark
            record = True

    if html[index] == ">":
        pass

    text = ""
    while record:
        text += html[index]
        index += 1

        if html[index] == '"': # Only happens when scanning 'title='
            record = False
            url_scans.append(stock_url + text)
        elif html[index] == "<": # Only happens when scanning names
            url_titles.append(text)
            
        
def div_scan(index):
    pass # End scan at </div>
