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


def test_traffic_sources():
    x = traffic.Traffic()
    s = x.get_source(0)
    d = s.next()

    assert "vehicleCount" in d
    assert "avgSpeed" in d


def test_pollution_sources():
    x = pollution.Pollution()
    s = x.get_source(0)
    d = s.next()

    assert "carbon_monoxide" in d
    assert "nitrogen_dioxide" in d


def test_multi_sources_read():
    x = traffic.Traffic()
    s = x.get_source(0)
    d0 = s.next()

    s = x.get_source(448)
    d = s.next()

    assert d != d0
    assert "avgSpeed" in d

    x = pollution.Pollution()
    s = x.get_source(0)
    d = s.next()

    assert d != d0
    assert "carbon_monoxide" in d
