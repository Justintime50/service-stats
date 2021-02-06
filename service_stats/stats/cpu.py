import psutil


class Cpu():
    @staticmethod
    def serve_data():
        """Serve CPU info
        """
        # Title
        cpu_title = '='*15 + ' CPU Information ' + '='*15

        # Cores
        physical_cores = 'Physical cores:' + \
            str(psutil.cpu_count(logical=False))
        total_cores = 'Total cores:' + str(psutil.cpu_count(logical=True))

        # CPU Frequencies
        cpufreq = psutil.cpu_freq()
        max_freq = f'Max Frequency: {cpufreq.max:.2f}Mhz'
        min_freq = f'Min Frequency: {cpufreq.min:.2f}Mhz'
        current_freq = f'Current Frequency: {cpufreq.current:.2f}Mhz'

        # CPU Usage
        usage_message = 'CPU Usage Per Core:'
        all_core_percentage = ''
        for i, percentage in enumerate(
            psutil.cpu_percent(
                percpu=True,
                interval=1
            )
        ):
            core_percentage = f'Core {i}: {percentage}%\n'
            # Combine each core into a variable
            all_core_percentage += core_percentage
        total_usage = f'Total CPU Usage: {psutil.cpu_percent()}%'

        final_message = (
            '\n' + cpu_title +
            '\n' + physical_cores +
            '\n' + total_cores +
            '\n' + max_freq +
            '\n' + min_freq +
            '\n' + current_freq +
            '\n' + usage_message +
            '\n' + all_core_percentage + total_usage
        )
        return final_message
