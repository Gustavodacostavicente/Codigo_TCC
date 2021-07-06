import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Plota_Junto = True

Dados = pd.read_csv('Epagri2.csv',sep=';')

Dados_Vila_Nova_Media = Dados['Litoral Norte']

Dados_Pirabeiraba_Media = Dados['Litoral Norte.1']

Dados_Vila_Nova_Minima = Dados['Litoral Norte.2']

Dados_Pirabeiraba_Minima = Dados['Litoral Norte.3']

Dados_Vila_Nova_Maxima = Dados['Litoral Norte.4']

Dados_Pirabeiraba_Maxima = Dados['Litoral Norte.5']

Datas_Dados = Dados['R.Climática']

Datas = Datas_Dados[6:]

Temperatura_Vila_Nova_Minima = Dados_Vila_Nova_Minima[6:]
Temperatura_Vila_Nova_Media = Dados_Vila_Nova_Media[6:]
Temperatura_Vila_Nova_Maxima = Dados_Vila_Nova_Maxima[6:]

Temperatura_Pirabeiraba_Minima = Dados_Pirabeiraba_Minima[6:]
Temperatura_Pirabeiraba_Media = Dados_Pirabeiraba_Media[6:]
Temperatura_Pirabeiraba_Maxima = Dados_Pirabeiraba_Maxima[6:]

Temperatura_Vila_Nova_Minima_Lista = []
Temperatura_Vila_Nova_Media_Lista = []
Temperatura_Vila_Nova_Maxima_Lista = []

Temperatura_Pirabeiraba_Minima_Lista = []
Temperatura_Pirabeiraba_Media_Lista = []
Temperatura_Pirabeiraba_Maxima_Lista = []


for i in range(7,len(Temperatura_Pirabeiraba_Maxima)+6):
    if(Temperatura_Vila_Nova_Minima[i] == '-'): 
        Temperatura_Vila_Nova_Minima_Lista.append(round(float(Temperatura_Vila_Nova_Minima[i-1]),1))
    else:
        Temperatura_Vila_Nova_Minima_Lista.append(round(float(Temperatura_Vila_Nova_Minima[i]),1))
        
    if(Temperatura_Vila_Nova_Media[i] == '-'):
        Temperatura_Vila_Nova_Media_Lista.append(round(float(Temperatura_Vila_Nova_Media[i-1]),1))
    else:
        Temperatura_Vila_Nova_Media_Lista.append(round(float(Temperatura_Vila_Nova_Media[i]),1))
        
    if(Temperatura_Vila_Nova_Maxima[i] == '-'): 
        Temperatura_Vila_Nova_Maxima_Lista.append(round(float(Temperatura_Vila_Nova_Maxima[i-1]),1))
    else:
        Temperatura_Vila_Nova_Maxima_Lista.append(round(float(Temperatura_Vila_Nova_Maxima[i]),1))

    if(Temperatura_Pirabeiraba_Minima[i] == '-'): 
        Temperatura_Pirabeiraba_Minima_Lista.append(round(float(Temperatura_Pirabeiraba_Minima[i-1]),1))
    else:
        Temperatura_Pirabeiraba_Minima_Lista.append(round(float(Temperatura_Pirabeiraba_Minima[i]),1))
        
    if(Temperatura_Pirabeiraba_Media[i] == '-'):
        Temperatura_Pirabeiraba_Media_Lista.append(round(float(Temperatura_Pirabeiraba_Media[i-1]),1))
    else:
        Temperatura_Pirabeiraba_Media_Lista.append(round(float(Temperatura_Pirabeiraba_Media[i]),1))
        
    if(Temperatura_Pirabeiraba_Maxima[i] == '-'): 
        Temperatura_Pirabeiraba_Maxima_Lista.append(round(float(Temperatura_Pirabeiraba_Maxima[i-1]),1))
    else:
        Temperatura_Pirabeiraba_Maxima_Lista.append(round(float(Temperatura_Pirabeiraba_Maxima[i]),1))
        
  
Datas_Exemplo = []    
Vetores_J = []

