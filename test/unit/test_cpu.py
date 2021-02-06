from service_stats import Cpu


def test_cpu_serve():
    result = Cpu.serve_data()
    assert 'CPU Information' in result
