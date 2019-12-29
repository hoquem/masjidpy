from config import config

class TestConfig(Config):
    TESTING = true;
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unitttest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
