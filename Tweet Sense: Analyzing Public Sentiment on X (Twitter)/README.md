# Tweet Sense: Sentiment Analysis of Tweets Using Natural Language Processing

## Project Overview

"Tweet Sense" aims to analyze the sentiment of tweets using advanced Natural Language Processing (NLP) techniques. By applying machine learning models, this project identifies the sentiment behind tweets—whether positive, negative, or neutral. This analysis provides insights into public opinion, brand perception, and trends on social media platforms.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation and Setup](#installation-and-setup)
3. [Python Packages Used](#python-packages-used)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Results and Evaluation](#results-and-evaluation)
7. [Future Work](#future-work)
8. [Acknowledgments/References](#acknowledgmentsreferences)

## Installation and Setup

1. **Install Anaconda:** Download and install Anaconda from [Anaconda's official website](https://www.anaconda.com/products/distribution).
2. **Open Anaconda Navigator:** Launch Anaconda Navigator from your application menu or command line.
3. **Open Jupyter Notebook:** Click on the Jupyter Notebook icon in Anaconda Navigator to open it in your web browser.
4. **Create or Open a Notebook:** Create a new notebook or open an existing one to start working with Python.

## Python Packages Used

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- nltk
- tweepy
- textblob
- vaderSentiment

## Data

The dataset used for this term project can be accessed on Kaggle and includes 74,682 records for training and 1,000 records for validation. Each record represents a tweet categorized into different sentiment classes. The dataset comprises the following key variables:

- Tweet_ID: A unique identifier for each tweet.
- Entity: The source or context of the tweet, such as a game or brand name.
- Sentiment: The sentiment classification of the tweet (e.g., Positive, Negative, Neutral, or Irrelevant).
- Tweet_content: The actual text of the tweet, which serves as the primary input for sentiment analysis.
- 
This dataset includes labeled tweets that will be used for training and validating sentiment analysis models.

## Source Data

The dataset used in this project was sourced from Kaggle's Safe Acquifiers Dataset). Ensure you download the dataset and place it in the appropriate directory within the project folder.

## Results and Evaluation

### Key Findings:
- The sentiment analysis models successfully classified tweets into positive, negative, and neutral categories.
- TextBlob and VADER sentiment analysis libraries provided comparable results, with VADER showing slightly better performance on short, informal text.
- The analysis revealed trends in public sentiment towards specific events or brands.

### Model Performance:
Various models and libraries were evaluated, including TextBlob, VADER, and custom machine learning models. Evaluation metrics include accuracy, precision, recall, and F1-score.

## Future Work

Future enhancements for this project include:
- Implementing deep learning models such as LSTM or BERT for improved sentiment classification.
- Incorporating additional features such as tweet hashtags and mentions for more nuanced analysis.
- Expanding the dataset to include a wider variety of topics and tweet sources.

## Acknowledgments/References

- [Tweepy](https://www.tweepy.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
- [NLTK](https://www.nltk.org/)
- [Machine Learning Mastery - Sentiment Analysis](https://machinelearningmastery.com/sentiment-analysis/)
- [Kaggle - Sentiment Analysis](https://www.kaggle.com)
