import pandas as pd

df = pd.read_excel("../data/USAforeignworkerssalarydata.csv")

print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing values:\n", df.isnull().sum())
