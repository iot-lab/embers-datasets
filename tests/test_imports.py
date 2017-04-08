import pytest


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



def get_dataset(dataset, event_type):
    package_name = "embers.datasets." + dataset + "." + event_type
    class_name = event_type.capitalize()
    package = __import__(package_name, fromlist=[class_name])
    return package.__dict__[class_name]()
