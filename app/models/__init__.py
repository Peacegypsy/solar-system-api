from flask import Flask

def create_app(test_config=None):
    
    from app.models.planet import Planet

    return app