import datetime


class DiaryEntry(object):


    def __init__(self, data):
        
        self.title = data['title']
        self.body = data['body']
        #self.date_created = datetime.datetime.utcnow()
        #self.date_created = datetime.strftime((datetime.strptime(data['start time'],
                                            #'%B %d %Y %I:%M%p')),'%B %d %Y %I:%M%p')
        #self.date_modified = None
      
    def getDict(self):
        return self.__dict__












    '''

    def create_diary(self):
        """
        Adds diary object to list
        :return: 
        """
        DiaryEntry.diary.append(self)
        return self.diary_id


    @staticmethod
    def check_for_diaries():
        """ This checks whether there are any diary entries"""
        if len(DiaryEntry.diary) >=1:
            return (len(DiaryEntry.diary))

    @classmethod
    def retrieve_all_entries(cls):
        all_diaries = []
        for this_diary in DiaryEntry.diary:
            all_diaries.append({
                'id': this_diary.diary_id,
                'title': this_diary.title,
                'body': this_diary.body,
                'Date created': this_diary.date_created,
                'Date Modified': this_diary.date_modified


            })
        return all_diaries

    @staticmethod
    def check_diary_by_id(search_id):
        for this_diary in DiaryEntry.diary:
            if this_diary.diary_id == search_id:
                print(this_diary.diary_id)
                return this_diary.diary_id

    @staticmethod
    def check_title(title):
        for this_diary in DiaryEntry.diary:
            if this_diary.title == title:
                return this_diary.title

    @staticmethod
    def retrieve_entry_by_id(search_id):
        response = []
        for this_diary in DiaryEntry.diary:
            if this_diary.diary_id == search_id:
                response.append({
                    'id': this_diary.diary_id,
                    'title': this_diary.title,
                    'body': this_diary.body,
                    'Date created': this_diary.date_created,
                    'Date Modified': this_diary.date_modified
                })
                return response

    @staticmethod
    def edit_entry(diary_id, title,body):
        for this_diary in DiaryEntry.diary:
            if this_diary.diary_id == diary_id:
                #if this_diary.title == title:
                    #if this_diary.body == body:

                        #return None
                this_diary.title = title
                this_diary.body = body
                this_diary.date_modified = datetime.datetime.utcnow()
                return this_diary.diary_id
    '''