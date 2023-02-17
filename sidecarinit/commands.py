import click
import os
import sys
import logging
from pathlib import Path
import sidecarinit.config as config
import sidecarinit.download as download

logger = logging.getLogger(__name__)


@click.command()
@click.argument('env_yml', required=False, default='/deployments/config/application.yaml')
# help='Target environment, Same as sidecar application.yml'
def run(env_yml):

    suite = config.read_config(env_yml)

    archive_name = os.environ.get('build.config.id')

    logger.info('Downloading from : %s to %s .', suite.archive_api, suite.local_repository)
    Path(suite.local_repository).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(suite.local_repository, archive_name)).touch(exist_ok=True)

    if archive_name:
        download.download_archive(suite.archive_api +  "/" + archive_name,
                                  suite.local_repository)
    else:
        logger.info('BUILD_ID does not exist, exit now.')

    sys.exit(0)
