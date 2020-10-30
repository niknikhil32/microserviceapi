'''
Service Two Convert The Given Timezone in IST

'''

from flask import Flask,request,jsonify
from datetime import datetime
import pytz
ist = pytz.timezone("US/Mountain")


#Init App
app=Flask(__name__)

@app.route('/',methods=['GET'])
def getStatus():
    return jsonify({'message':'US MountainTime Zone And String Time Zone Service Running'})

@app.route('/convert/<timestamp>',methods=['GET'])
def getTimestampIst(timestamp):
    #date = datetime.fromtimestamp(int(timestamp), ist).replace(tzinfo=None)
     try:
       date = datetime.fromtimestamp(int(timestamp), ist).replace(tzinfo=None)
       return jsonify({'date':str(date),'timezone':"US Mountain Time"})    

     except:
      print("An exception occurred")
      return jsonify({'error':'Please Insert Correct timezone'})    
    


    
@app.route('/string/<timestamp>',methods=['GET'])
def getTimestampString(timestamp):
    #date = datetime.fromtimestamp(int(timestamp), ist).replace(tzinfo=None)
    try:
        date = datetime.fromtimestamp(int(timestamp))
        return jsonify({'date':date,'timezone':"String"})    

    except:
      print("An exception occurred")
      return jsonify({'error':'Please Insert Correct timezone'})    
   


    
#Run server

if __name__=='__main__':
    app.run(host='0.0.0.0', port=7000,debug=True)
