import logging
import pathlib
import runpy

import pytest

logger = logging.getLogger(__name__)

all_scripts = pathlib.Path(__file__, "..", "..", "..", "examples", "user").resolve().glob("*.py")
scripts = (script for script in all_scripts if "async_" not in script.name)


def idfn(val):
    script_path = pathlib.Path(val)
    return script_path.name


@pytest.mark.integration
@pytest.mark.parametrize("script", scripts, ids=idfn)
def test_example_execution(script):
    logger.info(f"Executing Example scipt: {script}")
    runpy.run_path(str(script))
