from src.data_preprocessing import load_data, clean_data
from src.visualization import run_visualizations

df = load_data("data/sales_data.csv")

df = clean_data(df)

run_visualizations(df)