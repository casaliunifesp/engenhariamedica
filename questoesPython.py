"""
Respostas de questões sobre Python para a Unidade Curricular "Engenharia Médica Aplicada"
Instituto de Ciência e Tecnologia
Universidade Federal de São Paulo
@author: Adenauer G. CASALI (casali@unifesp.br)
"""

## Este código responde algumas das principais questões envolvendo
#métodos e bibliotecas em Python para a solução das atividades 
#práticas do curso. Será atualizado na medida em que questões forem
#surgindo. 


#%% Bibliotecas necessárias:
import numpy as np
import matplotlib.pyplot as plt




#%% Questão sobre indexação de arrays em python:

#Em aprendizado de máquina é muito comum trabalharmos com
#uma matriz de dados no formato "Características x Padrões" 
# e com um vetor de classes para cada um dos padrões contidos nos dados.
#Por exemplo, suponha que esta seja a matriz de dados
#no formato "Característica x Padrões"
Dados = np.random.rand(5,20)
#E suponha que este seja o vetor com as classes:
classes = np.random.permutation(np.hstack((np.ones([13]), np.zeros([7]))))
#no qual temos 7 padrões com classes =0 e 13 com classes =1. 

#Note que o array com as classes tem um formato de vetor (unidimensional): 
print(np.shape(classes))
#Muitas vezes, porém, o vetor de classes tem uma dimensão do tipo 1 x 20
#ou 20 x 1. Nestes casos, a dimensão "1" será inútil (vazia) e 
# poderá gerar problemas se você não souber lidar com ela. 
# Se esse for o caso, você pode eliminar esta dimensão extra com o 
# commando "squeeze" assim.
classes=np.squeeze(classes)

#Muito bem, considerando o array unidimensional "classes", suponha
# que você queira selecionar apenas os padrões que pertencem
#à classe =0. Você não precisa usar loops para isso! 
# Veja como fazer abaixo:
#O seguinte comando
classes==0
#retorna um array de verdadeiros ou falsos, onde os verdadeiros
# estão localizados nas posições correspondentes aos padrões em 
# que a classe é igual à 0.
#Para extrair estes padrões, você pode usar este vetor lógico como
#um indexador da matriz:
Dados_classe0 = Dados[:,classes==0]
#Note que estamos usando classes==0 na segunda dimensão da matriz
# Dados, pois é nesta dimensão que estão os padrões. 
# Veja que a dimensão da matriz resultante,
np.shape(Dados_classe0)
#é de características por padrões, mas apenas com os padrões 
# dos quais a classe é zero!
#Se você quiser selecionar os padrões com classe 1 é só fazer o
# mesmo procedimento, substituindo 0 por 1:
Dados_classe1 = Dados[:,classes==1]
#Fácil, não?

#Agora suponha que você quer juntar os padrões novamente. 
#Há várias formas de se fazer isso, mas caso você queira preservar 
#as posições das classes (tal que o vetor "classes" continue
# válido), você pode fazer assim: primeiro crie uma matriz com zeros
#na dimensão correta:
Dados_juntos=np.zeros_like(Dados)
#E agora preencha a matriz com os dados de cada classe usando o
#teste lógico como indexador:
Dados_juntos[:,classes==0]=Dados_classe0
Dados_juntos[:,classes==1]=Dados_classe1

#Esta nova matriz corresponde à mesma matriz com os dados originais?
print(np.array_equal(Dados_juntos,Dados))
#Sim! É assim que podemos facilmente separar e juntar classes de 
# padrões.




# %%Questão sobre mudanças das dimensões em arrays:

#Por vezes queremos transformar uma matriz bidimensional em
# um vetor. Por exemplo, imagine que você tem uma matriz Nc x Np que 
# corresponde a uma determinada características calculada em um certo 
# número Np de padrões e um certo número Nc de classes, como esta:
CaracteristicaUnica=np.concatenate((np.random.rand(1,20), np.random.rand(1,20)+2))
#Verifique as dimensões:
(Nc,Np)=np.shape(CaracteristicaUnica)
print('A matriz tem '+str(Np)+' padrões em '+str(Nc)+' classes')

#Vamos fazer um gráfico para visualizar as classes:
plt.figure()
plt.plot(CaracteristicaUnica[0,:],'ob')
plt.plot(CaracteristicaUnica[1,:],'or')
plt.xlabel('Número do padrão')
plt.ylabel('Valor da característica')
plt.title('Classes originais')
plt.show()

#Agora suponha que você queira juntar as classes em um vetor unidimensional
#mas sem perder informação de onde elas estão. 
#Para isso, você pode usar o comando reshape:
CaracteristicaUnica_classesjuntas=CaracteristicaUnica.reshape(Nc*Np,)
#Note que o input do reshape é a dimensão dos dados que será neste
#exemplo de um elemento unidimensional (40,) com todos os 40 padroes 
#juntos.
print(np.shape(CaracteristicaUnica_classesjuntas))

#Agora como separar as classes de volta? Use o reshape (veja a 
# diferença nos itens entre parênteses, agora a matriz será 2 x 20):
CaracteristicaUnica_classesseparadas=CaracteristicaUnica_classesjuntas.reshape(Nc,Np)
print(np.shape(CaracteristicaUnica_classesseparadas))

#Será que as classes foram misturadas? Vamos conferir fazendo o 
#mesmo gráfico de antes:
plt.figure()
plt.plot(CaracteristicaUnica_classesseparadas[0,:],'ob')
plt.plot(CaracteristicaUnica_classesseparadas[1,:],'or')
plt.xlabel('Número do padrão')
plt.ylabel('Valor da característica')
plt.title('Depois de Juntar e Separar')
plt.show()



