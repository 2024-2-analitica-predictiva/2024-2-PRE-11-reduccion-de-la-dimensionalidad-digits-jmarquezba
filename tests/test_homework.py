"""Autograding script"""

import os


def test_01():
    """Check if the files are present"""
    assert os.path.exists("digits_pca.png")
    assert os.path.exists("digits_tsne.png")
    assert os.path.exists("digits_umap.png")