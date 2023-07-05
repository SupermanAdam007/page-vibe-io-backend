import logging

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import cmudict

log = logging.getLogger("app")

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

pronunciation_dict = cmudict.dict()


def get_text_sentiment(text: str):
    # Analyze the sentiment of the text
    sentiment_scores = sia.polarity_scores(text)

    # Extract the sentiment polarity score
    sentiment_score = sentiment_scores['compound']

    # Scale the sentiment score to the range of 1 to 10
    scaled_score = round((sentiment_score + 1) * 5)

    # Ensure the scaled score is within the range of 1 to 10
    scaled_score = max(1, min(10, scaled_score))

    # Print the scaled sentiment score
    log.info(f"Sentiment Score scaled: {scaled_score}, raw: {sentiment_score}")

    return scaled_score


def get_text_readibility_and_complexity(text: str):
    # Tokenize the text into sentences and words
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)

    # Count the number of words and sentences
    word_count = len(words)
    sentence_count = len(sentences)

    # Calculate the average number of syllables per word
    def count_syllables(word):
        if word.lower() in pronunciation_dict:
            return [len(list(y for y in x if y[-1].isdigit())) for x in pronunciation_dict[word.lower()]][0]
        else:
            return 0

    syllable_count = sum(count_syllables(word) for word in words)
    avg_syllables_per_word = syllable_count / word_count

    # Calculate the Flesch Reading Ease score
    flesch_reading_ease = 206.835 - (1.015 * (word_count / sentence_count)) - (84.6 * (avg_syllables_per_word))

    # Scale the Flesch Reading Ease score to the range of 1 to 10
    scaled_flesch_reading_ease = round((flesch_reading_ease - 0) * (10 - 1) / (100 - 0) + 1)

    # Calculate the Flesch-Kincaid Grade Level
    flesch_kincaid_grade_level = (0.39 * (word_count / sentence_count)) + (11.8 * (avg_syllables_per_word)) - 15.59

    # Scale the Flesch-Kincaid Grade Level score to the range of 1 to 10
    scaled_flesch_kincaid_grade_level = round((flesch_kincaid_grade_level - 0) * (10 - 1) / (20 - 0) + 1)

    # Ensure the scaled scores are within the range of 1 to 10
    scaled_flesch_reading_ease = max(1, min(10, scaled_flesch_reading_ease))
    scaled_flesch_kincaid_grade_level = max(1, min(10, scaled_flesch_kincaid_grade_level))

    # Print the calculated metrics
    log.info(f"Flesch Reading Ease scaled: {scaled_flesch_reading_ease}, raw: {flesch_reading_ease}")
    log.info(f"Flesch-Kincaid Grade Level scaled: {scaled_flesch_kincaid_grade_level}, raw: {flesch_kincaid_grade_level}")

    return scaled_flesch_reading_ease, scaled_flesch_kincaid_grade_level
