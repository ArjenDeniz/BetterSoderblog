from ProcessingData import Process_From_Raw_Data
from WebScraper import Link_To_Text
import os

for year in range (2009,2024):
    if os.path.exists('Raw_Data_'+ str(year) + '.txt') == False:
        Link_To_Text(year)
    Process_From_Raw_Data(year)