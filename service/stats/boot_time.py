from datetime import datetime
import psutil


class Boot():
    @classmethod
    def serve(cls):
        """Serve boot time info
        """
        # Title
        boot_title = '='*15 + ' Boot Time ' + '='*15

        # Timestamp
        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.fromtimestamp(boot_time_timestamp)
        boot_message = (
            f'Boot Time: {boot_time.year}/{boot_time.month}/{boot_time.day}'
            f' {boot_time.hour}:{boot_time.minute}:{boot_time.second}'
        )

        final_message = '\n' + boot_title + '\n' + boot_message
        return final_message
