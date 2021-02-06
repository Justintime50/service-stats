import mock
from service_stats import Boot, ServiceStats


def test_serve_data():
    result = ServiceStats.serve_data(Boot)
    assert 'Boot Time' in result


@mock.patch('service_stats.slack.Slack.message')
def test_app_slack(mock_slack):
    result = ServiceStats.run(boot=True, cpu=True, disk=True,
                              memory=True, network=True, system=True, slack=True)
    assert 'SERVICE' in result
    assert 'Boot Time' in result
    assert 'CPU Info' in result
    assert 'Disk Information' in result
    assert 'Memory Information' in result
    assert 'Network Information' in result
    assert 'System Information' in result
    mock_slack.assert_called_once()


@mock.patch('service_stats.slack.Slack.message')
def test_app_no_slack(mock_slack):
    result = ServiceStats.run(boot=True, cpu=True, disk=True,
                              memory=True, network=True, system=True, slack=False)
    assert 'SERVICE' in result
    assert 'Boot Time' in result
    assert 'CPU Info' in result
    assert 'Disk Information' in result
    assert 'Memory Information' in result
    assert 'Network Information' in result
    assert 'System Information' in result
    mock_slack.assert_not_called()
