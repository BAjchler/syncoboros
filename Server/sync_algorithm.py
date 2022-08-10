ACCEPTABLE_DESYNC = 2000


class SyncAlgorithms:

    @staticmethod
    def sync_playback_time(priority_user: int, host_delay: int, user_delay: int) -> int:
        return priority_user + (host_delay // 2) + (user_delay // 2)

    @staticmethod
    def determine_sync(host_time: int, host_delay: int, user_time: int, user_delay: int) -> bool:
        return (abs(host_time-user_time) - host_delay - user_delay) > ACCEPTABLE_DESYNC
