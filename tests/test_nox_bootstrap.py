#!/usr/bin/env python

"""Tests for `nox_bootstrap` package."""

import pytest


@pytest.fixture
def response():
    return 1, 2


def a_function(a, b):
    return a, b


def test_a_function(response):
    a, b = response
    assert a_function(a, b) == (a, b)
