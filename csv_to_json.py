#!/usr/bin/env python
# coding: utf-8

# As discussed in the class use object oriented paradigm to build a CSV parser.
# 
# Pasted pseudo-code below.
# add necessary methods for performing CSV operations. I have also made a short note under each method for understanding
# 
# import json
# 
# class Csvread:
# path
# data = []
# def __init__(self,path):
# """
# Constructor
# """
# self.path = path
# self.readfile()
# 
# def save_to_json():
# json.dumps()
# 
# def addItem(self,data):
# """
# Should get dictionary from argument
# append to DAta
# """
# self.data.append(data)
# 
# def delete():
# """
# Should delete selected Item from data
# Allow the user to selected index to delete
# """
# 
# def serach(term):
# """
# Should be to search values of each row against the given param
# loop over the data. where each item is a dictionary. if any values of dictionary contians the quert `term`
# show as hit
# 
# 
# """
# 
# 
# def readfile(self):
# """
# """
# with open(path) as f:
# # self.data = f.read()
# for line in f:
# self.data.append(line)
# 
# #example for creating object and calling methods
# csvFile = Csvread("path_to_file")
# csvFile.addItem({})
# csvFile.save_to_json()

# In[1]:


import json
import csv
import logging as lg

lg.basicConfig(filename = "classparser.log", level = lg.ERROR)


class csvread:
    
    try:
        
        def __init__(self, csv_path, json_path, new_data, json_path_2):
            self.csv_path = csv_path
            self.json_path = json_path
            self.new_data = new_data
            self.json_path_2 = json_path_2


    except Exception as e:
        self.logging(e)
        
        
    
    try: 
        
        def save_to_json(self):
            with open(self.csv_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                data = {"names": []}
                for row in reader:
                    data["names"].append({"firstname": row[0], "lastname": row[1], "Building": row[2], "Town": row[3], "City": row[4], "Pin": row[5]})

                with open(json_path, "w") as f:
                    json.dump(data, f, indent=4)

            with open(json_path, "w+") as f:
                json.dump(data, f, indent=4)
   
    except Exception as e:
        self.logging(e)
            
    
    
    try:
        
        def add_item(self):
            with open(self.new_data, 'r') as fi:
                    reader = csv.reader(fi)
                    data1 = {"Name": []}
                    for row in reader:
                        data1["Name"].append({"Name": row[0], "Sex": row[1], "Age": row[2], "Height": row[3], "Weight": row[4]})

            with open(self.json_path_2, "w+") as fi:
                json.dump(data1, fi, indent=4)

            with open(self.json_path, 'a') as fi:
                json.dump(data1, fi, indent=4)
            
    except Exception as e:
        self.logging(e)
        
        
    def logging(self, log):
        lg.error(log)
            


csv_path = r'C:\Users\Lakshya\Downloads\addresses.csv'
json_path = 'addresses5.json'
new_data = r'C:\Users\Lakshya\Downloads\biostats.csv'
json_path_2 = "bio.json"
d = csvread(csv_path, json_path, new_data, json_path_2)
d.save_to_json()
d.add_item()

            


# In[ ]:




