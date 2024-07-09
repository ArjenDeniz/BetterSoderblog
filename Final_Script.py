from ProcessingData import Process_From_Raw_Data
from WebScraper import Link_To_Text
import os

for year in range (2009,2024):
    #checks if the text file exists to save on performance before scraping it
    if os.path.exists('Raw_Data_'+ str(year) + '.txt') == False:
        Link_To_Text(year)
    Process_From_Raw_Data(year)