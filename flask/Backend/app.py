from flask import Flask,request

app = Flask(__name__)

@app.route("/home",methods=["GET"])
def home():
    return "hello from home"

@app.route("/")
def slash():
    return "this is the home path"

# @app.route("/login",methods=["POST"])
# def login():
#     print("please provide your credentials")
#     username=request.form["name"]
#     password=request.form["password"]
#     print (f"{username},{password}")

#     return f"hello {username} your {password} has been recieved successfully"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    name = data["name"]
    password = data["password"]

    return f"hello {name}, your password is {password}"


if __name__ == "__main__":
    app.run(debug=True)