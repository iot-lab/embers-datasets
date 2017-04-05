import pytest

import embers.datasets.citypulse.traffic as traffic
import os


def test_traffic_download(monkeypatch):
    x = traffic.Traffic()
    x.download()
    monkeypatch.chdir("embers.datasets.citypulse")

    dest_dir = "traffic_june_sep"
    metadata = "trafficMetaData.csv"

    assert os.path.isdir(dest_dir)
    assert len(os.listdir(dest_dir)) == 449
    assert os.path.isfile(metadata)
    assert len(open(metadata).read()) == 103917
