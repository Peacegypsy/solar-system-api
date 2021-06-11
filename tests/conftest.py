import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    with app.app_context():
        db.create_all()
        yield app
    with app.app_context():
        db.drop_all()
        
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def add_two_planets(app):
    venus = Planet(name="venus",description="Planet of love")
    neptune = Planet(name="neptune",description="Big love more")
    db.session.add_all([venus,neptune])
    db.session.commit()
    
@pytest.fixture
def get_one_planet(app):
    jupiter = Planet(name="Jupiter",description="An amazing planet of incredible size.")
    db.session.add_all([jupiter])
    db.session.commit()    
    
@pytest.fixture
def get_all_planets(app):
    earth = Planet(name="Earth",description="An incredible beauty of blue and green.")
    venus = Planet(name="Venus",description="The planet of love.")
    neptune = Planet(name="Neptune",description="Named after the ruler of the seas.")
    db.session.add_all([earth,venus,neptune])
    db.session.commit()
    
@pytest.fixture
def create_one_planet(app):
    pluto = Planet(name="Pluto",description="Some might say its not a planet but we disagree.")
    db.session.add_all([pluto])
    db.session.commit()