from datetime import datetime
import unittest
from app import app
from models import db, Message

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Setup method to delete existing messages and create a new one.'''
        with app.app_context():
            m = Message.query.filter(
                Message.body == "Hello 👋"
            ).filter(Message.username == "Liza")

    def setUp(self):
        '''Set up method to initialize the Flask-Testing client.'''
        self.app = app.test_client()

    def tearDown(self):
        '''Tear down method to clean up resources.'''
        # You can consider rolling back the database session here

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

    # Other test methods...

if __name__ == '__main__':
    unittest.main()
