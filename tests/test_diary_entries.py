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
        self.entry_without_title = {
            "title": "",
            "body": "Probably the best movie ever"

        }

        self.entry_without_body = {
            "title": "Titanic",
            "body": ""
        }



    def tearDown(self):
        """Release flask app instance"""
        self.app = None
        self.entry = None
        

    def test_create_entry(self):
        """test user can create a diary entry"""
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'diary entry added successfully.')

    def test_get_all_entries(self):
        """test user can get all diary entries"""
        response = self.app.get('/api/v1/entries',
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_cannot_create_entry_without_details(self):

        entry = {}
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         "make sure you provide all required fields.")
        
    def test_get_entry_that_does_not_exist(self):
        """Assumes no entry with a negative id number"""
        id = 23
        response = self.app.get('/api/v1/entries/{}'.format(id),
                                content_type='application/json')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'], 'entry does not exist')

    '''

    def test_cannot_create_entry_without_details(self):

        entry = {}
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 500)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'Entry not updated,make sure you provide all details')
    

    def test_cannot_create_entry_without_title(self):

        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry_without_title),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'diary entry missing title.')


   

    def test_cannot_create_entry_without_body(self):

        
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry_without_body),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 500)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                        'diary entry missing body.')

    
     def test_edit_entry(self):

        #"""Test API can edit an existing bucketlist. (PUT request)"""
        response = self.app.post('/api/v1/entries/',
                                data=json.dumps(self.entry),
                                content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.put('/api/v1/entries/1',
                                data=json.dumps(self.entry2),
                                content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'Entry not updated,make sure you provide all details')


    def test_edit_entry(self):

        Test API can edit an existing bucketlist. (PUT request)
        response = self.app.post(
            '/api/v1/entries/',
            data=json.dumps(self.entry),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.put(
            '/api/v1/entries/1',
            data=json.dumps(self.entry2),
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         'Diary entry updated successfully.')
    
    


    def test_cannot_create_entry_without_details(self):

        entry = {}
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(entry),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         "make sure you provide all required fields.")

    def test_cannot_create_entry_without_title(self):


        entry = {"title": " ","body": "Harry Porter"}
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry_without_title),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         "Diary entry missing title field.")

    def test_cannot_create_entry_without_body(self):

        entry = {"title": "Harry Porter","body": ""}
        response = self.app.post('/api/v1/entries',
                                 data=json.dumps(self.entry_without_body),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'],
                         "Diary entry missing body field.")



    def test_get_all_entries(self):
        
        response = self.app.get('/api/v1/entries',
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

   

    def test_get_entry_that_does_not_exist(self):
       
        id = -1
        response = self.app.get('/api/v1/entries/{}'.format(id),
                                content_type='application/json')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response_data['message'], 'Diary entry does not exist')
    '''
    



if __name__ == '__main__':
    unittest.main()