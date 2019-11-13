#!/usr/bin/python
#File for confgiuring dynamic template information

def config_generators(app):
  @app.context_processor
  def get_nav_icons():
    return dict(nav_icons=[
      {"name": "Explore",   "src" : "/replays",  "img" : "header-player.png",   "class" : "home",},
      {"name": "Upload",    "src" : "/upload",   "img" : "header-matchups.png", "class" : "mu",},
      ])

  @app.context_processor
  def get_characters():
    chardata = [
      {"id" : 22, "name" : "Dr. Mario",        "intname" : "DOCTOR",  "csspos" : 0,  },
      {"id" : 8,  "name" : "Mario",            "intname" : "MARIO",   "csspos" : 1,  },
      {"id" : 7,  "name" : "Luigi",            "intname" : "LUIGI",   "csspos" : 2,  },
      {"id" : 5,  "name" : "Bowser",           "intname" : "BOWSER",  "csspos" : 3,  },
      {"id" : 12, "name" : "Peach",            "intname" : "PEACH",   "csspos" : 4,  },
      {"id" : 17, "name" : "Yoshi",            "intname" : "YOSHI",   "csspos" : 5,  },
      {"id" : 1,  "name" : "Donkey Kong",      "intname" : "KONG",    "csspos" : 6,  },
      {"id" : 0,  "name" : "Captain Falcon",   "intname" : "FALCON",  "csspos" : 7,  },
      {"id" : 25, "name" : "Ganondorf",        "intname" : "GANON",   "csspos" : 8,  },
      {"id" : 20, "name" : "Falco",            "intname" : "FALCO",   "csspos" : 9,  },
      {"id" : 2,  "name" : "Fox",              "intname" : "FOX",     "csspos" : 10, },
      {"id" : 11, "name" : "Ness",             "intname" : "NESS",    "csspos" : 11, },
      {"id" : 14, "name" : "Ice Climbers",     "intname" : "CLIMBER", "csspos" : 12, },
      {"id" : 4,  "name" : "Kirby",            "intname" : "KIRBY",   "csspos" : 13, },
      {"id" : 16, "name" : "Samus",            "intname" : "SAMUS",   "csspos" : 14, },
      {"id" : 18, "name" : "Zelda",            "intname" : "ZELDA",   "csspos" : 15, },
      {"id" : 6,  "name" : "Link",             "intname" : "LINK",    "csspos" : 16, },
      {"id" : 21, "name" : "Young Link",       "intname" : "YOUNG",   "csspos" : 17, },
      {"id" : 19, "name" : "Sheik",            "intname" : "SHEIK",   "csspos" : 18, },
      {"id" : 24, "name" : "Pichu",            "intname" : "PICHU",   "csspos" : 19, },
      {"id" : 13, "name" : "Pikachu",          "intname" : "PIKACHU", "csspos" : 20, },
      {"id" : 15, "name" : "Jigglypyff",       "intname" : "JIGGLY",  "csspos" : 21, },
      {"id" : 10, "name" : "Mewtwo",           "intname" : "MEWTWO",  "csspos" : 22, },
      {"id" : 3,  "name" : "Mr. Game & Watch", "intname" : "WATCH",   "csspos" : 23, },
      {"id" : 9,  "name" : "Marth",            "intname" : "MARTH",   "csspos" : 24, },
      {"id" : 23, "name" : "Roy",              "intname" : "ROY",     "csspos" : 25, },
      {"id" : -1, "name" : "All Characters",   "intname" : "_NONE",   "csspos" : 26, },
      ]
    return dict(chardata=chardata)

  @app.context_processor
  def get_stages():
    stagedata = [
      { "id" :  32, "name" : "Final Destination",  "intname": "FINAL"     },
      { "id" :  31, "name" : "Battlefield",        "intname": "BATTLE"    },
      { "id" :  2 , "name" : "Fountain of Dreams", "intname": "FOUNTAIN"  },
      { "id" :  8 , "name" : "Yoshi's Story",      "intname": "STORY"     },
      { "id" :  3 , "name" : "Pokemon Stadium",    "intname": "STADIUM"   },
      { "id" :  28, "name" : "Dream Land",         "intname": "DREAMLAND" },
      { "id" : -1 , "name" : "Any Stage",          "intname": "_NONE0"    },
      ]
    return dict(stagedata=stagedata)

  @app.context_processor
  def get_sorts():
    sortdata = [
      { "name" : "Recently Played",    "intname": "play"     },
      { "name" : "Recently Uploaded",  "intname": "upload"   },
      ]
    return dict(sortdata=sortdata)

  @app.context_processor
  def utility_functions():
    #Check if P1 / P2 has a higher value for a statistic and highlight if so
    def hl_if_higher(replay,index,key):
      return "hl-green" if replay["p"][index-1][key] > replay["p"][2-index][key] else ""
    #Check if P1 / P2 has a lower value for a statistic and highlight if so
    def hl_if_lower(replay,index,key):
      return "hl-green" if replay["p"][index-1][key] < replay["p"][2-index][key] else ""
    return dict(hl_if_higher=hl_if_higher,hl_if_lower=hl_if_lower)
