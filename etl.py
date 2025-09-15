import pandas as pd
import os 
import glob

#um funcao de extract que le e consolida no json
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivo_json = glob.glob(os.path.join(pasta,'*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

#print(df_total)
#print(arquivo_json) ##imprimir nome dos arquivos
#print(df_list) ##imprime os dados dos arquivos
#pd.read_json(path_or_buf=)



# uma funcao que transforma

# uma funcao que da load em csv ou parquet