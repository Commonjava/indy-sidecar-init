import click
import os
import sys
from time import sleep
from traceback import format_exc
import sidecarinit.config as config

@click.command()
@click.argument('env_yml', required=False) #help='Target environment, Same as sidecar application.yml'
@click.option('-B', '--artifact-dir', help='Dir for saving artifacts', default='artifacts')
def run(env_yml, artifact_dir):
    
    #suite = config.read_config(env_yml)
    print("hello world")