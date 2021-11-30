import itertools
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import xgboost as xgb
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score ,precision_score, recall_score


df = pd.read_csv("urldata.csv", low_memory=False)

length_of_url = []  # length of url
number_of_letters = []  # number of alphanumeric characters
number_of_digits = []  # number of digits
count_of_dotcom = []  # count of '.com'
count_of_codot = []  # count of '.co.'
count_of_dotnet = []  # count of '.net'
count_of_forward_slash = []  # count of '/'
count_of_percentage = []  # count of '%'
count_of_upper_case = []  # count of upper case characters
count_of_lower_case = []  # count of upper case characters
count_of_dot = []  # count of "."
count_of_upper_case = []  # count of upper case characters
count_of_lower_case = []  # count of lower case characters
count_of_dot_info = []  # count of '.info'
count_of_https = []  # count of 'https'
count_of_www_dot = []  # count of 'www.'
count_of_not_alphanumeric = []  # count of non-alphanumeric characters

for item in df["url"]:
    try:
        length_of_url.append(len(item))
    except:
        length_of_url.append(0)

    try:
        number_of_letters.append(sum(c.isalpha() for c in item))
    except:
        number_of_letters.append(0)

    try:
        number_of_digits.append(sum(c.isdigit() for c in item))
    except:
        number_of_digits.append(0)

    try:
        count_of_dotcom.append(item.count(".com"))
    except:
        count_of_dotcom.append(0)

    try:
        count_of_codot.append(item.count(".co."))
    except:
        count_of_codot.append(0)

    try:
        count_of_dotnet.append(item.count(".net"))
    except:
        count_of_dotnet.append(0)

    try:
        count_of_forward_slash.append(item.count("/"))
    except:
        count_of_forward_slash.append(0)

    try:
        count_of_percentage.append(item.count("%"))
    except:
        count_of_percentage.append(0)

    try:
        count_of_dot.append(item.count("."))
    except:
        count_of_dot.append(0)

    try:
        count_of_upper_case.append(sum(c.isupper() for c in item))
    except:
        count_of_upper_case.append(0)

    try:
        count_of_lower_case.append(sum(c.islower() for c in item))
    except:
        count_of_lower_case.append(0)

    try:
        count_of_dot_info.append(item.count(".info"))
    except:
        count_of_dot_info.append(0)

    try:
        count_of_https.append(item.count("https"))
    except:
        count_of_https.append(0)

    try:
        count_of_www_dot.append(item.count("www."))
    except:
        count_of_www_dot.append(0)

    try:
        count_of_not_alphanumeric.append(sum(not c.isalnum() for c in item))
    except:
        count_of_not_alphanumeric.append(0)

df["length_of_url"] = length_of_url
df["number_of_letters"] = number_of_letters
df["number_of_digits"] = number_of_digits
df["count_of_dotcom"] = count_of_dotcom
df["count_of_codot"] = count_of_codot
df["count_of_dotnet"] = count_of_dotnet
df["count_of_forward_slash"] = count_of_forward_slash
df["count_of_upper_case"] = count_of_upper_case
df["count_of_lower_case"] = count_of_lower_case
df["count_of_dot"] = count_of_dot
df["count_of_upper_case"] = count_of_upper_case
df["count_of_lower_case"] = count_of_lower_case
df["count_of_dot_info"] = count_of_dot_info
df["count_of_https"] = count_of_https
df["count_of_www_dot"] = count_of_www_dot
df["count_of_not_alphanumeric"] = count_of_not_alphanumeric
df["count_of_percentage"] = count_of_percentage

## Amount of symbols to letters ratio
df["not_alphanumeric_to_letters_ratio"] = (
    df["count_of_not_alphanumeric"] / df["number_of_letters"]
)

## Amount of '%' to length ratio
df["percentage_to_length_ratio"] = df["count_of_percentage"] / df["length_of_url"]

## Amount of '%' to length ratio
df["percentage_to_length_ratio"] = df["count_of_percentage"] / df["length_of_url"]

