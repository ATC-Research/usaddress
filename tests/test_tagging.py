from collections import OrderedDict

import usaddress


def test_broadway():
    s1 = '1775 Broadway And 57th, Newyork NY'
    assert usaddress.tag(s1)[0] == OrderedDict(
        [('AddressNumber', '1775'), ('StreetName', 'Broadway And 57th'), ('PlaceName', 'Newyork'), ('StateName', 'NY')])
