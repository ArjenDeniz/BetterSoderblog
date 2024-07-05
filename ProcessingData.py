import re
#reads the data
with open('Raw_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

#finds the dates in the expression and seperates them
regex_dates = r'\d{2}/\d{2}'
dates = re.findall(regex_dates, content)
content = re.sub(regex_dates, '', content)

#removes instances of data-mce-fragment and </em> or </strong>
content = re.sub(r' data-mce-fragment="1"', '', content)
content  = re.sub(r'</(em|strong)>', '', content)

print(content)
