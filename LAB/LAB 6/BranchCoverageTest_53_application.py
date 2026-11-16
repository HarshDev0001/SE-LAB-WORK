import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock

def test_ride_cost_branches():
    with pytest.raises(ValueError):
        ride_cost("unknown", 30, False, False)

    with pytest.raises(ValueError):
        ride_cost("standard", 0, False, False)

    assert ride_cost("standard", 30, True, False) == 0
    assert ride_cost("electric", 30, False, True) == 50
    assert ride_cost("cargo", 210, False, True) == 450

def test_dock_status_branches():
    with pytest.raises(ValueError):
        dock_status(0, 0)

    with pytest.raises(ValueError):
        dock_status(-1, 10)

    with pytest.raises(ValueError):
        dock_status(11, 10)

    assert dock_status(0, 10) == "empty"
    assert dock_status(10, 10) == "full"
    assert dock_status(2, 10) == "few bikes"
    assert dock_status(8, 10) == "few slots"
    assert dock_status(5, 10) == "available"

def test_can_unlock_branches():
    assert can_unlock(100, True, 20) is False
    assert can_unlock(100, False, 15) is False
    assert can_unlock(100, False, 17) is True
    assert can_unlock(60, False, 20) is True
    assert can_unlock(40, False, 20) is False
def test_subscriber_blocks_become_zero():
    assert ride_cost("standard", 30, True, False) == 0
def test_subscriber_discount_branch():
    assert ride_cost("standard", 60, True, False) == 20