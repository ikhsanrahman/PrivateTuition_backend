from flask_restplus import Api
from flask import Blueprint

from app.api.student.controller import api as student
from app.api.tutor.controller import home as home, api as tutor
from ..summary.controller import api as summary
from ..tutor.subject.controller import api as subject

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='KRISFI API ',
          version='1.0',
          # description='a engine to score object'
          )

 
api.add_namespace(home, path='/')
api.add_namespace(tutor, path='/tutor')
api.add_namespace(student, path='/student')
api.add_namespace(summary, path='/summary')
api.add_namespace(subject, path='/subject')
# api.add_namespace(admin, path='/admin')