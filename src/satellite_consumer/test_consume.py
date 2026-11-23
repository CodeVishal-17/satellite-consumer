
import datetime as dt
import unittest

from satellite_consumer.consume import _find_missing_timestamps


class TestFindMissingTimestamps(unittest.TestCase):
    """Test detection of timestamps missing from the store."""

    def test_finds_missing_timestamp(self) -> None:
        start = dt.datetime(2024, 1, 1, 0, 0, tzinfo=dt.UTC)

        expected_times = [
            start,
            start + dt.timedelta(minutes=15),
            start + dt.timedelta(minutes=30),
            start + dt.timedelta(minutes=45),
        ]

        actual_times = [
            expected_times[0],
            expected_times[1],
            expected_times[3],
        ]

        missing_times = _find_missing_timestamps(expected_times, actual_times)

        self.assertEqual(missing_times, [expected_times[2]])
    
    
    def test_returns_empty_list_when_all_timestamps_exist(self) -> None:
        start = dt.datetime(2024, 1, 1, 0, 0, tzinfo=dt.UTC)

        expected_times = [
            start,
            start + dt.timedelta(minutes=15),
            start + dt.timedelta(minutes=30),
        ]

        actual_times = expected_times.copy()

        missing_times = _find_missing_timestamps(expected_times, actual_times)

        self.assertEqual(missing_times, [])

