#import necessary libraries
import pandas as pd

#loading required dataset
file_path = 'C:\\Users\\ELCOT\\Downloads\\movies.csv.csv'

df = pd.read_csv(file_path)

#exploring the dataset
print(df.info())
print(df.describe())
print(df.head(5))
