from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://patrycja:mypassword@localhost/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from views import *

#from models import db
#db.create_all()


if __name__ == '__main__':
	import os

	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)