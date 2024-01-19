from module_flatten_json import flatten_json
import json
import pandas as pd

file = r"C:\apps\development\py_proj\json_parsing\centric_poc_0dummy_employees.json"

json_file = open(file)
json_data = json.load(json_file)

# print(json_data)


flatten_json_data = flatten_json(json_data)

df_json= pd.DataFrame(flatten_json_data , ['key'])

df_json.to_csv('./s3_1.csv', index=False

print(df_json)
