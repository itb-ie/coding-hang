from pytrends.request import TrendReq
from matplotlib import pylab as plt
import time
import pandas

pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=3, backoff_factor=0.3)

data = plt.load('queries.npy', allow_pickle=True).tolist()

while len(data):
    print(f"{data[0]}")
    # if data[0] != "AAPL":
    #     del data[0]
    #     continue
    try:
        pytrend.build_payload(kw_list=[data[0]], geo="US", timeframe='2021-09-15 2021-10-15', cat=7, )
        df = pytrend.interest_over_time()
    except:
        print("Error from google probably, sleep 10 and try again")
        time.sleep(10)
        continue

    df.to_csv(f"results-only-us-last-month/{data[0]}.csv")
    del data[0]
    # save it
    plt.save("queries.npy", data)
    time.sleep(1)
