"""Import modules"""
# pylint: disable=R0903
import psutil
from .globals import Global


class Disk():
    """Disk information"""
    @classmethod
    def serve(cls):
        """Serve disk info"""
        # Disk Information
        print("="*40, "Disk Information", "="*40)
        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {Global.get_size(partition_usage.total)}")
            print(f"  Used: {Global.get_size(partition_usage.used)}")
            print(f"  Free: {Global.get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {Global.get_size(disk_io.read_bytes)}")
        print(f"Total write: {Global.get_size(disk_io.write_bytes)}")
