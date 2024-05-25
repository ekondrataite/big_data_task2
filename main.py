
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    california = fetch_california_housing()

    print(california.DESCR)

    california_df = pd.DataFrame(california.data, columns=california.feature_names)

    california_df = california_df[['MedInc', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']]

    print("First few rows of the dataset:")
    print(california_df.head())

    print("\nPrimary Data Analysis:")

    print("\nChecking for missing values:")
    print(california_df.isnull().sum())

    print("\nSummary statistics:")
    print(california_df.describe())

    print("\nCorrelation matrix:")
    print(california_df.corr())

    print("\nCreating a regression model to predict house prices in California")

    X = california_df
    y = california.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123)

    print("\nShape of train set: {}".format(X_train.shape))
    print("Shape of test set: {}".format(X_test.shape))

    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)

    predictions = linear_regression.predict(X_test)

    print("\nModel evaluation:\n")
    print(f'The R2 score: {metrics.r2_score(y_test, predictions)}')
    print(f'The MSE: {metrics.mean_squared_error(y_test, predictions)}')

