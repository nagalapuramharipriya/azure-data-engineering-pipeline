# Azure Data Engineering Pipeline 🚀

## 📌 Overview
This project demonstrates an end-to-end Azure Data Engineering pipeline using Azure Data Factory, Databricks, and PySpark.

## 🧠 Architecture
Source → ADF → Bronze → Silver → Gold → Analytics

## ⚙️ Tech Stack
- Azure Data Factory (ADF)
- Azure Databricks
- PySpark
- Azure Data Lake Storage (ADLS)
- SQL

## 📊 Project Workflow

### 🔹 Bronze Layer
- Raw data ingestion from source (CSV)

### 🔹 Silver Layer
- Data cleaning (null handling)
- Data transformation using PySpark

### 🔹 Gold Layer
- Aggregation (total sales by product)
## 📁 Project Structure
```
data/
notebooks/
pipelines/
sql/
```

---

## 📈 Key Highlights
- Built ETL pipeline using Azure Data Factory and Databricks  
- Implemented Medallion Architecture (Bronze, Silver, Gold)  
- Performed data transformation using PySpark  
- Designed scalable data workflow  

---

## 🔮 Future Enhancements
- Real-time streaming using Kafka  
- CI/CD pipeline using Azure DevOps  
- Power BI dashboard integration  
