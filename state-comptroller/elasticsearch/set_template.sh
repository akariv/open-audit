#!/bin/sh
curl -sSXPUT localhost:9200/_template/default?pretty --data @template.json
