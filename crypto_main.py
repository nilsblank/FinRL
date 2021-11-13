import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import preprocessing

matplotlib.use("Agg")

import ccxt
import pandas
import os
from pathlib import Path
import sys
import csv
import datetime

from finrl.apps import config
from finrl.neo_finrl.preprocessor.yahoodownloader import YahooDownloader
from finrl.neo_finrl.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.neo_finrl.env_stock_trading.env_stocktrading import StockTradingEnv
from finrl.drl_agents.stablebaselines3.models import DRLAgent
from finrl.plot import backtest_stats, backtest_plot, get_daily_return, get_baseline
from finrl.neo_finrl.data_processors import processor_ccxt
from finrl.neo_finrl.preprocessor.binancedownloader import *
import finrl.neo_finrl.preprocessor.binancedownloader
from finrl.neo_finrl.data_processors import processor_ccxt


import itertools

#Download Data and save to /data

#scrape_candles_to_csv('dot_usdt_15m.csv', 'binance', 3, 'DOT/USDT', '15m', '2021-08-0100:00:00Z',limit=1000)

data_processor = processor_ccxt.CCXTEngineer()
data = data_processor.data_fetch('20210801 01:00:00','20210820 01:00:00',period='4h',pair_list=['DOT/USDT'])

#%%
data_cleaned = data.drop_duplicates()
data_indicators = data_processor.add_technical_indicators(data_cleaned,["DOT/USDT"])
