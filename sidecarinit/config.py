from ruamel.yaml import YAML
import os

ENV_ARCHIVE_API = 'archive-api'
ENV_LOCAL_REPOSITORY = 'local-repository'

DEFAULT_PROXY_PORT = 8081
DEFAULT_LOCAL_REPOSITORY = os.path.expanduser('~/preSeedRepo')


class Environment:
    def __init__(self, env_config_dict):
        self.archive_api = env_config_dict.get('sidecar').get(ENV_ARCHIVE_API)
        self.local_repository = env_config_dict.get('sidecar').get(ENV_LOCAL_REPOSITORY).replace('${user.home}', os.path.expanduser('~')) or DEFAULT_LOCAL_REPOSITORY


def read_config(env_yml):
    """ Read the suite configuration that this worker should run, from a config.yml file 
    (specified on the command line and passed in as a parameter here).
    Once we have a suite YAML file (from the suite_yml config), that file will be parsed
    and passed back with the rest of the config values, in a Config object.
    If any required configs are missing and don't have default values, error messages will
    be generated. If the list of errors is non-empty at the end of this method, an error
    message containing all of the problems will be logged to the console and an
    exception will be raised.
    """
    errors = []

    env_config_dict = {}
    if env_yml is None:
        errors.append(f"Missing test environment config file")
    elif not os.path.exists(env_yml):
        errors.append(f"Missing test environment config file")
    else:
        with open(env_yml) as f:
            yaml = YAML(typ='safe')
            env_config_dict = yaml.load(f)

    env = Environment(env_config_dict)

    return env
