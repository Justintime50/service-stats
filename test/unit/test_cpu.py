from service.stats.cpu import Cpu


def test_cpu_serve():
    result = Cpu.serve()
    assert 'CPU Information' in result