for j in range(6,len(Temperatura_Pirabeiraba_Maxima)):
    if(Datas[j][0:2]=='25'):  
        Vetores_J.append(j)
        
        

Temperatura_Jan_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[:Vetores_J[0]-5]
Temperatura_Fev_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[0]-5:Vetores_J[1]-5]
Temperatura_Mar_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[1]-5:Vetores_J[2]-5]
Temperatura_Abr_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[2]-5:Vetores_J[3]-5]
Temperatura_Mai_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[3]-5:Vetores_J[4]-5]
Temperatura_Jun_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[4]-5:Vetores_J[5]-5]
Temperatura_Jul_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[5]-5:Vetores_J[6]-5]
Temperatura_Ago_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[6]-5:Vetores_J[7]-5]
Temperatura_Set_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[7]-5:Vetores_J[8]-5]
Temperatura_Out_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[8]-5:Vetores_J[9]-5]
Temperatura_Nov_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[9]-5:Vetores_J[10]-5]
Temperatura_Dez_2019_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[10]-5:Vetores_J[11]-5]

Temperatura_Maxima_2019_Maxima = [np.mean(Temperatura_Jan_2019_Maxima),np.mean(Temperatura_Fev_2019_Maxima),
np.mean(Temperatura_Mar_2019_Maxima),np.mean(Temperatura_Abr_2019_Maxima), 
np.mean(Temperatura_Mai_2019_Maxima),np.mean(Temperatura_Jun_2019_Maxima),
np.mean(Temperatura_Jul_2019_Maxima),np.mean(Temperatura_Ago_2019_Maxima),
np.mean(Temperatura_Set_2019_Maxima),np.mean(Temperatura_Out_2019_Maxima),
np.mean(Temperatura_Nov_2019_Maxima),np.mean(Temperatura_Dez_2019_Maxima)]


Temperatura_Jan_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[11]-5:Vetores_J[12]-5]
Temperatura_Fev_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[12]-5:Vetores_J[13]-5]
Temperatura_Mar_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[13]-5:Vetores_J[14]-5]
Temperatura_Abr_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[14]-5:Vetores_J[15]-5]
Temperatura_Mai_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[15]-5:Vetores_J[16]-5]
Temperatura_Jun_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[16]-5:Vetores_J[17]-5]
Temperatura_Jul_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[17]-5:Vetores_J[18]-5]
Temperatura_Ago_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[18]-5:Vetores_J[19]-5]
Temperatura_Set_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[19]-5:Vetores_J[20]-5]
Temperatura_Out_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[20]-5:Vetores_J[21]-5]
Temperatura_Nov_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[21]-5:Vetores_J[22]-5]
Temperatura_Dez_2020_Maxima = Temperatura_Vila_Nova_Maxima_Lista[Vetores_J[22]-5:Vetores_J[23]-5]

Temperatura_Maxima_2020_Maxima = [np.mean(Temperatura_Jan_2020_Maxima),np.mean(Temperatura_Fev_2020_Maxima),
 np.mean(Temperatura_Mar_2020_Maxima),np.mean(Temperatura_Abr_2020_Maxima), 
np.mean(Temperatura_Mai_2020_Maxima),np.mean(Temperatura_Jun_2020_Maxima),
np.mean(Temperatura_Jul_2020_Maxima),np.mean(Temperatura_Ago_2020_Maxima),
np.mean(Temperatura_Set_2020_Maxima),np.mean(Temperatura_Out_2020_Maxima),
np.mean(Temperatura_Nov_2020_Maxima),np.mean(Temperatura_Dez_2020_Maxima)]


