"""Import modules"""
# pylint: disable=R0903
import psutil
from .globals import Global


class Memory():
    """Memory (RAM) information"""
    @classmethod
    def serve(cls):
        """Serve memory info"""
        # Memory Information
        print("="*40, "Memory Information", "="*40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {Global.get_size(svmem.total)}")
        print(f"Available: {Global.get_size(svmem.available)}")
        print(f"Used: {Global.get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {Global.get_size(swap.total)}")
        print(f"Free: {Global.get_size(swap.free)}")
        print(f"Used: {Global.get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")
