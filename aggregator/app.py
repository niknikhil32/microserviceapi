from flask import Flask,request,jsonify,redirect, Response
import requests
app = Flask(__name__)

@app.route('/',methods=['GET'])
def status():
    return jsonify({'message':'Api Gateway Running'})

@app.route('/<timestamp>/ist',methods=['GET'])
def redirist(timestamp):
    url = 'http://servicetwo.sock-shop.svc.cluster.local:5000/convert/'+timestamp
    r = requests.get(url)
    return Response(r.content)

@app.route('/<timestamp>/us',methods=['GET'])
def redirutc(timestamp):
    url = 'http://servicethree.sock-shop.svc.cluster.local:7000/convert/'+timestamp
    r = requests.get(url)
    return Response(r.content)    
    
 
@app.route('/<timestamp>/string',methods=['GET'])
def redirectString(timestamp):
    url = 'http://servicethree.sock-shop.svc.cluster.local:7000/string/'+timestamp
    r = requests.get(url)
    return Response(r.content)      


#Run server

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000,debug=True)