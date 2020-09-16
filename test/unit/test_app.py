from service.app import Service
from service.stats.boot_time import Boot


def test_serve_data():
    result = Service.serve_data(Boot)
    assert 'Boot Time' in result


def test_app():
    result = Service.run(boot=True, cpu=True, disk=True,
                         memory=True, network=True, system=True)
    assert 'SERVICE' in result
    assert 'Boot Time' in result
    assert 'CPU Info' in result
    assert 'Disk Information' in result
    assert 'Memory Information' in result
    assert 'Network Information' in result
    assert 'System Information' in result
    # TODO: Assert/test Slack message printed
