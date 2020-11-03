import mock
from service.app import Service
from service.stats.boot_time import Boot


def test_serve_data():
    result = Service.serve_data(Boot)
    assert 'Boot Time' in result


@mock.patch('service.slack.Slack.message')
def test_app_slack(mock_slack):
    result = Service.run(boot=True, cpu=True, disk=True,
                         memory=True, network=True, system=True, slack=True)
    assert 'SERVICE' in result
    assert 'Boot Time' in result
    assert 'CPU Info' in result
    assert 'Disk Information' in result
    assert 'Memory Information' in result
    assert 'Network Information' in result
    assert 'System Information' in result
    mock_slack.assert_called_once()


@mock.patch('service.slack.Slack.message')
def test_app_no_slack(mock_slack):
    result = Service.run(boot=True, cpu=True, disk=True,
                         memory=True, network=True, system=True, slack=False)
    assert 'SERVICE' in result
    assert 'Boot Time' in result
    assert 'CPU Info' in result
    assert 'Disk Information' in result
    assert 'Memory Information' in result
    assert 'Network Information' in result
    assert 'System Information' in result
    mock_slack.assert_not_called()
