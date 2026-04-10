from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

filename = "todo.json"

def create_file():
    file_exists = os.path.exists(filename)
    if not file_exists:
        with open(filename, "w") as f:
            json.dump([],f)
    else:
        print("file already exists")

def read_file():
    with open (filename, "r") as f:
        list = json.load(f)
    return list

def save_file(list):
    with open(filename, "w") as f:
        json.dump(list,f)


# function to read the to-do list
@app.route("/todo", methods=["GET"])
def get_entries():
    udpated_list = read_file()
    return jsonify(udpated_list)

@app.route("/todo",methods=["POST"])
def add_data():
    entry = request.get_json()
    updated_list = read_file()
    new_task = entry["task"]
    if any(item["task"] == new_task for item in updated_list):
        return f"Error: can not add {new_task}, it already exists"
    todo_entry = {
        "id": len(updated_list)+1,
        "task": entry["task"]
    }
    updated_list.append(todo_entry)
    save_file(updated_list)
    return f"your final list is saved successfully"

@app.route("/todo/<int:todo_id>",methods=["DELETE"])
def delete_todo(todo_id):
    todos = read_file()
    for todo in todos:
        if todo_id == todo["id"]:
            todos.remove(todo)
            save_file(todos)
            return f"todo is deleted successfully"
    return f"Error: todo not found"



# ---- create a file if it is not created already -----

create_file()
if __name__ == "__main__":
    app.run(debug=True)
