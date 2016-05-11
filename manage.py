from flask_script import Manager,commands
from todoapp import app
from models import db

manager = Manager(app)

@manager.command
def init_db():
	print("1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    with app.test_request_context():
        from models import db
        db.engine.echo = True
        db.metadata.bind = db.engine
        db.metadata.create_all(checkfirst=True)

        #db.create_all(checkfirst=True)

if __name__ == "__main__":
	print("2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    manager.run()
