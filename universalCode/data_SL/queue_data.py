def queue_data(file_name ='123'):
    from pandas import read_csv
    from numpy import shape
    #读取新数据的格式
    filePath = r'D:\桌面\PyUI' + '\\' +file_name + '.csv'
    data = read_csv(filePath)
    data_without_feature = data.values
    #print(data_without_feature)
    year = int(input('Date-Year:'))
    Month = int(input('Date-Month:'))
    Day = int(input('Date-Day:'))
    for i in range(list(shape(data_without_feature))[0]):
        if data_without_feature[i,0] == year and int(data_without_feature[i,1]) == Month and int(data_without_feature[i,2]) == Day:
            ans = data_without_feature[i,:]
            print(ans)
            #print(i)
            return i+1
    print('Not Found!')
    return None
#queue_data()