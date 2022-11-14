#!/usr/local/bin/python3.9

import pandas as pd
import matplotlib.pyplot as plt


def df_stats(DataFrame):

    min = df["WindSpeed"].min()
    max = df["WindSpeed"].max()
    mean = df["WindSpeed"].mean()
    median = df["WindSpeed"].median()
    std = df["WindSpeed"].std()
    var = df["WindSpeed"].var()
    moda = df["WindSpeed"].mode()
    mode = ""
    for i in range(0, len(moda)):
        mode += str(moda[i])
    
    print("RIGHE x COLONNE:\t" + str(df.shape[0]) + " x " + str(df.shape[1]))
    print("MIN:\t" + str(df["WindSpeed"].min()) + " m/s")
    print("MAX:\t" + str(df["WindSpeed"].max()) + " m/s")
    print("MODA:\t\t", mode)
    print("MEDIA:\t\t" + str(round(df["WindSpeed"].mean(), 2)))
    print("MEDIANA:\t" + str(df["WindSpeed"].median()) + "\n")
    print("STD:\t" + str(df["WindSpeed"].std()))
    print("VAR:\t" + str(df["WindSpeed"].var()) + "\n")

    return




def set_plt(plt):
    df["WindSpeed"].plot(kind = "hist", x = "WindSpeed", xticks = (range(0, 80, 2)), yticks = (range(0, 45000, 1000)), grid = True) # RIGHE NON NULLE
    df["WindSpeed"].plot(kind = "hist", x = "WindSpeed", xticks = (range(0, 80, 2)), yticks = (range(0, 120000, 10000)), grid = True) # RIGHE NULLE
    df.plot(kind = "hist", x = "DateTime", y = "WindSpeed", yticks = (range(0, 100, 20)), grid = True)
    plt.title("GRAFICO FREQUENZE RIGHE NULLE")
    plt.xlabel("Velocità")
    plt.ylabel("Frequenza")
    plt.show()

    return

### DateTime, Velocity

df = pd.read_csv("/Users/bankich/Desktop/Sparx99/anemometro/dati_anemometro.csv") # DateFrame NULL
#df = df.loc[(df["WindSpeed"] != 0)] # DataFrame NOTNULL

#df_stats(df)

df["WindSpeed"].plot(kind = "hist", x = "WindSpeed", xticks = (range(0, 90, 2)), yticks = (range(0, 140000, 2000)), grid = True) # RIGHE NULLE
#df["WindSpeed"].plot(kind = "hist", x = "WindSpeed", xticks = (range(0, 90, 2)), yticks = (range(0, 55000, 1500)), grid = True) # RIGHE NON NULLE

plt.title("GRAFICO FREQUENZE CON RIGHE NULLE")
plt.xlabel("Velocità")
plt.ylabel("Frequenza")


plt.show()

