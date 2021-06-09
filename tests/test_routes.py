import pytest 

def test_add_two_planets(client, add_two_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    #assert response_body == []
    
def test_get_one_planet(client, get_one_planet):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body == {
                "description": "An amazing planet of incredible size.", 
                "id": 1, 
                "name": "Jupiter"
}