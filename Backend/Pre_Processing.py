import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class Preprocessing_Data:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df= None 
        self.x = None
        self.y = None 

        self.x_train = None 
        self.x_test = None 
        self.y_train = None 
        self.y_test = None 

        self.x_train_std = None
        self.x_test_std = None

        self.new_data = None
        
        self.x_train_std_re = None 
        self.x_test_std_re = None 

        scaler = None

    def read_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df
    
    def feature_selection(self):
        if self.df is not None:
            self.x = self.df.iloc[:,:-1].values
            self.y = self.df.iloc[:,-1].values
            print(self.y.shape)

            return self.x , self.y
        
    
        else: 
            print("Data Frame is Empty")
    
    def shape_x(self):
        print(self.x.shape)

    def shape_y(self):
        print(self.y.shape)

    def split_data(self):

        print("Shape of x before split:", self.x.shape)
        print("Shape of y before split:", self.y.shape)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=1) 

    
        print("Train set" , self.x_train.shape, self.y_train.shape)
        
        print("NaNs in X_train:", np.isnan(self.x_train).sum())
        print("NaNs in y_train:", np.isnan(self.y_train).sum()) 
        return self.x_train, self.x_test, self.y_train, self.y_test
    
    def standardize_data(self):
        self.scaler = StandardScaler()

        self.x_train_std = self.scaler.fit_transform(self.x_train)

        
        self.x_test_std = self.scaler.transform(self.x_test)
       
        
        
       
        return self.x_train_std, self.x_test_std
      


    def standardize_instance(self, instance):

        new_instance = self.scaler.transform(instance)


        return new_instance



        