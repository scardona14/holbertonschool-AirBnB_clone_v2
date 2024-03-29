import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User

class TestDBStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        """Tear down test environment"""
        self.db.close()

    def test_all(self):
        """Test the all() method"""
        # Create some objects
        user1 = User()
        user2 = User()
        user3 = User()
        # Add objects to the database
        self.db.new(user1)
        self.db.new(user2)
        self.db.new(user3)
        self.db.save()
        # Retrieve all objects from the database
        all_objects = self.db.all()
        # Check if all objects are retrieved
        self.assertEqual(len(all_objects), 3)
        # Check if the retrieved objects are of the correct type
        self.assertIsInstance(all_objects[user1.__class__.__name__ + '.' + user1.id], User)
        self.assertIsInstance(all_objects[user2.__class__.__name__ + '.' + user2.id], User)
        self.assertIsInstance(all_objects[user3.__class__.__name__ + '.' + user3.id], User)

    def test_new(self):
        """Test the new() method"""
        # Create a new object
        user = User()
        # Add the object to the database
        self.db.new(user)
        self.db.save()
        # Retrieve the object from the database
        retrieved_user = self.db.all()[user.__class__.__name__ + '.' + user.id]
        # Check if the retrieved object is the same as the original object
        self.assertEqual(user, retrieved_user)

    def test_delete(self):
        """Test the delete() method"""
        # Create an object
        user = User()
        # Add the object to the database
        self.db.new(user)
        self.db.save()
        # Delete the object from the database
        self.db.delete(user)
        self.db.save()
        # Check if the object is no longer in the database
        self.assertNotIn(user.__class__.__name__ + '.' + user.id, self.db.all())

if __name__ == '__main__':
    unittest.main()