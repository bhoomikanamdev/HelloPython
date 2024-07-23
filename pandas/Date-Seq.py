import pandas as pd
'''start_date = '01-01-2024'
end_date= '30-01-2024'

output = pd.date_range(start= start_date, end = end_date )
for date in output:
    print(date)'''


'''71.Convert below list into date format and order should be same -
['2002-10-20','2004-04-12','2020-09-07']
The order sequence after converting should remain same'''
from datetime import datetime

# List of date strings
date_strings = ['2002-10-20', '2004-04-12', '2020-09-07']

# Convert to date objects
date_objects = [datetime.strptime(date, '%Y-%m-%d').date() for date in date_strings]

for x in date_objects:
# Print the date objects to verify
    print(x)





