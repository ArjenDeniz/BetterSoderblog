from ProcessingData import Process_From_Raw_Data
from WebScraper import Link_To_Text

for year in range (2009,2023):
    Link_To_Text(year)
    Process_From_Raw_Data(year)