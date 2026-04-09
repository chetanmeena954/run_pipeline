import pandas as pd

def run_pipeline():
    df = pd.read_csv("sales.csv")

    # Create new column
    df['Revenue'] = df['Quantity'] * df['Price']

    # Group by product
    result = df.groupby('Product')['Revenue'].sum()

    print("Processed Data:")
    print(result)

    return result
