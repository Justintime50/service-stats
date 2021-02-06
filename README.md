<div align="center">

# Service Stats

Service serves savvy server stats.

[![Build Status](https://github.com/Justintime50/service-stats/workflows/build/badge.svg)](https://github.com/Justintime50/service-stats/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/service-stats/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/service-stats?branch=main)
[![PyPi](https://img.shields.io/pypi/v/service-stats)](https://pypi.org/project/service-stats/)
[![Licence](https://img.shields.io/github/license/justintime50/service-stats)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

Service Stats is completely configurable, allowing you to request data about boot time, CPU usage, disk usage, memory usage, network usage, and system information. You can send all this right to Slack. Great for a daily/weekly server snapshot of what's going on. Build custom logic to warn you about high CPU/memory usage or low available disk space.

## Install

```bash
# Install Service Stats
pip3 install service-stats

# Install locally
make install

# Setup Slack ENV variables (optional)
cp .env.example .env

# Get Makefile help
make help
```

## Usage

Grab all server data and send it to Slack.

```
Usage:
    service-stats --boot --cpu --disk --memory --network --system --slack

Options:
    -h, --help     show this help message and exit
    -b, --boot     Show boot time stats.
    -c, --cpu      Show CPU stats.
    -d, --disk     Show disk stats.
    -m, --memory   Show memory stats.
    -n, --network  Show network stats.
    -s, --system   Show system stats.
    -sl, --slack   Send Service report to Slack.

Environment Variables (optional):
    SLACK_BOT_TOKEN     The Slackbot token to use for authentication
    SLACK_CHANNEL       The channel to post a message to
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage

# Run the scripts locally
venv/bin/python service_stats/app.py --help
```

## Attribution

Based on [this article](https://www.thepythoncode.com/article/get-hardware-system-information-python).
