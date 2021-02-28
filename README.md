## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [Technologies](#technologies)
* [Sources](#sources)
* [Project organization](#project-organization)


## General info
A Temporal Difference (TD) Learning approach (SARSA in this case) for a modelled mikroactuator, shaped like a hemisphere.
Also, a parallel Q-Learning approach is tested and compared.

## Sources
In collaboration with University of Augsburg. <br>
good source: https://towardsdatascience.com/td-in-reinforcement-learning-the-easy-way-f92ecfa9f3ce

## Requirements
Jupyter Notebook

## Technologies
Jupyter Notebook, Python3, Numpy, Pandas, Seaborn, matplotlib, sklearn, Support Vector Machine, Decision Tree Classifier, Logistic Regression Classifier

## Illustrations
<img src="https://user-images.githubusercontent.com/78420756/109026600-33376980-76c0-11eb-9154-674b188818f3.png" width="260" height="200"> <img src="https://user-images.githubusercontent.com/78420756/109413524-31b2bd80-79ae-11eb-8086-ac63b7592757.png" width="280" height="200"> <br>
Source: Michael Olbrich Universität Augsburg

<img src="https://user-images.githubusercontent.com/78420756/109413719-18f6d780-79af-11eb-9b0b-b8d82debbd10.PNG" width="800" height="200"> <br>
Left: A sinus trajectory followed by our TD Agent. Mid: The (negative) rewards collected. Right: The exploration parameter epsilon.
  
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

