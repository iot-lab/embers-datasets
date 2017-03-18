import pytest


def test_package_imports():
    import embers.datasets.synthetic
    import embers.datasets.synthetic.traffic
    import embers.datasets.synthetic.parking
    import embers.datasets.synthetic.pollution


def test_dataset_constructor():
    import embers.datasets.synthetic.traffic as traffic
    dataset = traffic.Traffic()


def test_dataset_basic_usage(traffic):
    source = traffic.get_source(device_id=3)
    data = source.next()
    data = source.next()


def test_dataset_get_source(traffic):
    source = traffic.get_source(0)
    source1 = traffic.get_source(0)

    assert source == source1

    source2 = traffic.get_source(2)

    assert source2 != source


def test_dataset_next(traffic):
    source = traffic.get_source(0)
    data1 = source.next()
    data2 = source.next()

    assert data1 != data2


def test_dataset_multi_next(traffic):
    source1 = traffic.get_source(1)
    source2 = traffic.get_source(2)

    data1 = source1.next()
    data2 = source2.next()

    assert data1 != data2


@pytest.fixture
def traffic():
    from embers.datasets.synthetic.traffic import Traffic
    return Traffic()
