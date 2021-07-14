#!/usr/local/bin/python3

# Test Modules
import sys
import os

# Import module under test
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from bikit.utils import list_datasets, download_dataset


def test_list_datasets():
    res = list_datasets(verbose=False)
    keys = list(res.keys())
    assert len(keys) >= 3
    assert res[keys[0]]


def test_download_dataset():
    cache_dir = os.path.expanduser('~/.bikit-test')

    #download_dataset(name='demo_zip', cache_dir=cache_dir)
    download_dataset(name='demo_rar', cache_dir=cache_dir)
    assert os.path.exists(os.path.join(cache_dir, "rar_demo/demo_rar.rar"))
    assert os.path.exists(os.path.join(cache_dir, "rar_demo/multi_classifier_data"))

    print("===Done===")