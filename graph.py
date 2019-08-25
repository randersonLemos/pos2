# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:24:07 2019

@author: randerson
"""


class Graph():
    @staticmethod
    def oil_rate_sc(df):
        ax = df.plot(x_compat=True)
        ax.set_xlabel('') 
        ax.set_ylabel('($m^3$/d)') 
        ax.set_title('Oil Rate SC')
        
    @staticmethod
    def oil_cumu_sc(df):
        df = df/10e3
        ax = df.plot(x_compat=True)
        ax.set_xlabel('') 
        ax.set_ylabel('($10^3m^3$)') 
        ax.set_title('Cumulative Oil SC')

