# Exploratory Data Analysis for California Housing
An exploratory analysis of the California Housing dataset from Sci-kit Learn module.

<br/>

![alt text](https://github.com/shahriar-rahman/EDA-California-Housing/blob/main/assets/readme_images/GettyImages_619686566.jpg)\
'Busy City Street in New York, United States' by Andres Escalona Vergara  |  [Pexels Licensed](https://www.pexels.com/)

<br/>
 
<p align="left">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" /> 
<img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" />
<img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?style=for-the-badge&logo=cookiecutter" />
</p>


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/shahriar-rahman/EDA-California-Housing/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/shahriar-rahman/EDA-California-Housing/blob/main/LICENSE)
[![GitHub branches](https://badgen.net/github/branches/shahriar-rahman/EDA-California-Housing)](https://github.com/shahriar-rahman/EDA-California-Housing/)
[![GitHub commits](https://badgen.net/github/commits/shahriar-rahman/EDA-California-Housing)](https://GitHub.com/shahriar-rahman/EDA-California-Housing/commit/)
[![GitHub issues-open](https://badgen.net/github/open-issues/shahriar-rahman/EDA-California-Housing)](https://github.com/shahriar-rahman/EDA-California-Housing/issues?q=is%3Aopen)
[![GitHub issues](https://img.shields.io/github/issues/shahriar-rahman/EDA-California-Housing.svg)](https://GitHub.com/shahriar-rahman/EDA-California-Housing/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/shahriar-rahman/EDA-California-Housing.svg)](https://GitHub.com/shahriar-rahman/EDA-California-Housing/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/shahriar-rahman/EDA-California-Housing.svg)](https://GitHub.com/shahriar-rahman/EDA-California-Housing/pull/)

<br/>

### ◘ Data Definition
 Attributes and the target

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

<br/><br/>

### ◘ Data Dictionary
| features | dtype | mean value | standard deviation | min | max | 
| :-: | :-: | :-: | :-: | :-: | :-: | 
| medinc | float64 | 3.9 | 1.9 | 0.5 | 15.0 | 
| houseage | float64 | 28.6 | 12.6 | 1.0 | 52.0 | 
| averooms | float64 | 5.4 | 2.5 | 0.8 | 141.9 | 
| avebedrms | float64 | 1.1 | 0.5 | 0.3 | 34.1 | 
| population | float64 | 1425.5 | 1132.5 | 3.0 | 35682.0 | 
| aveoccup | float64 | 3.1 | 10.4 | 0.7 | 1243.3 |  |
| latitude | float64 | 35.6 | 2.1 | 32.5 | 42.0 |  |
| longitude | float64 | -119.6 | 2.0 | -124.3 | -114.3 | 
| medhouseval | float64 | 2.1 | 1.2 | 0.1 | 5.0 | 

<br/><br/>

### ◘ Dataset Information
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

<br/><br/>

### ◘ Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- folder containing dataset description and definition.
│
│
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         xai and configuration for tools like black
│
│
├── reports            <- Generated analysis
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
│
└── california_housing   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes xai a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── feature_exploration.py       <- Code for exploring dataset
    │
    ├── feature_cleaning.py       <- Code to clean or simplify dataset
    │
    ├── aggregating_statistics.py       <- Code to explore the statistical aspect of the features
    │
    ├── feature_transformation          < - Transform features to prepare data
    │
    └── plots.py                <- Code to create visualizations
```

<br/><br/>

### ◘ Methodologies & Technologies applied
* Diagnose and fix structural errors
* Check and Clean data
* Address duplicates & outliers
* Logical feature amalgamation to construct a unique variable
* Univariate inspection
* Bivariate inspection
* Multivariate Inspection
* Feature correlations
* Seaborn & Matplotplib visualizations

<br/><br/>

![alt text](https://github.com/shahriar-rahman/EDA-California-Housing/blob/main/assets/readme_images/edaFlowchart.png)

<br/><br/>

### ◘ Execution Sequence
The following scripts are to be executed in the subsequent orders:
1. dataset.py
2. feature_exploration.py
3. feature_cleaning.py
4. aggregating_statistics
5. feature_transformation

<br/><br/>

### ◘ Requirements
* matplotlib==3.7.1
* numpy==1.24.2
* pandas==2.0.0
* scikit-learn==1.2.2
* python_utils @ git+https://github.com/shahriar-rahman/Python-Utils@9c54c9a3204fceaaeeca048096f5004f1c058f99

<br/><br/>

### ◘ Dependency Commands (using pip)
To install any modules, type the following commands:
1. For Pandas, run:
```
pip install pandas                                                  
```
2. To install missingNo:
```
pip install missingno                                                  
```
3. Matplotlib can be installed by running the following command:
```
pip install matplotlib
```
4. For scikit-learn:
```
pip install scikit-learn
```
5. Lastly, for seaborn:
```
pip install seaborn
```

<br/><br/>

### ◘ Package Imports
To *import* the dependencies, simply open the preferred IDE or Notebook: 
1. For Pandas, run the following command:
```
import pandas as pd                                   
```
2. To use missingno, run:
```
import missingno as msn                                      
```  
3. Import matplotlib using:
```
import matplotlib.pyplot as plt                                     
```
4. Scikit-learn can be introduced by:
```
import sklearn
```
5. Seaborn can be accessed by:
```
import seaborn as sns                                      
```

<br/><br/>

### ◘ Supplementary Resources
* https://pypi.org/project/pandas/
* https://pypi.org/project/matplotlib/
* https://pypi.org/project/seaborn/
* https://pypi.org/project/missingno/
* https://pypi.org/project/scikit-learn/

<br/><br/>

--------

