ACCEPTABLE_DESYNC = 2000


class SyncAlgorithms:
    """
    Class containing methods for playback synchronization.
    """

    @staticmethod
    def sync_playback_time(host_time: int, host_delay: int, user_delay: int) -> int:
        """
        Generates new correct time created from current host playback time.

        :param host_time: host playback time.
        :param host_delay: host->server->host delay in milliseconds.
        :param user_delay: user->server->user delay in milliseconds.
        :return: new playback time value close to host playback time.
        """
        return host_time + (host_delay // 2) + (user_delay // 2)


    @staticmethod
    def determine_sync(host_time: int, host_delay: int, user_time: int, user_delay: int) -> bool:
        """
        Determines whether synchronization between host and another user is needed.

        :param host_time: host playback time.
        :param user_time: user playback time.
        :param host_delay: host->server->host delay in milliseconds.
        :param user_delay: user->server->user delay in milliseconds.
        :return: boolean value, true if synchronization is needed.
        """
        return (abs(host_time-user_time) - host_delay - user_delay) > ACCEPTABLE_DESYNC
