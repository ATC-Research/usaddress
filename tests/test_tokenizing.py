from usaddress import tokenize


def test_hash():
    assert tokenize('# 1 abc st') == ['#', '1', 'abc', 'st']
    assert tokenize('#1 abc st') == ['#', '1', 'abc', 'st']
    assert tokenize('box # 1 abc st') == ['box', '#', '1', 'abc', 'st']
    assert tokenize('box #1 abc st') == ['box', '#', '1', 'abc', 'st']
    assert tokenize('box# 1 abc st') == ['box', '#', '1', 'abc', 'st']
    assert tokenize('box#1 abc st') == ['box', '#', '1', 'abc', 'st']


def test_split_on_punc():
    assert tokenize('1 abc st,suite 1') == ['1', 'abc', 'st,', 'suite', '1']
    assert tokenize('1 abc st;suite 1') == ['1', 'abc', 'st;', 'suite', '1']
    assert tokenize('1-5 abc road') == ['1-5', 'abc', 'road']


def test_spaces():
    assert tokenize('1 abc st') == ['1', 'abc', 'st']
    assert tokenize('1  abc st') == ['1', 'abc', 'st']
    assert tokenize('1 abc st ') == ['1', 'abc', 'st']
    assert tokenize(' 1 abc st') == ['1', 'abc', 'st']


def test_capture_punc():
    assert tokenize('222 W. Merchandise Mart Plaza') == ['222', 'W.', 'Merchandise', 'Mart', 'Plaza']
    assert tokenize('222 W Merchandise Mart Plaza, Chicago, IL') == ['222', 'W', 'Merchandise', 'Mart', 'Plaza,',
                                                                     'Chicago,', 'IL']
    assert tokenize('123 Monroe- St') == ['123', 'Monroe-', 'St']


def test_nums():
    assert tokenize('222 W Merchandise Mart Plaza Chicago IL 60654') == ['222', 'W', 'Merchandise', 'Mart', 'Plaza',
                                                                         'Chicago', 'IL', '60654']


def test_ampersand():
    assert tokenize('123 & 456') == ['123', '&', '456']
    assert tokenize('123&456') == ['123', '&', '456']
    assert tokenize('123& 456') == ['123', '&', '456']
    assert tokenize('123 &456') == ['123', '&', '456']
    assert tokenize('123 &#38; 456') == ['123', '&', '456']
    assert tokenize('123&#38;456') == ['123', '&', '456']
    assert tokenize('123&#38; 456') == ['123', '&', '456']
    assert tokenize('123 &#38;456') == ['123', '&', '456']
    assert tokenize('123 &amp; 456') == ['123', '&', '456']
    assert tokenize('123&amp;456') == ['123', '&', '456']
    assert tokenize('123&amp; 456') == ['123', '&', '456']
    assert tokenize('123 &amp;456') == ['123', '&', '456']


def test_paren():
    assert tokenize('222 W Merchandise Mart Plaza (1871) Chicago IL 60654') == ['222', 'W', 'Merchandise', 'Mart',
                                                                                'Plaza', '(1871)', 'Chicago', 'IL',
                                                                                '60654']
    assert tokenize('222 W Merchandise Mart Plaza (1871), Chicago IL 60654') == ['222', 'W', 'Merchandise', 'Mart',
                                                                                 'Plaza', '(1871),', 'Chicago', 'IL',
                                                                                 '60654']
    assert tokenize('222 W Merchandise Mart Plaza(1871) Chicago IL 60654') == ['222', 'W', 'Merchandise', 'Mart',
                                                                               'Plaza', '(1871)', 'Chicago', 'IL',
                                                                               '60654']
