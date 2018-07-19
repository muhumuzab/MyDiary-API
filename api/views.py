from flask import jsonify,request,json,render_template
from classes.auth import Authentication
from classes.diary import Diary
from classes.item import DiaryItem
from api import create_app