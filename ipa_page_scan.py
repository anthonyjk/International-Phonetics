from urllib.request import urlopen
url = 'https://en.wikipedia.org/wiki/Help:IPA/Standard_German'
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

wikitable_index = html.find('<table class="wikitable"')
html = html[wikitable_index:len(html)] # Cut off all text before wikitable
start = html.find('class="IPA"') + len('class="IPA"') # Starting index

def mini_scan(index): # Scans a single line for IPA name and symbol
    data = []
    scanning = True
    while scanning:

        record = False

        if html[index] == "t": # Looks for title= to start recording symbol name
            title_check = ""
            for i in range(6): # Checks next few indices to match to 'title='
                title_check += html[index + i]
            if title_check == "title=":
                index += 7 # 7 because skipping the quotation mark
                record = True

        if html[index] == ">": # Looks for '>' to start recording the IPA symbol
            record = True
            index += 1 # Moves index forward so as to not record '>' in text.

        text = ""
        while record: # Records index into string
            text += html[index]
            index += 1
            if html[index] == '"': # Ends symbol name statement
                data.append(text)
                record = False
            elif html[index] == "<": # Ends symbol statement & the miniscan
                data.append(text)
                record = False
                scanning = False
                
        index += 1
    return [data, index]

def title_jump(index):
    global html
    html = html[index:len(html)]
    return html.find('title=')

def table_scan(index):
    global html

    table_data = []
    scanning = True
    while scanning:
        ipa_dist = html.find('class="IPA"')
        table_dist = html.find('</table>')

        if ipa_dist < table_dist:
            index = title_jump(index)
            line_data = mini_scan(index)
            index = line_data[1] # Sets new index
            table_data.append(line_data[0])
        else:
            scanning = False

    return table_data
        
data = table_scan(start)

clean_data = []
for row in data:
    if "Voiced" in row[0] or "Voiceless" in row[0] or "Glottal" in row[0]:
        clean_data.append(row)

print(clean_data)
