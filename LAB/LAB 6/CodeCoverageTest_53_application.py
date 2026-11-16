import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock


# RIDE COST TEST CASES

def test_standard_ride():
    assert ride_cost("standard", 45, False, False) == 40


def test_electric_ride():
    assert ride_cost("electric", 30, False, False) == 35


def test_cargo_ride():
    assert ride_cost("cargo", 30, False, False) == 50


def test_unknown_bike_type():
    with pytest.raises(ValueError):
        ride_cost("mountain", 30, False, False)


def test_invalid_duration():
    with pytest.raises(ValueError):
        ride_cost("standard", 0, False, False)


def test_subscriber_free_ride():
    assert ride_cost("standard", 30, True, False) == 0


def test_subscriber_discount():
    assert ride_cost("standard", 60, True, False) == 20


def test_peak_pricing():
    assert ride_cost("standard", 30, False, True) == 35


def test_cargo_peak_pricing():
    assert ride_cost("cargo", 30, False, True) == 50


def test_long_ride_surcharge():
    assert ride_cost("standard", 210, False, False) == 240


# DOCK STATUS TEST CASES

def test_empty_dock():
    assert dock_status(0, 10) == "empty"


def test_full_dock():
    assert dock_status(10, 10) == "full"


def test_few_bikes():
    assert dock_status(2, 10) == "few bikes"


def test_few_slots():
    assert dock_status(8, 10) == "few slots"


def test_available_dock():
    assert dock_status(5, 10) == "available"


def test_invalid_capacity():
    with pytest.raises(ValueError):
        dock_status(2, 0)


def test_negative_bikes():
    with pytest.raises(ValueError):
        dock_status(-1, 10)


def test_bikes_exceed_capacity():
    with pytest.raises(ValueError):
        dock_status(11, 10)


# UNLOCK TEST CASES

def test_active_ride():
    assert can_unlock(200, True, 20) is False


def test_underage_user():
    assert can_unlock(200, False, 15) is False


def test_age_16_sufficient_balance():
    assert can_unlock(100, False, 16) is True


def test_age_16_insufficient_balance():
    assert can_unlock(50, False, 16) is False


def test_adult_sufficient_balance():
    assert can_unlock(50, False, 18) is True


def test_adult_insufficient_balance():
    assert can_unlock(40, False, 20) is False