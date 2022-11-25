import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


'''
# This is the document title

This is some _markdown_.
'''

url_1='https://fbref.com/en/partidoes/109ad6ba/Argentina-Saudi-Arabia-November-22-2022-World-Cup#shots_all'
urls=[url_1]

def cambio_min(partido):
    suma=[]
    for x in partido.Minute:
        min=x.split('+')
        i = 2
        if i == len(min):
            nuevo_min=int(min[0])+int(min[1])
            suma.append(nuevo_min)
        else:
            suma.append(int(min[0]))
    partido.Minute=suma

def buscar(urls):

    for url in urls:

        df=pd.read_html(url)
        partido=df[17].dropna(axis=0,how='all')
        team1=df[18].dropna(axis=0,how='all')
        team2=df[19].dropna(axis=0,how='all')
        partido.columns=['Minute'	,'Player'	,'Squad','xG'	,'PSxG'	,'Outcome'	,'Distance'	,'Body Part'	,'Notes'	,'sca_1_Player'	,'sca_1_Event'	,'sca_2_Player'	,'sca_2_Event']
        cambio_min(partido)
        equipos=[df[2].columns[0][0],[2].columns[1][1]]

    return partido, equipos


partido, df=buscar(urls)

def plot(partido,df):
    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                    int(np.ceil(len(partido.Minute)/6)))[:len(partido.Minute)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)
    titulo=df[2].columns[0][0]+'vs. '+[2].columns[1][1]
    ax.set(title=titulo)

    ax.vlines(partido.Minute, 0, levels, color="tab:red")  # The vertical stems.
    ax.plot(partido.Minute, np.zeros_like(partido.Minute), "-o",
            ms=15, lw=2, alpha=0.7, mfc='orange')  # Baseline and markers on it.
    min=partido.Minute.astype(str)
    salida=min+"' :"+partido.Player+'\n'+partido.Outcome+'\n'+'Evento: '+partido.sca_1_Event
    # annotate lines
    for d, l, r, h in zip(partido.Minute, levels, salida, partido.Outcome):
        if h=='Goal':
            ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top",color="tab:red")
        else:
            ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top")

    # format xaxis with 4 month intervals

    plt.setp(ax.get_xticklabels(), ha="left")

    # remove y axis and spines
    ax.yaxis.set_visible(False)


    ax.margins(y=0.21)
    
    
    return fig

fig=plot(partido,df)

st.pyplot(fig)


