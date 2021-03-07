import pytest
from peopleanalyticsdata.peopleanalyticsdata import charity_donation

def test_type_of_output():
    assert type(charity_donation()) == 'pandas.core.frame.DataFrame'