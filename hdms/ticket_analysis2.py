import pandas as pd


tkt_data = pd.read_excel('C:/Users/Linux/PycharmProjects/hdms/datasets/Automatic Ticket Assignment.xlsx', usecols=[0, 1, 3])

row1, column1 = tkt_data.shape
col_names1 = list(tkt_data.columns)
print(col_names1)

print("\nsuccess")
