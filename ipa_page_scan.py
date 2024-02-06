from urllib.request import urlopen
url = 'https://en.wikipedia.org/wiki/Help:IPA/Mongolian'
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

start = title_jump(start)
recieved = mini_scan(start)
print(recieved)
start = recieved[1]
start = title_jump(start)
recieved.append(mini_scan(start)[0])
print(recieved)
