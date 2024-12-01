import pandas as pd
import re

class DataRepresentation:
    def __init__(self):
        pass
    
    def read_excel_dataset(self, path, sheet_list, new_column=None, head_num=0):
        dataset = pd.read_excel(path, sheet_name=None, header=head_num)
        dataframe = pd.DataFrame()
        for sheet in sheet_list:
            df = dataset[sheet]
            if new_column is not None:
                df[new_column] = sheet
            dataframe = pd.concat([dataframe, df])
        return dataframe
    
    def cyrillic_to_latin(self, text):
        mapping = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
        }
        return ''.join(mapping.get(c, c) for c in text)

    def columns_to_latin(self, dataframe):
        for col in dataframe.columns:
            if isinstance(col, str):
                dataframe.rename(columns={col: self.cyrillic_to_latin(col.lower())}, inplace=True)
        return dataframe
    
    def values_to_latin(self, dataframe, column):
        dataframe[column] = dataframe[column].apply(lambda x: self.cyrillic_to_latin(x.lower()))
        return dataframe[column]
    
    def date_transform(self, dataframe, column):
        dataframe['chislo'] = dataframe[column].dt.day
        dataframe['mesyats'] = dataframe[column].dt.month
        dataframe['god'] = dataframe[column].dt.year
        try:
            dataframe['chas'] = dataframe[column].dt.hour
        except:
            pass
        dataframe = dataframe.drop(column, axis=1)
        return dataframe
    
    def transform(self, path, sheet_list, new_column=None, head_num=0):
        dataframe = self.read_excel_dataset(path, sheet_list, new_column, head_num)
        dataframe = self.columns_to_latin(dataframe)
        return dataframe