




#Import Libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity




# read dataset
#df=pd.read_csv('Book1.csv',encoding='utf-8')
df= pd.read_csv('Book1.csv',encoding ='latin1')

#df['titile'][201]


#Create a list of important columns 
#features = ['titile']

#Clean and preprocess the data
#for feature in features:
    
#    df[feature] = df[feature].fillna('') 

# Create a function to combine the values of the important columns into a single string
#def combine_features(row):
#    return row['titile']

# Apply the function to each row in the data set to store the combined strings into a new column called ‘combined_features’

#df["combined_features"] = df.apply(combine_features,axis=1)

# Convert the text from the combined_features column to a matrix/vector of word counts, and store it into a variable called count_matrix

count_matrix = CountVectorizer().fit_transform(df["titile"])

# Get the cosine similarity matrix from the count matrix. This will give us a similarity score for each text (row of data) to every other text in the data set (the columns)
cosine_sim = cosine_similarity(count_matrix)

# The similarity score for row at position 0 to the column at position 0 should always be 1 since they are the same text. The row at position 0 similarity value may be different for the column at position 5, depending on how similar the text  in row 5 and row 0 are.
cosine_sim.shape

# Create two helper functions, one to get the title of a product from the index and the other to get the index from the title of a product

#Helper function to get the title from the index
def get_titile_from_index(index):
  
    
    
    return df[df.index ==index]["titile"].values[0]


#Helper function to get the index from the title
def get_index_from_titile(titile):
    
   return df[df.titile == titile]["index"].values[0]

# Get the title of the product that the user likes and store it into a variable

product_user_search =input('Enter your product name = ')


    
# Find that product title’s index and store it into a variable 

product_index =get_index_from_titile(product_user_search)
    
    

# Then we will enumerate through all the similarity scores of that product to make a tuple of product index and similarity score

similar_products =  list(enumerate(cosine_sim[product_index]))

# Sort the list of similar product according to the similarity scores in descending order

sorted_similar_products = sorted(similar_products,key=lambda x:x[1],reverse=True)[:]

# Create a loop to print the first 12 entries from the sorted similar product list
i=0
print("Top 5 similar product to "+product_user_search +" are:\n\n")
for element in sorted_similar_products:
    print(get_titile_from_index(element[0]))
    i=i+1
    if i>=5:
        break



