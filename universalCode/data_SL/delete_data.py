def delete_data(file_name ='123'):
    from queue_data import queue_data
    #读取新数据的格式
    filePath = r'D:\桌面\UI&Data' + '\\' +file_name + '.csv'
    index_to_be_deleted = queue_data(file_name)
    if index_to_be_deleted == None:
        return None
    #print(index_to_be_deleted)
    data = open(filePath, 'rt').readlines()
    with open(filePath, 'wt') as handle:
        handle.writelines(data[:index_to_be_deleted])
        handle.writelines(data[index_to_be_deleted + 1:])

delete_data()
