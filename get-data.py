from pytrends.request import TrendReq
from matplotlib import pylab as plt
import time

pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=3, backoff_factor=0.3)
data = plt.load('queries.npy', allow_pickle='TRUE').tolist()

while len(data) > 1:
    search = data[0]
    items = search.split()

    kw_list = [items[0]]
    geo = items[1]
    print("getting for {} {}".format(items[0], items[1]))
    try:
        pytrend.build_payload(kw_list=kw_list, geo=geo, timeframe='2019-01-01 2020-07-01', cat=7, )
        df = pytrend.interest_over_time()
    except:
        print("Error from google probably, sleep 10 and try again")
        time.sleep(10)
        continue
    df.to_csv("results/{}-{}.csv".format(items[0], items[1]))
    del data[0]
    # save it
    plt.save("queries.npy", data)
    time.sleep(1)


