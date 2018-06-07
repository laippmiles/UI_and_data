from array2CSV import array2CSV,CSVDeleteSpace

def save_data(outputdata):

    filePath = r'D:\桌面\UI&Data' + '\\'
    array2CSV(outputdata,filePath,'save_data.csv')
    CSVDeleteSpace(filePath,'save_data.csv')
