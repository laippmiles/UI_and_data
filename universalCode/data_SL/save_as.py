def save_as(outputdata,file_name):
    from array2CSV import array2CSV,CSVDeleteSpace
    filePath = r'D:\桌面\PyUI' + '\\'
    feature = ['Date-Year', 'Date-Month', 'Date-Day', 'Classfication', 'Q-E', 'ZN-E',
               'PH-E', 'DBO-E', 'DQO-E', 'SS-E', 'SSV-E', 'SED-E ', 'COND-E', 'PH-P',
               'DBO-P', 'SS-P', 'SSV-P', 'SED-P', 'COND-P', 'PH-D', 'DBO-D', 'DQO-D',
               'SS-D', 'SSV-D', 'SED-D', 'COND-D', 'PH-S', 'DBO-S', 'DQO-S', 'SS-S',
               'SSV-S', 'SED-S ', 'COND-S', 'RD-DBO-P', 'RD-SS-P ', 'RD-SED-P',
               'RD-DBO-S', 'RD-DQO-S', 'RD-DBO-G', 'RD-DQO-G', 'RD-SS-G', 'RD-SED-G']
    from numpy import shape
    array2CSV(feature, filePath, file_name + '.csv')
    for i in range(list(shape(outputdata))[0]):
        #print(outputdata[i,:])
        array2CSV(outputdata[i,:],filePath,file_name + '.csv')
    CSVDeleteSpace(filePath,file_name + '.csv')