import pandas as pd

# Called inside of script
def create_csv(df, title = "generated_data"):
    df.to_csv(title+".csv")

def list_to_dataframe(col_titles, data_list):
    shell = pd.DataFrame()
    data = []
    for j in range(len(data_list[0])): # Create space to combine list row elements together
        data.append([])

    for r in data_list: # Create new list that has each column with the correct data
        for r_i in range(len(r)):
            data[r_i].append(r[r_i])

    for i in range(len(col_titles)): # Put new list into data frame
        shell[col_titles[i]] = data[i]

    return shell

# To be called outside of script
def generate_csv(data, col_titles, title):
    df = list_to_dataframe(col_titles, data)
    create_csv(df, title)
