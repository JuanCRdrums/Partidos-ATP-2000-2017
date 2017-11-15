import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
	

jugador = 'Andy Roddick'
year = 2004

route = "atp/" + "atp_matches_" + str(year) + ".csv"
titleAces = "Aces " + jugador + " " + str(year)
titleRanking = "Rangink ATP " + jugador + " " + str(year)
titleTime = "Minutos jugados por partido " + jugador + " " + str(year)
titleDF = "Dobles faltas " + jugador + " " + str(year)
titleSP = "Puntos ganados en servicio " + jugador + " " + str(year)
titleFS = "Puntos ganados en primer servicio " + jugador + " " + str(year)
titleSS = "Puntos ganados en segundo servicio " + jugador + " " + str(year)
titleSG = "Games ganados en servicio " + jugador + " " + str(year)
titleBPS = "Break Points salvados " + jugador + " " + str(year)
titleBPF = "Break Points enfrentados " + jugador + " " + str(year)

df = pd.read_csv(route)



ranking = df[df.winner_name == jugador]
ranking = ranking['winner_rank']
ranking.plot(label = 'Ranking ATP',ls = 'steps')
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Ranking')
plt.title(titleRanking)
plt.show()

aw = df[df.winner_name == jugador]
al = df[df.loser_name == jugador]
aw = aw['w_ace']
aw.plot(label = 'Ganados',ls = 'steps')
al = al['l_ace']
al.plot(label = 'Perdidos',ls = 'steps')
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Aces')
plt.title(titleAces)
plt.show()

wDF = df[df.winner_name == jugador]
wDF = wDF['w_df']
lDF = df[df.loser_name == jugador]
lDF = lDF['l_df']
wDF.plot(label = 'Ganados', ls = 'steps')
lDF.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleDF)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Dobles Faltas')
plt.show()


wSp = df[df.winner_name == jugador]
wSp = wSp['w_svpt']
lSp = df[df.loser_name == jugador]
lSp = lSp['l_svpt']
wSp.plot(label = 'Ganados', ls = 'steps')
lSp.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleSP)
plt.legend()
plt.ylabel('Puntos ganados en servicio')
plt.xlabel('ID Partido')
plt.show()

wFS = df[df.winner_name == jugador]
wFS = wFS['w_1stWon']
lFS = df[df.loser_name == jugador]
lFS = lFS['l_1stWon']
wFS.plot(label = 'Ganados', ls = 'steps')
lFS.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleFS)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Puntos ganados en primer servicio')
plt.show()


wFS = df[df.winner_name == jugador]
wFS = wFS['w_2ndWon']
lFS = df[df.loser_name == jugador]
lFS = lFS['l_2ndWon']
wFS.plot(label = 'Ganados', ls = 'steps')
lFS.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleSS)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Puntos ganados en segundo servicio')
plt.show()

wSG = df[df.winner_name == jugador]
wSG = wSG['w_SvGms']
lSG = df[df.loser_name == jugador]
lSG = lSG['l_SvGms']
wSG.plot(label = 'Ganados', ls = 'steps')
lSG.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleSG)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Games ganados en servicio')
plt.show()

wBPF = df[df.winner_name == jugador]
wBPF = wBPF['w_bpFaced']
lBPF = df[df.loser_name == jugador]
lBPF = lBPF['l_bpFaced']
wSG.plot(label = 'Ganados', ls = 'steps')
lSG.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleBPF)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Break Points enfrentados')
plt.show()

wBPS = df[df.winner_name == jugador]
wBPS = wBPS['w_bpSaved']
lBPS = df[df.loser_name == jugador]
lBPS = lBPS['l_bpSaved']
wSG.plot(label = 'Ganados', ls = 'steps')
lSG.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleBPS)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Break Points salvados')
plt.show()

wmin = df[df.winner_name == jugador]
wmin = wmin['minutes']
lmin = df[df.loser_name == jugador]
lmin = lmin['minutes']
wmin.plot(label = 'Ganados', ls = 'steps')
lmin.plot(label = 'Perdidos', ls = 'steps')
plt.title(titleTime)
plt.legend()
plt.xlabel('ID Partido')
plt.ylabel('Minutos Jugados')
plt.show()


