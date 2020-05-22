# -*- coding: utf-8 -*-

import thriftpy2
thriftpy2.install_import_hook()

import const_thrift as const    # noqa


def test_num_const():
    assert const.NEGATIVE_I16 == -10
    assert const.NEGATIVE_DOUBLE == -123.456

    assert const.I16_CONST == 10
    assert const.I32_CONST == 100000
    assert const.DOUBLE_CONST == 123.456


def test_string_const():
    assert "hello" == const.DOUBLE_QUOTED_CONST
    assert "hello" == const.SINGLE_QUOTED_CONST


def test_const_with_sep():
    assert "hello" == const.CONST_WITH_SEP1
    assert "hello" == const.CONST_WITH_SEP2


def test_list_const():
    assert [1, 2, 3] == const.I32_LIST_CONST
    assert [1.1, 2.2, 3.3] == const.DOUBLE_LIST_CONST
    assert ["hello", "world"] == const.STRING_LIST_CONST

    assert [[1, 2, 3], [4, 5, 6]] == const.I32_LIST_LIST_CONST
    assert [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]] == const.DOUBLE_LIST_LIST_CONST
    assert [["hello", "world"], ["foo", "bar"]] == const.STRING_LIST_LIST_CONST
