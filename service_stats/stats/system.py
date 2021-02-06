import platform


class System():
    @staticmethod
    def serve_data():
        """Serve system info
        """
        # Title
        system_title = '='*15 + ' System Information ' + '='*15

        # System info
        uname = platform.uname()
        system_name = f'System: {uname.system}'
        node_name = f'Node Name: {uname.node}'
        release = f'Release: {uname.release}'
        version = f'Version: {uname.version}'
        machine = f'Machine: {uname.machine}'
        processor = f'Processor: {uname.processor}'

        final_message = (
            '\n' + system_title +
            '\n' + system_name +
            '\n' + node_name +
            '\n' + release +
            '\n' + version +
            '\n' + machine +
            '\n' + processor
        )
        return final_message
