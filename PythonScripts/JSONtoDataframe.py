import json
import pandas as pd

def flatten_json(data, parent_key='', sep='_'):
  """
    Função recursiva pra expandir os objetos do JSON.
    Vai ignorar objetos chamados "Conversations", "ChatgptSharing" e "ListOfCode"
      pois esses tem tamanho variável (ou seja, podem ter de 0 a N objetos dentro).
      Esse objetos vão ser expandidos posteriormente.
  """
  items = {}

  for chave, valor in data.items():
    new_key = f"{parent_key}{sep}{chave}" if parent_key else chave

    if isinstance(valor, dict):
      items.update(flatten_json(valor, new_key, sep))

    elif isinstance(valor, list):
      if chave in ["Conversations", "ChatgptSharing", 'ListOfCode']:
        items[new_key] = valor
      else:
        for i, sub_item in enumerate(valor):
          if isinstance(sub_item, dict):
            items.update(flatten_json(sub_item, f"{new_key}_{i}", sep))
          else:
            items[f"{new_key}_{i}"] = sub_item

    else:
      items[new_key] = valor

  return items


# abrindo o arquivo e salvando como json
with open("../snapshot_20230727/20230727_195927_pr_sharings.json") as file:
  json_data = json.load(file)

# se existe o objeto Sources no JSON, pegamos direto a lista de dentro de Sources
# se Sources tiver outros atributos, e vc quiser guardar esses valores
# isso vai ter que ser modificado
if isinstance(json_data, dict) and "Sources" in json_data:
  json_data = json_data["Sources"]

# pra cada coluna do JSON, vamos achatar ele
# não é mais um passo extremamente necessário, pode ser simplificado
# funcionava assim antes porque ChatgptSharing tinha os objetos de Mention
# mas agora o ChatgptSharing é tratado posteriormente
# se o código ficar muito pesado, da pra otimizar essa parte
# (ou seja, simplificar o uso da função aqui)
data_flat = [flatten_json(item) for item in json_data]
df = pd.DataFrame(data_flat)

# Expandir ChatgptSharing
if 'ChatgptSharing' in df.columns:
    df = df.explode('ChatgptSharing').reset_index(drop=True)
    # a linha abaixo achata as colunas de Mention, principalmente
    # pode ser otimizado fazendo algo como flatten_json(df['ChatgptSharing'].get('Mention')))
    # (mas acho que o jeito que eu escrevi ali ta errado, teria que dar uma olhada)
    chatgpt_expanded = pd.DataFrame([flatten_json(obj) for obj in df['ChatgptSharing']])
    chatgpt_expanded = chatgpt_expanded.add_prefix("ChatgptSharing_")
    df = df.drop(columns=['ChatgptSharing']).reset_index(drop=True)
    df = df.join(chatgpt_expanded)

# Expandir Conversations
if 'ChatgptSharing_Conversations' in df.columns:
    df = df.explode('ChatgptSharing_Conversations')
    conversations_expanded = pd.json_normalize(df['ChatgptSharing_Conversations'])
    conversations_expanded = conversations_expanded.add_prefix("ChatgptSharing_Conversations_")
    df = df.drop(columns=['ChatgptSharing_Conversations']).reset_index(drop=True)
    df = df.join(conversations_expanded)
    print(list(conversations_expanded.columns.values))

# Expandir ListOfCode
if 'ChatgptSharing_Conversations_ListOfCode' in df.columns:
    df = df.explode('ChatgptSharing_Conversations_ListOfCode')
    listofcode_expanded = pd.json_normalize(df['ChatgptSharing_Conversations_ListOfCode'])
    listofcode_expanded = listofcode_expanded.add_prefix("ChatgptSharing_Conversations_ListOfCode_")
    df = df.drop(columns=['ChatgptSharing_Conversations_ListOfCode']).reset_index(drop=True)

# lembrando que:
# se o código ficar muito demorado pra rodar, podes otimizar dois pontos:
# o uso do flatten_json pra fazer o achatamento inicial
# o uso do flatten_json nos objetos dentro de ChatgptSharing

# print('ok!')

# assim vc consegue printar o nome das colunas do dataframe
# print(df.columns)

# inclusive consegues fazer um for em cima disso
# for col in df.columns

# pra renomear as colunas, ficaria algo como:
# df_tmp1 = df.rename(columns = {
#     'ChatgptSharing_Conversations_ListOfCode_Content': 'ListOfCode_Content',
#     'ChatgptSharing_Conversations_ListOfCode_Type': 'ListOfCode_Type',
#     # 'Nome_Atual': 'Novo_Nome'
# })
# print(df_tmp1.columns)
# podes fazer quantas colunas quiser por vez

# df.shape te mostra a quantidade de colunas e linhas do dataframe
# print(df.shape)

# se você fizer algo como
rows, cols = df.shape
# rows recebe a quantidade de linhas e cols recebe a quantidade de colunas
# print(f'linhas: {rows}')
# print(f'colunas: {cols}')

# consegues filtrar um Dataframe assim:
# nome_do_df[nome_do_df['nome_da_coluna'] operador valor]
df[df['Author'] == 'jabrena']
print(df['Author'])

# da pra usar multiplas colunas também:
# IMPORTANTE: cada condição TEM que estar entre ()
# nome_do_df[(nome_do_df['nome_da_coluna'] operador valor) & (nome_do_df['nome_da_coluna'] operador valor)]
# exemplo:
# df[(df['Author'] == 'jabrena') & (df['ChatgptSharing_NumberOfPrompts'] <= 2)]

# OBS.: abaixo tem mais coisa

# você pode deletar colunas do dataframe
# df_tmp2 = df.drop(columns = ['URL', 'Body', 'ChatgptSharing_HTMLContent'])
# print(df_tmp2.columns)

# também podes mostrar apenas colunas especificas, em vez de o dataframe todo
# df[['Author', 'ChatgptSharing_Conversations_Prompt', 'ChatgptSharing_Conversations_ListOfCode_ReplaceString']]


df_tmp2 = df[['Type', 'Author', 'ChatgptSharing_Conversations_Prompt', 'ChatgptSharing_Conversations_Answer']]
print(df_tmp2[df_tmp2.isnull()])
df[df['ChatgptSharing_Status'] != 200].to_csv('out.csv', index=False) 