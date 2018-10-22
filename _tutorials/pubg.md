---
title: PUBG Finish Placement
date: 2018-10-20T
header:
  teaser: assets/images/tutorials/pubg/PUBG_teaser.jpg
  overlay_image: /assets/images/tutorials/pubg/overlay_pubg.jpg
excerpt: ""
categories:
  - programming
  - kaggle
  - tutorial
tags:
  - python
  - competition
feature_row:
        - image_path: /assets/images/pexels-photo-1492239.jpeg
          alt: "Image Placeholder Code Snippets"
          caption: "To code snippets"
          url: /code-archive/
        - image_path: /assets/images/pexels-photo-1492239.jpeg
          alt: "Image Placeholder Code Snippets"
          url: "/code-archive/"
          btn_label: "To Code Snippets"
          btn_class: "btn--info"
---
# What's the best strategy to win in PUBG?

Objective:
- Predict 

Data:
- 65,000 games' worth of anonymized player data

<h2>Project Folder Tree</h2>

```bash
pubg project                # project name
├── data                    # folder which contains data sets
|  └── train.csv            # train sample
|  └── test.csv             # test sample
├── pubg.ipynb              # main file
├── utils_data.py           # contains some utility functions
```

## Lets get it started

![PUBG Start](https://media3.giphy.com/media/3oKIPmaM8aFolCcuI0/giphy.gif?cid=3640f6095bcd07f94d6745734149843e)

```python
%matplotlib inline

import pandas as pd
import numpy as np

from data_utils import df_info
```

We will start by importing required packages and loading the training set. `data_utils` is a file I prepared in advance some useful function utilities especially when working with tabular data.
You can view the code of the file [here](/code_snippets/utils_data/).

**Tip!** The `csv_read()` parameter `nrows=` can be used to limit the number of imported rows to the number given. This might be practical for performance reasons in case you don't need the whole dataset and just want to do some minor data analysis or for function testing purposes etc.. If `nrows=None` everything will be loaded.
{: .notice--info}

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)


```python
train = pd.read_csv("data/train.csv", nrows=None)
```

In the following I will use some functions I prepared in advance. You can view the code for the functions [here](/code_snippets/utils_data/).

```python
def get_cats(df):
    cats = []
    for col in df:
        if pd.api.types.is_string_dtype(df[col]):
            cats.append(len(df[col].unique()))
        else:
            cats.append(np.nan)
    return pd.DataFrame(cats, index=df.columns, columns=['categories'])


def df_info(df: pd.DataFrame, show_rows: int=2, horizontal: bool=True, percentiles: list=[.25, .5, .75], selected_cols: list=None, includes: str=None): 
    df = df.copy()
    if includes == 'objects':
        for col in df:
            if not pd.api.types.is_string_dtype(df[col]): 
                df.drop([col], axis=1, inplace=True)
    elif includes == 'numeric':
        for col in df:
            if not pd.api.types.is_numeric_dtype(df[col]): 
                df.drop([col], axis=1, inplace=True)
    if df.empty: raise ValueError(f'No "{includes}" type columns!')
    
    # in case you just want information on certain rows, specify those columns in selected_cols
    if selected_cols:
        df = df[selected_cols]
    
    # data types
    types = pd.DataFrame(df.dtypes, columns=["dtype"])
    
    # description of the dataframe (mean, median, std, min-max values)
    descr = df.describe(percentiles=percentiles).drop(["count"])
    
    # count missing values
    nans = pd.DataFrame(df.isnull().sum(), columns=["missings"])
    
    # count how many categories are contained in each string type column
    cats = get_cats(df)
    
    # show the first few rows depending on how many you want to show
    head = df.head(show_rows)
    
    # display it either vertically or horizontally
    if horizontal:
        info_df = pd.concat([types, nans, cats, descr.T, head.T], axis=1)
    else:
        info_df = pd.concat([types.T, nans.T, cats.T, descr, head], axis=0)
            
    # show all rows and columns, no matter how large the dataframe is
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        display(info_df) 
```


```python
df_info(train, horizontal=False, percentiles=[.5], includes="all")
```


