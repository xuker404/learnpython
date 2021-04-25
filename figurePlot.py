# -*- coding: utf-8 -*-
# ====================================== #
# @Author  : Yanbo Han
# @Email   : yanbohan98@gmail.com
# @File    : figurePlot.py
# ALL RIGHTS ARE RESERVED UNLESS STATED.
# ====================================== #

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class PlotterStyle:
    """
    The base class for all plotter styles.

    ...

    Attributes
    ----------
    styleName : str
        Name of PlotterStyle.

    fonts : str
        Name of fonts using in PlotterStyle.
        Default : "Arial"

    label_size : float
        Size of labels in graphs.
        Default : 20
        # TODO: self-adapted label size.

    seaborn_style : str
        Style name used of seaborn package.

    Methods
    -------
    set_style()

    """

    def __init__(self, styleName: str = None, fonts: str = "Arial", label_size: float = 20, seaborn_style: str = "whitegrid", **kwargs):
        self.styleName = styleName
        self.fonts = fonts
        self.label_size = label_size
        self.seaborn_style = seaborn_style
        self.setDict = kwargs

    def set_style(self):
        sns.set_style(self.seaborn_style)
        plt.rc("font", family=self.fonts)
        styledict = {
            "labelsize": self.label_size,
            **self.setDict
        }
        return styledict


class Plotter:
    """
    The base class for all plotter instances.

    Attributes
    ----------
    style : PlotterStyle
        Style of plotting styles, default by sns.set_style("whitegrid").
        Some additional options such as fonts, fontsize are set.
        See also
        ----------
        Class PlotterStyle

    Methods
    -------
    draw(x, y, markers="+", xlim=None, ylim=None)

    """

    def __init__(self, style: PlotterStyle = None, xlabels: str = r"Please define xlabels", ylabels: str = "Please define ylabels", drawer=sns.lmplot, **kwargs):
        self.style = style
        self.xlabels = xlabels
        self.ylabels = ylabels
        self.drawer = drawer

    def draw(self, x, y, markers="+", xlim=None, ylim=None, figsize=(15, 10)):
        if type(x[0]) is float or type(x[0]) is int or type(x[0]) is np.float64:
            data = pd.DataFrame({"xi": [xi for xi in x], "yi": [yi for yi in y]})
        else:
            data = pd.DataFrame({"xi": [xi[0] for xi in x], "yi": [yi[0] for yi in y]})
        set_dict = self.style.set_style()
        g = self.drawer(x="xi", y="yi", data=data, markers=markers)
        if not xlim:
            plt.xlim(xlim)
        if not ylim:
            plt.ylim(ylim)
        g.fig.set_size_inches(*figsize)
        g.set_xlabels(label="${}$".format(self.xlabels), fontsize=set_dict["labelsize"])
        g.set_ylabels(label="${}$".format(self.ylabels), fontsize=set_dict["labelsize"])
        plt.tight_layout()
        plt.show()
