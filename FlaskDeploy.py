from flask import Flask,jsonify,request,make_response
import json
import os
import pickle

def someFun(cname,op,hi,lo):
    if cname=="Google":
        hh="GoLR.pkl"
    elif cname=="Apple":
        hh="ApLR.pkl"
    elif cname=="Facebook":
        hh="FbLR.pkl"
    elif cname=="Amazon":
        hh="AmLR.pkl"
    print("ststs")
    clf = pickle.load(open(hh,"rb"))
    print("clfclf")
    y_pred=clf.predict([[float(op),float(hi),float(lo)]])
    print(y_pred)
    return(float(y_pred))


app = Flask(__name__)
@app.route('/psp', methods=['POST'])
def getReviewDetails():
    try:
        cnamex = request.json['cname']
        opx=request.json['op']
        hix=request.json['hi']
        lox=request.json['lo']
        cl=0
        print(cnamex)
    except:
        return make_response(jsonify({'error' :'bad request'}),400)
    try:
        print(cl)
        cl=someFun(cnamex,opx,hix,lox)
    except:
        print("FGGG")
        return make_response(jsonify({'error' :'internal server error'}),500)
        
    return make_response(jsonify({"closingPrice": cl}),200)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5004,debug=True)
