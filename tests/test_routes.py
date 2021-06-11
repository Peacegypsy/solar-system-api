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
    
def test_get_planet_when_no_planet(client):
    #Act
    response = client.get("/planet/1")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 404
    
def test_get_all_planets(client, get_all_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
#     assert response_body == [
#                 {"description": "An amazing planet of incredible size.", 
#                 "id": 1, 
#                 "name": "Jupiter"},
#                 {"description": "The planet of love.",
#                 "id": 2,
#                 "name": "Venus"},
#                 {"description": "An incredible beauty of blue and green.",
#                 "id": 1,
#                 "name": "Earth"}
# ]

def test_create_one_planet(client, create_one_planet):
    #Act
    response = client.post("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 201
    # assert response_body == {
    #     "name": "Pluto",
    #     "description": "Some might say its not a planet but we disagree."
    # }