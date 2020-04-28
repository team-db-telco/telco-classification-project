import numpy as np
import pandas as pd
pd.options.display.float_format = '{:.3f}'.format
import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def model_maker(X, y, model_type, random_state):
    if model_type == 'LR':
        model = LogisticRegression(random_state=random_state)
        return model.fit(X, y)
    elif model_type == 'DT':
        model = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=random_state)
        return model.fit(X, y)
    elif model_type == 'RF':
        model = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', 
                                       min_samples_leaf=3, n_estimators=100, max_depth=20, random_state=random_state)
        return model.fit(X, y)
    else:
        return print ("unacceptable model_type entry. options are: LR, DT or RF")
     
def model_predictor(X, model):
    predictions = model.predict(X)
    # Calulate probabilities and turn them into a df
    probs = model.predict_proba(X)
    return predictions, probs
    
def model_evaluator(y, predictions):    
    # Confusion Matrix
    labels = ['loyal', 'churn']
    predicted_labels = [name + " predicted" for name in labels ]
    conf_matrix = pd.DataFrame(confusion_matrix(y, predictions), index=labels, columns=[predicted_labels])
    conf_matrix.index.name = "actual"
    # Classification Report
    class_report = classification_report(y, predictions)
    return conf_matrix, class_report