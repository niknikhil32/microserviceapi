'''
Service Two Convert The Given Timezone in IST

'''

from flask import Flask,request,jsonify
from datetime import datetime
import pytz
ist = pytz.timezone("Asia/Kolkata")


#Init App
app=Flask(__name__)

@app.route('/',methods=['GET'])
def getStatus():
    return jsonify({'message':'Service One Running'})

@app.route('/convert/<timestamp>',methods=['GET'])
def getTimestampIst(timestamp):
    #date = datetime.fromtimestamp(int(timestamp), ist).replace(tzinfo=None)
  
    try:
       date = datetime.fromtimestamp(int(timestamp), ist).replace(tzinfo=None)
       return jsonify({'date':str(date),'timezone':"IST"})    
    except:
      print("An exception occurred")
      return jsonify({'error':'Please Insert Correct timezone'})    
     

   
    

#Run server

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
