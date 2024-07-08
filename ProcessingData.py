import re
import pandas as pd

#drops the first few irrelevant rows
#drops every row that does not start with a date of the form xx/xx

def Droprows(df):
    regex = r'^(\d{2}/\d{2}|\s\d{2}/\d{2})'
    mask = df.astype(str).apply(lambda row: row.str.match(regex).any(), axis=1)
    return df[mask].reset_index(drop=True)

#takes text file and makes it a dataframe
def Make_Df_From_Txt(text):
    df = pd.DataFrame([text],columns=['Content'])
    split_content= df.iloc[0,0].split('\n')
    new_df = pd.DataFrame(split_content, columns=['Content'])
    new_df = Droprows(new_df) 
    return new_df

#removes the irrelevant parts of the text file and removes the unneeded parts of the string
def Remove_Extra_From_DF(df): 
    #extracts the dates
    df["Dates"] = df["Content"].str.extract(r'(\d{2}/\d{2})')
    #removes the first 5 elements (corresponding to dates) 
    df["Content"] = df["Content"].apply(lambda x: x[5:])
    #removes unnecessary tags like </em> or data-mce-fragment
    df["Content"] = df["Content"].str.replace(r' data-mce-fragment="1"', "")
    df["Content"] = df["Content"].str.replace(r'(</em>,)[^,]*', r'\1', regex=True)
    return df

def Split_Titles(df):
    df = df.assign(Content = df.Content.str.split('</em>')).explode("Content")
    df = df.assign(Content = df.Content.str.split('</strong>')).explode("Content")
    df = df.assign(Content = df.Content.str.split(',')).explode("Content")
    df = df[df["Content"] != ""]
    return df

#creates the columns where tags are what it is looking for and cols are the column names
def Type_Identifier(tags,cols ,df):
    if(len(cols) != len(tags)):
        print('your tags to check and corresponding column names dont match up')
        return 0
    length = len(cols)
    for i in range(0,length):
        df[cols[i]] = df["Content"].apply(lambda x: 1 if tags[i] in x else 0)
    return df

#checks if there are quotes in the string and inputs 1 if there are quotes
def Check_Quotes(df):
    def has_quoted_string(text):
        pattern = r'\u201c([^\u201d]*)\u201d'
        return 1 if re.search(pattern, str(text)) else 0
    df["Quoted"] = df["Content"].apply(lambda x: has_quoted_string(x))
    return df

def Delete_Tags(df,tags):
    for tag in tags:
        df["Content"] = df["Content"].str.replace(tag, "")
    return df



#main function
def Process_From_Raw_Data(inputfilename):
    tags = ['<strong>', '<em>', '*']
    cols = ['Bold', 'Italic', 'Short']
    with open(inputfilename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    df = Make_Df_From_Txt(content)
    df = Remove_Extra_From_DF(df)
    df = Split_Titles(df)
    df = Type_Identifier(tags, cols, df)

    #this is seperate because it uses isupper()
    df["AllCaps"] = df["Content"].apply(lambda x: 1 if x.isupper() else 0)
    #checks for quotation marks
    df = Check_Quotes(df)

    #deletes tags given at the start
    df = Delete_Tags(df,tags)

    df.to_csv('Content2023.csv', index=False)
    


Process_From_Raw_Data('Raw_Data_2023.txt')