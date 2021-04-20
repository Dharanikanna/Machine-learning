import pandas as pd
print("Libraries imported Sucessfully...!")


dataframes = pd.read_csv("SalaryGender.csv", header=1)
print(dataframes.head)