from flask import Flask, request, jsonify
from task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_manager.get_tasks())

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_manager.get_task(task_id)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/task', methods=['POST'])
def add_task():
    data = request.json
    if not data.get("title") or not data.get("description"):
        return jsonify({"error": "Missing title or description"}), 400
    task = task_manager.add_task(data["title"], data["description"])
    return jsonify(task), 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = task_manager.update_task(task_id, data.get("title"), data.get("description"))
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_manager.delete_task(task_id):
        return jsonify({"message": "Task deleted successfully"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
