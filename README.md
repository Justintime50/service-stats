<div align="center">

# Service

Service serves savvy server stats.

[![Build Status](https://travis-ci.com/Justintime50/service.svg?branch=master)](https://travis-ci.com/Justintime50/service)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png" alt="Showcase">

</div>

Service is completely configurable, allowing you to request data about boot time, CPU usage, disk usage, memory usage, network usage, and system information. You can send all this right to Slack. Great for a daily/weekly server snapshot of what's going on. Build custom logic to warn you about high CPU/memory usage or low available disk space.

## Install

```bash
# Install Service
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
    service --boot --cpu --disk --memory --network --system --slack

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

## Cron

```bash
crontab -e

0 9 * * 1 service --boot --cpu --disk --memory --network --system --slack
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run the scripts locally
venv/bin/python service/app.py --help
```

## Attribution

Based on [this article](https://www.thepythoncode.com/article/get-hardware-system-information-python).
