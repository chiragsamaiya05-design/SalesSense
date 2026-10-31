from src.data_preprocessing import (
    load_data,
    inspect_data,
    clean_data
)

df = load_data("data/sales_data.csv")

inspect_data(df)

cleaned_df = clean_data(df)

print("\nCleaned Dataset:")
print(cleaned_df.head())

print("\nFinal Shape:", cleaned_df.shape)

print("\nRemaining Missing Values:")
print(cleaned_df.isnull().sum())