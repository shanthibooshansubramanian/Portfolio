# MultiSource FraudBuster

## Project Overview

This project focuses on detecting fraudulent credit card transactions using various data sources and machine learning techniques. The goal is to build an efficient fraud detection system that can identify and prevent fraudulent activities with high accuracy.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Future Work](#future-work)
7. [Contributing](#contributing)
8. [Acknowledgments](#acknowledgments)

    
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

## Milestone 1

### Accomplishments and Data Interpretation

The three data sources provided are all related to fraud detection in financial transactions. The data sources include the FraudLabs Pro API and Fraud Detection dataset CSV files. The credit card information in the CSV file can be used as input for the FraudLabs Pro API to screen for fraudulent orders.

The Fraud Detection dataset contains anonymized credit card transaction data, including the transaction amount, timestamp, and various features such as merchant ID, cardholder information, and location. This information can be used to train a machine learning model to predict whether a transaction is fraudulent based on patterns and correlations in the data. All three datasets contain information that can be used to detect potential fraud, such as transaction details, customer information, merchant information, and indicators of fraudulent activity.

The FraudLabs Pro API provides an automated fraud screening solution that analyzes various aspects of an order such as geolocation, IP address, email address, and credit card information to determine if it is a legitimate order or not. By integrating the machine learning model trained on the Fraud Detection dataset into the FraudLabs Pro API, the screening process can be improved in terms of accuracy and efficiency.

### Steps to Accomplish Milestone 1

1. Explore the FraudLabs Pro API documentation to understand its capabilities and limitations.
2. Examine the credit card CSV files to ensure they do not contain sensitive information such as cardholder names or billing addresses. Remove these fields if they exist to ensure privacy.
3. Import the Fraud Detection dataset CSV files into Python.
4. Write code to iterate through each row of the file and use the FraudLabs Pro API to screen each order for fraud.
5. Make API calls to the FraudLabs Pro API and analyze the responses to determine if an order is legitimate or not.
6. Use statistical and machine learning techniques to analyze the data and identify patterns or anomalies that may indicate fraudulent activity.
7. Use visualization techniques to better understand the data and identify trends or patterns.

### Ethical Implications

- The potential for false positives or false negatives: Balancing the need for fraud prevention with the need to avoid rejecting legitimate orders can be challenging.
- Quality of the data: Data cleaning and preprocessing may be necessary to remove outliers or errors that could negatively impact the accuracy of the analysis. The synthetic dataset may not accurately represent real-world transactions, which could limit the effectiveness of any fraud detection methods developed using this dataset.

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




