import pytest

from embers.datasets.lib.lookup import get_dataset


def test_citypulse_traffic():
    import embers.datasets.citypulse.traffic as traffic
    x = traffic.Traffic()
    x.download # just check this exists, don't run it


@pytest.mark.parametrize("events", [
    "traffic",
    "pollution",
])
def test_citypulse(events):
    x = get_dataset("citypulse", events)

    x.download # just check this exists, don't run it
    x.get_source


@pytest.mark.parametrize("events", [
    "traffic",
    "parking",
    "pollution",
])
def test_synthetic(events):
    x = get_dataset("synthetic", events)

    x.get_source

    with pytest.raises(AttributeError):
        x.download
