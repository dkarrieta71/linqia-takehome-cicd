import sys
from sample_app.__main__ import main


def test_main_success():
    assert main(["2", "3"]) == 0


def test_main_invalid_args():
    assert main(["not", "numbers"]) == 2


def test_main_wrong_arg_count():
    assert main(["1"]) == 2


def test_main_default_argv(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["script", "4", "5"])
    assert main() == 0
