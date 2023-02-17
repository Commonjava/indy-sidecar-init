import urllib.request
import shutil
import os


def download_archive(url, repository):
    archive_name = "/" + os.environ.get('build.config.id') + '.zip'

    with urllib.request.urlopen(url) as response, open(repository + archive_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    shutil.unpack_archive(repository + archive_name, repository)