<div style="overflow-y:auto;">
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>groupId</th>
      <th>matchId</th>
      <th>assists</th>
      <th>boosts</th>
      <th>damageDealt</th>
      <th>DBNOs</th>
      <th>headshotKills</th>
      <th>heals</th>
      <th>killPlace</th>
      <th>killPoints</th>
      <th>kills</th>
      <th>killStreaks</th>
      <th>longestKill</th>
      <th>maxPlace</th>
      <th>numGroups</th>
      <th>revives</th>
      <th>rideDistance</th>
      <th>roadKills</th>
      <th>swimDistance</th>
      <th>teamKills</th>
      <th>vehicleDestroys</th>
      <th>walkDistance</th>
      <th>weaponsAcquired</th>
      <th>winPoints</th>
      <th>winPlacePerc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>dtype</th>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>float64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>float64</td>
      <td>int64</td>
      <td>int64</td>
      <td>int64</td>
      <td>float64</td>
      <td>int64</td>
      <td>float64</td>
      <td>int64</td>
      <td>int64</td>
      <td>float64</td>
      <td>int64</td>
      <td>int64</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>missings</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>categories</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>499.5</td>
      <td>1.75983e+06</td>
      <td>499.5</td>
      <td>0.371</td>
      <td>1.134</td>
      <td>174.757</td>
      <td>0.964</td>
      <td>0.341</td>
      <td>1.391</td>
      <td>42.427</td>
      <td>1116.12</td>
      <td>1.322</td>
      <td>0.699</td>
      <td>25.3916</td>
      <td>41.064</td>
      <td>39.613</td>
      <td>0.199</td>
      <td>387.059</td>
      <td>0.003</td>
      <td>3.97792</td>
      <td>0.014</td>
      <td>0.006</td>
      <td>1087.49</td>
      <td>3.717</td>
      <td>1506.99</td>
      <td>0.486571</td>
    </tr>
    <tr>
      <th>std</th>
      <td>288.819</td>
      <td>877624</td>
      <td>288.819</td>
      <td>0.817329</td>
      <td>1.70908</td>
      <td>230.343</td>
      <td>1.7337</td>
      <td>0.809552</td>
      <td>2.77954</td>
      <td>28.4318</td>
      <td>150.125</td>
      <td>2.17372</td>
      <td>0.806877</td>
      <td>51.0182</td>
      <td>23.7698</td>
      <td>23.1409</td>
      <td>0.547447</td>
      <td>1095.86</td>
      <td>0.0948683</td>
      <td>21.0137</td>
      <td>0.133498</td>
      <td>0.0772656</td>
      <td>1142.88</td>
      <td>2.97755</td>
      <td>39.9435</td>
      <td>0.316501</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>908</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1349</td>
      <td>0</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>499.5</td>
      <td>1.98371e+06</td>
      <td>499.5</td>
      <td>0</td>
      <td>0</td>
      <td>100</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>38</td>
      <td>1057.5</td>
      <td>1</td>
      <td>1</td>
      <td>1.406</td>
      <td>29</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>581.55</td>
      <td>3</td>
      <td>1500</td>
      <td>0.4792</td>
    </tr>
    <tr>
      <th>max</th>
      <td>999</td>
      <td>2.7006e+06</td>
      <td>999</td>
      <td>7</td>
      <td>10</td>
      <td>2285</td>
      <td>22</td>
      <td>8</td>
      <td>29</td>
      <td>98</td>
      <td>1792</td>
      <td>26</td>
      <td>4</td>
      <td>415.4</td>
      <td>100</td>
      <td>99</td>
      <td>5</td>
      <td>8197</td>
      <td>3</td>
      <td>251.8</td>
      <td>2</td>
      <td>1</td>
      <td>5176</td>
      <td>37</td>
      <td>1744</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>247.3</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>17</td>
      <td>1050</td>
      <td>2</td>
      <td>1</td>
      <td>65.32</td>
      <td>29</td>
      <td>28</td>
      <td>1</td>
      <td>591.3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>782.4</td>
      <td>4</td>
      <td>1458</td>
      <td>0.8571</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>440875</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>37.65</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>45</td>
      <td>1072</td>
      <td>1</td>
      <td>1</td>
      <td>13.55</td>
      <td>26</td>
      <td>23</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>119.6</td>
      <td>3</td>
      <td>1511</td>
      <td>0.04</td>
    </tr>
  </tbody>
</table>
</div>



```python
def trn_val_split(df, size=0.8):
    idxs = np.random.permutation(range(len(df)))[:int(len(df) * size)]
    trn, val = df.iloc[idxs], df.drop([idxs])
    return trn, val
```

{% include feature_row %}
