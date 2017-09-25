This is the EMBERS datasets repository

[![build][build-icon]][build-page]

[build-icon]: https://travis-ci.org/iot-lab/embers-datasets.svg?branch=master
[build-page]: https://travis-ci.org/iot-lab/embers-datasets/branches


This repository contains code for datasets "plugins" which expose
existing datasets of various kinds for e.g. iotlab-injectors to use.

The intent of this repository is twofold:

1./ provide a catalogue of (and landing zone for) EMBERS datasets
2./ propose a common framework for describing and provinding data


Available datasets
------------------

The list of currently available datasets is as follows:

	citypulse: pollution, traffic          / 455 devices  / historical
	paris:     parking                     / 1226 devices / real-time
	synthetic: parking, traffic, pollution / any nb of devices

The "citypulse" dataset is file-based, it needs to be downloaded prior to use.
The "paris" dataset says parking but this is the Velib bike-stations parking.
The "synthetic" dataset is code-generated and provides simple numbered events.

Available datasets plugins live in directory `src/embers/datasets/`.
