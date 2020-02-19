import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    for game in json_data:
        gamenum = json_data[game]
        plat = gamenum["platform"]
        for i in plat:
            newplat = test_data.Platform(plat["name"], plat["launch year"])
        new_game = test_data.Game(title=gamenum["title"], platform=newplat,year=gamenum["Year"])
        game_library.add_game(new_game)
    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable family_json_data
    json_data = json.load(reader)
ans= make_game_library_from_json(json_data)
print(ans)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
