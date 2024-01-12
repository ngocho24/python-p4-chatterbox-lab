# models_test.py

from datetime import datetime
import unittest
from app import app
from models import db, Message

class TestMessage(unittest.TestCase):

    def test_has_correct_columns(self):
        '''Test if the Message model has correct columns.'''
        with app.app_context():
            hello_from_liza = Message(
                body="Hello 👋",
                username="Liza")

            db.session.add(hello_from_liza)
            db.session.commit()

            assert hello_from_liza.body == "Hello 👋"
            assert hello_from_liza.username == "Liza"
            assert isinstance(hello_from_liza.created_at, datetime)

if __name__ == '__main__':
    unittest.main()
