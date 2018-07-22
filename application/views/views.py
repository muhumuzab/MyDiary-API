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

    @api.doc('list of entries', responses={200: 'OK'})
    def get(self):
        """Fetch all diary entries."""
        return (entries), 200

api.add_resource(Entries, '/entries')

class SingleEntry(Resource):

    @api.doc('Fetch a single entry',
             params={'entry_id': 'Id for a single entry'},
             responses={200: 'OK', 404: 'NOT FOUND'})
    def get(self, entry_id):
        """Fetch a single diary entry."""
        try:
            entry = entries[int(entry_id)]
            entry['id'] = int(entry_id)
            return  jsonify(entry, {'message': 'diary entry retrieved successfully'}, 200)
        except Exception as e:
            return {'message': 'entry does not exist'}, 404

api.add_resource(SingleEntry, '/entries/<int:entry_id>')