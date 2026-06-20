# 📊 Soul Foods Sales Data Project

## 🧠 Overview
This project processes raw transaction data from Soul Foods and converts it into a clean dataset for analysis.

It focuses on cleaning, filtering, and transforming multiple CSV files into a single structured output.

---

## 📁 Dataset
The project uses three CSV files located in the `data/` folder:

- daily_sales_data_0.csv  
- daily_sales_data_1.csv  
- daily_sales_data_2.csv  

Each file contains:

- product  
- quantity  
- price  
- date  
- region  

---

## 🎯 Objective
The goal of this project is to:

- Merge multiple CSV files into one dataset  
- Filter only **Pink Morsels**  
- Clean and convert data types  
- Create a new calculated column: **sales**  
- Export a final clean dataset  

---

## ⚙️ Data Processing Steps

### 1. Load Data
Read all CSV files using pandas.

### 2. Merge Data
Combine all datasets into one DataFrame.

### 3. Filter Product
Keep only rows where product is:

- pink morsel  

---

### 4. Clean Price Column
Remove `$` and convert values to float.

---

### 5. Convert Quantity
Ensure quantity is numeric (int).

---

### 6. Create Sales Column
Calculate sales using:

- sales = quantity × price  

---

### 7. Select Final Columns
Keep only:

- sales  
- date  
- region  

---

### 8. Export File
Save final dataset as:

- formatted_sales_data.csv  

---

## 📊 Output Example

| sales | date       | region |
|------|------------|--------|
| 300  | 2024-01-01 | north  |
| 150  | 2024-01-02 | south  |

---

## 🛠️ Tech Stack

- Python 🐍  
- Pandas 📊  
- CSV Processing  

---

## 🚀 How to Run

```bash id="run1"
pip install pandas
python main.py
