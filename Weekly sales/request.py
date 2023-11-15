import requests
url='http://localhost:5000/predict_api'
r=requests.post(url,json={'Holiday flag':1,'Month':12,'Year':2010,'Week':2,'temperature category':3})





