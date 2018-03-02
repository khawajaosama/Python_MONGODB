from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_DBNAME']='saylani'
app.config['MONGO_URI']='mongodb://pretty:printed@ds151908.mlab.com:51908/saylani'
mongo=PyMongo(app)

@app.route('/')
def index_1():
    return render_template('index_1.html')

@app.route('/about',methods=['GET','POST'])
def index_2():
    return 'Hi'+request.args.get('USER_NAME')+', You are using '+request.method+\
    "and your email is"+request.args.get('PASSWORD')

@app.route('/add')
def index_3():
    mongo.db.mycustomers.insert({"name":"khawaja osama",\
    "age":"16","gender":"male"})
    return 'Added Succesfully'

@app.route('/show')
def index_4():
    store=[]
    records=mongo.db.mycustomers.find({"name":"khawaja osama"})
    for user in records:
        store.append({"name":user["name"], \
        "age":user["age"],"gender":user["gender"]})

    return jsonify({"Details":store})
    
if __name__=='__main__':
    app.run(debug=True)