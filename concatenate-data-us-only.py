import sys
import os
import pandas

path = "results-only-us-last-month"

dic = {}

files = []
for item in os.listdir(f"{path}"):
    if os.path.isfile(f"{path}/{str(item)}") and "csv" in item:
        files.append(item)

print(files)

# i can now open each file and prepare the results


for item in files:
    not_found = False
    print(item)
    ticker = item.split(".csv")[0]

    rz = pandas.read_csv(f"{path}/{str(item)}")
    #print(rz)
    print(rz.columns)
    #print("si types")
    # print(rz.dtypes)
    # print(rz.date, type(rz.date), rz.date.tolist())

    if "Date" not in dic:
        dic["Date"] = rz.date.tolist()
    if not ticker in rz:
        continue
    dic[ticker] = rz[f"{ticker}"].tolist()
    # if not_found:
    #     dic[state].extend(52 * ["None", ])
    #     continue
    # else:
    #     dic[state].extend(list(rz[ticker]))
    # if ticker not in dic["Ticker"]:
    #     dic["Ticker"].extend(len(list(rz[ticker])) * [ticker,])
    #     dic["Date"].extend(list(rz["date"]))
    #print(dic[state])

print("si acuma print dictionarul")
print(dic)

df = pandas.DataFrame.from_dict(dic, orient="index")
print(df.transpose())
df.transpose().to_csv("concat.csv")