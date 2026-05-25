import pandas as pd
data = {
    "name" : ["sam","ram","sita","laxman","hanu"],
    "age"  : [19,25,23,24,22]
}


df = pd.DataFrame(data, index = ["owner_1" , "owner_2" , "owner_3" , "owner_4", "owner_5"])
df["bussiness_name"] = ["restaurent" , "shopping mall" , "N/a" , "archerer" , "gym"]
new_row = pd.DataFrame([{"name" : "jatayu" , "age" : 27 ,"bussiness_name" : "flying school"}],
                       index = ["owner_6"])
df = pd.concat([df,new_row])
print(df)
