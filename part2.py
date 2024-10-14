import pandas as pd
import numpy as np
income = np.array([111, 222, 251, 333, 444, 555, 666, 777, 888, 899])
income_without_tax = income * 0.7
expenses = ([20, 30, 40, 50, 60, 66, 33, 45, 89, 44])
x = ['Jan', 'Feb', 'Mr', 'Apr', 'May', 'Jn', 'Jl', 'Av', 'Sp', 'Oct']
dataframe = pd.DataFrame({
    'Month': x,
    'Income (without tax)': income_without_tax,
    'Expenses': expenses
})
print(dataframe)

print(dataframe.iloc[0:3])