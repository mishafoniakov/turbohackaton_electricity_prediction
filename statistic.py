from statsmodels.api import OLS
from scipy import stats
import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

class ANOVA:
    def __init__(self, data):
        self.data = data

    def anova_fitting(self):
        anova_dataset = np.array(self.data, dtype=np.float64)
        X = anova_dataset[:, :-1]
        y = anova_dataset[:, -1]
        model = OLS(y, X).fit()
        tables = model.summary()
        return tables
    
    def welch_anova_fitting(self):
        X = self.data.columns[:-1]
        y = self.data.columns[-1]
        formula = f"{y} ~ {' + '.join(X)}"
        model = ols(formula, data=self.data).fit()
        result = anova_lm(model)
        return result

class StatisticTests:
    def __init__(self):
        pass

    def levene_test(self, *array):
        stat, pvalue = stats.levene(*array)
        print(f'Statistic: {stat} P-value {pvalue}')
        if pvalue > 0.05:
            return 'Дисперсии одинаковые'
        else:
            return 'Дисперсии не одинаковые'
    
    def bartlett_test(self, *array):
        stat, pvalue = stats.bartlett(*array)
        print(f'Statistic: {stat} P-value {pvalue}')
        if pvalue > 0.05:
            return 'Дисперсии одинаковые'
        else:
            return 'Дисперсии не одинаковые'
    
    def shapiro_test(self, array):
        w, p_value = stats.shapiro(array)
        print(f"Shapiro-Wilk W Statistic: {w:.3f}, p-value: {p_value:.3f}")
        if p_value > 0.05:
            return 'Нормальное распределение'
        else:
            return 'Ненормальное распределение'
    
class CorrelationTests:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    def pearson_correlation(self):
        correlation = self.dataframe.corr(method='pearson')
        correlation = correlation.apply(pd.to_numeric)
        return correlation
    
    def person_correlation_manually(self):
        data_columns = self.dataframe.columns
        for i in range(len(data_columns)):
            for j in range(len(data_columns)):
                if i != j:
                    corr, p_value = stats.pearsonr(self.dataframe[data_columns[i]], self.dataframe[data_columns[j]])
                    if p_value <= 0.05:
                        print(f"Корреляция между {data_columns[i]} и {data_columns[j]} является статистически значимой: {float(corr)}")

    