import pandas as pd
import numpy as np

playersDF = pd.read_csv('C:/Users/admin/source/repos/KoP_JKH_var12/KoP6/football.csv')

maxPenaltiesPlayerDF = pd.DataFrame(playersDF[playersDF['Penalties']==playersDF['Penalties'].max()],columns = ['Wage'])
headingAccuracyPlayersDF = pd.DataFrame(playersDF[playersDF['HeadingAccuracy']==playersDF['HeadingAccuracy'].max()],columns = ['Wage'])

difPlayers = maxPenaltiesPlayerDF['Wage'].mean() - headingAccuracyPlayersDF['Wage'].mean()
print(difPlayers)