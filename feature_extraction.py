"""
@Project : COVID-19 Preprint classification
@File    : Download preprints
@Time    : 2021/1/7 19:10
@Author  : Xu Zuo
@Class   : BMI 6319 Spring 2021
"""

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import spacy
from imblearn.over_sampling import SMOTE


def load_data(filename):
    """
    Loads data from a TSV file.
    :param filename: str - The filename of the TSV file to load
    :return: DataFrame - The loaded data
    """
    data = pd.read_csv(filename, sep='\t')
    return data


def preprocess_data(data):
    """
    Preprocesses the data by encoding labels and handling missing values.
    :param data: DataFrame - The data to preprocess
    :return: DataFrame, LabelEncoder - The preprocessed data and the label encoder used
    """
    # Encode categorical labels
    label_encoder = LabelEncoder()
    data['Label'] = label_encoder.fit_transform(data['Label'])

    # Fill missing values if any
    data = data.fillna('')

    return data, label_encoder


def generate_embeddings(data):
    """
    Generates word embeddings for each abstract using a SciSpaCy model.
    :param data: DataFrame - The data containing text in the 'Abstract' column
    :return: list - A list of embedding vectors
    """
    nlp = spacy.load("en_core_sci_lg")
    embeddings = [nlp(text).vector for text in data['Abstract']]
    return np.array(embeddings)


def balance_data(features, labels):
    """
    Balances the dataset using SMOTE to over-sample the minority classes.
    :param features: list - The features of the data
    :param labels: list - The labels of the data
    :return: list, list - The balanced features and labels
    """
    # Count the number of instances per class
    label_counts = Counter(labels)
    min_samples = min(label_counts.values())
    k_neighbors = max(min_samples - 1, 1)  # Ensure at least one neighbor

    smote = SMOTE(k_neighbors=k_neighbors, random_state=42)
    features_balanced, labels_balanced = smote.fit_resample(features, labels)
    return features_balanced, labels_balanced


def split_data(features, labels):
    """
    Splits the data into training and testing sets.
    :param features: list - The features of the data
    :param labels: list - The labels of the data
    :return: tuple - Training and testing datasets
    """
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def process_preprints_for_training(filename):
    """
    Processes preprint data from a TSV file for training: loads data, preprocesses it,
    generates embeddings, balances classes, and splits into train/test datasets.
    :param filename: str - The filename of the TSV file containing preprint data
    :return: tuple - Training and testing datasets (X_train, X_test, y_train, y_test)
    """
    data = load_data(filename)
    data, label_encoder = preprocess_data(data)
    embeddings = generate_embeddings(data)
    features_balanced, labels_balanced = balance_data(embeddings, data['Label'].tolist())
    X_train, X_test, y_train, y_test = split_data(features_balanced, labels_balanced)
    return X_train, X_test, y_train, y_test


def check_class_distribution(labels):
    """
    Prints the distribution of classes.
    :param labels: Series or array - The labels of the data
    """
    from collections import Counter
    class_counts = Counter(labels)
    print("Class Distribution:", class_counts)
    return class_counts


if __name__ == "__main__":
    process_preprints_for_training("data/preprints.tsv")
    # data = load_data("data/preprints.tsv")
    # check_class_distribution(data["Label"])
