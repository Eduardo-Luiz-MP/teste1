import numpy as np
import pandas as pd
import openpyxl as op

num_rows = 50

data = {
    "Produto":[f"Produto_{i}"for i in range(1,num_rows+1)],
    "Categoria":np.random.choice(["Televisão","Computador","Celular","Tablet","Impressora"],size=num_rows),
    "Preço":np.random.uniform(100.0,2000.0,size=num_rows).round(2),
    "Quantidade_Vendida":np.random.randint(1,50,size=num_rows)
    }
df = pd.DataFrame(data)
df["Faturamento"] = df["Preço"] * df["Quantidade_Vendida"]
def multiplicar(x):
    return x["Preço"]  * x["Quantidade_Vendida"]
df["Faturamento2"] = df.apply(multiplicar, axis = 1)
df["Faturamento"].min()
df["Faturamento"].mean()
df["Faturamento"].std()
df["Faturamento"].max()
df_filtrado_computador = df[df["Categoria"]=="Computador"]
df_filtrado_computador_maior500 = df[(df["Preço"]>500) & (df["Categoria"]=="Computador")]
df_filtrado_maior40_ou_impressora = df[(df["Quantidade_Vendida"]>40) | (df["Categoria"]=="Impressora")]
caminho = r'C:\Users\eduardo_pasqualotto\Desktop\Pasta Git\atividade.xlsx'
df.to_excel(caminho)

##---------------------------##

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
caminho_arquivo = r"C:\Users\eduardo_pasqualotto\Desktop\Pasta Git\Frutas.xlsx"
df_Frutas = pd.read_excel(caminho_arquivo)
df_Frutas = df_Frutas["Fruta     Cor        Gosto      Formato    Casca"].str.split(expand=True)

df_Frutas.columns = ["Frutas","Cor","Sabor","Formato","Textura"]

X = df_Frutas[["Cor","Sabor","Formato","Textura"]]
y = df_Frutas["Frutas"]
mapeamento_cor = {"Verde":0,"Amarelo":1,"Marrom":2}
mapeamento_sabor = {"Azedo":0,"Doce":1}
mapeamento_formato = {"Oval":0,"Curvado":1,"Alongado":2}
mapeamento_textura = {"Liso":0,"Peludo":1}
X = df_Frutas [["Cor","Sabor","Formato","Textura"]]
X["Cor"] = X["Cor"].map(mapeamento_cor)
X["Sabor"] = X["Sabor"].map(mapeamento_sabor)
X["Formato"] = X["Formato"].map(mapeamento_formato)
X["Textura"] = X["Textura"].map(mapeamento_textura)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=37)
modelo = DecisionTreeClassifier()

modelo.fit(X_train, y_train)
previsoes = modelo.predict(X_test)
caminho_arquivo2 = r"C:\Users\eduardo_pasqualotto\Desktop\Pasta Git\Frutas2.xlsx"
df_frutas2 = pd.read_excel(caminho_arquivo2)
df_frutas2["Cor"] = df_frutas2["Cor"].map(mapeamento_cor)
df_frutas2["Sabor"] = df_frutas2["Sabor"].map(mapeamento_sabor)
df_frutas2["Textura"] = df_frutas2["Textura"].map(mapeamento_textura)
df_frutas2["Formato"] = df_frutas2["Formato"].map(mapeamento_formato)
previsoes_novos_dados = modelo.predict(df_frutas2)
previsoes_novos_dados

##-------------------##

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
caminho1 = r"C:\Users\eduardo_pasqualotto\Desktop\Pasta Git\cliente_compras.xlsx"
caminho2 = r"C:\Users\eduardo_pasqualotto\Desktop\Pasta Git\clientes_compra_misterio.xlsx"
df_compras = pd.read_excel(caminho1)
df_compras2 = pd.read_excel(caminho2)
X = df_compras[["tempo_gasto_site","numero_itens_visualizados","compras_anteriores"]]
y = df_compras["compra"]
mapeamento_compra_antes = {"Sim":0,"Não":1}
X["compras_anteriores"] = X["compras_anteriores"].map(mapeamento_compra_antes)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=37)
modelo = DecisionTreeClassifier()

modelo.fit(X_train, y_train)
previsoes = modelo.predict(X_test)
df_compras2["compras_anteriores"] = df_compras2["compras_anteriores"].map(mapeamento_compra_antes)
previsoes_novos_dados = modelo.predict(df_compras2)
previsoes_novos_dados