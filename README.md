This is the EMBERS datasets repository

[![build][build-icon]][build-page]

[build-icon]: https://travis-ci.org/iot-lab/embers-datasets.svg?branch=master
[build-page]: https://travis-ci.org/iot-lab/embers-datasets/branches


This repository contains code for datasets "plugins" which expose
existing datasets of various kinds for e.g. iotlab-injectors to use.

The intent of this repository is twofold:

 1. provide a catalogue of (and landing zone for) EMBERS datasets
 2. propose a common framework for describing and provinding data


Available datasets
------------------

The list of currently available datasets is as follows:

	citypulse: pollution, traffic          / 449 devices  / historical
	paris:     parking                     / 1226 devices / real-time
	synthetic: parking, traffic, pollution / any nb of devices

The "citypulse" dataset is file-based, it needs to be downloaded prior to use.
The "paris" dataset says parking but this is the Velib bike-stations parking.
The "synthetic" dataset is code-generated and provides simple numbered events.

Available datasets plugins live in directory `src/embers/datasets/`.


Overview
--------

In the context of EMBERS, datasets are roughly restricted to belong to
only three mobility-oriented categories: parking, traffic and pollution.
There is no real technological, philosophical or political justification
to this choice other than keeping things stupid and simple.

This leads to a basic design - a draft really - for datasets "descriptors"
and for the python-based datasets "plugins" framework which are overviewed
in the following sections.


Dataset "descriptors"
---------------------

A dataset descriptor is nothing more than a json file, with rather generic
and self describing fields.  The current proposal is a draft, which might
need to be extended or refined as needed in the future.

For file-based datasets e.g. citypulse, field `download_url` is used by
helper class `Downloader` via the iotlab-injectors `datasets` tool to actually
download the dataset files.  Other than that, fields are simply descriptive.

For an example descritor, see e.g. `src/embers/datasets/citypulse/traffic.json`

Having a "common" json-based format for datasets descriptors is supposed
to allow for easier automatic basic metadata import into a user-friendly
EMBERS datasets dashboard.


Dataset "plugin" harness
------------------------

A dataset "plugin" is an adapter for EMBERS datasets which offers a simple
uniform interface to the iotlab-injectors toolset - or any other piece of
python code that fancies using it.  Basically, a dataset exposes a set
of "sensors", each providing a set of data "samples" which will be accessed
in sequence.

A dataset class is therefore expected to offer a `.get_source(id)` method,
expected to return an iterator-like object offering a `.next()` method.
Method `.next()` is expected to return the "payload" i.e. the "sample"
data item as a python dictionary object, expected to be json-able.

For an example dataset class, see e.g. `src/embers/datasets/synthetic/main.py`

In order to be auto-discoverable, datasets plugins need to be named
and packaged in a specific manner.  Utility `lib/lookup.py` is used to lookup
available datasets and looks for classes `Parking`, `Traffic`, `Pollution`,
that is, the three event types mentioned in the intro.  It looks for those
in any python packages lying under the `embers.datasets` root, except 'lib'.
That is, all packages/directories under `embers.datasets` are expected to be
in effect datasets names.

Package `embers.datasets` is a "namespace package", allowing for out-of-tree
alien providers to simply plug into the package tree.  It is then possible to
distribute and/or install datasets selectively using e.g. `pip` and still
keep a simple uniform api.
