# Project 6: Analysis of the PPP Loans Issued to Small Businesses During COVID-19

## Introduction

This Group Project is a comprehensive exercise in building a data warehouse and creating a robust data architecture. It encompasses the entire journey of data from sourcing to visualization, integrating aspects of data collection, storage, transformation, and presentation. This project requires both technical skills in handling and processing data and an understanding of effective data structuring (data architecture) and meaningful data presentation (data visualization).

### Background

The Paycheck Protection Program (PPP) is a U.S. government initiative designed to help small businesses during times of economic hardship such as the COVID-19 pandemic. Initiated during the Trump administration in 2020, the PPP provides loans to small businesses to cover essential expenses like employee salaries, rent, mortgage payments, and utilities. The key feature of these loans is their potential for forgiveness, encouraging businesses to use the funds for these approved expenses.

### Business Problem

The goal of this analysis is to gain insights into the distribution of the PPP loans, understand which companies and states received the most significant support, identify the top lenders by state, and determine the overall loan distribution by lenders. The analysis aims to provide a comprehensive picture of how the PPP loans were distributed geographically, which companies and states benefited the most, and the role of different lenders in supporting small businesses during the COVID-19 pandemic.

### Stakeholders

Primary Stakeholder: Professor Jefferson Bien-Aime.

### About the Dataset

The PPP Loans dataset provides detailed information on Paycheck Protection Program (PPP) loans issued to small businesses during the COVID-19 pandemic. It includes key data points such as loan amounts, borrower details, loan status, and information about the lenders. This data is crucial for analyzing how financial aid was distributed to businesses in need during a critical period.

This PPP loan dataset is not just a collection of numbers and names; it represents a critical part of the economic response to a global crisis. Analyzing this data provides insights into the effectiveness of the PPP loans in supporting small businesses, the equitable distribution of funds, and the overall impact on the economy during an unprecedented time.

If you want to access the source of the data for this project, please click on the following links:

- [Paycheck Protection Program (PPP) Data](https://data.sba.gov/dataset/ppp-foia)
- [North American Industry Classification System (NAICS)](https://www.census.gov/naics/)

### Analysis Questions
A tableau dashboard will be created with the goal to answer the following questions:

- Total loan amount by companies
- Total loan amount by State
- Total number of businesses by State
- Top 10 Lenders by State
- Total Loan amount by Lenders

### Project Requirements

#### Data Examination

- Assess the data format and requirements for the analysis.

#### Project Structure

1. **Data Scraping and Cloud Upload:** Write a Python script to scrape data from the source and save it in Azure cloud
2. **Data Normalization**
3. **Dimensional Modeling**
4. **Data Pipeline/ETL:** Use SQL for data cleaning, formatting, and transformation.
5. **Data Loading:** Load the cleaned data into a data warehouse and create a SQL view or connect it directly to Tableau

