# -*- coding: utf-8 -*-
from usaddress import token_features


def test_unicode():
    features = token_features(u'å')
    assert features['endsinpunc'] is False
