---
layout: single
title: "utils_data"
classes: wide
sidebar:
    nav: "sidebar-tutorials"
---

```python
import pandas as pd
import numpy as np
from IPython.core.display import display


def get_cats(df):
    # returns the number of different categories for each category as a dataframe object
    cats = []
    for col in df:
        if pd.api.types.is_string_dtype(df[col]):
            cats.append(len(df[col].unique()))
        else:
            cats.append(np.nan)
    return pd.DataFrame(cats, index=df.columns, columns=['categories'])


def df_info(df: pd.DataFrame,
            show_rows: int = 2,
            horizontal: bool = True,
            percentiles: tuple = (.25, .5, .75),
            includes: tuple = ("objects", "numeric", "bool"),
            selected_cols: list = None
            ):

    df = df.copy()

    # you can either exclude some data types or specify columns to
    # reduce the numbers of columns which are being analyzed
    if 'objects' not in includes:
        # "objects" refers to string type columns
        for col in df:
            if pd.api.types.is_string_dtype(df[col]):
                df.drop([col], axis=1, inplace=True)
    elif 'numeric' not in includes:
        for col in df:
            if pd.api.types.is_numeric_dtype(df[col]):
                df.drop([col], axis=1, inplace=True)
    elif 'bool' not in includes:
        for col in df:
            if pd.api.types.is_numeric_dtype(df[col]):
                df.drop([col], axis=1, inplace=True)

    if df.empty: raise ValueError(f'The DataFrame is empty!')

    # in case you just want information on certain columns, specify those columns in selected_cols
    # -> be aware that those column dtypes have to be in the includes list
    if selected_cols:
        df = df[selected_cols]

    # data types
    types = pd.DataFrame(df.dtypes, columns=["dtype"])

    # description of the dataframe (mean, median, std, min-max values)
    if 'numeric' in includes:
        descr = df.describe(percentiles=percentiles).drop(["count"])
    else:
        descr = pd.DataFrame()

    # count missing values
    nans = pd.DataFrame(df.isnull().sum(), columns=["missing"])

    # count how many categories are contained in each string type column
    if 'strings' in includes:
        cats = get_cats(df)
    else:
        cats = pd.DataFrame()

    # show the first few rows depending on how many you want to show
    head = df.head(show_rows)

    # display resulting df either vertically or horizontally
    if horizontal:
        info_df = pd.concat([types, nans, cats, descr.T, head.T], axis=1)
    else:
        info_df = pd.concat([types.T, nans.T, cats.T, descr, head], axis=0)

    # show all rows and columns, no matter how large the actual dataframe is
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        # do not permanently change pandas settings -> with statement
        display(info_df)
```
