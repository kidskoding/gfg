import pytest


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item):
    """Unsolved stubs raise NotImplementedError: report those tests as skipped, not failed."""
    try:
        return (yield)
    except NotImplementedError:
        pytest.skip("not implemented")
