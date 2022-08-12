from unittest import TestCase

from Server.sync_algorithm import SyncAlgorithms


class TestSyncAlgorithms(TestCase):
    """
    Class with synchronization algorithm tests.

    """

    def test_determine_sync(self):
        host_time = 4000
        member_time = 1100
        host_delay = 20
        member_delay = 30
        """Test if determining synchronization is correct"""
        self.assertEqual(SyncAlgorithms.determine_sync(host_time, host_delay, member_time, member_delay), True)
        self.assertEqual(SyncAlgorithms.determine_sync(host_time, host_delay, host_time, host_delay), False)

    def test_sync_playback_time(self):
        host_time = 4000
        host_delay = 20
        member_delay = 30
        """Test if playback is changed to host + delay time."""
        self.assertEqual(SyncAlgorithms.sync_playback_time(host_time, host_delay, member_delay), 4025)