## Amount of '/' to length ratio
df["forwards_slash_to_length_ratio"] = (
    df["count_of_forward_slash"] / df["length_of_url"]
)

## Amount captialised vs. non-capitalised
df["upper_case_to_lower_case_ratio"] = (
    df["count_of_upper_case"] / df["count_of_lower_case"]
)

X = df[
    [
        "length_of_url",
        "number_of_letters",
        "number_of_digits",
        "count_of_dotcom",
        "count_of_codot",
        "count_of_dotnet",
        "count_of_forward_slash",
        "count_of_upper_case",
        "count_of_lower_case",
        "count_of_dot",
        "count_of_dot_info",
        "count_of_https",
        "count_of_www_dot",
        "count_of_not_alphanumeric",
        "count_of_percentage",
        "percentage_to_length_ratio",
        "forwards_slash_to_length_ratio",
    ]
]

y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=234
)

depth_list = []
accuracy_list = []

for depth in range(1, len(X.columns)):
    decision_tree = DecisionTreeClassifier(max_depth=depth)
    decision_tree.fit(X_train, y_train)
    accuracy = decision_tree.score(X_test, y_test)
    accuracy_list.append(decision_tree.score(X_test, y_test))
    depth_list.append(depth)



score = {}
# DECISION TREE
decision_tree = DecisionTreeClassifier(max_depth=17)
cv_score = cross_val_score(decision_tree, X_train, y_train, cv=5)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=567
)

decision_tree = DecisionTreeClassifier(max_depth=17)
decision_tree.fit(X_train, y_train)
y_hat = decision_tree.predict(X_test)
#pickle.dump(decision_tree, open("tree.pkl", "wb"))
acc = accuracy_score(y_test, y_hat)
pre_dt = precision_score(y_test, y_hat, average='macro')
recall_dt = recall_score(y_test, y_hat, average='macro')
score["dt"] = []
score["dt"].append(recall_dt)
score["dt"].append(pre_dt)
score["dt"].append(acc)

# XGBOOSTER
model = xgb.XGBClassifier(n_estimators=1000)
model.fit(X_train, y_train)
y_xgb = model.predict(X_test)
#pickle.dump(model, open("xgb.pkl", "wb"))
acc_xgb = accuracy_score(y_test, y_xgb)
pre_xgb = precision_score(y_test, y_xgb, average='macro')
recall_xgb = recall_score(y_test, y_xgb, average='macro')
score["xgb"] = []
score["xgb"].append(recall_xgb)
score["xgb"].append(pre_xgb)
score["xgb"].append(acc_xgb)

# LGB
lgb = LGBMClassifier(objective='binary',boosting_type= 'gbdt',n_jobs = 5, silent = True, random_state=5)
lgb.fit(X_train, y_train)
y_lgb = lgb.predict(X_test)
#pickle.dump(lgb, open("lgb.pkl", "wb"))
acc_lgb = accuracy_score(y_test, y_lgb)
pre_lgb = precision_score(y_test, y_lgb, average='macro')
recall_lgb = recall_score(y_test, y_lgb, average='macro')
score["lgb"] = []
score["lgb"].append(recall_lgb)
score["lgb"].append(pre_lgb)
score["lgb"].append(acc_lgb)

#Random Forrest
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_rfc = rfc.predict(X_test)
#pickle.dump(rfc, open("rfc.pkl", "wb"))
acc_rfc = accuracy_score(y_test, y_rfc)
pre_rfc = precision_score(y_test, y_rfc, average='macro')
recall_rfc = recall_score(y_test, y_rfc, average='macro')
score["rfc"] = []
score["rfc"].append(recall_rfc)
score["rfc"].append(pre_rfc)
score["rfc"].append(acc_rfc)

pickle.dump(score, open("metrics.pkl","wb"))

# END HERE
#def metrics():
    #f1_score = f1_score(y_test, y_hat, average='macro')




#score.append(f1_score)

# print(format(f1_score))
# print(accuarcy_score)
# print(precision_score)
# print(recall_score)


#metrics()