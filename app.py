#Flask app routing

from flask import Flask, render_template, request, redirect, url_for, jsonify

#Create a simple flask application
app= Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "index"

@app.route("/success/<int:score> ",methods=["GET"])
def success(score):               #Score parameter hai( variable rule----------<int:score>)
    return "The person is pass : " + str(score)

@app.route("/fail/<int:score> ",methods=["GET"])
def fail(score):               #Score parameter hai( variable rule----------<int:score>)
    return "The person is Fail : " + str(score)

@app.route('/form', methods=["GET","POST"])
def form():
    if request.method== "GET":
        return render_template("form.html")
    else :
        maths = float(request.form['maths'])
        sci = float(request.form['sci'])
        social =float( request.form['social'])
         
        avg=(maths+sci+social)/3
        res=""
        if avg>=50:
            res="success"
        else:
            res="fail"
        
        return redirect(url_for(res,score=avg))
        # return render_template("form.html", score=avg)

@app.route("/api", methods=['POST'])
def cal():
    data=request.get_json()
    a_val=float(dict(data)["a"])
    b_val=float(dict(data)["b"])
    return jsonify(a_val+b_val)



if __name__=="__main__":
    app.run(debug =True)