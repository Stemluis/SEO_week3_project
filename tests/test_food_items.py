import unittest, sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append('../flask-example-3')
from main import app, db

class UsersTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    ###############
    #### tests ####
    ###############

    def register(self, purchase_date, expiration_date, item_name, item_category):
        return self.app.post('/add',
                            data=dict(purchase_date=purchase_date,
                                      expiration_date=expiration_date,
                                      item_name=item_name, 
                                      item_category=item_category),
                            follow_redirects=True)

    def test_valid_item_registration(self):
        response = self.register('2022-07-15', '2022-07-22', 'TestItem', 'Grocery')
        self.assertEqual(response.status_code, 200)
    
    # def test_invalid_date_registration(self):
    #     response = self.register('t', 'test@example.com', 'FlaskIsAwesome')
    #     self.assertIn(b'Field must be between 2 and 20 characters long.', response.data)

    # def test_invalid_email_registration(self):
    #     response = self.register('test2', 'test@example', 'FlaskIsAwesome')
    #     self.assertIn(b'Invalid email address.', response.data)


if __name__ == "__main__":
    unittest.main()