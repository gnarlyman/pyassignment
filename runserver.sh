#!/bin/bash
gunicorn crudapi.server:web_app --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker