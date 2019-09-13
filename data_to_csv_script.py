from tqdm import tqdm
import os
import pandas as pd
root_path = "./"
data_path = os.path.join(root_path,"bbc")
category = ['politics','business','entertainment','sport','tech']

data = []
count_data = {}
for list in category:
  count_data[list]=0
# read dataset
for i in tqdm(os.listdir(data_path)):
  if i in category:
    print(i)
    for j in os.listdir(os.path.join(data_path,i)):
      print(os.path.join(data_path,i,j))
      if os.path.splitext(j)[1] == ".txt":
        with open(os.path.join(data_path,i,j),"rb") as f:
          file = f.read().decode('utf-8','ignore')
          data.append({"content" : file , "label": category.index(i)})
          count_data[category[category.index(i)]] +=1
#save to csv file
df = pd.DataFrame(data)
df.to_csv(root_path+'/data.csv')
