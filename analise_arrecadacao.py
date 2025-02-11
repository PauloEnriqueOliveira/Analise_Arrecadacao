import pandas as pd
import holidays
from datetime import datetime, timedelta

feriados_brasil = holidays.Brazil()
data_ontem = datetime.now() - timedelta(days=2)
data_3_meses_atras = data_ontem - timedelta(days=90)
caminho = r'caminho do arquivo'

def Dia_Escolhidos():
    ontem = datetime.today() - timedelta(days=2)
    return ontem.weekday()

dia_atual = Dia_Escolhidos()

def Dia_Escolhido():
    ontem = datetime.today() - timedelta(days=2)
    return ontem

def nao_eh_feriado_brasileiro(data):
    return data not in feriados_brasil

df_bruto = pd.read_csv(caminho, parse_dates=['DATA_VENDA'], dayfirst=True)

df_outlayers = df_bruto
df_res_final = df_bruto[df_bruto['DATA_VENDA'].dt.date == Dia_Escolhido().date()]

df_outlayers = df_outlayers[df_outlayers['DATA_VENDA'].apply(nao_eh_feriado_brasileiro)]
df_outlayers = df_outlayers[(df_outlayers['DATA_VENDA'] >= data_3_meses_atras) & (df_outlayers['DATA_VENDA'] <= data_ontem)]

df_outlayers['Dia_semana'] = df_outlayers['DATA_VENDA'].dt.weekday
df_outlayers = df_outlayers[df_outlayers['Dia_semana'] != 6]
df_outlayers = df_outlayers[df_outlayers['Dia_semana'] == dia_atual]

Q1_arrecadacao = df_outlayers['VALOR_RECEBIDO'].quantile(0.25)
Q3_arrecadacao = df_outlayers['VALOR_RECEBIDO'].quantile(0.75)
IQR_arrecadacao = Q3_arrecadacao - Q1_arrecadacao
limite_inferior_arrecadacao = Q1_arrecadacao - 1.5 * IQR_arrecadacao
limite_superior_arrecadacao = Q3_arrecadacao + 1.5 * IQR_arrecadacao

filtro_dia = df_outlayers[(df_outlayers['VALOR_RECEBIDO'] >= limite_inferior_arrecadacao) & (df_outlayers['VALOR_RECEBIDO'] <= limite_superior_arrecadacao)]

soma_arrecadacao_por_dia = filtro_dia.groupby(filtro_dia['DATA_VENDA'].dt.date)['VALOR_RECEBIDO'].sum()

media_geral = soma_arrecadacao_por_dia.mean()
desvio_padrao = soma_arrecadacao_por_dia.std()

media_menor_valor = media_geral - desvio_padrao
media_maior_valor = media_geral + desvio_padrao

df_res_final = df_res_final[df_res_final['DATA_VENDA'].dt.date == Dia_Escolhido().date()]

soma_valoresd = df_res_final['VALOR_RECEBIDO'].sum()

if soma_valoresd == 0:
    print("Não foi encontrado registros ontem")
elif soma_valoresd < media_menor_valor:
    print(f"Os ganhos de ontem foram abaixo da média mínima: {soma_valoresd:.2f} (Mín: {media_menor_valor:.2f}, Máx: {media_maior_valor:.2f})")
elif soma_valoresd > media_maior_valor:
    print(f"Os ganhos de ontem foram acima da média máxima: {soma_valoresd:.2f} (Mín: {media_menor_valor:.2f}, Máx: {media_maior_valor:.2f})")
else:
    print(f"Os valores estão dentro da faixa esperada: {soma_valoresd:.2f} (Mín: {media_menor_valor:.2f}, Máx: {media_maior_valor:.2f})")
