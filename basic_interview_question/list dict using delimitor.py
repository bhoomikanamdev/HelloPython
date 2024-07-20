from datetime import datetime

# Original list of date strings
date_strings = ['2002-10-20', '2004-04-12', '2020-09-07']

# Convert strings to datetime objects
date_objects = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_strings]

# Print the converted dates
for date in date_objects:
    print(date)

