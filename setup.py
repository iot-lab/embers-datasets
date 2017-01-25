from distutils.core import setup
from setuptools import find_packages

PACKAGE = "embers_datasets"
VERSION = "0.1"


with open('COPYING.md') as f: LICENSE = f.read()

SUB_PACKAGES = [PACKAGE+"."+pkg for pkg in find_packages(".")]

setup(
    name           = "embers-datasets",
    version        = VERSION,
    author         = "The EMBERS consortium",
    author_email   = "dev@embers.city",
    description    = "datasets descriptors and providers for EMBERS",
    url            = "http://www.embers.city/",
    keywords       = ["Open Data", "Smart City"],
    license        = LICENSE,
    packages       = [PACKAGE] + SUB_PACKAGES,
    package_dir    = {PACKAGE: "."},
    package_data   = {PACKAGE: ['*/*.json']},
)
