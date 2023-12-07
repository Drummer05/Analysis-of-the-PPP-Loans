# Project 6: Analysis of the PPP Loans Issued to Small Businesses During COVID-19

## Table of Contents
1. [Introduction](#introduction)
2. [Background](#background)
3. [Business Problem](#business-problem)
4. [Stakeholders](#stakeholders)
5. [About the Dataset](#about-the-dataset)
6. [Tools](#tools)
7. [Analysis Questions](#analysis-questions)
8. [Project Requirements](#project-requirements)
9. [Business Impact](#business-impact)
10. [Business Persona](#business-persona)
11. [Dataset Size, Strengths, and Weaknesses](#dataset-size-strengths-and-weaknesses)
12. [ETL](#etl)
    - [Data Extraction / Storage](#data-extraction--storage)
    - [Data Transformation](#data-transformation)
    - [Data Loading](#data-loading)
    - [Tableau Dashboard](#tableau-dashboard)

## Introduction

This Group Project is a comprehensive exercise in building a data warehouse and creating a robust data architecture. It encompasses the entire journey of data from sourcing to visualization, integrating aspects of data collection, storage, transformation, and presentation. This project requires both technical skills in handling and processing data and an understanding of effective data structuring (data architecture) and meaningful data presentation (data visualization). The goal is to develop a data pipeline following the architecture below. We looked at the PPP Loans Data.

Group Members:
Carlos Silverio 
Tammie Celius
Fulei Chen

![ppp loans](https://github.com/Drummer05/Analysis-of-the-PPP-Loans/assets/144565034/9eb6580d-b9d4-48ec-b3dc-0202d1e84c69)

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

For a comprehensive understanding of the data fields used in this project, please refer to our [2022 NAICS Title](https://docs.google.com/spreadsheets/d/1Ejue9j_eugdCveuAJLtt5zJkvG5ZTkmlw0nsC3r_hqA/edit#gid=1974515149). This dictionary provides detailed descriptions of each field, ensuring clarity and consistency in data interpretation. You can also get the dictionary in the dictionary file in this repository.

### Tools

We used a range of tools:

- **Azure Cloud Storage**
- **Python Anaconda:** For Extraction and Transformation
- **Azure Synapse**
- **Azure SQL Database** 
- **SQL:** For data loading
- **DBSchema:** For data modeling
- **Tableau:** For data serving
- **GitHub:** For project documentation
- **Google Colab:** For writing and executing Python code

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

1. **Gather Requirements:** Gather the neccesary requirements to solve the problem.
2. **Understand the Data:** Get familiarize with the datasets. Understand the columns.
3. **Dimensional Modeling**: Create facts and dimensional tables
4. **Data Scraping and Cloud Upload:** Write a Python script to scrape data from the source and save it in Azure cloud storage.
5. **Data Pipeline/ETL:** Transport the data to anaconda python, where the data will be transformed.
6. **Data Loading:** Create the facts and Dimensions table on Azure Synapse, then Load the cleaned data into the data warehouse, insert the data into the tables and finally connect azure synapse to Tableau for data visualizaiton.

### Business Impact

#### Risks:
- **Data Privacy and Security**: Handling sensitive financial data comes with the risk of data breaches. Ensuring robust security measures is crucial.
- **Accuracy of Analysis**: Incorrect analysis due to data inconsistencies or errors could lead to misleading conclusions.
- **Compliance and Legal Risks**: Ensuring the project complies with financial regulations and data protection laws (like GDPR in Europe or CCPA in California) is essential.

#### Costs:
- **Data Acquisition and Storage**: Costs associated with accessing and storing large datasets, especially if cloud services are used.
- **Analytical Tools and Resources**: Investment in analytical tools (like Tableau for visualization) and potentially in computational resources for data processing.
- **Manpower**: Costs related to the team working on data analysis, including data scientists, analysts, and IT support.

#### Benefits:
- **Insightful Business Decisions**: The analysis can provide valuable insights into loan distribution patterns, aiding in strategic decision-making for future financial programs.
- **Policy Formulation**: Helps in assessing the effectiveness of the PPP loans, guiding policymakers in designing better economic support schemes.
- **Academic and Research Value**: Contributes to academic research in economics, finance, and data science.

#### Estimated Impact:
- **Baseline Scenario**: If the analysis aligns with expectations, it could lead to improved understanding and management of similar financial programs in the future.
- **Optimistic Scenario**: In the best-case scenario, the project could significantly influence policy decisions, leading to more effective economic support mechanisms and potentially driving economic recovery.

### Business Persona

- **Policy Makers**: Government officials who can use the insights to shape future economic relief programs.
- **Financial Analysts**: Professionals analyzing economic trends and impacts of government policies.
- **Academic Researchers**: Scholars studying the economic impact of COVID-19 and government interventions.
- **Data Scientists and Analysts**: Individuals directly involved in data processing, analysis, and visualization.
- **Public and Media**: For transparency and public knowledge, especially in understanding how public funds were utilized.

### Dataset Size, Strengths, and Weaknesses

- **Size**: The dataset is extensive, covering a wide range of loans across various states and industries.
- **Strengths**:
  - Comprehensive coverage of PPP loans.
  - Detailed information enabling multifaceted analysis.
- **Weaknesses**:
  - Potential gaps or inaccuracies in self-reported data.
  - The large size of the dataset may require significant computational resources for analysis.
  - Historical data may not fully predict future trends, especially in unprecedented scenarios like a pandemic.

## ETL

### Data Extraction / Storage

- The datasets were sourced using Web Scraping with Python. The code is provided in the [Data Ingestion Python file].
- The data for this project is stored on Azure, ensuring secure and reliable access. You can find the data in our Azure storage container through the following link: [Azure Storage - Health Alliance Data](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/overview/storageAccountId/%2Fsubscriptions%2Ffb36820a-997c-4308-8686-5b46f22b0328%2FresourceGroups%2Fppp%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Fstcis4400projects/path/pppdata/etag/%220x8DBDED1E19A4458%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None).
- Updated scripts for data ingestion are available in [ppp loans Data Ingenstion storage.py](https://github.com/Drummer05/Analysis-of-the-PPP-Loans/blob/main/ppp%20loans%20Data%20Ingenstion%20storage.py)

### Data Transformation

- Once the datasets were successfully extracted and stored in our Azure storage account, we transformed the data to make sure it is reliable, objective, and ready for analysis. Some of the data transformation techniques we performed were:
  
  1. Remove Duplicates.
  2. Change the data type of some columns.
  3. Check and treat null values.
  4. Standardize column names.
  5. Standardize string data values for some columns.
  6. Create a year, month, day from date columns.
  7. Appending 2022 NAICS to a new column named 2022_Naics_Sector.
  8. Creating unique IDs for BorrowerID, LoactionID, LenderID, BusinessTypeID, and LoanStatusID.
  9. Removing special characters.

- Updated scripts for data transformation are available in  [Data Transformation PPP Loans.py](Data%20Transformation%20PPP%20Loans.py)

### Data Loading
- After the data was cleaned, we uploaded the cleaned csv file to a container in Azure Synapse. Once the cleaned data was successfully in a container in the workspace created. From the same workspace we created a dedicated SQL Pool. In the decdicated SQL Pool, we created empty fact and dimensional tables using SQL code. Then we had to ingest the data performing a one-time load into the pipeline, from our Azure Data Lake Storage into our Synapse Datawarehouse. For us running a pipeline was successful 8 time, once for the LoanFact table and 7 for the dimensional tables and failed twice. Which can be seen here: [PPP Loans Pipeline Runs](PPP%20Loans%20Pipeline%20Runs.png) After our pipelines were successful we still needed to load our data into the empty table that were previously cretated and to do this we use a SQl code, which to done seperate for each table. Last, now that our tables were loaded we can serve the data. We connected Tableau Desktop to Synapse to extract the clean data and work on our dashboard.  

- [ppp loans Dimensional Modeling.png](ppp%20loans%20dimensional%20modeling.png)
- Updated scripts for data loading are available in [Data Loading PPP Loans.txt](Data%20Loading%20PPP%20Loans.txt)

### Tableau Dashboard
- Tableau Dashboard: https://public.tableau.com/app/profile/carlos.silveio/viz/Book2_17019077623510/Dashboard3
- Here is the link of our presentation slides: https://docs.google.com/presentation/d/1lsZYntDNpIC_iCDW7zth2UtaD03OXn3dhe441ZIhD_E/edit#slide=id.p



