from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print('user POSTed checkout')
    d = datetime.datetime.today()
    data = {
        'strawberry': request.form["strawberry"],
        'raspberry': request.form["raspberry"],
        'apple': request.form["apple"],
        'blackberry': request.form["blackberry"],
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'student_id': request.form["student_id"],
        'num_items': int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"]) + int(request.form["blackberry"]),
        'date_submitted': d.strftime("%B %d %Y %H:%M:%S")
    }
    print(data)
    return render_template("checkout.html", order_info=data)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)