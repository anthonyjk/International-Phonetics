from urllib.request import urlopen
url = 'https://en.wikipedia.org/wiki/Help:IPA/Japanese'
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

# TODO
# Deal with breaks in text generation for items such as <i>, <b>, etc.
# See if there can be a distinction between each column v. each item in a single column

# Find <table class="wikitable" -> that's where the IPA tables are
wikitable_index = html.find('<table class="wikitable"')
html = html[wikitable_index:len(html)] # Cut off all text before wikitable
start = html.find("<tr>") + len("<tr>") # Starting index

# Scans data between <tr> and </tr>
def mini_scan(index):
    data = []
    scanning = True
    while scanning:
        
        record = False
        if html[index] == ">": # Start recording text between '>' and '<'
            record = True
            text = ""
            index += 1
            while record: # Start recording text into string
                if html[index] == "<" or html[index] == "\n": # Check if ending or just a bold (<b>)
                    
                    bold_check = html[index] + html[index+1] + html[index+2]
                    if bold_check == "<b>":
                        index += 3 # Move index to '>' (the index += 1 at the end will push it to the next character)
                    else:
                        record = False
                        if html[index] == "\\":
                            print("found")
                        if(len(text) > 0): # Making sure not to add empty values
                            data.append(text) # Put text in list
                else: # Add characters to text
                    text += html[index]
                    index += 1
                    
        if html[index] == "/": # Look for /tr to know to end the scan
            tr_check = html[index] + html[index + 1] + html[index + 2]
            if tr_check == "/tr":
                scanning = False
                
        index += 1 # Move index forward to next character

    return [data, index]

# Scans data inbetween <table> and </table>
def table_scan(index):
    data = []
    scanning = True
    while scanning:
        if html[index] == "/": # Look for signs of '/table'
            end_table_check = ""
            for i in range(6): # Checks the next few characters to see if they match '/table'
                end_table_check += html[index + i]
            if end_table_check == "/table": # End overall scan
                scanning = False
                
        elif html[index] == "<": # Look for signs of '<tr>'
            tr_check = ""
            for i in range(4): # Checks next few characters for '<tr>'
                tr_check += html[index + i]
            if tr_check == "<tr>": # If it matches, run a mini scan for data
                ms_info = mini_scan(index) # Run mini scan
                data.append(ms_info[0]) # Append new set of data to overall set
                index = ms_info[1] # Set new index after mini scan

        index += 1

    return data

jp_ipa = table_scan(start)
print(jp_ipa)
