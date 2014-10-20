from ggplot import *
import pandas as pd
import numpy as np

#TODO: improve how data is passed in. Lots of different ways; see http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
df = pd.DataFrame([(0, 30), (1, 25), (2, 22), (3, 1)], columns=["Days since manager in office", "# of 'synergy' uses"])

foobar = ggplot(df, aes(x="Days since manager in office", y="# of 'synergy' uses")) +\
	geom_line() +\
	geom_hline(yintercept=2, color='red')

print foobar

