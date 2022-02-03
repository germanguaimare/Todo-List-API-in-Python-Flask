from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def taskfunction():
    return (jsonify(todos))

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    print("Este es el request_body: ", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)





# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)