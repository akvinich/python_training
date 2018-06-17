import pytest
from app.application import Application

from .data_providers import valid_customers


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


@pytest.mark.parametrize("customer", valid_customers)
def test_customer_can_request(app, customer):
    app.request_new_project(customer)

