from os import environ
import os
import yaml


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

config_yml_file_name = 'setup_config.yml'
config_yml_path = (os.path.join(PROJECT_ROOT, config_yml_file_name))
with open(config_yml_path, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
  

class Config(object):
    """"
    Contains the configuration settings
    """
    app_url = cfg['app']['url']
    app_username = cfg['app']['username']
    app_password = cfg['app']['password']
