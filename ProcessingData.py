import re
import csv
import pandas as pd

#takes text file and makes it a dataframe
def Make_Df_From_Txt(text):
    df = pd.DataFrame([text],columns=['Content'])
    split_content= df.iloc[0,0].split('\n')
    new_df = pd.DataFrame(split_content, columns=['Content'])
    new_df = new_df.iloc[10:].reset_index(drop=True)
    return new_df

#removes the irrelevant parts of the text file and removes the unneeded parts of the string
def Remove_Extra_From_DF(df):
    df["Dates"] = df["Content"].str.extract(r'(\d{2}/\d{2})')
    df["Content"] = df["Content"].apply(lambda x: x[5:])
    df["Content"] = df["Content"].str.replace(r' data-mce-fragment="1"', "")
    df["Content"] = df["Content"].str.replace(r'(</em>,)[^,]*', r'\1', regex=True)
    return df

def Split_Titles(df):
    df = df.assign(Content = df.Content.str.split('</em>')).explode("Content")
    df = df.assign(Content = df.Content.str.split('</strong>')).explode("Content")
    df = df.assign(Content = df.Content.str.split(',')).explode("Content")
    return df


#from here we need spesific functions that automate the .apply lambda functions

#main function
def Process_From_Raw_Data(inputfilename):
    with open(inputfilename, 'r', encoding='utf-8') as file:
        content = file.read()
    df = Make_Df_From_Txt(content)
    df = Remove_Extra_From_DF(df)
    df = Split_Titles(df)
    return df


print(Process_From_Raw_Data('Raw_Data.txt'))