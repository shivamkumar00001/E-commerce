import json
from flask import Flask

class database:
  
  def insert(self, email,name,password):

    with open('DB.json', 'r') as f:
      
      data = json.load(f)
      
      if email in data:
        return 0
      
      else:
        data[email] = [name,password]

    with open ('DB.json' , 'w') as f:
      json.dump(data, f,indent=4)
      return 1    
  
  def search(self, email, password):
     with open ('DB.json','r') as f:
        data = json.load(f)
        if email in data:
           if data[email][1] != password:
            return 0
           elif data[email][1] == password:
            return 1
        else :
          return 2   

