import datetime

from pandas import read_csv

from data_SL.save_data import save_data

#读取新数据的格式
data = read_csv('D:\桌面\PyUI\water_treatment_data.csv')
#print(data)
feature = list(data.columns.values)
#提取特征名
train_data = data.values[:,4:]
#训练数据
train_lebel = data.values[:,3]
#训练标签
print(list(feature))

#写入新数据的格式
date = [datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day]
outputdata =data.values[2:20,:]
from save_as import save_as
#save_data(outputdata)
file_name = input('file_name:')
save_as(outputdata,file_name)

