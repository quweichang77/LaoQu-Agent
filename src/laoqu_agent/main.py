"""CLI entrypoint for LaoQu-Agent."""

from __future__ import annotations

from laoqu_agent import __version__
from laoqu_agent.config import settings


def main() -> None:
    print(f"{settings.app_name} v{__version__}")
    print(f"env={settings.app_env} log_level={settings.log_level}")
    print("Ready. This is a clean independent project skeleton.")


if __name__ == "__main__":
    main()
