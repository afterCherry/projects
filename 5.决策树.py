# 决策树模型

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import pydot
import pydotplus as pydot
import graphviz




def decision():
    #数据处理
    titannic=pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    x=titannic[["pclass","age","sex"]] #[[]]
    y=titannic["survived"]
    x["age"].fillna(x["age"].mean(),inplace=True)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

    #处理特征
    dict=DictVectorizer(sparse=False)
    x_train=dict.fit_transform(x_train.to_dict(orient="records"))
    print(dict.get_feature_names())
    x_test=dict.transform(x_test.to_dict(orient="records"))

    #决策树
    dec=DecisionTreeClassifier(max_depth=7)
    dec.fit(x_train,y_train)
    print("预测的准确率：",dec.score(x_test,y_test))
    tree.export_graphviz(dec,out_file="./tree.dot",feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'],class_names=None,filled=True)




if __name__ == '__main__':
    decision()