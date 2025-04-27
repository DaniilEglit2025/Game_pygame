import psutil
import pytest
import os
from pathlib import Path
def test_check_folders():
    assert os.path.exists("easy_bot_assets")
    assert os.path.exists("hard_bot_assets")
    assert os.path.exists("player")

def test_check_count():
    assert len(os.listdir("easy_bot_assets")) == 11
    assert len(os.listdir("hard_bot_assets")) == 10
    assert len(os.listdir("player")) == 3

def test_png():
    for filename in os.listdir("easy_bot_assets"):
        assert filename.endswith(".png")

    for filename in os.listdir("hard_bot_assets"):
        assert filename.endswith(".png")

    for filename in os.listdir("player"):
        assert filename.endswith(".png")


def test_cpu_count():
    assert os.cpu_count() >= 2

def test_memory():
    memory = psutil.virtual_memory()
    available_memory = memory.available
    available_memory_gb = available_memory / (1024 * 1024 * 1024)
    assert available_memory_gb >= 1.5