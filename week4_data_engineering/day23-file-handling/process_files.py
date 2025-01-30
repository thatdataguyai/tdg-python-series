import os
import json
import pandas as pd

def process_files():
    # Define directories
    input_dir = "files"
    output_dir = "processed_files"
    os.makedirs(output_dir, exist_ok=True)
    
    # Process the JSON file
    json_path = os.path.join(input_dir, "top_tracks.json")
    if os.path.exists(json_path):
        with open(json_path, "r") as json_file:
            data = json.load(json_file)
        
        # Example: Filter tracks with popularity > 80
        filtered_tracks = [track for track in data["tracks"] if track["popularity"] > 80]
        
        # Save the processed JSON file
        processed_json_path = os.path.join(output_dir, "top_tracks_filtered.json")
        with open(processed_json_path, "w") as json_file:
            json.dump({"tracks": filtered_tracks}, json_file, indent=4)
    
    # Process the CSV file
    csv_path = os.path.join(input_dir, "top_tracks.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Example: Convert duration from ms to seconds
        df["Duration (s)"] = df["Duration (ms)"] / 1000
        
        # Save processed CSV
        processed_csv_path = os.path.join(output_dir, "top_tracks_processed.csv")
        df.to_csv(processed_csv_path, index=False)
    
    # Process Excel file
    excel_path = os.path.join(input_dir, "top_tracks.xlsx")
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path, engine="openpyxl")
        
        # Example: Sort by popularity
        df_sorted = df.sort_values(by="Popularity", ascending=False)
        
        # Save processed Excel
        processed_excel_path = os.path.join(output_dir, "top_tracks_sorted.xlsx")
        df_sorted.to_excel(processed_excel_path, index=False, engine="openpyxl")

if __name__ == "__main__":
    process_files()
