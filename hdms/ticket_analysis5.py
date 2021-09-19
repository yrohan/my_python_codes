import pandas as pd

tkt_data = pd.read_csv("C:/Users/Linux/PycharmProjects/hdms/datasets/helpdesk_anonymized.csv")
row1, column1 = tkt_data.shape
col_names1 = list(tkt_data.columns)
print(col_names1)

print("\nsuccess")
