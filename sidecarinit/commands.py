import click
import os
import sys
import logging
from pathlib import Path
import sidecarinit.config as config
import sidecarinit.download as download

logger = logging.getLogger(__name__)

# Decorator function triggers when script runs to define the CLI input options.
# Sets default value for env_yml, an optional argument with a help prompt that is used when it's provided by the user.
@click.command()
@click.argument('env_yml', required=False, default='/opt/indy-sidecar/config/application.yaml')
# help='Target environment, Same as sidecar application.yml'
def run(env_yml):
    # Calling read_config() function from the config module to parse a YAML file and load configuration into a named tuple suite.
    suite = config.read_config(env_yml)

    # Assigning the archive_name variable with the build.config.id environment variable if exists.
    archive_name = os.environ.get('build.config.id')

    # Downloading from suite.archive_api to suite.local_repository.
    logger.info('Downloading from : %s to %s .', suite.archive_api, suite.local_repository)
    Path(suite.local_repository).mkdir(parents=True, exist_ok=True)

    if archive_name:
        download.download_archive(suite.archive_api +  "/" + archive_name,
                                  suite.local_repository)
    else:
        logger.info('build.config.id does not exist, exit now.')

    sys.exit(0)
