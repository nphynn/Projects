Nick Phynn   
Business Data Filtering Script

PROCESS & STEPS

Script to process an Excel file containing business names, filtering out irrelevant entries
and retaining only those related to dry cleaning or laundromats. The script:
1. Loads the Excel file.
2. Excludes rows with unwanted keywords across all columns.
3. Filters relevant rows based on specific keywords in the 'Location Name' column.
4. Saves both filtered and excluded data into separate Excel files.

# Libraries
import pandas as pd

# Step 1: Load the Excel file
file_path = "drycleaners.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path)

# Step 2: Exclude rows containing specified keywords (case-insensitive) across all columns
exclude_keywords = (
    r"p\.o\. box|carpet|landscaping|landscaper|janitorial|restoration|duct|window|"
    r"power wash|commercial|chimney|cleaning solution|tile|furniture|upholstery|"
    r"cleaning svc|cleaning service|vacuum|plumbing|sweeping|drapery|blind|house|"
    r"housekeeping|wax|polish|"
    r"Johnson's Carpet Cleaning|Southland Technical Svc|Bovee Restoration Svc|"
    r"You Missed A Spot Cleaning Svc|Traco Maintenance Systems|"
    r"Absolute Cleaning Operations|Cleaning Super Hero G & G Svc|"
    r"Etheridge Insurance Agency|Dixie Pickup & Delivery Svc|"
    r"Indian Springs Animal Clinic|Ccr Furniture Upholstery Clnrs|"
    r"Mari's Property Mgmt & Clnng|Dirt Busters House Cleaning|"
    r"Hotel Cleaning Svc|Kiwee's Cleaning Co LLC|Jeeco Manufacturing & Supply"
)
mask_excluded = df.apply(lambda row: row.astype(str).str.contains(exclude_keywords, case=False, na=False, regex=True).any(), axis=1)
excluded_df = df[mask_excluded]
df = df[~mask_excluded]  # Keep only non-excluded rows for filtering

# Step 3: Filter relevant rows based on specific keywords in the 'Location Name' column
column_name = "Location Name"  # Change this to the correct column name
include_keywords = (
    r"laundromat|cleaner|coin|laundry|dry clean|dry cleaner|dry cleaners|"
    r"dryclean|drycleaner|drycleaners"
)
filtered_df = df[df[column_name].str.contains(include_keywords, case=False, na=False, regex=True)]

# Step 4: Capture rows that were neither in excluded_df nor in filtered_df
remaining_excluded_df = df[~df.index.isin(filtered_df.index)]

# Append these rows to the initially excluded dataset
final_excluded_df = pd.concat([excluded_df, remaining_excluded_df])

# Step 5: Save the filtered data to a new Excel file
output_file_filtered = "drycleaners_filtered_data.xlsx"
filtered_df.to_excel(output_file_filtered, index=False)

# Step 6: Save the final excluded data to a different Excel file
output_file_excluded = "drycleaners_excluded_data.xlsx"
final_excluded_df.to_excel(output_file_excluded, index=False)

print(f"Filtered data saved to {output_file_filtered}")
print(f"Excluded data saved to {output_file_excluded}")
