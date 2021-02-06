import argparse
from datetime import datetime

import service_stats


class ServiceCLI():
    def __init__(self):
        """Setup CLI args
        """
        parser = argparse.ArgumentParser(
            description='Service serves savvy server stats.'
        )
        parser.add_argument(
            '-b',
            '--boot',
            action='store_true',
            required=False,
            default=False,
            help='Show boot time stats.'
        )
        parser.add_argument(
            '-c',
            '--cpu',
            action='store_true',
            required=False,
            default=False,
            help='Show CPU stats.'
        )
        parser.add_argument(
            '-d',
            '--disk',
            action='store_true',
            required=False,
            default=False,
            help='Show disk stats.'
        )
        parser.add_argument(
            '-m',
            '--memory',
            action='store_true',
            required=False,
            default=False,
            help='Show memory stats.'
        )
        parser.add_argument(
            '-n',
            '--network',
            action='store_true',
            required=False,
            default=False,
            help='Show network stats.'
        )
        parser.add_argument(
            '-s',
            '--system',
            action='store_true',
            required=False,
            default=False,
            help='Show system stats.'
        )
        parser.add_argument(
            '-sl',
            '--slack',
            action='store_true',
            required=False,
            default=False,
            help='Send ServiceStats report to Slack.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        ServiceStats.run(
            boot=self.boot,
            cpu=self.cpu,
            disk=self.disk,
            memory=self.memory,
            network=self.network,
            system=self.system,
            slack=self.slack,
        )


class ServiceStats():
    @staticmethod
    def serve_data(data_type):
        """Serve data from the specified category
        """
        data = data_type.serve_data()
        print(data)
        return data

    @staticmethod
    def run(boot=True, cpu=False, disk=False, memory=False,
            network=False, system=False, slack=False):
        """Run the Service Stats app
        """
        # Preamble
        service_message = '='*15 + ' SERVICE ' + '=' * \
            15 + '\n' + f'Service Stats Report ({datetime.now()})'
        print(service_message)

        boot_message = ServiceStats.serve_data(
            service_stats.Boot) if boot else ''
        cpu_message = ServiceStats.serve_data(
            service_stats.Cpu) if cpu else ''
        disk_message = ServiceStats.serve_data(
            service_stats.Disk) if disk else ''
        memory_message = ServiceStats.serve_data(
            service_stats.Memory) if memory else ''
        network_message = ServiceStats.serve_data(
            service_stats.Network) if network else ''
        system_message = ServiceStats.serve_data(
            service_stats.System) if system else ''

        final_message = (
            f'\n{service_message}'
            f'\n{boot_message}'
            f'\n{system_message}'
            f'\n{cpu_message}'
            f'\n{disk_message}'
            f'\n{memory_message}'
            f'\n{network_message}'
        )

        if slack:
            slack_output = service_stats.Slack.message(final_message)
            print(slack_output)

        return final_message


def main():
    ServiceCLI().run()


if __name__ == '__main__':
    main()
