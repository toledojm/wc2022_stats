import pandas as pd

url_1='https://fbref.com/en/matches/109ad6ba/Argentina-Saudi-Arabia-November-22-2022-World-Cup#shots_all'
urls=[url_1]

def cambio_min(match):
    suma=[]
    for x in match.Minute:
        min=x.split('+')
        i = 2
        if i == len(min):
            nuevo_min=int(min[0])+int(min[1])
            suma.append(nuevo_min)
        else:
            suma.append(int(min[0]))
    match.Minute=suma

for url in urls:

    df=pd.read_html(url)
    match=df[17].dropna(axis=0,how='all')
    team1=df[18].dropna(axis=0,how='all')
    team2=df[19].dropna(axis=0,how='all')
    match.columns=['Minute'	,'Player'	,'Squad','xG'	,'PSxG'	,'Outcome'	,'Distance'	,'Body Part'	,'Notes'	,'sca_1_Player'	,'sca_1_Event'	,'sca_2_Player'	,'sca_2_Event']
    cambio_min(match)


