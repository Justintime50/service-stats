<div align="center">

# Service

Service serves savvy server stats. Talk about alliteration!

[![Build Status](https://travis-ci.com/Justintime50/service.svg?branch=master)](https://travis-ci.com/Justintime50/service)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

Service provides data about boot time, CPU usage, disk usage, memory usage, network usage, and system information. You can send all this right to Slack. Great for a daily/weekly server snapshot of what's going on. Build custom logic to warn you about high CPU/memory usage or low available disk space.

## Install

```bash
pip3 install -r requirements.txt
cp .env.example .env
```

## Usage

Grab all server data and send it to Slack.

```bash
python3 app.py
```

## Cron

```bash
crontab -e

0 9 * * 1 /usr/local/bin/python3 /Users/admin/Sites/service/app.py
```

## Attribution

Based on [this article](https://www.thepythoncode.com/article/get-hardware-system-information-python).
