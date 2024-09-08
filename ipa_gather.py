import ipa_page_scan as pg
import csv_generator as cg
import pandas as pd
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

stock_url = 'https://en.wikipedia.org'
url_scans = [std_url]
url_titles = ["Standard German"]

def link_scan(index):
    global url_scans

    scanning = True

    while scanning:
        record = False

        if html[index] == 'h':
            href_check = ""
            for i in range(5):
                href_check += html[index + i]
            if href_check == "href=":
                index += 6 # skip quotation mark
                record = True

        if html[index] == "/":
            enddiv_check = ""
            for i in range(4):
                enddiv_check += html[index + i]
            if enddiv_check == "/div":
                scanning = False

        text = ""
        while record:
            text += html[index]
            index += 1

            if html[index] == '"': # Looking for end statement
                record = False
                url_scans.append(stock_url + text)
        index += 1

link_scan(start)
master_data = []
master_data.append([])
master_data.append([])
master_data.append([])
for i in range(len(url_scans)):
    index = pg.set_html(url_scans[i])
    title = url_scans[i][len('https://en.wikipedia.org/wiki/Help:IPA/'):]
    data = pg.table_scan(index)
    data = pg.clean_data(data)
    for set in data:
        master_data[0].append(title)
        master_data[1].append(set[0])
        master_data[2].append(set[1])

print(master_data)
cg.generate_csv(master_data, ["Language", "Name", "Symbol"], "ipa_collection")
