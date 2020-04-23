import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def split_my_data(df, train_pct):
    '''
    Takes in df, train_pct and returns 2 items:
    train, test

    When using this function, in order to have usable datasets, be sure to call it thusly:
    train, test = split_my_data(df, train_pct)
    '''
    return train_test_split(df, train_size = train_pct, random_state = 294)

#### Encoder Functions ####
def ohe_encoder(df, col):
    encoded_values = sorted(list(df[col].unique()))
    le = preprocessing.LabelEncoder()
    enc = le.fit_transform(df[col])
    ohe_array = np.array(enc).reshape(len(enc), 1)
    ohe = preprocessing.OneHotEncoder(sparse=False, categories='auto')
    df_ohe = ohe.fit_transform(ohe_array)
    enc = pd.DataFrame(data=df_ohe, columns=encoded_values, index=df.index)
    df = df.join(enc)
    return df

def boolean_labeler(df, col):
    le = preprocessing.LabelEncoder()
    df[f'{col}_enc'] = le.fit_transform(df[col])
    return df

def more_than_two_labels(df, col):
    df[f'{col}_enc'] = np.where(df[col] == 'No', 0,
                                np.where(df[col] == 'Yes', 1, 0))
    return df

#### New Feature Functions ####
def months_to_years(df, col):
    df[f'{col}_months'] = (df[col] / 12).round(2)
    return df

def extra_lines(df):
    df['extra_lines'] = np.where(df['multiple_lines'] == 'Yes', 2,
                                np.where(df['multiple_lines'] == 'No', 1, 0))
    return df

def family_support(df):
    df['family_support'] = np.where( (df['partner'] == 'No') & (df['dependents'] == 'Yes'), 3,
                                    np.where( (df['partner'] == 'Yes') & (df['dependents'] == 'Yes'), 2,
                                             np.where( (df['partner'] == 'Yes') & (df['dependents'] == 'No'), 1, 0)))
    return df

def has_internet(df):
    df['has_internet'] = np.where(df.internet_service_type_id == 3, 0, 1)
    return df

def internet_services(df):
    df['internet_services'] = (df.has_internet + 
                               df.online_security_enc + 
                               df.online_backup_enc + 
                               df.tech_support_enc + 
                               df.streaming_tv_enc + 
                               df.streaming_movies_enc + 
                               df.device_protection_enc)
    return df

#### Scaler Functions ####
def standard_scaler(train, test):
    '''
    Uses the train & test datasets created by the split_my_data function
    Returns 3 items: std_scaler, train_scaled_std, test_scaled_std

    Scales datasets to Standard Normal Distribution (mean=0, stdev=1)
    '''
    std_scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)
    train_scaled_std = pd.DataFrame(std_scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled_std = pd.DataFrame(std_scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return std_scaler, train_scaled_std, test_scaled_std

def scale_inverse(std_scaler, train_scaled_std, test_scaled_std):
    '''
    Takes in the scaler and datasets created by the standard_scaler function
    returns scaled data to it's original values
    '''
    train_unscaled = pd.DataFrame(std_scaler.inverse_transform(train_scaled_std), columns=train_scaled_std.columns.values).set_index([train_scaled_std.index.values])
    test_unscaled = pd.DataFrame(std_scaler.inverse_transform(test_scaled_std), columns=test_scaled_std.columns.values).set_index([test_scaled_std.index.values])
    return train_unscaled, test_unscaled

def uniform_scaler(train, test):
    '''
    Uses the train & test datasets created by the split_my_data function
    Returns 3 items: unf_scaler, train_scaled_unf, test_scaled_unf

    This is a non-linear transformer, and it smooths out unusual distributions.
    It spreads out the most frequent values and reduces the impact of (marginal) outliers, therefore it is robust.
    It distorts correlations and distances within and across features.
    '''
    unf_scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(train)
    train_scaled_unf = pd.DataFrame(unf_scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled_unf = pd.DataFrame(unf_scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return unf_scaler, train_scaled_unf, test_scaled_unf

def gaussian_scaler(train, test):
    '''
    Uses the train & test datasets created by the split_my_data function
    Returns 3 items: gs_scaler, train_scaled_gs, test_scaled_gs

    Scale to Gaussian-like distribution using a PowerTransformer
    This uses the Yeo-Johnson method to transform the dataset to resemble standard normal distrubtion.
    '''
    gs_scaler = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(train)
    train_scaled_gs = pd.DataFrame(gs_scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled_gs = pd.DataFrame(gs_scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return gs_scaler, train_scaled_gs, test_scaled_gs

def min_max_scaler(train, test):
    '''
    Uses the train & test datasets created by the split_my_data function
    Returns 3 items: mm_scaler, train_scaled_mm, test_scaled_mm

    This is a linear transformation. Values will lie between 0 and 1
    '''
    mm_scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    train_scaled_mm = pd.DataFrame(mm_scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled_mm = pd.DataFrame(mm_scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return mm_scaler, train_scaled_mm, test_scaled_mm

def iqr_robust_scaler(train, test):
    '''
    Uses the train & test datasets created by the split_my_data function
    Returns 3 items: iqr_scaler, train_scaled_iqr, test_scaled_iqr

    Used for data with outliers. Median is removed, and data is scaled to the IQR
    '''
    iqr_scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    train_scaled_iqr = pd.DataFrame(iqr_scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled_iqr = pd.DataFrame(iqr_scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return iqr_scaler, train_scaled_iqr, test_scaled_iqr


