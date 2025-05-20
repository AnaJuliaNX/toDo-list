from flask import Blueprint, render_template, request, redirect, url_for
from app.models.task import Task, tasks

# Blueprint
task_bp =  Blueprint('task_bp', __name__)

# construindo a minha rota 
@task_bp.route('/')
def index(): 
    return render_template('index.html', tasks=tasks)

@task_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        new_task = Task(id=len(tasks)+1, title=title)
        tasks.append(new_task)
        return redirect(url_for('task_bp.index'))
    return render_template('create.html')

@task_bp.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return redirect(url_for('task_bp.index'))

