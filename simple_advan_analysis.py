import pandas as pd
import os

def analyze_data():
    output_dir = "analysis"
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv("advan_jan2020.csv")
    
    summary_stats = df.describe()
    summary_stats.to_csv(f"{output_dir}/summary_statistics.csv")
    
    missing_values = df.isnull().sum().to_frame(name="Missing Count")
    missing_values.to_csv(f"{output_dir}/missing_values.csv")
    
    # Top cities by frequency
    top_cities = df["city"].value_counts().head(10).to_frame(name="Count")
    top_cities.to_csv(f"{output_dir}/top_cities.csv")
    
    # Top NAICS codes
    top_naics = df["naics_code"].value_counts().head(10).to_frame(name="Count")
    top_naics.to_csv(f"{output_dir}/top_naics_codes.csv")
    
    print(f"Data analysis completed. Results saved in '{output_dir}' directory.")

if __name__ == "__main__":
    analyze_data()
