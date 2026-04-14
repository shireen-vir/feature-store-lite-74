class FeatureStoreLite74Exception(Exception):
    """Base exception class for feature-store-lite-74."""

class InvalidInputError(FeatureStoreLite74Exception):
    """Raised when invalid input is provided."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Loads data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise InvalidInputError("Invalid file path or file format.")

def split_data(data, test_size=0.2, random_state=42):
    """Splits data into training and testing sets."""
    try:
        X = data.drop('target', axis=1)
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        raise InvalidInputError("Invalid data or target column not found.")

def main():
    """Main function for feature-store-lite-74."""
    file_path = 'data.csv'
    data = load_data(file_path)
    X_train, X_test, y_train, y_test = split_data(data)
    print("Data loaded and split successfully.")

if __name__ == "__main__":
    main()