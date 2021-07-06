import pandas as pd
import matplotlib.pyplot as plt

Pluviometros_DG = []
Datas_DG = []
Lista_Maximos = []
Valores_Mensais_MM = []

Relatorios = ['relatorio_medida_ponto01.20.csv','relatorio_medida_ponto02.20.csv','relatorio_medida_ponto03.20.csv','relatorio_medida_ponto04.20.csv','relatorio_medida_ponto05.20.csv','relatorio_medida_ponto06.20.csv','relatorio_medida_ponto07.20.csv','relatorio_medida_ponto08.20.csv','relatorio_medida_ponto09.20.csv','relatorio_medida_ponto10.20.csv','relatorio_medida_ponto11.20.csv','relatorio_medida_ponto12.20.csv']
#Relatorios = ['relatorio_medida_ponto07.19.csv','relatorio_medida_ponto08.19.csv','relatorio_medida_ponto09.19.csv','relatorio_medida_ponto10.19.csv','relatorio_medida_ponto11.19.csv','relatorio_medida_ponto12.19.csv']

for z in range(0,len(Relatorios)):

    Dados = pd.read_csv(Relatorios[z],sep=';')
    
    Dados_Pluviometro = Dados['Relatório de Medidas - Ponto']
    
    Dados_Pluviometros_Lista = []
    Datas = []
    
    for i in range(0,len(Dados_Pluviometro)-5):
        try:
            Dados_Pluviometros_Lista.append(float(Dados_Pluviometro[5+i]))
            Datas.append(Dados['Unnamed: 2'][5+i])
        except:
            pass
        
    Dados_Pluviometros_Normal = []
    for i in range(0,len(Dados_Pluviometros_Lista)):
        if(Dados_Pluviometros_Lista[i] >= 1):
            Dados_Pluviometros_Normal.append(Dados_Pluviometros_Lista[i])
        else:
            Dados_Pluviometros_Normal.append(0)
    
    Maximos = []
    for i in range(0, len(Dados_Pluviometros_Normal),720):
        Lista_Maximos.append(max(Dados_Pluviometros_Normal[i:720+i]))
        Maximos.append(max(Dados_Pluviometros_Normal[i:720+i]))
         
    Valores_Mensais_MM.append(sum(Maximos))
        
    
    # plt.figure(z)        
    # plt.plot(Dados_Pluviometros_Normal)
    # plt.grid()
    # plt.title(Relatorios[z])
    
    Pluviometros_DG.append(Dados_Pluviometros_Normal)
    Datas_DG.append(Datas)
