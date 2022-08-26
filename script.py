import yaml
import pandas as pd

file_list= ["opb_analytics_overdraft", "opb_analytics_transactions"]
get_dict = "columns_description"

for file in file_list:
    with open(f"/Users/matheus.henrique/repos/teste/yaml/{file}.yml") as f:
        x = yaml.load(f, Loader=yaml.FullLoader)
        pd.DataFrame(x[get_dict]).to_csv(f"{file}.csv")
