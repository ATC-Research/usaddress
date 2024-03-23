from __future__ import print_function
from builtins import zip
from usaddress import parse
from parserator.training import readTrainingData
import pytest


def load_test_data(file_name, group_label):
    """
    Helper function to load test data from a file.
    """
    return list(readTrainingData([file_name], group_label))


def equals(addr, labels_pred, labels_true):
    """
    Asserts that predicted labels match the true labels.
    """
    pretty_print(addr, labels_pred, labels_true)
    assert labels_pred == labels_true


def fuzzy_equals(addr, labels_pred, labels_true):
    """
    Asserts that predicted labels match the true labels with some fuzziness.
    """
    labels = []
    fuzzy_labels = []
    for label in labels_pred:
        if label.startswith('StreetName'):
            fuzzy_labels.append('StreetName')
        elif label.startswith('AddressNumber'):
            fuzzy_labels.append('AddressNumber')
        elif label == ('Null'):
            fuzzy_labels.append('NotAddress')
        else:
            fuzzy_labels.append(label)
    for label in labels_true:
        labels.append(label)
    pretty_print(addr, fuzzy_labels, labels)
    assert fuzzy_labels == labels


def pretty_print(addr, predicted, true):
    """
    Prints the address, predicted labels, and true labels for debugging.
    """
    print("ADDRESS:    ", addr)
    print("PREDICTED:  ", predicted)
    print("TRUE:       ", true)


def prepare_test_data():
    test_cases = []
    datasets = [
        ('measure_performance/test_data/simple_address_patterns.xml', 'equals'),
        ('measure_performance/test_data/labeled.xml', 'equals'),
        ('measure_performance/test_data/synthetic_osm_data.xml', 'equals'),
        ('measure_performance/test_data/us50_test_tagged.xml', 'fuzzy_equals'),
    ]
    for test_file, test_function_id in datasets:
        data = list(readTrainingData([test_file], 'Label'))
        for labeled_address in data:
            address_text, components = labeled_address
            _, labels_true = list(zip(*components))
            _, labels_pred = list(zip(*parse(address_text)))
            test_cases.append((address_text, labels_pred, labels_true, test_function_id))
    return test_cases


test_data = prepare_test_data()


@pytest.mark.parametrize("address_text, labels_pred, labels_true, test_function_id", test_data)
def test_address_parsing(address_text, labels_pred, labels_true, test_function_id):
    if test_function_id == 'equals':
        equals(address_text, labels_pred, labels_true)
    elif test_function_id == 'fuzzy_equals':
        fuzzy_equals(address_text, labels_pred, labels_true)
