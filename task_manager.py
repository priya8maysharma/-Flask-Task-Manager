from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1
    
    def add_task(self, title, description):
        task = Task(self.counter, title, description)
        self.tasks.append(task)
        self.counter += 1
        return task.to_dict()
    
    def get_tasks(self):
        return [task.to_dict() for task in self.tasks]
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task.to_dict()
        return None
    
    def update_task(self, task_id, title, description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                return task.to_dict()
        return None
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False
