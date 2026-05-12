# Project Summary: Rwanda Education Indicators Analysis

## 1. Project Purpose

This project analyzes Rwanda education indicators to explore trends, progress, gaps, and policy-relevant insights using Python and public development-style data.

The project demonstrates how data science can support education monitoring, policy analysis, program planning, and evidence-based decision-making.

---

## 2. Background

Education indicators help governments, development partners, nonprofit organizations, and researchers understand how education systems are changing over time.

Important education questions include:

- Are school enrollment rates improving?
- Are students completing primary and secondary education?
- Is gender parity improving across education levels?
- Are pupil-teacher ratios improving?
- Which education areas may require more policy or program support?

This project uses a structured dataset to analyze education access, completion, equity, and quality indicators in Rwanda.

---

## 3. Dataset Description

The dataset used in this project is a sample Rwanda education indicators dataset. It includes annual indicator values from 2015 to 2023.

Key fields include:

- Year
- Indicator code
- Indicator name
- Education level
- Category
- Value
- Unit
- Source

Dataset file: `data/rwanda_education_indicators.csv`

The dataset includes indicators related to:

- Primary school enrollment
- Secondary school enrollment
- Primary completion
- Secondary completion
- Primary gender parity
- Secondary gender parity
- Primary pupil-teacher ratio

---

## 4. Methods

This project uses a basic data analytics workflow.

### Data Cleaning

The Python script loads the dataset, checks missing values, reviews data types, checks duplicate records, summarizes indicator values, and saves a cleaned dataset.

Script file: `scripts/01_data_cleaning_and_eda.py`

### Exploratory Data Analysis

The analysis explores:

- Average indicator values
- Indicator trends over time
- Differences by education level
- Differences by indicator category
- Access, completion, equity, and quality patterns

### Visualization

The visualization script creates chart outputs for enrollment trends, completion trends, gender parity trends, pupil-teacher ratio trends, and average indicator values by category.

Visualization script: `scripts/02_visualizations.py`

---

## 5. Key Analysis Questions

This project is designed to answer the following questions:

1. How have primary and secondary enrollment rates changed over time?
2. How have primary and secondary completion rates changed over time?
3. Has gender parity improved in primary and secondary education?
4. How has the primary pupil-teacher ratio changed over time?
5. Which education categories show stronger or weaker performance?
6. What trends may be useful for education planning and program monitoring?

---

## 6. Expected Insights

This project is expected to produce insights such as:

- Primary enrollment remains high across the years.
- Secondary enrollment shows gradual improvement over time.
- Completion rates improve, but secondary completion remains lower than primary completion.
- Gender parity improves across both primary and secondary education.
- The pupil-teacher ratio declines over time, suggesting improvement in classroom staffing conditions.
- Education indicators can help identify areas where continued support may be needed.

---

## 7. Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- CSV data files

---

## 8. Skills Demonstrated

This project demonstrates the following skills:

- Data cleaning
- Exploratory data analysis
- Descriptive analytics
- Trend analysis
- Education indicator analysis
- Data visualization
- Public development data analysis
- Policy-relevant reporting
- Portfolio documentation

---

## 9. Portfolio Relevance

This project connects data science with education policy, public development indicators, and monitoring and evaluation. It reflects how analytics can support education-sector decision-making, especially in contexts where governments and development partners track progress over time.

It also strengthens a data science portfolio by showing practical use of Python, structured datasets, trend analysis, and visual communication.

---

## 10. Next Steps

Future improvements to this project may include:

- Adding visualization images to the `visuals/` folder
- Updating the README with chart outputs
- Creating a full Jupyter Notebook version of the analysis
- Expanding the dataset with more indicators
- Adding real World Bank data
- Comparing Rwanda with other East African countries
- Building an interactive dashboard in Google Looker Studio
