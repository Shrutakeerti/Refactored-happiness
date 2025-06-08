import os
import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from excel_handler import extract_labels_from_excel, update_excel_with_values
from ai_mapper import map_labels_to_values
import shutil
# these are the imports I need to run the code
app = FastAPI()
# Constants for file paths
TEMPLATE_PATH = r"D:\Prodgen Assignment\templates\template.xlsx"
OUTPUT_PATH = r"D:\Prodgen Assignment\output\filled_template.xlsx"
UPLOAD_DIR = r"D:\Prodgen Assignment\Source File"

def save_uploaded_files(files):# this func saves the uploaded files to a specific directory
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    for file in files:
        with open(os.path.join(UPLOAD_DIR, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

def load_all_source_csvs(): # this func loads all CSV files from the upload directory
    dfs = []
    for filename in os.listdir(UPLOAD_DIR):
        if filename.lower().endswith(".csv"):
            df = pd.read_csv(os.path.join(UPLOAD_DIR, filename))
            dfs.append(df)
    return dfs

@app.post("/analyze") # this is the endpoint that will be called to analyze the files
async def analyze(files: list[UploadFile] = File(...)):
    try:
        save_uploaded_files(files)

        print("Extracting labels...")
        labels = extract_labels_from_excel(TEMPLATE_PATH)

        print("Loading CSVs...")
        source_data = load_all_source_csvs()

        print(" Running AI mapping...")
        value_map = map_labels_to_values(labels, source_data)

        print(" Updating Excel...")
        update_excel_with_values(TEMPLATE_PATH, OUTPUT_PATH, value_map)

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "mapped_fields": value_map,
                "message": "Excel filled successfully."
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )
