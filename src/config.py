import configparser

config = configparser.ConfigParser()

config['Screen'] = {
  'width': '1500',
  'height': '750',
  'border': '10',
}

with open('config.ini', 'w') as configfile:
  config.write(configfile)