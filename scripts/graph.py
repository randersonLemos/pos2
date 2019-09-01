# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:24:07 2019

@author: randerson
"""

import matplotlib.pyplot as plt

class Graph():
    @staticmethod
    def rate(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('$m^3/d$')
        ax.set_title(title)

    @staticmethod
    def cumu(df, title):
        ax = df.plot(x_compat=True)
        ax.set_ylabel('$m^3$')
        ax.set_xlabel('years')
        ax.set_title(title)

    @staticmethod
    def ratio(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('$m^3/m^3$')
        ax.set_title(title)

    @staticmethod
    def percent(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('%')
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
    def pressure(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('$kg/m^2$')
        ax.set_title(title)

    @staticmethod
    def dot_pressure(df, title):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('years')
        ax.set_ylabel('$kg/m^2/day$')
        ax.set_title(title)



    @staticmethod
    def show():
        plt.show()
