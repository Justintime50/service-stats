"""Import modules"""
# pylint: disable=R0903
import psutil
from .globals import Global


class Memory():
    """Memory (RAM) information"""
    @classmethod
    def serve(cls):
        """Serve memory info"""
        # Title
        memory_title = '='*15 + ' Memory Information ' + '='*15
        swap_title = '='*8 + ' SWAP ' + '='*8

        # Memory Information
        svmem = psutil.virtual_memory()
        memory_total = f'Total: {Global.get_size(svmem.total)}'
        memory_available = f'Available: {Global.get_size(svmem.available)}'
        memory_used = f'Used: {Global.get_size(svmem.used)}'
        memory_percentage = f'Percentage: {svmem.percent}%'

        # Get the swap memory details (if it exists)
        swap = psutil.swap_memory()
        swap_total = f'Total: {Global.get_size(swap.total)}'
        swap_free = f'Free: {Global.get_size(swap.free)}'
        swap_used = f'Used: {Global.get_size(swap.used)}'
        swap_percentage = f'Percentage: {swap.percent}%'

        final_message = '\n' + memory_title + '\n' + memory_total + '\n' + \
            memory_available + '\n' + memory_used + '\n' + \
            memory_percentage + '\n' + swap_title + '\n' + swap_total + \
            '\n' + swap_free + '\n' + swap_used + '\n' + swap_percentage
        return final_message
