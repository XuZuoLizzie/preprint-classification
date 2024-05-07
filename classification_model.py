"""
@Project : COVID-19 Preprint classification
@File    : Download preprints
@Time    : 2021/1/8 10:41
@Author  : Xu Zuo
@Class   : BMI 6319 Spring 2021
"""

import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier

from feature_extraction import process_preprints_for_training


def train_svm(X_train, y_train):
    """
    Trains an SVM model on the provided training data.
    :param X_train: ndarray - The training features
    :param y_train: ndarray - The training labels
    :return: SVM model - The trained SVM model
    """
    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train, y_train)
    return svm_model


def train_xgboost(X_train, y_train):
    """
    Trains an XGBoost model on the provided training data.
    :param X_train: ndarray - The training features
    :param y_train: ndarray - The training labels
    :return: XGBoost model - The trained XGBoost model
    """
    xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    xgb_model.fit(X_train, y_train)
    return xgb_model


def evaluate_model(model, X_test, y_test):
    """
    Evaluates a model on the testing set and prints classification metrics.
    :param model: trained model - The model to be evaluated
    :param X_test: ndarray - The testing features
    :param y_test: ndarray - The testing labels
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", classification_report(y_test, predictions))


def main(filename):
    """
    Main function to load data, train, and evaluate SVM and XGBoost models.
    :param filename: str - The filename of the TSV file containing preprint data
    """
    X_train, X_test, y_train, y_test = process_preprints_for_training(filename)

    print("Training SVM model...")
    svm_model = train_svm(X_train, y_train)
    print("Evaluating SVM model...")
    evaluate_model(svm_model, X_test, y_test)

    print("Training XGBoost model...")
    xgb_model = train_xgboost(X_train, y_train)
    print("Evaluating XGBoost model...")
    evaluate_model(xgb_model, X_test, y_test)


if __name__ == "__main__":
    main("data/preprints.tsv")