Temperatura_Jan_2019_Media = Temperatura_Vila_Nova_Media_Lista[:Vetores_J[0]-5]
Temperatura_Fev_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[0]-5:Vetores_J[1]-5]
Temperatura_Mar_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[1]-5:Vetores_J[2]-5]
Temperatura_Abr_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[2]-5:Vetores_J[3]-5]
Temperatura_Mai_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[3]-5:Vetores_J[4]-5]
Temperatura_Jun_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[4]-5:Vetores_J[5]-5]
Temperatura_Jul_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[5]-5:Vetores_J[6]-5]
Temperatura_Ago_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[6]-5:Vetores_J[7]-5]
Temperatura_Set_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[7]-5:Vetores_J[8]-5]
Temperatura_Out_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[8]-5:Vetores_J[9]-5]
Temperatura_Nov_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[9]-5:Vetores_J[10]-5]
Temperatura_Dez_2019_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[10]-5:Vetores_J[11]-5]

Temperatura_Media_2019_Media = [np.mean(Temperatura_Jan_2019_Media),np.mean(Temperatura_Fev_2019_Media),
np.mean(Temperatura_Mar_2019_Media),np.mean(Temperatura_Abr_2019_Media), 
np.mean(Temperatura_Mai_2019_Media),np.mean(Temperatura_Jun_2019_Media),
np.mean(Temperatura_Jul_2019_Media),np.mean(Temperatura_Ago_2019_Media),
np.mean(Temperatura_Set_2019_Media),np.mean(Temperatura_Out_2019_Media),
np.mean(Temperatura_Nov_2019_Media),np.mean(Temperatura_Dez_2019_Media)]


Temperatura_Jan_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[11]-5:Vetores_J[12]-5]
Temperatura_Fev_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[12]-5:Vetores_J[13]-5]
Temperatura_Mar_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[13]-5:Vetores_J[14]-5]
Temperatura_Abr_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[14]-5:Vetores_J[15]-5]
Temperatura_Mai_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[15]-5:Vetores_J[16]-5]
Temperatura_Jun_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[16]-5:Vetores_J[17]-5]
Temperatura_Jul_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[17]-5:Vetores_J[18]-5]
Temperatura_Ago_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[18]-5:Vetores_J[19]-5]
Temperatura_Set_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[19]-5:Vetores_J[20]-5]
Temperatura_Out_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[20]-5:Vetores_J[21]-5]
Temperatura_Nov_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[21]-5:Vetores_J[22]-5]
Temperatura_Dez_2020_Media = Temperatura_Vila_Nova_Media_Lista[Vetores_J[22]-5:Vetores_J[23]-5]    

Temperatura_Media_2020_Media = [np.mean(Temperatura_Jan_2020_Media),np.mean(Temperatura_Fev_2020_Media),
np.mean(Temperatura_Mar_2020_Media),np.mean(Temperatura_Abr_2020_Media), 
np.mean(Temperatura_Mai_2020_Media),np.mean(Temperatura_Jun_2020_Media),
np.mean(Temperatura_Jul_2020_Media),np.mean(Temperatura_Ago_2020_Media),
np.mean(Temperatura_Set_2020_Media),np.mean(Temperatura_Out_2020_Media),
np.mean(Temperatura_Nov_2020_Media),np.mean(Temperatura_Dez_2020_Media)]

    
Temperatura_Jan_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[:Vetores_J[0]-5]
Temperatura_Fev_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[0]-5:Vetores_J[1]-5]
Temperatura_Mar_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[1]-5:Vetores_J[2]-5]
Temperatura_Abr_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[2]-5:Vetores_J[3]-5]
Temperatura_Mai_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[3]-5:Vetores_J[4]-5]
Temperatura_Jun_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[4]-5:Vetores_J[5]-5]
Temperatura_Jul_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[5]-5:Vetores_J[6]-5]
Temperatura_Ago_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[6]-5:Vetores_J[7]-5]
Temperatura_Set_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[7]-5:Vetores_J[8]-5]
Temperatura_Out_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[8]-5:Vetores_J[9]-5]
Temperatura_Nov_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[9]-5:Vetores_J[10]-5]
Temperatura_Dez_2019_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[10]-5:Vetores_J[11]-5]

