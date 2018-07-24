import json
import unittest

from application import create_app


class DiaryEntryTests(unittest.TestCase):

    def setUp(self):
        """Prepare testing environment """

        self.app = create_app('testing')
        self.app = self.app.test_client()

        self.entry = {
            "title": "Harry Porter",
            "body": "Probably the best movie ever"

        }

        self.entry2 = {
            "title": "Titanic",
            "body": "Probably the best movie ever"

        }

    def tearDown(self):
        """Release flask app instance"""

        self.app = None
        self.entry = None

    def test_create_diary_entry(self):
        """test user can create a diary entry"""
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'diary entry added successfully.')

    def test_get_single_diary_entry(self):
        """ test user can retrieve a single diary entry """
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry),
                                 content_type='application/json')

        response = self.app.get('/api/v1/entries/1',
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_all_entries(self):
        """test user can get all diary entries"""
        response = self.app.get('/api/v1/entries',
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_diary_entry(self):
        """ test user can update a diary entry """
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry),
                                 content_type='application/json')

        response = self.app.put('/api/v1/entries/1',
                                data=json.dumps(self.entry2),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_cannot_create_entry_without_details(self):
        """ test user cannot create an empty diary entry """

        entry = {
            "title": "",
            "body": ""

        }
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(entry),
                                 content_type='application/json')
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'cannot post empty diary entry')

    def test_cannot_create_entry_without_title(self):
        """ test user cannot create an entry without title """

        entry_without_title = {
            "title": "",
            "body": "Probably the best movie ever"
        }

        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(entry_without_title),
                                 content_type='application/json')
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'please input title')

    def test_cannot_create_entry_without_body(self):
        """ test user cannot create an entry without title """

        entry_without_body = {
            "title": "Harry Porter",
            "body": ""
        }

        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(entry_without_body),
                                 content_type='application/json')
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'please input body')

    def test_get_entry_that_does_not_exist(self):
        """ test user cannot get a diary entry that does not exist """

        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry),
                                 content_type='application/json')

        response = self.app.get('/api/v1/entries/23',
                                content_type='application/json')
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'entry does not exist')


if __name__ == '__main__':
    unittest.main()
