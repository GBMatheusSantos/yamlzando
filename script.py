import yaml
import pandas as pd

# nome dos arquivos .yaml que devem ser transformados em csv
file_list= ["opb_analytics_overdraft", "opb_analytics_transactions"]

# estrutura de dict_list que deve ser considerado
get_dict = "columns_description"

for file in file_list:
    with open(f"yamls/{file}.yml") as f:
        x = yaml.load(f, Loader=yaml.FullLoader)
        pd.DataFrame(x[get_dict]).to_csv(f"{file}.csv")
