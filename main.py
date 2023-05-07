import pandas as pd

# Read the Excel file
df = pd.read_excel('main.xlsx')

# Create an empty DataFrame to create a new Excel file
new_df = pd.DataFrame(columns=['Column A', 'Column B', 'Column C'])

# Loop through each row
for index, row in df.iterrows():
    # Get the data
    name = row['title']
    phone_number = row['phone']
    is_mobile = "No"
    if str(phone_number)[:2] in ["05", "+9"]: # Phone numbers starting with 05 or +9 are considered mobile.
        is_mobile = "Yes"
    
    # Add to the new DataFrame
    new_df = new_df.append({'Column A': name, 'Column B': phone_number, 'Column C': is_mobile}, ignore_index=True)

# Change the data type of the 'Column C' column to 'category' and sort it
new_df['Column C'] = new_df['Column C'].astype('category')
new_df['Column C'].cat.reorder_categories(['Yes', 'No'], inplace=True)
new_df = new_df.sort_values(by='Column C', ascending=False)

# Create a new Excel file
new_df.to_excel('new_file.xlsx', index=False)
