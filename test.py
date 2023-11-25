import pandas as pd

data=[
    
    {"name":"sunny","age":20,"city":"bhopal"},
    {"name":"Krish","age":25,"city":"delhi"},
    {"name":"debu","age":21,"city":"jajpur"},
    {"name":"vikash","age":23,"city":"Mumbai"}
     
]
df=pd.DataFrame(data)
df.to_csv("data/data.csv",index=False)