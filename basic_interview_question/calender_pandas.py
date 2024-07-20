
import pandas as pd

# Define your start and end dates
start_date = '2024-07-01'
end_date = '2024-07-10'

# Generate the date range using pandas
date_range = pd.date_range(start=start_date, end=end_date)

# Print the generated dates
print("Generated dates using pandas:")
for date in date_range:
    print(date.strftime('%Y-%m-%d'))
