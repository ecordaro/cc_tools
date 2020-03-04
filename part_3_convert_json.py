import cc_dat_utils as ccd
import json
import cc_classes as ccc
#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file


def make_level(data):
	levelpack = ccc.CCLevelPack()
	for l in data:
		level = ccc.CCLevel()
		level.level_number = l["level_number"]
		level.time = l["time"]
		level.num_chips = l["num_chips"]
		level.upper_layer = l["upper_layer"]

		for field in l["optional_fields"]:
			ftype = field["field_type"]
			if ftype == "title":
				title = ccc.CCMapTitleField(field["value"])
				level.add_field(title)
			elif ftype == "hint":
				hint = ccc.CCMapHintField(field["value"])
				level.add_field(hint)
			elif ftype == "password":
				password = ccc.CCEncodedPasswordField(field["value"])
				level.add_field(password)
			elif ftype == "monsters":
				monsterslist = []
				for mons in field["value"]:
					monster = ccc.CCCoordinate(mons["x"], mons["y"])
					monsterslist.append(monster)
				monsters_list = ccc.CCMonsterMovementField(monsterslist)
				level.add_field(monsters_list)

		levelpack.add_level(level)
	return levelpack

inputfile = "ecordaro_cc1.json"
with open(inputfile, "r") as reader:
	levelfile = json.load(reader)

finalLevel = make_level(levelfile)

ccd.write_cc_level_pack_to_dat(finalLevel, "data/ecordaro_cc1.dat")

