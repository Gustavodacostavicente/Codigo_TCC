import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

from sklearn.preprocessing import MinMaxScaler

Planilhas_de_Dados = ['Dados_DFrancisca.csv','Dados_Espinheiros.csv','Dados_Jorge.csv','Dados_Telles.csv','Dados_Timbo.csv']

np.random.seed(7)# Gerar resultado simulável
Dados_CAJ =  pd.read_csv(Planilhas_de_Dados[0],  sep=';')


Temperatura_Valor = Dados_CAJ.iloc[:,1:2].values
Pluviometro_Valor = Dados_CAJ.iloc[:,2:3].values
Energia_Valor = Dados_CAJ.iloc[:,3:4].values

Dados_Planilha = Dados_CAJ.drop(Dados_CAJ.iloc[:,0:1],1)

    
Separador = int(3)# Separação de dados em relação a Valores
Periodos = 1 # Relação móvel de preços passados para prever o próximo preço

Entrada = Dados_Planilha

Normaliza = MinMaxScaler(feature_range=(0, 1))# Função de Normalização entre 0 e 1

Entrada = Normaliza.fit_transform(Entrada) # Normaliza os valores de entrada
Saida = Normaliza.fit_transform(Energia_Valor[1:21])

Valor_Treinamento = Entrada[:-Separador] # Separa Treinamento
Valor_Teste = Entrada[-3:] # Separa Teste

Valor_Entrada = []
Valor_Seguinte=[]

for i in range(Periodos,len(Valor_Treinamento)): 
    Valor_Entrada.append(Valor_Treinamento[i-Periodos:i])# Cria matriz (Dados Treinamento - Periodos, Periodos)

Valor_Seguinte = Saida# Matriz de previsores do próximo valor buscado pela RNN
Valor_Entrada, Valor_Seguinte = np.array(Valor_Entrada),np.array(Valor_Seguinte)# Transforma numpy
Valor_Seguinte = Valor_Seguinte.reshape(Valor_Seguinte.shape[0],1,1)
Valor_Entrada = Valor_Entrada.reshape(Valor_Entrada.shape[0], Valor_Entrada.shape[1], Valor_Entrada.shape[2])# Transforma no formato de leitura da RN em (inputs,timesteps,1)
#%%
model = Sequential()
model.add(Dense(units=100, activation="sigmoid", input_shape=(Valor_Entrada.shape[1],Valor_Entrada.shape[2])))
model.add(Dense(units=100, activation="sigmoid"))
model.add(Dense(units=100, activation="sigmoid"))
model.add(Dense(units=1,activation="sigmoid"))# Bloco neural final
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
history = model.fit(Valor_Entrada, Valor_Seguinte, epochs = 1000, batch_size = 1 ,verbose=1)
model.save('model.h5')
#%%

plt.figure(2,figsize=(14,8), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel('Perda'); plt.xlabel('Épocas')
plt.semilogy(history.history['loss'])
plt.grid(True)
plt.title('Gráfico Função de Custo')


Teste = []
for i in range(1,len(Entrada)-3):
   Teste.append(Entrada[i][2])
Prev = model.predict(Valor_Entrada)

Previsao=Prev.tolist()
Previsao_Lista=[]
for i in range(0,len(Prev)):
    Previsao_Lista.append(Previsao[i][0])
plt.figure(3)
plt.plot(Previsao_Lista)
plt.plot(Teste)

#%% 
# Valor_Entrada_Novo = []
# Valor_Seguinte_Novo = []


# for i in range(Periodos,len(Valor_Treinamento)):
#     Valor_Entrada_Novo.append(Valor_Teste[i-Periodos:i])
#     Valor_Seguinte_Novo.append(Valor_Teste[i][0])
    
# Valor_Seguinte_Novo = np.array(Valor_Seguinte_Novo)
# Valor_Seguinte_Novo = Valor_Seguinte_Novo.reshape(len(Valor_Seguinte_Novo),1) 
# Valor_Seguinte_Novo = Normaliza.inverse_transform(Valor_Seguinte_Novo)

# Valor_Entrada_Novo = np.array(Valor_Entrada_Novo)

# Valor_Entrada_Novo = Valor_Entrada_Novo.reshape((Valor_Entrada_Novo.shape[0], Valor_Entrada_Novo.shape[1], Valor_Entrada_Novo.shape[2]))
# Preco_Previsao_Ponto_Movel = model.predict(Valor_Entrada_Novo)