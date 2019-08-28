# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:24:07 2019

@author: randerson
"""

import matplotlib.pyplot as plt

class Graph():
    @staticmethod
    def rate_sc(df, title, y_factor):
        df = df/y_factor
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('${:.0E} m^3/d$'.format(y_factor))
        ax.set_title(title)

    @staticmethod
    def cumu_sc(df, title, y_factor):
        df = df/y_factor
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('${:.0E} m^3$'.format(y_factor))
        ax.set_title(title)

    @staticmethod
    def cut_sc(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('%')
        ax.set_title(title)

    @staticmethod
    def gas_oil_ratio(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('$m^3/m^3$')
        ax.set_title(title)

    @staticmethod
    def show():
        plt.show()
