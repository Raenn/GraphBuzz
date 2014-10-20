from ggplot import *
import pandas as pd
import numpy as np
import word_loader

words = word_loader.get_buzzwords().split()[0:3]

#TODO: improve how data is passed in. Lots of different ways; see http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
df = pd.DataFrame([(words[0], 1), (words[1], 2), (words[2], 3)], columns=["Buzzword", "# of uses"])

foobar = ggplot(df, aes(x='Buzzword', fill='Buzzword', weight='# of uses')) +\
	geom_bar() +\
	geom_hline(yintercept=2, color='red')

print foobar

