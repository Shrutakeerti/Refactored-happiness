# 🧠 GenAI Excel Auto-Filler with LLaMA 7B via Groq API

This project automates the extraction and population of financial or HR data into an Excel template using GenAI (LLaMA 7B 16E Instruct via Groq API). Upload multiple CSVs, and get a filled Excel file with mapped values — no manual work needed.

---

##  Features

- Accepts multiple CSV source files via FastAPI
-  Extracts label placeholders from an Excel template
-  Uses LLaMA 7B (Groq) for intelligent value mapping
-  Outputs a new filled Excel file maintaining original formatting
- Returns clean JSON response with matched fields

---

##  Project Structure
├── main.py # FastAPI entry point
├── ai_mapper.py # Handles prompt building + Groq API calling
├── excel_handler.py # Template parsing and Excel writing
├── config.py # Groq API key and model config
├── data/
│ ├── templates/ # Contains the input Excel template
│ ├── Source File/ # Folder for uploaded CSVs
│ └── output/ # Folder for generated output Excel
└── README.md # This file


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/genai-excel-filler.git
cd genai-excel-filler
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
## 3. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt

```

###  Configuration

In `config.py`, set your Groq API key and model slug:

```python
GROQ_API_KEY = "your_groq_api_key_here"
GROQ_MODEL = "meta-llama/llama-7b-16e-instruct"
```

## ▶️ Run the API Server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```


### Request Format
- **Type:** `multipart/form-data`
- **Field Name:** `files`
- **Value:** Upload one or more `.csv` files

### Example in Postman
1. Set method to **POST**
2. URL: `http://127.0.0.1:8000/analyze`
3. Go to **Body** → Select **form-data**
4. Add a key named `files`, set type to **File**, and upload one or more CSV files
5. Click **Send**

### Sample JSON Response
```json
{
    "status": "success",
    "mapped_fields": {
        "◦ Registered nurses": 47696,
        "◦ Enrolled nurses (registered with the NMBA)": 50621.2,
        "◦ Personal care workers / assistant in nursing": 42298,
        "◦ Care management staff": 75426.17,
        "◦ Allied health": 72213.12,
        "◦ Diversional/Lifestyle/Recreation/Activities officer": 83796.32,
        "◦ Registered nurses - Highest Rate": 55.26,
        "◦ Registered nurses - Average Rate": 47.12,
        "◦ Registered nurses - Lowest Rate": 38.97,
        "◦ Enrolled nurses (registered with the NMBA) - Highest Rate": 75.99,
        "◦ Enrolled nurses (registered with the NMBA) - Average Rate": 69.18,
        "◦ Enrolled nurses (registered with the NMBA) - Lowest Rate": 62.37,
        "◦ Personal care workers / assistant in nursing - Highest Rate": 51.73,
        "◦ Personal care workers / assistant in nursing - Average Rate": 46.38,
        "◦ Personal care workers / assistant in nursing - Lowest Rate": 41.03,
        "Occupied bed days": 6161,
        "Available bed days": 6291,
        "Registered nurses care minutes per occupied bed day": 0,
        "Enrolled nurses (registered with the NMBA) care minutes per occupied bed day": 0,
        "Personal care workers / assistant in nursing care minutes per occupied bed day": 0,
        "Infection Prevention and Control (IPC) lead costs": 19363,
        "Residential Support costs": 27359,
        "Preventative measures costs": 19150,
        "Employee and agency labour costs": 26162,
        "Other outbreak costs": 58823
    },
    "message": "Excel filled successfully."
}
```
![API Response Screenshot](https://github.com/Shrutakeerti/Refactored-happiness/blob/main/Screenshot%20(307).png)

###  Output Location

After successful processing, the filled Excel file will be saved at:

`D:\Prodgen Assignment\output\filled_template.xlsx`

This output file maintains the original Excel structure, but with semantically matched values filled in using LLM-based extraction.
### Author - Shrutakeerti Datta.
Made with pain.



