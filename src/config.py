config = {}

config['Drawer'] = {
  'Screen': {
    'width': 1500,
    'height': 750,
    'border': 10,
  },
  'Surface': {
    'width': 1140,
    'height': 730
  },
  'Colors': {
    'white': (255, 255, 255),
    'gray': (193,193,193),
    'black': (0, 0, 0),
    'brown': (139,115,85),
    'cornsilk': (205,200,177),
    'cornsilk2': (139,136,120),
    'burntsienna': (138,54,15),
    'cobaltgreen': (61,145,64),
    'skyblue': (0,104,139),
    'firebrick': (205,38,38),
    'darkorange': (238,118,0),
    'yellow': (238,238,0),
    'Player': ['skyblue', 'cobaltgreen', 'firebrick', 'darkorange', 'yellow', 'gray']
  },
  'Images': {
    'Map': {
      'name': 'Map',
      'image': r'..\lib\images\map.jpg',
      'width': 1120,
      'height': 710
    },
    'Target': {
      'name': 'Target',
      'image': r'..\lib\images\misc\bullseye.png',
      'width': 32,
      'height': 32
    },
    'Units': {
      'name': {
        'Warrior': r'..\lib\images\Units\Land\warrior.png',
        'Horseman': r'..\lib\images\Units\Land\horseman.png',
        'Swordsman': r'..\lib\images\Units\Land\swordsman.png',
        'Knight': r'..\lib\images\Units\Land\knight.png',
        'Musketman': r'..\lib\images\Units\Land\musketman.png',
        'Cavalry': r'..\lib\images\Units\Land\cavalry.png',
        'Infantry': r'..\lib\images\Units\Land\infantry.png',
        'Tank': r'..\lib\images\Units\Land\tank.png',
        'Archer': r'..\lib\images\Units\Land\archer.png',
        'Cannon': r'..\lib\images\Units\Land\cannon.png',
        'Artillery': r'..\lib\images\Units\Land\artillery.png',
        'Anti-Air Gun': r'..\lib\images\Units\Land\anti-air gun.png',
        'Trireme': r'..\lib\images\Units\Sea\trireme.png',
        'Caravel': r'..\lib\images\Units\Sea\caravel.png',
        'Battleship': r'..\lib\images\Units\Sea\battleship.png',
        'Aircraft Carrier': r'..\lib\images\Units\Sea\aircraft carrier.png',
        'Fighter': r'..\lib\images\Units\Air\fighter.png',
        'Bomber': r'..\lib\images\Units\Air\bomber.png',
        'Jet Fighter': r'..\lib\images\Units\Air\jet fighter.png',
        'Helicopter': r'..\lib\images\Units\Air\helicopter.png'
      },
      'width': 50,
      'height': 50
    },
    'Resources': {
      'name': {
        'Food': r'..\lib\images\Resources\food.png',
        'Metal': r'..\lib\images\Resources\metal.png',
        'Oil': r'..\lib\images\Resources\oil.png',
        'Wood': r'..\lib\images\Resources\wood.png'
      },
      'width': 40,
      'height': 40
    }
  },
  'Rects': {
    'Border': {
      'start': (10, 10),
      'width': 1480,
      'height': 730,
      'color': 'black'
    },
    'Map': {
      'start': (20, 20),
      'width': 1120,
      'height': 710,
      'color': 'white'
    },
    'Side': {
      'start': (1150, 20), 
      'width': 330, 
      'height': 710,
      'color': 'brown'
    },
    'Info': {
      'start': (1160, 590), 
      'width': 310,
      'height': 130,
      'color': 'black'
    },
    'Turn': {
      'start': (1160, 30),
      'width': 150,
      'height': 60,
      'color': 'black'
    },
    'Color': {
      'start': (1320, 30),
      'width': 150,
      'height': 60,
      'color': 'black'
    },
    'Resources': {
      'start': (1160, 100),
      'width': 310,
      'height': 60,
      'color': 'black'
    },
    'Shop': {
      'start': (1160, 170),
      'width': 310,
      'height': 410,
      'color': 'black'
    },
    'ShopBoxes': {
      'start': [1175, 185],
      'width': 60,
      'height': 60,
      'color': 'black'
    },
    'PlayerBoxes': {
      'start': [25, 25],
      'width': 40,
      'height': 40,
      'color': 'black'
    }
  }
}

