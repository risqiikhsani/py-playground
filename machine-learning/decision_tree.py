import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("data_person.csv")

print(df) 

# To make a decision tree, all data has to be numerical.
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df) 

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features) 


# Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?
print(dtree.predict([[40, 10, 7, 1]])) 

# What would the answer be if the comedy rank was 6?
print(dtree.predict([[40, 10, 6, 1]])) 