from src.data_preprocessing import load_data, clean_data
from src.analysis import run_analysis

# Load dataset
df = load_data("data/sales_data.csv")

# Clean dataset
df = clean_data(df)

# Perform analysis
run_analysis(df)