from flask import Flask, render_template

#Todo backend server
#get all lists
#update a list
#get a single list

#data 
list = {
    1 : "Fruits",
    "2" : "Vegetables",
    "3" : "Rice",
    "4" : "Gari"
}


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items')
def get_items():
    return list

@app.route("/items/{id}")
def get_item(id: str):
    print(id)
    

@app.route('/items/first')
def get_first():
    return list["1"]

@app.route('/items/last')
def get_last():
    return list["4"]


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')