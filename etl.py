import pandas as pd
import os # Biblioteca para se comunicar com o sistema operacional
import glob

# Função de extract que le e consolida

pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta,'*.json')) # Como são vários arquivos json usamos o glob e o os para listar e fazer um join em tudo o que estiver dentro da pasta data e tenham qualquer nome (*) com .json.
df_list = [pd.read_json(arquivo)for arquivo in arquivos_json] # Agora com o for nos estamos lendo cada arquivo dentro dos arquivos_json e tranformar em um json.
df_total = pd.concat(df_list, ignore_index=True) # Aqui estamos concatenando os jsons e criando um indice novo.
print(df_total)

# Função que transforma



# Função que da load em csv ou parque