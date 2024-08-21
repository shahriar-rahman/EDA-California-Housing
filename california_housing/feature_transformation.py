import python_utils.common_utils as cu
import pandas as pd
from sklearn import preprocessing
from plots import Visualize
input_path = "../dataset/interim/california_housing.csv"
save_path = "../reports/figures/"
output_path = "../dataset/processed/california_housing_"


def show_on_console(text, code):
    print('\n')
    print('-' * 150)
    print("◘ ", text)
    print(code)
    print('-' * 150)


def robust_scaling(df, new_columns):
    # One approach to standardizing input variables in the presence of outliers is to ignore the outliers
    # from the calculation of the mean and standard deviation, then use the calculated values to scale the variable.
    # This is called robust standardization or robust data scaling.
    scaler = preprocessing.RobustScaler()
    df_robust = scaler.fit_transform(df)
    df_robust = pd.DataFrame(df_robust, columns=new_columns)
    print(df_robust.sample(5))

    # Save the processed dataset
    cu.save_df(df=df_robust, ext_type='csv', path=output_path+"robust.csv")
    return df_robust


def standardization(df, new_columns):
    # Standardization is another scaling method where the values are centered around the mean with a unit std.
    # This means that the mean of the attribute becomes zero, and the resultant distribution has a unit std.
    scaler = preprocessing.StandardScaler()
    df_standard = scaler.fit_transform(df)
    df_standard = pd.DataFrame(df_standard, columns=new_columns)
    print(df_standard.sample(5))

    # Save the processed dataset
    cu.save_df(df=df_standard, ext_type='csv', path=output_path+"std.csv")
    return df_standard


def min_max_scaling(df, new_columns):
    # Also known as min-max normalization is the simplest method and consists in rescaling the range of features
    # to scale the range in [0, 1] or [−1, 1]. Selecting the target range depends on the nature of the data
    scaler = preprocessing.MinMaxScaler()
    df_minmax = scaler.fit_transform(df)
    df_minmax = pd.DataFrame(df_minmax, columns=new_columns)
    df_minmax.sample(5)

    # Save the processed dataset
    cu.save_df(df=df_minmax, ext_type='csv', path=output_path+"min_max.csv")
    return df_minmax


class FeatureTransformation:
    def __init__(self):
        self.input_path = input_path
        self.show = Visualize()
        self.save_path = save_path
        self.output_path = output_path

    def feature_transformation(self):
        df = cu.load_df(ext_type='csv', library='pd', path=self.input_path, d_type=False)
        show_on_console("Dataset inspection", df.head(10).to_string())

        # Inspect latitude & longitude data type
        show_on_console("latitude data type:", df['latitude'].dtype)
        show_on_console("longitude data type:", df['longitude'].dtype)

        # Transform features to round data to reduce feature complexity
        df['latitude'] = round(df['latitude'], 2)
        df['longitude'] = round(df['longitude'], 2)
        show_on_console("latitude:", df['latitude'].unique())
        show_on_console("longitude:", df['longitude'].unique())

        # A popular technique is to remove latitude & longitude.
        # However, truncating might lead to a loss of valuable information,
        # especially if the geographic resolution is important for the model's predictions.
        # Therefore, a safe option is to keep the aforementioned features and use Feature Scaling.

        # Apply different scaling procedures
        df_robust = robust_scaling(df, df.columns)
        df_standard = standardization(df, df.columns)
        df_minmax = min_max_scaling(df, df.columns)

        # Compare the effect of feature values for each scaler
        super_title = "Robust, Standard, and Min-Max Scaler distribution"
        self.show.plot_compare_kde(df_robust, df_standard, df_minmax, columns=df.columns, super_title=super_title,
                                   path=self.save_path)


if __name__ == "__main__":
    main = FeatureTransformation()
    main.feature_transformation()
