class FeatureStoreLite74:
    """
    A lightweight data science tool for managing and processing features.

    This class provides basic functionality for loading, transforming, and saving features.
    It is designed to be a simplified alternative to more comprehensive feature stores.
    """

    def __init__(self):
        pass

    def load_features(self, file_path):
        # Load features from a file
        import pandas as pd
        return pd.read_csv(file_path)

    def transform_features(self, features):
        # Apply basic transformations to the features
        features['new_feature'] = features['existing_feature'] * 2
        return features

    def save_features(self, features, file_path):
        # Save the features to a new file
        features.to_csv(file_path, index=False)


def main():
    feature_store = FeatureStoreLite74()
    file_path = 'features.csv'
    features = feature_store.load_features(file_path)
    transformed_features = feature_store.transform_features(features)
    feature_store.save_features(transformed_features, 'transformed_features.csv')


if __name__ == '__main__':
    main()