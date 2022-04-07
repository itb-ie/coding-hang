from pytrends.request import TrendReq
from matplotlib import pylab as plt
import time
import pandas

pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=3, backoff_factor=0.3)

pytrend.build_payload(kw_list=["AAPL"], geo="US", timeframe='2021-09-15 2021-10-15', cat=7, )
df = pytrend.interest_over_time()

df.to_csv(f"apple_test.csv")

