import pandas as pd

ticket_data1 = pd.read_csv("C:/Users/Linux/PycharmProjects/hdms/datasets/SampleInput.csv", usecols=[0, 1, 2, 3, 6, 7, 8, 9, 10, 11])
ticket_data2 = pd.read_csv("C:/Users/Linux/PycharmProjects/hdms/datasets/clean_data.csv", usecols=[1, 2])
row1, column1 = ticket_data1.shape
col_names1 = list(ticket_data1.columns)
row2, column2 = ticket_data2.shape
col_names2 = list(ticket_data2.columns)
print(col_names1)
print(col_names2)

print("\nsuccess")
