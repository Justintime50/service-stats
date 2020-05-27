"""Import modules"""
# pylint: disable=R0903
from datetime import datetime
import psutil


class Boot():
    """Boot time information"""
    @classmethod
    def serve(cls):
        """Serve boot time info"""
        # Boot Time
        print("="*40, "Boot Time", "="*40)
        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.fromtimestamp(boot_time_timestamp)
        print(
            f"Boot Time: {boot_time.year}/{boot_time.month}/{boot_time.day}" +
            f"{boot_time.hour}:{boot_time.minute}:{boot_time.second}")
