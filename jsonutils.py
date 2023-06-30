import pandas as pd
from pandas import DataFrame


# this class reads json file passed as parameter as a pandas dataframe
class JsonUtils:
    @staticmethod
    def read_json(url) -> DataFrame:
        df = pd.read_json(url)
        df['index'] = df.index
        df['delta_corners'] = df['rb_corners'] - df['gt_corners']
        return df
