import pytest
import shutil
from pathlib import Path

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    allure_results_dir = Path(session.config.getoption("--alluredir"))
    if allure_results_dir.exists() and allure_results_dir.is_dir():
        shutil.copy("executor.json", allure_results_dir / "executor.json")
