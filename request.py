import requests
import json

#Feito por Thiago Narcizo

###############COVID - CASOS###############

url = 'https://covid19-brazil-api.now.sh/api/report/v1'

f2 = open("caso/casos.txt", "r")
contents = f2.readlines()

f5 = open("caso/obitos.txt", "r")
contents2 = f5.readlines()

def soma():
    casos_totais = int(contents[0].rstrip('\n')) + int(contents[1].rstrip('\n')) + int(contents[2].rstrip('\n')) + int(contents[3].rstrip('\n')) + int(contents[4].rstrip('\n')) + int(contents[5].rstrip('\n')) + int(contents[6].rstrip('\n')) + int(contents[7].rstrip('\n')) + int(contents[8].rstrip('\n')) + int(contents[9].rstrip('\n')) + int(contents[10].rstrip('\n')) + int(contents[11].rstrip('\n')) + int(contents[12].rstrip('\n')) + int(contents[13].rstrip('\n')) + int(contents[14].rstrip('\n')) + int(contents[15].rstrip('\n')) + int(contents[16].rstrip('\n')) + int(contents[17].rstrip('\n')) + int(contents[18].rstrip('\n')) + int(contents[19].rstrip('\n')) + int(contents[20].rstrip('\n')) + int(contents[21].rstrip('\n')) + int(contents[22].rstrip('\n')) + int(contents[23].rstrip('\n')) + int(contents[24].rstrip('\n')) + int(contents[25].rstrip('\n')) + int(contents[26].rstrip('\n'))
    return casos_totais

def soma_mortes():
    mortes_totais = int(contents2[0].rstrip('\n')) + int(contents2[1].rstrip('\n')) + int(contents2[2].rstrip('\n')) + int(contents2[3].rstrip('\n')) + int(contents2[4].rstrip('\n')) + int(contents2[5].rstrip('\n')) + int(contents2[6].rstrip('\n')) + int(contents2[7].rstrip('\n')) + int(contents2[8].rstrip('\n')) + int(contents2[9].rstrip('\n')) + int(contents2[10].rstrip('\n')) + int(contents2[11].rstrip('\n')) + int(contents2[12].rstrip('\n')) + int(contents2[13].rstrip('\n')) + int(contents2[14].rstrip('\n')) + int(contents2[15].rstrip('\n')) + int(contents2[16].rstrip('\n')) + int(contents2[17].rstrip('\n')) + int(contents2[18].rstrip('\n')) + int(contents2[19].rstrip('\n')) + int(contents2[20].rstrip('\n')) + int(contents2[21].rstrip('\n')) + int(contents2[22].rstrip('\n')) + int(contents2[23].rstrip('\n')) + int(contents2[24].rstrip('\n')) + int(contents2[25].rstrip('\n')) + int(contents2[26].rstrip('\n'))
    return mortes_totais

response = requests.get(url)

json_str = json.dumps(response.json())
data = json.loads(json_str)

f = open("caso/casos.txt", "w")

for i in data.items():
        tudo = i[1]
        for i in tudo:
            casos = i['cases']
            f.write(str(casos) + '\n')

f.write(str(soma()))
f.close()

###############COVID - ÓBITOS###############
f4 = open("caso/obitos.txt", "w")

for i in data.items():
        tudo2 = i[1]
        for i in tudo2:
            deaths = i['deaths']
            f4.write(str(deaths) + '\n')

f4.write(str(soma_mortes()))
f4.close()

###############DISTRITO FEDERAL - CASOS###############
url2 = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/df'

response_df = requests.get(url2)
json_str2 = json.dumps(response_df.json())
data2 = json.loads(json_str2)

f3 = open("caso/casos_df.txt", "w")

casos_df = [[i[1]] for i in data2.items()]

a = str(casos_df[3]).replace('[', '')
b = a.replace(']', '')

f3.write(b)
f3.close()

###############DISTRITO FEDERAL - ÓBITOS###############

f6 = open("caso/obitos_df.txt", "w")

mortes_df = [[i[1]] for i in data2.items()]

a2 = str(mortes_df[4]).replace('[', '')
b2 = a2.replace(']', '')

f6.write(b2)
f6.close()

###############REPORT - PRINTS###############
print('Fonte: https://covid19-brazil-api.now.sh' + '\n\n')
print('Casos totais de covid-19 no Brasil: ' + str(soma()) + '\n')
print('Mortes totais de covid-19 no Brasil: ' + str(soma_mortes()) + '\n')
print('Casos de covid-19 no DF: ' + str(b) + '\n')
print('Mortes de covid-19 no DF: ' + str(b2))
input()
