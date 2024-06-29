# Hotel Booking Analysis using Big Data Approach

## Project Overview

The hotel industry is rapidly evolving, with Big Data playing a transformative role in reshaping how hotels manage reservations. This project explores the integration of Big Data analytics into hotel reservation management to address challenges related to cancellations, optimize booking strategies, and enhance guest experiences. Leveraging advanced analytical techniques, the project aims to predict cancellations, personalize guest experiences, and improve operational efficiency.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation and Setup](#installation-and-setup)
3. [Codes and Resources Used](#codes-and-resources-used)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Data Processing and Analysis](#Data)
7. [Results and Evaluation](#results-and-evaluation)
8. [Future Work](#future-work)
9. [Acknowledgments/References](#acknowledgmentsreferences)

## Installation and Setup

1. **Sign up for Google Cloud**
   - Visit [Google Cloud website](https://cloud.google.com/).
   - Click **Get Started for Free**.
   - Follow the prompts to create your account and get $300 in credits.

2. **Create SSH Key**
   - Generate SSH key:
     - macOS: `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
     - Windows: Use PuTTYgen to generate keys.

3. **Add SSH Key to Google Cloud**
   - Upload your public key to Google Cloud Console -> Compute Engine -> Metadata.

4. **Set up Ubuntu Instance**
   - Create Ubuntu 22.04 LTS instance with specified configurations.

5. **Start Big Data Software**
   - Navigate to relevant directories (`hadoop-hive-spark-hbase`, `kafka`, `solr`, `nifi`).
   - Start services using Docker Compose: `cd <directory-name> && docker-compose up -d`

Remember to manage your Google Cloud credits and shut down instances when not in use.

## Codes and Resources Used

1. Hadoop Distributed File System (HDFS) for data storage.
2. Apache Hive for data organization and querying.
3. Apache Spark for data processing and analysis.
4. Apache Kafka for real-time data streaming.
5. Apache NiFi for data ingestion.

## Source Data

The dataset used in this project includes detailed hotel booking records, comprising attributes such as hotel type, booking status, lead time, arrival date, stay duration, guest demographics, meal type, country of origin, market segment, distribution channel, previous cancellations, room type, and more. This rich dataset provides comprehensive insights into reservation dynamics and customer behavior.

## Data Processing and Analysis

- **Data Ingestion with Apache NiFi:** Collect data from various booking channels in real-time.
- **Data Storage in HDFS:** Store ingested data in a scalable and reliable manner.
- **Data Organization with Apache Hive:** Structure data for easy querying and analysis.
- **Data Processing with Apache Spark:** Clean, transform, and analyze data to extract actionable insights.
- **Real-Time Data Streaming with Apache Kafka:** Ensure continuous data flow for up-to-date analytics.

## Results and Evaluation

- Predictive models trained using logistic regression achieved an accuracy of approximately 64.07%.
- Analysis of booking patterns revealed insights into guest behavior, booking lead times, and cancellation trends.

## Future Work

- Explore advanced machine learning techniques such as deep learning and ensemble models to improve prediction accuracy.
- Implement natural language processing (NLP) for sentiment analysis on guest reviews.
- Integrate Internet of Things (IoT) data for real-time monitoring of hotel operations.
- Expand data sources to include social media and web traffic for comprehensive market analysis.


## Acknowledgments/References

  - [Kaggle](https://www.kaggle.com)
  - [365 Data Science](https://365datascience.com/)
  - [Python Plain English](https://python.plainenglish.io/)
  - [Journal of Big Data - Springer](https://journalofbigdata.springeropen.com/)
  - [Towards Data Science](https://towardsdatascience.com/)
  - [Analytics Vidhya](https://www.analyticsvidhya.com/)
  - [Machine Learning Mastery](https://machinelearningmastery.com/)
