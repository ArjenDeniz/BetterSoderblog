import re
import csv
import pandas as pd
from io import StringIO

#reads the data
with open('Raw_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

#finds the dates in the expression and seperates them
regex_dates = r'\d{2}/\d{2}'
dates = re.findall(regex_dates, content)

#removes instances of data-mce-fragment and </em> or </strong>
content = re.sub(r' data-mce-fragment="1"', '', content)
content  = re.sub(r'</(em|strong)>', '', content)

#adds a comma before dates and tags for csv
content = re.sub(regex_dates, r'\g<0>,', content)
regex_tags = r'<(em|strong)>'
content = re.sub(regex_tags, r'\g<0>,', content)

print(content)