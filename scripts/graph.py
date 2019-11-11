# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:24:07 2019

@author: randerson
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

locator = mdates.MonthLocator(bymonth=[1])
formatter = mdates.DateFormatter('%Y')

class Graph():
    @staticmethod
    def fluid(df, title):
        fig, ax = plt.subplots()
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$m^3 std$')

    @staticmethod
    def fluid_dot(df, title):
        fig, ax = plt.subplots()
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_title(title)
        ax.set_xlabel('date')
        ax.set_ylabel('$m^3/d$')

    @staticmethod
    def fluid_ratio(df, title):
        fig, ax = plt.subplots()
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('$m^3/m^3$')
        ax.set_title(title)

    @staticmethod
    def percent(df, title):
        fig, ax = plt.subplots()
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('%')
        ax.set_title(title)

    @staticmethod
    def pressure(df, title):
        fig, ax = plt.subplots()
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('$kg/m^2$')
        ax.set_title(title)

    @staticmethod
    def pressure_dot(df, title):
        fig, ax = plt.subplots()
        df.plot(ax=ax, x_compat=True)
        plt.setp( ax.xaxis.get_majorticklabels(), rotation=90, horizontalalignment='center' )
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.set_xlabel('date')
        ax.set_ylabel('$kg/m^2/day$')
        ax.set_title(title)

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def tight_layout():
        plt.tight_layout()
