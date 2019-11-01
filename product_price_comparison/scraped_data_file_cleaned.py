import pandas as pd

dataFrame=pd.read_csv('scraped_data_file.csv')

print(dataFrame)

df = dataFrame.drop_duplicates('link')

df.to_csv(r'C:\Users\Tushar\Desktop\CSE499-Group01-best-price.com\product_price_comparison\cleaned_scraped_data_file.csv', index=False)



