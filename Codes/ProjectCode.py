# Program In Python On Getting The Data
import pandas as pd         
import os
import time
from datetime import datetime
import csv
import glob
import numpy as np 
import matplotlib.pyplot as plt 

path="C:/Users/Chinmay/Desktop/ProjectMLsem6/Data"  # Path for the directory

def Get_Data(name='All_Customers_Data',addr='C:/Users/Chinmay/Desktop/ProjectMLsem6/Data/ProjectData'):     # Function to get the data
    statspath=path
    Clist=[x[0] for x in os.walk(statspath)]
    totaldataf=pd.DataFrame(columns=['CustomerID','Gender','Age','Income(Annual)','Spending_Score'],index=None)

    
    for each_dir in Clist[1:]:
        each_file=os.listdir(each_dir)      # List of files in directory
        print('Files In Directory Are : ',each_file)
        if len(each_file)>0:
            for file in each_file:
                full_file_path=each_dir+'/'+file
                x=pd.read_csv(full_file_path)
                try:
                    totaldataf=totaldataf.append(x,sort=False)  # Copy the data in one data frame
                except Exception as e:
                    print(e)
                    pass

    save=addr+'/'+name+('.csv') # Save the data frame as a .csv file 
    print('Location Of File : ',save)
    totaldataf.to_csv(save,index=False)
    cols=list(totaldataf)
    for x in cols : 
        if x=='Unnamed: 0' :    # Removing unnecessary column
            totaldataf=totaldataf.drop('Unnamed: 0',1)
            print('Unnecessary Columns Removed.')
    print('List Of Columns In Dataframe : ',list(totaldataf))   # List of columns in the dataframe
    print('Dimensions Of The Frame : ',totaldataf.shape)


def Clean_Data(name='All_Customers_Data',addr='C:/Users/Chinmay/Desktop/ProjectMLsem6/Data/ProjectData'):   # Cleaning Process Of The Data
    loc=addr+'/'+'Temp'+('.csv')
    print('\nFile Location : '+loc)     # Location of file
    try:
        data=pd.read_csv(loc)   # Read the data in the dataframe
    except Exception as e:
        print(e)
        pass     
    print('DataFrame : \n',data,'\n') # Print the data of the dataframe


    check=data.isnull().sum()   # Check for null values
    print('Checking The Data : \n',check)
    
    cols=list(data)     # List of columns in the dataframe
    for x in cols : 
        if x=='Unnamed: 0' :    # Removing unnecessary column
            data=data.drop('Unnamed: 0',1)
            print('Unnecessary Columns Removed.')
    print(list(data))

    data=data.dropna(subset=['CustomerID','Gender'],how='all')  # Delete the row if both the columns have null value
    data=data.dropna(subset=['Gender'])     # Delete the row if Gender is not known


    avg_score=data['Spending_Score'].mean()     # Finding average values
    avg_income=data['Income(Annual)'].mean()
    print('\nAverage Value Of Spending_Score : '+str(avg_score))
    print('\nAverage Value Of Income : '+str(avg_income))
    
    
    data['Spending_Score'].fillna(value=avg_score,inplace=True)     # Fill avg value in blank columns in the dataframe column
    check=data.isnull().sum()
    print(check)


    null_values=data.isnull().sum()     # Again check for null elements
    print('Checking The Data Again : \n',null_values)
    print('DataFrame (After Data Cleaning) : \n',data)

    save=addr+'/'+('Cleaned')+('.csv') # Save the data frame as a .csv file 
    print('Location Of File : ',save)
    data.to_csv(save,index=False)    

def Analyse_Data(name='Temp',addr='C:/Users/Chinmay/Desktop/ProjectMLsem6/Data/ProjectData'):

    loc=addr+'/'+name+('.csv')
    try:
        data=pd.read_csv(loc)
    except Exception as e:
        print(e)
        pass  

    print(data['Spending_Score'].describe())


def Plot_Diagram():

    x=np.arange(0,3*np.pi,0.1) 
    y=np.sin(x) 
    plt.title("sine wave form") 

    # Plot the points using matplotlib 
    plt.plot(x,y) 
    plt.show() 

def Main():
    # Get_Data()
    Clean_Data()
    # Plot_Diagram()
    # Analyse_Data()

if __name__ == '__main__':
    Main()