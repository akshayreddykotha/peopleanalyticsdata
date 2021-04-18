import pytest, pandas
from peopleanalyticsdata.peopleanalyticsdata import charity_donation, employee_survey, health_insurance, job_retention, managers, politics_survey, salespeople, soccer, sociological_data, speed_dating, ugtests

def test_shape_of_output():
#     assert type(charity_donation()) == '<class 'pandas.core.frame.DataFrame'>'
    assert charity_donation().shape[1] == 8
    assert employee_survey().shape[1] == 14
    assert health_insurance().shape[1] == 6
    assert job_retention().shape[1] == 7
    assert managers().shape[1] == 13
    assert politics_survey().shape[1] == 23
    assert salespeople().shape[1] == 4
    assert soccer().shape[1] == 7
    assert sociological_data().shape[1] == 9
    assert speed_dating().shape[1] == 11
    assert ugtests().shape[1] == 4