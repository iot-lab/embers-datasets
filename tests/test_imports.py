import pytest


def test_citypulse_traffic():
    import embers.datasets.citypulse.traffic as traffic
    x = traffic.Traffic()
    x.download # just check this exists, don't run it
