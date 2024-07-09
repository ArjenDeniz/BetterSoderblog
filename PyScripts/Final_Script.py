from ProcessingData import Process_From_Raw_Data
from WebScraper import Link_To_Text
import os

for year in range (2009,2024):
    #checks if the text file exists to save on performance before scraping it
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_name = 'TextFiles'
    file_path = os.path.join(current_dir,folder_name ,'Raw_Data_'+ str(year) +'.txt')
    if os.path.exists(file_path) == False:
        Link_To_Text(year)
    Process_From_Raw_Data(year)




    