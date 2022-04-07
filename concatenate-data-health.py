import sys
import os
import pandas



dic = {"Date": [], "Entire US": []}
df_states = pandas.read_csv("state-abrev.csv")
states = df_states["Abbreviation"]
for state in states:
    dic[state] = []
print(dic)


files = []
for item in os.listdir("results"):
    if os.path.isfile("results/"+str(item)) and "csv" in item and "health" in item:
        files.append(item)

print(files)

# i can now open each file and prepare the results


for item in files:
    not_found = False
    print(item)
    splited = item.split("-")
    ticker = "Health"
    #print(splited)
    if len(splited) == 2:
        state = "Entire US"
    else:
        state = splited[2].split(".")[0]
    #print(ticker, state)
    rz = pandas.read_csv("results/"+str(item))
    if not len(dic["Date"]):
        dic["Date"].extend(list(rz["date"]))
    #print(rz)
    #print(rz.columns)
    #print("si types")
    #print(rz.dtypes)
    if "date" not in rz.columns:
        not_found = True

    # add just the values on the proper position
    #print(list(rz["date"]))
    if not_found:
        dic[state].extend(52 * ["None", ])
        continue
    else:
        dic[state].extend(list(rz.iloc[:, 1]))
        print("Deci am coloana")
        print(dic[state])
        #exit(0)
    #print(dic[state])

print("si acuma print dictionarul")
print(dic)

df = pandas.DataFrame.from_dict(dic, orient="index")
print(df.transpose())
df.transpose().to_csv("health-concat.csv")