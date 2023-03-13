import pandas as pd

#-------criando um dataframe-----------
'''
* O DATAFRAME é uma tabela, com linhas e colunas.
* As colunas são chamadas de SÉRIES. Pode ter apenas um tipo de variável (float, int, boleana...), é do tipo lista
* As linhas são chmadasd de REGISTROS, ou AMOSTRAS. Pode conter vários tipos de variáveis (float, int, boleana...), é do tipo dicionário
* Ocabeçalho da tabela é chamado de FEATURES, ATRIBUTO ou VARIÁVEL
'''
print('CRIANDO UM DATAFRAME\n')
df = pd.DataFrame({     # passando um dicionário como parâmetro de entrada do dataframe
    "NOME":["marcos", "edivânia", "leonide", "josivaldo"],           #cada chave do dicionário pade conter mais de um valor (uma lista)
    "IDADE":[32, 56, 78, 92],
    "PESO":[60.3, 49.2, 80.4, 72.4],
    "VIVO":[True, True, True, False]
})
print(f"df.info: \n{df.info()}")
print(f"df: \n{df}")
print("------------------------------------")

#-----ALTERANDO o ÍNDICE-----------------
print("ALTERANDO o ÍNDICE")
df.index=df.NOME
print(f"df: \n{df}")
print("------------------------------------")

#--------CRIANDO SÉRIES DO TIPO COLUNA------------------
print('CRIANDO SÉRIES DO TIPO COLUNA')
#df.Series({"NOME": "Juvenal", "IDADE":26, "PESO": 96.8, "VIVO":False})
sn1 = pd.Series(["Santana", "Santos", "Silva","Bento"], name="SOBRENOME")    # cria uma série do para uma nova coluna
sn2 = pd.Series(["Pr", "Sc", "Sp","Rj"], name="NATURALIDADE")
tabela = pd.DataFrame({sn1.name:sn1, sn2.name:sn2})    # adiciona as colunas no dataframe 'tabela'
print(f"df: \n{tabela}")
print("------------------------------------")

#-------INSERINDO COLUNAS NO DATAFRAME----------
print('INSERINDO COLUNAS NO DATAFRAME')
df.insert(1, "SOBRENOME",["Santana", "Santos", "Silva","Bento"])    # insere uma coluna no índice 1
df["FILHOS"] = [0, 1, 2, 3]             # adiciona uma coluna ao final do dicionario
df["AUTO MÓVEL"] = True     # adiciona uma coluna ao final do dicionario, com todas as linhas igual a 'True'
print(f"df: \n{df}")
print("------------------------------------")

#----------APAGANDO UM COLUNA DO DATAFRAME -----
print('APAGANDO UM COLUNA DO DATAFRAME')
#del df["SOBRENOME"]        # apaga a coluna in-place(no próprio dataframe)
new = df.pop("SOBRENOME")    # apaga a coluna 'sobrenome' do dataframe 'df', e passa para o dateframe 'new'
print(f"new: \n{new}")
print(f"df: \n{df}")
new = df.drop(["AUTO MÓVEL","FILHOS"], axis=1)    # 'new' recebe 'df' com aa colunaa 'AUTO MÓVEL' e "FILHOS" apagados (axis 1 para apagar coluna, 0 para apagar linha)
print(f"new: \n{new}")
print(f"df: \n{df}")
df.drop("VIVO", axis=1, inplace=True)    # o 'inplace=True' retorna a alteração para o próprio dataframe
print(f"df: \n{df}")
print("------------------------------------")


#--------------APAGANDO UMA LINHA------------------
print("APAGANDO UMA LINHA\n")
new = df.drop("marcos")        # 'new' recebe 'df' com o índice 'marcos' apagado
print(f"new: \n{new}")
print(f"df: \n{df}")
df.drop(["edivânia","leonide"], inplace=True)        # o 'inplace=True' retorna a alteração para o próprio dataframe
print(f"df: \n{df}")
print("------------------------------------")

#-------salvando em um csv---------------
df.to_csv("dados.csv", index=False, encoding="UTF-32", sep=";")         # salva em CSV sem o índice, e UTF-32 para salvar os caracteres especiais
df.to_excel("dadosExcel.xlsx", index=False)         # salva em excel
