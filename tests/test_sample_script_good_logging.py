"""
It's a little funky to test the guts of the log setup like this, but in
production logs behavior is critical. A small mistake like a missed prefix in
simulate mode can cause user-facing impact when it changes log formats and
then a log monitor doesn't trigger and an operator doesn't get an alert.
"""

import logging

import pytest

from sample_scripts import good


@pytest.fixture(autouse=True)
def remove_simulator_filter():
    logger = logging.getLogger(good.__name__)
    for f in logger.filters:
        if isinstance(f, good.SimulatorFilter):
            logger.removeFilter(f)


def test_simulate_filter_applied_when_simulate_true():
    good.setup_logging('INFO', simulate=True)
    logger = logging.getLogger(good.__name__)
    simulator_filters = [f for f in logger.filters
                         if isinstance(f, good.SimulatorFilter)]
    assert len(simulator_filters) == 1


def test_simulate_filter_applied_when_simulate_false():
    good.setup_logging('INFO', simulate=False)
    logger = logging.getLogger(good.__name__)
    simulator_filters = [f for f in logger.filters
                         if isinstance(f, good.SimulatorFilter)]
    assert len(simulator_filters) == 1


def test_prefix_applied_to_log_records_when_simulate_true():
    good.setup_logging('INFO', simulate=True)
    logger = logging.getLogger(good.__name__)
    dummy_record = logging.LogRecord(name='dummy', level='INFO',
                                     pathname='dummy.py', lineno=0,
                                     msg='dummy', args=list(), exc_info=None)
    logger.filter(dummy_record)
    assert dummy_record.prefix.strip() == 'SIMULATE'


def test_empty_prefix_applied_to_log_records_when_simulate_false():
    good.setup_logging('INFO', simulate=False)
    logger = logging.getLogger(good.__name__)
    dummy_record = logging.LogRecord(name='dummy', level='INFO',
                                     pathname='dummy.py', lineno=0,
                                     msg='dummy', args=list(), exc_info=None)
    logger.filter(dummy_record)
    assert dummy_record.prefix == ''
