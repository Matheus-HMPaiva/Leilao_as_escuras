

programming_dictionay = { "teste" : "teste", "casa" : "moradia", "Bug": "1234"

}



#Loop through a dictionary

for thing in programming_dictionay:
    print(thing)
    print(programming_dictionay[thing])


cidades = {
    "MG" : ["Pouso Alegre", "Congonhal"],
}

print(cidades["MG"][0])

travel_log = {
        "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
        "Alemanha": {
            "cities_visited": ["Berlin ", "Hamburg", "Stuttgart"],
            "total_visits": 17
        },

}

print(travel_log["Alemanha"]["cities_visited"][1])