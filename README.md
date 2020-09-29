# Intuito do Programa

Programa criado com o intuito de me aprofundar nos estudos de JSON e de Python, assim como na forma em que ocorre a integração dos dois.

# COVID-19
Tendo em vista a vontade de ter acesso às estatísticas concernentes à covid-19, eu escolhi a plataforma [COVID-19 Brazil API](https://covid19-brazil-api.now.sh) para ser a fonte dos casos totais tanto do Brasil quanto de Brasília (cidade que eu moro).

# Funcionalidade
Ele é inteiramente rodado em Python, com ajuda dos módulos *requests*, *json* e *pandas*. O *requests* entra em contato com a API, retira os dados e, com a ajuda do *json*, lança tudo em arquivos *.txt*

Após lidos, os arquivos servem como base para mostrar na própria Shell as informações por meio de um DataFrame do *pandas* (casos totais e óbitos).
