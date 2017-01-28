from setuptools import setup, find_packages

PACKAGE = "embers.datasets"
VERSION = "0.1"


setup(
    name           = PACKAGE,
    version        = VERSION,
    author         = "The EMBERS consortium",
    author_email   = "dev@embers.city",
    description    = "datasets descriptors and providers for EMBERS",
    url            = "http://www.embers.city/",
    keywords       = ["Open Data", "Smart City"],
    license        = open('COPYING.md').read(),
    packages       = [PACKAGE] + [PACKAGE+"."+p for p in find_packages()],
    package_dir    = {PACKAGE: "."},
    package_data   = {PACKAGE: ['*/*.json']},
    namespace_packages = [PACKAGE],
)
