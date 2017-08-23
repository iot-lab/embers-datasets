import pytest


def test_package_imports():
    import embers.datasets.paris
    import embers.datasets.paris.parking


def test_dataset_constructor():
    import embers.datasets.paris.parking as velib
    dataset = velib.Parking()


def test_dataset_basic_usage(dataset):
    source = dataset.get_source(device_id=3)
    data = source.next()
    data = source.next()


def test_dataset_get_source(dataset):
    source = dataset.get_source(0)
    source1 = dataset.get_source(0)

    assert source == source1

    source2 = dataset.get_source(2)

    assert source2 != source


def test_dataset_multi_next(dataset):
    source1 = dataset.get_source(1)
    source2 = dataset.get_source(2)

    data1 = source1.next()
    data2 = source2.next()

    assert data1 != data2


@pytest.fixture
def dataset():
    from embers.datasets.paris.parking import Parking
    return Parking()
