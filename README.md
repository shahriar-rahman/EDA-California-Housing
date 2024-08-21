# ◘ Explainable Artificial Intelligence (XAI)

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

An exploratory analysis of the California Housing dataset from Sci-kit Learn.


## • Data Definition
 attributes and the target

    :Attribute Information:
        - MedInc        median income in block group
        - HouseAge      median house age in block group
        - AveRooms      average number of rooms per household
        - AveBedrms     average number of bedrooms per household
        - Population    block group population
        - AveOccup      average number of household members
        - Latitude      block group latitude
        - Longitude     block group longitude

    :Missing Attribute Values: None

This dataset was obtained from the StatLib repository.
https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html

The target variable is the median house value for California districts,
expressed in hundreds of thousands of dollars ($100,000).

This dataset was derived from the 1990 U.S. census, using one row per census
block group. A block group is the smallest geographical unit for which the U.S.
Census Bureau publishes sample data (a block group typically has a population
of 600 to 3,000 people).

A household is a group of people residing within a home. Since the average
number of rooms and bedrooms in this dataset are provided per household, these
columns may take surprisingly


## • Data Dictionary
| features | dtype | mean value | standard deviation | min | max | description |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| medinc | float64 | 3.9 | 1.9 | 0.5 | 15.0 |  |
| houseage | float64 | 28.6 | 12.6 | 1.0 | 52.0 |  |
| averooms | float64 | 5.4 | 2.5 | 0.8 | 141.9 |  |
| avebedrms | float64 | 1.1 | 0.5 | 0.3 | 34.1 |  |
| population | float64 | 1425.5 | 1132.5 | 3.0 | 35682.0 |  |
| aveoccup | float64 | 3.1 | 10.4 | 0.7 | 1243.3 |  |
| latitude | float64 | 35.6 | 2.1 | 32.5 | 42.0 |  |
| longitude | float64 | -119.6 | 2.0 | -124.3 | -114.3 |  |
| medhouseval | float64 | 2.1 | 1.2 | 0.1 | 5.0 |  |


## • Dataset Information
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 9 columns):
| Index | Column | Non-Null Count | Dtype |
| :-: | :-: | :-: | :-: |
 |0 | medinc | 20640 non-null | float64 |
 |1 | houseage | 20640 non-null | float64 |
 |2 | averooms | 20640 non-null | float64 |
 |3 | avebedrms | 20640 non-null | float64 |
 |4 | population | 20640 non-null | float64 |
 |5 | aveoccup | 20640 non-null | float64 |
 |6 | latitude | 20640 non-null | float64 |
 |7 | longitude | 20640 non-null | float64 |
 |8 | medhouseval | 20640 non-null | float64 |
dtypes: float64(9)
memory usage: 1.4 MB


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         xai and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── xai   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes xai a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```
### ◘ Execution Sequence
1. After installation, the 'dataset.py' needs to be executed.
2. Next is 'feature_exploration.py'.
3. Followed by 'feature_cleaning.py'
--------