Temperatura_Minima_2019_Minima = [np.mean(Temperatura_Jan_2019_Minima),np.mean(Temperatura_Fev_2019_Minima),
np.mean(Temperatura_Mar_2019_Minima),np.mean(Temperatura_Abr_2019_Minima), 
np.mean(Temperatura_Mai_2019_Minima),np.mean(Temperatura_Jun_2019_Minima),
np.mean(Temperatura_Jul_2019_Minima),np.mean(Temperatura_Ago_2019_Minima),
np.mean(Temperatura_Set_2019_Minima),np.mean(Temperatura_Out_2019_Minima),
np.mean(Temperatura_Nov_2019_Minima),np.mean(Temperatura_Dez_2019_Minima)]


Temperatura_Jan_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[11]-5:Vetores_J[12]-5]
Temperatura_Fev_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[12]-5:Vetores_J[13]-5]
Temperatura_Mar_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[13]-5:Vetores_J[14]-5]
Temperatura_Abr_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[14]-5:Vetores_J[15]-5]
Temperatura_Mai_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[15]-5:Vetores_J[16]-5]
Temperatura_Jun_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[16]-5:Vetores_J[17]-5]
Temperatura_Jul_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[17]-5:Vetores_J[18]-5]
Temperatura_Ago_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[18]-5:Vetores_J[19]-5]
Temperatura_Set_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[19]-5:Vetores_J[20]-5]
Temperatura_Out_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[20]-5:Vetores_J[21]-5]
Temperatura_Nov_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[21]-5:Vetores_J[22]-5]
Temperatura_Dez_2020_Minima = Temperatura_Vila_Nova_Minima_Lista[Vetores_J[22]-5:Vetores_J[23]-5]

Temperatura_Minima_2020_Minima = [np.mean(Temperatura_Jan_2020_Minima),np.mean(Temperatura_Fev_2020_Minima),
np.mean(Temperatura_Mar_2020_Minima),np.mean(Temperatura_Abr_2020_Minima), 
np.mean(Temperatura_Mai_2020_Minima),np.mean(Temperatura_Jun_2020_Minima),
np.mean(Temperatura_Jul_2020_Minima),np.mean(Temperatura_Ago_2020_Minima),
np.mean(Temperatura_Set_2020_Minima),np.mean(Temperatura_Out_2020_Minima),
np.mean(Temperatura_Nov_2020_Minima),np.mean(Temperatura_Dez_2020_Minima)]


        
# if(Plota_Junto == False):        
#     plt.figure(0)
#     plt.plot(Temperatura_Vila_Nova_Minima_Lista)
#     plt.title('Vila Nova Temp.Min')
    
#     plt.figure(1)
#     plt.plot(Temperatura_Vila_Nova_Media_Lista)
#     plt.title('Vila Nova Temp.Med')
    
#     plt.figure(2)
#     plt.plot(Temperatura_Vila_Nova_Maxima_Lista)
#     plt.title('Vila Nova Temp.Max')
    
#     plt.figure(3)
#     plt.plot(Temperatura_Pirabeiraba_Minima_Lista)
#     plt.title('Pirabeiraba Temp.Min')
    
#     plt.figure(4)
#     plt.plot(Temperatura_Pirabeiraba_Media_Lista)
#     plt.title('Pirabeiraba Temp.Med')
    
#     plt.figure(5)
#     plt.plot(Temperatura_Pirabeiraba_Maxima_Lista)
#     plt.title('Pirabeiraba Temp.Max')
# else:
#     plt.figure(0)
#     plt.plot(Temperatura_Vila_Nova_Minima_Lista)
#     plt.plot(Temperatura_Vila_Nova_Media_Lista)
#     plt.plot(Temperatura_Vila_Nova_Maxima_Lista)
#     plt.title('Vila Nova Temperaturas')
#     plt.legend(['Mínima','Média','Máxima'])
    
#     plt.figure(1)
#     plt.plot(Temperatura_Pirabeiraba_Minima_Lista)
#     plt.plot(Temperatura_Pirabeiraba_Media_Lista)
#     plt.plot(Temperatura_Pirabeiraba_Maxima_Lista)
#     plt.title('Pirabeiraba Temperaturas')
#     plt.legend(['Mínima','Média','Máxima'])