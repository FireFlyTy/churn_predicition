import pandas as pd
from utils import *
from sklearn.utils import resample
from config import *
from sklearn.model_selection import train_test_split


def data_prepare_resample():

    df = pd.read_excel(get_resource_path('Churn.xls'))
    df.columns = COLUMN_NAMES
    data_majority = df[df['churn'] == 0]
    data_minority = df[df['churn'] == 1]
    data_minority_upsampled = resample(data_minority,
                                       replace=True,
                                       n_samples=2850,
                                       random_state=1)

    data_upsampled = pd.concat([data_majority, data_minority_upsampled])

    X_r = pd.DataFrame(data=data_upsampled, columns=FEATURES)
    y_r = data_upsampled['churn']

    X_train, X_test, y_train, y_test = train_test_split(X_r,
                                                        y_r,
                                                        test_size=0.33,
                                                        random_state=7)

    return X_train, X_test, y_train, y_test


def data_prepare():

    df = pd.read_excel(get_resource_path('Churn.xls'))
    df.columns = COLUMN_NAMES
    X = pd.DataFrame(data=df, columns=FEATURES)
    y = df['churn']
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=7)

    return X_train, X_test, y_train, y_test