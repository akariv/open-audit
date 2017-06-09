#!/usr/bin/env python

import json
import sys

from elasticsearch import Elasticsearch

INDEX_NAME = 'default'

if __name__ == '__main__':
    es = Elasticsearch()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            preface = json.loads(line)

            offices_to_defects = preface['offices_to_defects'].items()
            del preface['offices_to_defects']
            for office, defects in offices_to_defects:
                es.create(INDEX_NAME, doc_type='office',
                         body={
                             'preface_id': preface['id'],
                             'office': office,
                             'defects': defects,
                         })

            keywords_to_defects = preface['keywords_to_defects'].items()
            del preface['keywords_to_defects']
            for keyword, defects in keywords_to_defects:
                es.create(INDEX_NAME, doc_type='keyword',
                         body={
                             'preface_id': preface['id'],
                             'keyword': keyword,
                             'defects': defects,
                         })

            es.create(INDEX_NAME, doc_type='preface', body=preface)
