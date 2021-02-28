## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [Technologies](#technologies)
* [Sources](#sources)
* [Project organization](#project-organization)


## General info
First simple classifiers for the titanic dataset from kaggle https://www.kaggle.com/hesh97/titanicdataset-traincsv
I used jupyter notebooks to make myself a data exploration and data cleaning collection for future use. <br>

The project organization at the bottom shows where I want to go. The next step is to make the model portable. I recommend to look inside the notebooks to see what I am doing. I trained a logistic regression classifier, a decision tree classifier (once with entropy, once with gini) and a support vector machine. <p>
  
The accuracy of the models so far: <br>
Logistic Regression classifier: 83% <br>
Decision Tree classifier: 78% <br>
SVM: 82%

## Sources
Kaggle

## Requirements
Jupyter Notebook

## Technologies
Jupyter Notebook, Python3, Numpy, Pandas, Seaborn, matplotlib, sklearn, Support Vector Machine, Decision Tree Classifier, Logistic Regression Classifier

## Illustrations
<img src="https://user-images.githubusercontent.com/78420756/109414369-ca4b3c80-79b2-11eb-9ac1-31e2af9c03d6.PNG" width="320" height="500"> <img src="https://user-images.githubusercontent.com/78420756/109414440-3cbc1c80-79b3-11eb-8fbc-5b2228849684.PNG" width="280" height="500"> <br>
Boxplots and histograms over some features of the titanic dataset. <p>
<img src="https://user-images.githubusercontent.com/78420756/109414446-434a9400-79b3-11eb-9b64-ca746594cca7.PNG" width="320" height="280"> <br>
A heatmap over all cleaned features.
  
## Project status
Active 

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

