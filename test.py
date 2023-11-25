import pandas as pd

data=[
    
    {"name":"sunny","age":20,"city":"hopal"},
    {"name":"Krish","age":25,"city":"delhi"},
    {"name":"debu","age":21,"city":"jajpur"}
     
]
df=pd.DataFrame(data)
df.to-csv("data/data.csv",index=False)