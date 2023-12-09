import pandas as pd
from datetime import datetime

startTime = datetime.now()

my_df = pd.read_csv("data/sr_my_hex.csv")
val_df = pd.read_csv("data/sr_hex.csv")

# Create a dictionary for faster lookups
val_dict = val_df.set_index('reference_number')['h3_level8_index'].to_dict()

def validate(my_row):

    reference_number = my_row['reference_number']

    if reference_number in val_dict:
        return val_dict[reference_number] == my_row['h3_level8_index']
    else:
        return False

# Use vectorized operations instead of apply
my_df['val'] = my_df.apply(validate, axis=1)

filtered_rows = my_df[my_df['val']]

# Get the number of rows using len()
number_of_rows = len(filtered_rows)

my_df_len = len(my_df)

print(f"Number of validated rows: {number_of_rows} out of {my_df_len} - {number_of_rows/my_df_len:.2%}")

elapsed_time = datetime.now() - startTime
print(f"Elapsed time: {elapsed_time.total_seconds():.2f} seconds")
