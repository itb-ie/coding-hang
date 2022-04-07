import sys
import os
import pandas



dic = {"Date": [], "Ticker": [], "Entire US": []}
df_states = pandas.read_csv("state-abrev.csv")
states = df_states["Abbreviation"]
for state in states:
    dic[state] = []
print(dic)


files = []
for item in os.listdir("results"):
    if os.path.isfile("results/"+str(item)) and "csv" in item:
        files.append(item)

print(files)

# i can now open each file and prepare the results

#five = 555
for item in files:
    not_found = False
    #five -= 1
    #if not five:
        #break
    print(item)
    splited = item.split("-")
    #print(splited)
    ticker = splited[0]
    if len(splited) == 2:
        state = "Entire US"
    else:
        state = splited[2].split(".")[0]
    #print(ticker, state)
    rz = pandas.read_csv("results/"+str(item))
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
        dic[state].extend(list(rz[ticker]))
    if ticker not in dic["Ticker"]:
        dic["Ticker"].extend(len(list(rz[ticker])) * [ticker,])
        dic["Date"].extend(list(rz["date"]))
    #print(dic[state])

print("and now print the dict")
print(dic)

df = pandas.DataFrame.from_dict(dic, orient="index")
print(df.transpose())
df.transpose().to_csv("concat.csv")