# -*- coding: utf-8 -*-
from usaddress import token_to_features


def test_unicode():
    features = token_to_features(u'å')
    assert features['endsinpunc'] is False
