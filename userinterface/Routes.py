from flask import Flask
import userinterface.PersonController as personController
import userinterface.SystemController as systemController

app = Flask(__name__)

get = ['GET']
post = ['POST']
put = ['PUT']
delete = ['DELETE']

app.add_url_rule('/healthCheck', '', systemController.healthCheck, methods=get)
app.add_url_rule('/', '', personController.hello_world, methods=get)
app.add_url_rule('/sandboxpython/setup', '', systemController.setupData, methods=get)
app.add_url_rule('/sandboxpython/person/<id>', '', personController.getPersonById, methods=get)
app.add_url_rule('/sandboxpython/person', '', personController.getPersonByCriteria, methods=get)
app.add_url_rule('/sandboxpython/person', '', personController.updatePerson, methods=put)
app.add_url_rule('/sandboxpython/person', '', personController.insertPerson, methods=post)
app.add_url_rule('/sandboxpython/person/<id>', '', personController.deletePerson, methods=delete)
