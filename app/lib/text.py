import logging
from typing import List

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.lib.element import ElementInfo


log = logging.getLogger("app")


def filter_out_similar(
    elements_list: List[ElementInfo], similarity_threshold: int = 0.2
) -> List[ElementInfo]:
    # Tokenize and stem the strings
    stemmer = PorterStemmer()
    stemmed_strings = [
        " ".join(
            [stemmer.stem(token) for token in word_tokenize(sentence.text.lower())]
        )
        for sentence in elements_list
    ]

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Compute the TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(stemmed_strings)

    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Filter out similar strings
    filtered_strings = []
    for i in range(len(elements_list)):
        is_similar = False
        for j in range(i + 1, len(elements_list)):
            if similarity_matrix[i][j] >= similarity_threshold:
                is_similar = True
                break
        if not is_similar:
            filtered_strings.append(elements_list[i])

    log.info(
        f"Elements was reduced by cosine similarity from {len(elements_list)} to {len(filtered_strings)}."
    )

    return filtered_strings
