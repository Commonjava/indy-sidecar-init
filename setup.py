from setuptools import setup, find_packages
import sys

setup(
    zip_safe=True,
    use_2to3=False,
    name='sidecarinit',
    version='0.0.1',
    long_description='sidecar-init container for download archive and decompress',
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: Apache Public License v2 (APL)",
      "Programming Language :: Python :: 3",
      "Topic :: Software Development :: Build Tools",
      "Topic :: Utilities",
    ],
    license='APLv2+',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=[
      "requests",
      "ruamel.yaml",
      "click"
    ],
    entry_points={
        'console_scripts': [
            'run-sidecar-init = sidecarinit:run'
        ],
    }
)