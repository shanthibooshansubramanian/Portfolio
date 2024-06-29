# MultiSource FraudBuster

## Project Overview

This project focuses on detecting fraudulent credit card transactions using various data sources and machine learning techniques. The goal is to build an efficient fraud detection system that can identify and prevent fraudulent activities with high accuracy.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Source Data](#source-data
6. [Milestone1](#Milestone1)
7. [Milestone2](#Milestone2)
8. [Milestone3](#Milestone3)
9. [Milestone4](#Milestone4)
10. [Milestone5](#Milestone5)
11. [Future Work](#future-work)
12. [Contributing](#contributing)
13. [Acknowledgments](#acknowledgments)

    
## Installation

1. Ensure Python 3.8 or above is installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Install [PyCharm](https://www.jetbrains.com/pycharm/download/) (recommended for development).
3. Install the required packages


## Usage

1. Clone the repository:
2. Open the project in PyCharm:
3. Run the Python scripts to preprocess data, train models, and evaluate results.

## Data

The project utilizes several data sources related to credit card fraud detection. The data includes transaction details, customer information, merchant information, and indicators of fraudulent activity.

## Source Data

- **API**: [FraudLabs Pro API](https://www.fraudlabspro.com/developer/api/screen-order?ref=apilist.fun)
  - This REST API detects all possible fraud traits based on the input parameters supplied. The more input parameters supplied, the higher the accuracy of fraud detection.

- **CSV File**: [Credit Card Fraud Detection Dataset on Kaggle](https://www.kaggle.com/datasets/shayannaveed/credit-card-fraud-detection)
  - A simulated dataset containing legitimate and fraud transactions from January 1, 2019, to December 31, 2020. It covers credit cards of 1000 customers doing transactions with a pool of 800 merchants.

- **CSV File**: [PaySim Synthetic Dataset on Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)
  - PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behavior to evaluate the performance of fraud detection methods.

- **Web**: [ Synthetic Payments Data](https://datahub.io/machine-learning/creditcard/datapackage.json')
  - Data representing transactions from a subject-centric view with the goal of identifying fraudulent transactions. This data contains a variety of transaction types representing normal activities and abnormal/fraudulent activities introduced with predefined probabilities.

## Milestone 1: Data Preparation and Integration

Integrated data from CSV files, web sources, and APIs to create a unified dataset for fraud detection.

## Milestone 2: Data Transformation and Cleaning (Flat File Source)

Performed data cleaning and transformation on the CSV file, addressing missing values, formatting issues, and ensuring data consistency.

## Milestone 3: Data Transformation and Cleaning (Website Source)

Fetched, cleaned, and transformed credit card data from a web source, standardizing formats and handling duplicates.

## Milestone 4: Data Transformation and Cleaning (API Source)

Interfaced with the FraudLabs Pro API for real-time fraud validation, and cleaned and formatted the API response data.

## Milestone 5: Merging Data and Storing in Database/Visualizing Data

Merged the cleaned datasets into a SQLite database and created visualizations to explore trends and patterns in fraud detection.

## Future Work

Future improvements could include:
- Enhancing the model's accuracy and robustness.
- Incorporating additional data sources for better prediction.
- Developing a user-friendly interface for easier interaction with the fraud detection system.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

This project was developed as part of the learning process by Shanthibooshan Subramanian. If you plan to use it, please provide appropriate citations to the dataset and other pages you might have referred to for your learning process.

Special thanks to the following resources:
- [Kaggle](https://www.kaggle.com/)
- [Python](https://www.python.org/)
- [FraudLabs Pro](https://www.fraudlabspro.com/)
- [DataCamp](https://app.datacamp.com/)
- [JPMorgan Synthetic Payments Data](https://www.jpmorgan.com/synthetic-data/payments-data-for-fraud-detection)




