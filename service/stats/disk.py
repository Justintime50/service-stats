import psutil
from service.stats.globals import Global


class Disk():
    @classmethod
    def serve(cls):
        """Serve disk info
        """
        # Title
        disk_title = '='*15 + ' Disk Information ' + '='*15
        partition_title = 'Partitions and Usage:'

        # Disk Information
        partitions = psutil.disk_partitions()
        disk = ''
        for partition in partitions:
            device = f'=== Device: {partition.device} ==='
            mountpoint = f'  Mountpoint: {partition.mountpoint}'
            filesystem_type = f'  File system type: {partition.fstype}'
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # Catch errors when a disk isn't ready
                continue
            total_size = f'  Total Size: {Global.get_size(partition_usage.total)}'  # noqa
            used = f'  Used: {Global.get_size(partition_usage.used)}'
            free = f'  Free: {Global.get_size(partition_usage.free)}'
            percentage = f'  Percentage: {partition_usage.percent}%'
            # Combine each disk into a variable
            disk += device + '\n' + mountpoint + '\n' + filesystem_type + \
                '\n' + total_size + '\n' + used + '\n' + free + '\n' + \
                percentage + '\n'

        # Get IO stats since boot
        disk_io = psutil.disk_io_counters()
        total_read = f'Total read (since boot): {Global.get_size(disk_io.read_bytes)}'  # noqa
        total_write = f'Total write (since boot): {Global.get_size(disk_io.write_bytes)}'  # noqa

        final_message = '\n' + disk_title + '\n' + partition_title + \
            '\n' + disk + '\n' + total_read + '\n' + total_write
        return final_message
