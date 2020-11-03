from datetime import datetime
import argparse
from service import (
    Boot,
    Cpu,
    Disk,
    Memory,
    Network,
    System,
    Slack,
)


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
            help='Send Service report to Slack.'
        )
        parser.parse_args(namespace=self)

    def run(self):
        Service.run(
            boot=self.boot,
            cpu=self.cpu,
            disk=self.disk,
            memory=self.memory,
            network=self.network,
            system=self.system,
            slack=self.slack,
        )


class Service():
    @classmethod
    def serve_data(cls, data_type):
        """Serve data from the specified category
        """
        data = data_type.serve()
        print(data)
        return data

    @classmethod
    def run(cls, boot=True, cpu=False, disk=False, memory=False,
            network=False, system=False, slack=False):
        """Run the Service app
        """
        # Preamble
        service_message = '='*15 + ' SERVICE ' + '=' * \
            15 + '\n' + f'Service Report ({datetime.now()})'
        print(service_message)

        boot_message = cls.serve_data(Boot) if boot else None
        cpu_message = cls.serve_data(Cpu) if cpu else None
        disk_message = cls.serve_data(Disk) if disk else None
        memory_message = cls.serve_data(Memory) if memory else None
        network_message = cls.serve_data(Network) if network else None
        system_message = cls.serve_data(System) if system else None

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
            slack_output = Slack.message(final_message)
            print(slack_output)

        return final_message


def main():
    ServiceCLI().run()


if __name__ == '__main__':
    main()
