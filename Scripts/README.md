###Instruções

##Extratores

#hdfsWikipediaConstrutor.py

O script hdfsWikipediaConstrutor.py faz uma consulta à uma query na wikipedia, e retorna um arquivo h5 contendo uma database com os seguintes dados: ?com ?comLabel ?inception ?industry ?industryLabel ?coordinate ?country, onde ?com se refere a identificação da companhia na wikipedia, ?comLabel se refere ao nome comercial da empresa, ?inception se refere à data de criação,
?coordinate é um par de coordenadas latitude e longitude, ?industry é um índice numérico sobre a atividade da companhia, ?industryLabel é uma descrição do ramo da companhia e ?country é a identificação do país na wikipedia

#hdfsWikipediaVisualizador.py

O script hdfsWikipediaVisualizador.py Lê o arquivo h5 gerado por hdfsWikipediaConstrutor.py e retorna até o presente momento um arquivo chamado industries.csv com as infos do arquivo h5 num formato mais universal. 

#csvLinkedInVisualizador.py

