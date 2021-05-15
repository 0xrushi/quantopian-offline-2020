import pandas as pd
from collections import OrderedDict
import pytz
import pandas_datareader as pdr

def get_from_pdr_to_panel(symbol="NVDA", datefrom="2016-01-01", dateto="2018-01-01"):
    nvidia=pdr.get_data_yahoo(symbol, datefrom, dateto)
    nvidia.head()
    data = OrderedDict()
    data[symbol] = nvidia
    data[symbol] = data[symbol][["Open","High","Low","Close","Volume"]]
    #print(data[symbol].head())
    panel = pd.Panel(data)
    panel.minor_axis = ["open","high","low","close","volume"]
    panel.major_axis = panel.major_axis.tz_localize(pytz.utc)
    print(panel)
    return panel