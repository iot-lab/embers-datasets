import pytest

import embers.datasets.citypulse.traffic as traffic
import embers.datasets.citypulse.pollution as pollution
import os


def test_traffic_download(monkeypatch):
    x = traffic.Traffic()
    x.download()
    monkeypatch.chdir("embers.datasets.citypulse")

    dest_dir = "traffic_june_sep"  # dataset is aug_sep_2014
    metadata = "trafficMetaData.csv"

    check_dataset(dest_dir, metadata)


def check_dataset(dest_dir, metadata):
    assert os.path.isdir(dest_dir)
    assert len(os.listdir(dest_dir)) == 449
    assert os.path.isfile(metadata)
    assert len(open(metadata).read()) == 103917


def test_pollution_download(monkeypatch):
    x = pollution.Pollution()
    x.download()
    monkeypatch.chdir("embers.datasets.citypulse")

    dest_dir = "pollution"
    metadata = "trafficMetaData.csv"

    check_dataset(dest_dir, metadata)
