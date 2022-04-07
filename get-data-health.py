from pytrends.request import TrendReq
from matplotlib import pylab as plt
import time

pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=3, backoff_factor=0.3)
data = plt.load('state-health.npy', allow_pickle='TRUE').tolist()

while len(data) > 1:
    search = data[0]
    items = search.split()

    kw_list = ""
    geo = items[0]
    print(f"getting for {geo}")

    pytrend.build_payload(kw_list=[""], geo=geo, timeframe='2019-07-01 2020-07-01', cat=45, )
    df = pytrend.interest_over_time()
    df.to_csv("results/health-{}.csv".format(geo))

    del data[0]
    #save it
    plt.save("queries.npy", data)
    time.sleep(5)


