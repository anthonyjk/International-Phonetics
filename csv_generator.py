import pandas as pd

# Called inside of script
def create_csv(df, title = "generated_data"):
    df.to_csv(title+".csv")

def list_to_dataframe(col_titles, data_list):
    shell = pd.DataFrame()

    for i in range(len(col_titles)): # Put new list into data frame
        shell[col_titles[i]] = data_list[i]

    return shell

# To be called outside of script
def generate_csv(data, col_titles, title):
    df = list_to_dataframe(col_titles, data)
    print(df)
    create_csv(df, title)
