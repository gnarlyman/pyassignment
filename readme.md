# Crowdstrike Python Assignment Server

### Description
This is a CRUD server implemented in python using aiohttp.

The server uses an in-memory dictionary to remember GUID's submitted
via the rest api.

### Usage
1. `sh runserver.sh`
2. `python runclient.py`
3. browse to http://localhost:8080/guid to see a list of guids