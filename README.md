# Análise de Arrecadações 

Este script realiza a análise de valores de arrecadação diária com base em dados históricos de vendas. Ele filtra os dados do último dia útil (excluindo feriados e domingos) e calcula estatísticas sobre os valores recebidos, como a média e o desvio padrão, para determinar se os ganhos estão dentro de uma faixa esperada. O script também identifica e filtra os dados fora do intervalo interquartil (outliers) e gera um alerta se os valores arrecadados estiverem abaixo ou acima da média estabelecida.

Essas funcionalidades podem ser úteis para a monitoração de performance financeira e análise de consistência de arrecadações diárias. Qualquer dúvida, sinta-se à vontade para me chamar no [linkedin](https://www.linkedin.com/in/paulo-oliveira-a6650121a/).

## Bibliotecas Utilizadas

* Pandas 
* Holidays

> [!IMPORTANT]
> Caso queira estar testando este script e precisar gerar uma base, você pode estar acessando meu outro repositório que gera bases ficticias para estudos, apenas clicando [aqui](https://github.com/PauloEnriqueOliveira/Geracao_Bases_Ficticias).
