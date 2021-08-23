import click
import os
from pathlib import Path
import sidecarinit.config as config
import sidecarinit.download as download

@click.command()
@click.argument('env_yml', required=False, default='/deployments/config/application.yml') #help='Target environment, Same as sidecar application.yml'
def run(env_yml):
    
    suite = config.read_config(env_yml)

    archive_name = '/' + os.environ.get('BUILD_ID') + '.zip'

    print('Downloading from :', suite.archive_api, ' to ' ,suite.local_repository)
    Path(suite.local_repository).mkdir(parents=True, exist_ok=True)
    Path(suite.local_repository + archive_name ).touch(exist_ok=True)

    download.download_archive(suite.archive_api + archive_name, suite.local_repository)