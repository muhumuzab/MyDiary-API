from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from datetime import datetime


from application.models.models import DiaryEntry

api = Namespace('Diary Entry', Description='Operations on Diary Entry')

entries = {}


class Entries(Resource):

    def post(self):
        """Create an entry."""
        data = request.get_json()

        # Check whether entry has empty title and body

        if data['title'] == "" and data['body'] == "":
            return {'message': 'cannot post empty diary entry'}, 400

        # Check whether entry has empty title
        if data['title'] == "":
            return {'message': 'please input title'}, 400

        # Check whether entry has empty body
        if data['body'] == "":
            return {'message': 'please input body'}, 400

        # Check whether entry has both title and body
        if data['title'] and data['body']:

            # Check for duplicate titles
            if not any(True for entry in entries.values()
                       if entry["title"] == data["title"]):
                diary_entry = DiaryEntry(data)
                entry_id = len(entries) + 1
                entries[(entry_id)] = diary_entry.getDict()

                return {'message': 'diary entry added successfully.'}, 200
            else:
                return {'message': 'entry with that title already exists,\
                            please choose another title.', 'status_code': 400}

        else:
            return {'message': 'something is wrong with the server.'}, 500

    def get(self):
        """Fetch all diary entries."""
        return {'entries': entries}, 200


api.add_resource(Entries, '/entries')


class SingleEntry(Resource):

    def get(self, entry_id):
        """Fetch a single diary entry."""
        try:
            entry = entries[int(entry_id)]
            entry['id'] = int(entry_id)
            return {'entry': entry }, 200
        except Exception as e:
            return {'message':
                    'diary entry with given id does not exist'}, 404

    def put(self, entry_id):
        """ Edit an entry """

        data = request.get_json()

        # Check whether title and body are empty
        if data['title'] == "" and data['body'] == "":
            return {'message': 'cannot post empty diary entry'}, 400

        # Check whether entry has empty title
        if data['title'] == "":
            return {'message': 'please input title'}, 400

        # Check whether entry has empty body
        if data['body'] == "":
            return {'message': 'please input body'}, 400

        # Check whether entry has both title and body
        if data['title'] and data['body']:

            try:

                # Check for duplicate titles
                if not any(True for entry in entries.values()
                           if entry["title"] == data["title"]):

                    entries[int(entry_id)]['title'] = data['title']
                    entries[int(entry_id)]['body'] = data['body']
                    return {'message':
                            'diary entry updated successfully'}, 201
                else:
                    return {'message':
                            'entry with such title already exists'}, 404

            except Exception as e:
                return {'message':
                        'Something wrong with the server'}, 500


api.add_resource(SingleEntry, '/entries/<int:entry_id>')
