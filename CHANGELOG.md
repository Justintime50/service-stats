# CHANGELOG

## v1.2.1 (2020-11-16)

* Swapping `None` for empty strings on those items that aren't present in reports, otherwise it'll literally print `None` when we don't want anything printed

## v1.2.0 (2020-11-03)

* Fixed a bug where variables were not being referenced properly and the app could not be run
* Made package importable with `__init__.py` file
* Added unit tests for Slack

## v1.1.0 (2020-09-15)

* Added unit tests and test coverage
* Various code refactor and cleanup
* Updated documentation
* Added a Makefile
* Automated releasing via Travis

## v1.0.2 (2020-06-21)

* Travis fixes
* Fixed a bug where only a single disk data was read instead of all of them

## v1.0.1 (2020-06-21)

* Fixed Slack message to contain null values for system data not selected
* Added CHANGELOG

## v1.0.0 (2020-06-11)

* Added command line arguments to enable/disable which system info to display
* Returned data in addition to printing it so it could be used however you'd need
* Added `setup.py` and created an executable file
* Published to Pypi

## v0.0.1 (2020-05-29)

* Initial version printing all system data to console
