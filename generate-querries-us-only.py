import pandas
from matplotlib import pylab as plt

df_companies = pandas.read_csv("constituents.csv")
companies = df_companies["Symbol"]
print(companies)

plt.save("queries.npy", companies)

