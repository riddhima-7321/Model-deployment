import requests
url='http://localhost:5000/predict_api'
r=requests.post(url,json={'RI':1,'Na':12,'Mg':3,'Al':2,'Si':72,'K':1,'Ca':8,'Ba':0,'Fe':1 })