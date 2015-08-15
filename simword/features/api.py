# -*- coding: utf-8 -*-
import json

from django.test import Client
from lettuce import (step, world)


@step(u'I make (.*) request to (.*)')
def make_request(step, method, url):
    client = Client()
    request_method = getattr(client, method.lower())
    get_params_dict = getattr(world, 'get_params', {})
    world.response = request_method(url, get_params_dict, follow=True)
    world.response_dict = json.loads(world.response.content)


@step(u'I should get list results with following keys')
def check_response_keys(step):
    for res in world.response_dict:
        for item in step.hashes:
            assert item['keys'] in res.keys(), 'Key: %s not in %s' % (item['keys'], res.keys())


@step(u'I should get detail results with following keys')
def check_response_keys(step):
    for item in step.hashes:
        assert item['keys'] in world.response_dict.keys(), 'Key: %s not in %s' % (item['keys'],
                                                                                  world.response_dict.keys())
