import pandas as pd
import numpy as np
import random,matplotlib
from matplotlib import pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager
import seaborn as sns

file_path="Tantannic.csv"
# 收集泰坦尼克号乘客数据
df=pd.read_csv(file_path)
# 把内存数据以csv格式写入磁盘中保存
# pd.to_csv(file_path)
# print(df.info) #输出所有数据信息
# print("-"*50)
# print(df.head())
# print(df.shape)
print(df.describe())
# print(df.describe)
# 第一行就是属性名字
# print(df.head(0))
print(df.isnull().sum())

# df["Embarked"]是Series对象
# 进行填充前Embarked字段的缺失值的数量
print(df["Cabin"].isnull().sum())
# 众数填充—mode()求众数—可能不唯一，返回是一个列表，常用mode()[0]
df["Cabin"].fillna(df["Cabin"].mode()[0],inplace=True)
# 填充后Embarked字段的缺失值的数量
print(df["Cabin"].isnull().sum())

# 热力图显示
plt.rcParams["font.sans-serif"]="/System/Library/Fonts/STHeiti Medium.ttc"
sns.heatmap(df.isnull(),cbar=False).set_title(r"heatmap")

#乘客的人数
passenger_list=df["Name"].tolist()
passenger_sex_list=df["Sex"].tolist()
passenger_num=len(set(passenger_list))
# 一个名字对应一个人，对名字列表获取个数即为乘客人数
print("乘客的人数是：")
print(passenger_num)

# 性别分布直方图—性别改为年龄列就得到年龄分布直方图
passenger_info=df["Name"].values
plt.figure(figsize=(20,8),dpi=80)
my_font=font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc',size=10)
x=passenger_list
y=passenger_sex_list
plt.xlabel('姓名',fontproperties=my_font)
plt.ylabel('性别',fontproperties=my_font)
plt.xticks(range(len(x)),x,fontproperties = my_font,rotation = 45)

#条形图
rects=plt.bar(range(len(x)),y,width=0.5,color='orange')
#在条形图上加标注
for rect in rects:
    height=rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2,height+0.5,str(height),ha="center")


plt.show()


# 用机器学习模型来处理两个数据集
# 训练集
train_clean=df[df["Survived"].notnull()] #数据清洗
train_clean.to_csv(train_clean.csv)
# 测试集
test_clean=df[df["Survived"].isnull()] #数据清洗
test_clean.drop("Survived",axis=1).to_csv("test_clean.csv")