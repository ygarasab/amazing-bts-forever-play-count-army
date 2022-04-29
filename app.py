import requests
from get_discos import get_discos
from get_musicas import get_musicas
import pandas

auth_token='BQDBwc3V0v9aWjIuZPct6M_uoZBL8h2oMenHpMOqcttbCXEU49HCsexxkM6VWRN_dede5ZkSkAmBOueO6wc'
head = {'Authorization': 'Bearer ' + auth_token}

album_ids = get_discos(head)
musics = [ get_musicas(head, id) for id in album_ids ]

resultado = []

for i in musics: resultado += i

df = pandas.DataFrame(resultado)
pandas.set_option('display.max_rows', df.shape[0]+1)

print(df)
