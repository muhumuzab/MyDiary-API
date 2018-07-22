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



class Entries(Resource):
    

    @api.doc(responses={'message': 'diary entry added successfully.',
                        201: 'Created', 400: 'BAD FORMAT'})
    @api.expect(entry)
    def post(self):
        """Create an entry."""
        data = request.get_json()
        # Check whether there is data

        if any(data):
            # save entry to data structure
            
            
            # set id for the entry offer
            diary_entry = DiaryEntry(data)
            entry_id = len(entries) + 1
            entries[(entry_id)] = diary_entry.getDict()
            response = {'message': 'diary entry added successfully.',
                            'entry id': entry_id}
            return (response), 201
        else:
            return {'message': 'make sure you provide all required fields.'}, 400



    

api.add_resource(Entries, '/entries')