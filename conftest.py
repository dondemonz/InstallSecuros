import pytest
a = "test"



@pytest.fixture
def fix(request):
    fixture = a
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture


