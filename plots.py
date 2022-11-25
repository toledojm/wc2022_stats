import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data import df, match

def plot(match):
    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                    int(np.ceil(len(match.Minute)/6)))[:len(match.Minute)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)
    titulo=df[2].columns[0][0]+'vs. '+[2].columns[1][1]
    ax.set(title=titulo)

    ax.vlines(match.Minute, 0, levels, color="tab:red")  # The vertical stems.
    ax.plot(match.Minute, np.zeros_like(match.Minute), "-o",
            ms=15, lw=2, alpha=0.7, mfc='orange')  # Baseline and markers on it.
    min=match.Minute.astype(str)
    salida=min+"' :"+match.Player+'\n'+match.Outcome+'\n'+'Evento: '+match.sca_1_Event
    # annotate lines
    for d, l, r, h in zip(match.Minute, levels, salida, match.Outcome):
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
    return plt.show()