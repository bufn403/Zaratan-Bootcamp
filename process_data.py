import pandas as pd
import json

def expand_json_columns(df, json_columns):
    for col in json_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
            df = df.drop(columns=[col]).join(pd.json_normalize(df[col]).add_prefix(f"{col}_"))
    return df

def convert_parquet_to_csv(parquet_file, csv_file):
    df = pd.read_parquet(parquet_file)

    json_columns = [
        "visits_by_day", "visitor_home_cbgs", "visitor_home_aggregation",
        "visitor_daytime_cbgs", "visitor_country_of_origin", "bucketed_dwell_times",
        "related_same_day_brand", "related_same_month_brand", "popularity_by_day",
        "popularity_by_hour", "device_type", "carrier_name"
    ]
    
    df = expand_json_columns(df, json_columns)

    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    convert_parquet_to_csv("advan_jan2020.parquet", "advan_jan2020.csv")
