from  flask import Flask #import visivel global

def create_app():
    app = Flask(__name__)

    #import controller
    from app.controllers.task_controller import task_bp #import visivel local
    app.register_blueprint(task_bp)

    return app