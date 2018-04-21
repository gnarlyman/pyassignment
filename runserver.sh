#!/bin/bash
gunicorn crudapi.server:create_app --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker