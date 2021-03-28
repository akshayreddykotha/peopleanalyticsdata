import pytest, pandas
from peopleanalyticsdata.peopleanalyticsdata import charity_donation

def test_type_of_output():
#     assert type(charity_donation()) == '<class 'pandas.core.frame.DataFrame'>'
    assert charity_donation().shape[1] == 8