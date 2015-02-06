#!/usr/bin/python

from flask import Flask, request
from flask import jsonify

import argparse
import json
import requests


class Predictor(object):

    def __init__(self, pdb_host, path_prefix):
        self.pdb_host = pdb_host
        self.path_prefix = path_prefix

    def affected_nodes(self, change_set):
        changed_nodes = {}
        change_set = [self.path_prefix + f for f in change_set]
        url = "{pdb}/v3/resources".format(pdb=self.pdb_host)
        print change_set
        for f in change_set:
            body = {
                'limit': 9000001,
                'query': '["=", "file", "{f}"]'.format(f=f)
            }

            r = requests.get(url, params=body)
            changed_nodes[f] = list(set([node['certname'] for node in r.json()]))
        return changed_nodes


def main():
    parser = argparse.ArgumentParser(
        description="""
    A small web service to predict which Puppet nodes have pending changes
    based on a file change set.
    """
    )

    parser.add_argument('--puppetdb_host', type=str, default='http://localhost:8080')
    parser.add_argument('--bind_address', type=str, default='localhost')
    parser.add_argument('--path_prefix', type=str, default='/etc/puppetlabs/puppet/environments/production/')
    args = parser.parse_args()
    p = Predictor(args.puppetdb_host, )

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def predict_runs():
        print request.data
        return jsonify(**p.affected_nodes(json.loads(request.data)))
    app.debug = True
    app.run(host=args.bind_address)

if __name__ == '__main__':
    main()
