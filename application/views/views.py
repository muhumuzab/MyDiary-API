from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from datetime import datetime


from application.models.models import DiaryEntry

api = Namespace('Diary Entry', Description='Operations on Diary Entry')

# data structure to store ride offers
entries = {}

entry = api.model('Diary Entry', {
    'title': fields.String(description='title of the diary entry'),
    'body': fields.String(description='body of the diary entry'),
})




