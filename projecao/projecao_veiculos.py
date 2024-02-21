import pandas as pd
from prophet import Prophet

# Carregar o dataset
df = pd.read_csv("carro_eletrico.csv")

# Filtrar os dados para considerar apenas carros eletricos
df_electric = df[df['Eletr_Flag'] == 'ELETRIFICADO']

# Converter a coluna de Data para o formato correto
df_electric['Data'] = pd.to_datetime(df_electric['Data'], format='%m/%d/%Y')

# Agrupar os dados por estado, cidade e data
grouped = df_electric.groupby(['UF', 'Municipio', pd.Grouper(key='Data', freq='M')])['Quantidade'].sum().reset_index()

# Renomear as colunas para o formato esperado pelo Prophet
grouped.rename(columns={'Data': 'ds', 'Quantidade': 'y'}, inplace=True)

# Função para criar e treinar o modelo Prophet para cada grupo (estado, cidade)
def create_and_train_prophet_model(data):
    if len(data) < 2:
        return pd.DataFrame() # Retorna um DataFrame vazio se houver menos de 2 linhas de dados
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=24, freq='M')
    forecast = model.predict(future)
    forecast['UF'] = data['UF'].iloc[0]
    forecast['Municipio'] = data['Municipio'].iloc[0]
    return forecast

# Aplicar a função para cada grupo
forecasts = grouped.groupby(['UF', 'Municipio']).apply(create_and_train_prophet_model).reset_index(drop=True)

# Filtrar resultados vazios
forecasts = forecasts[forecasts['yhat'].notna()]

# Exportar os resultados para um novo arquivo CSV
forecasts[['UF', 'Municipio', 'ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("projetos_carros_eletricos.csv", index=False)
