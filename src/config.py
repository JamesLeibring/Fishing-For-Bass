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
    'black': (0, 0, 0),
    'brown': (153, 76, 0),
    'dark_brown': (102, 51, 0),
    'grey': (128, 128, 128),
    'light_grey': (192, 192, 192),
    'dark_grey': (100, 100, 100),
    'blue': (51, 51, 255),
    'red': (230, 30, 30),
    'green': (0, 153, 0),
    'purple': (153, 0, 153),
    'dirt': (148, 107, 37),
    'fill': (104, 107, 37)
  },
  'Images': {
    'Map': {
      'name': r'..\lib\images\map.jpg',
      'width': 1120,
      'height': 710
    },
    'Target': {
      'name': r'..\lib\images\misc\bullseye.png',
      'width': 32,
      'height': 32
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
      'color': 'red'
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
    }
  }
}
