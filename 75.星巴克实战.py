import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager


file_path="starbucks_directory.csv"
df=pd.read_csv(file_path)
# print("列名：")
# print(df.head(0)) #第一行
# print("-"*50)
# print("字段信息：")
# print(df.info())
# print("-"*50)
groups=df.groupby(by="Country")
# print("国家：")
# print(groups)
# print("-"*50)
#对国家遍历
# for i,j in groups:
#     print(i) #国家
#     print("*" * 50)
#     print(j,type(j)) #这个国家的具体信息
#     print("*"*50)
# print("-"*50)
# print("每个国家的店的数量：")
# country_cnt=groups["Brand"].count()
# print(country_cnt)
# print("美国的店的数量：")
# print(country_cnt["US"])
# print("中国的店的数量：")
# print(country_cnt["CN"])
# print("-"*50)
# print("中国的店：")
china_data=df[df["Country"]=="CN"]
# print(china_data)
groups=china_data.groupby(by="State/Province").count()["Store Number"]
print("中国各个城市的店的数量：")
print(groups)
# print("-"*50)
#
# #按照多个条件分组，返回Series类型-用df["Brand"]去分组，就一列
# print("返回Series:")
# groups=df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(groups)
# print(type(groups))
# print("-"*50)
#
# #按照多个条件分组，返回DataFrame类型-用df[["Brand"]]去分组
# print("返回DataFrame:")
# groups1=df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
# groups2=df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
# groups3=df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
# print(groups1,type(groups1))
# print("索引：")
# print(groups1.index)
# print("*"*50)
# print(groups2,type(groups2))
# print("索引：")
# print(groups2.index)
# print("*"*50)
# print(groups3,type(groups3))
# print("索引：")
# print(groups3.index)
# print("*"*50)
#
# #绘出店铺总数排名前10的国家
# data1=df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]
# x=data1.index
# y=data1.values
# plt.figure(figsize=(20,8),dpi=80)
# #画直方图
# plt.bar(range(len(x)),y,color="orange")
# plt.xticks(range(len(x)),y)
# plt.show()
# print("*"*50)
#
# #绘出中国每个店铺数量前30的城市直方图
# my_font=font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc',size=20)
# df=df[df["Country"]=="CN"]
# data2=df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:30]
# x=data1.index
# y=data1.values
# plt.figure(figsize=(20,8),dpi=80)
# #画直方图
# plt.bar(range(len(x)),y,color="red")
# plt.xticks(range(len(x)),x,fontproperties=my_font)
# plt.show()
# print("*"*50)
#
#
#
#
