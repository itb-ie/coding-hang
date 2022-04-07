import pandas
from matplotlib import pylab as plt

df_states = pandas.read_csv("state-abrev.csv")
states = df_states["Abbreviation"]
print(states)

#df_companies = pandas.read_csv("constituents.csv")
#companies = df_companies["Symbol"]
#print(companies)

querries = ["US"]

for state in states:
    print(f"{state}")
    querries.append(f"US-{state}")

plt.save("state-health.npy", querries)

