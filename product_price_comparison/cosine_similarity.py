#Import Libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("cleaned_scraped_data_file.csv",encoding ='latin1')

df.head(3) #Print the first 3rows

#Create a list of important columns 
features = ["titile"]
df[features].head(3)



#Clean and preprocess the data
for feature in features:
    df[feature] = df[feature].fillna('') 
    
    
def combine_features(row):
    return row['titile'] 


df["combined_features"] = df.apply(combine_features,axis=1)

df.head(3)

count_matrix = CountVectorizer().fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(count_matrix)

cosine_sim.shape


#Helper function to get the title from the index
def get_titile_from_index(index):
  return df[df.index == index]["titile"].values[0]
#Helper function to get the index from the title
def get_index_from_titile(titile):
  return df[df.titile == titile]["index"].values[0]





product_user_search =input("Search - : ")


product_index = get_index_from_titile(product_user_search)



similar_product =  list(enumerate(cosine_sim[product_index]))


sorted_similar_product = sorted(similar_product,key=lambda x:x[1],reverse=True)[:]


#i=0
#print("Top 5 similar product to "+product_user_search+" are:")
#for element in sorted_similar_product:
#    print(get_titile_from_index(element[0]))
#    i=i+1
#    if i>=5:
#        break

i=0
print("\n\nTop 5 similar products are  showing below ---\n")

for i in range( len(sorted_similar_product)):
    print('Product Title : ',get_titile_from_index(sorted_similar_product[i][0]))
    print('Product price : ',df['price'][i],' Taka ')
    print('Website Link  : ',df['link'][i])
    print('Similarity Score: ',sorted_similar_product[i][1] )
    print("\n")
    i=i+1
    if i>=5:
        
        break