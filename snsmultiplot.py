# -*- coding: utf-8 -*-
# ====================================== #
# @Author  : Yanbo Han
# @Email   : yanbohan98@gmail.com
# @File    : snsmultiplot.py
# ALL RIGHTS ARE RESERVED UNLESS STATED.
# ====================================== #

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.ExcelFile("CV.xlsx")
df = data.parse(0, parse_cols=[0])

from figurePlot import PlotterStyle, Plotter

style = PlotterStyle("Default")
x = df["V1"].to_numpy()
y = df["A1"].to_numpy()

plotter = Plotter(style=style, xlabels=r"U", ylabels=r"I", drawer=sns.lineplot)

plotter.draw(x, y, figsize=(10, 5))
