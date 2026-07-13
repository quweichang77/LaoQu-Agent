"""Smoke tests for the independent project skeleton."""

from laoqu_agent import __version__
from laoqu_agent.config import Settings
from laoqu_agent.main import main


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_settings_defaults() -> None:
    s = Settings.from_env()
    assert s.app_name
    assert s.app_env


def test_main_runs(capsys) -> None:
    main()
    out = capsys.readouterr().out
    assert "LaoQu-Agent" in out
