import datetime


class DiaryEntry(object):


    def __init__(self, data):
        
        self.title = data['title']
        self.body = data['body']
        
      
    def getDict(self):
        return self.__dict__











