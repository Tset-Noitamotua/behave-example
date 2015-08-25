# -*- coding: utf-8 -*-

from behave import given, when, then
from banking import Customer


@given('we have a new customer')
def step_impl(context):
    client_id = context.conf['client_id']
    client_name = context.conf['client_name']
    context.customer = Customer(client_id, client_name)


@given('we have {n} in the account')
def step_impl(context, n):
    context.account = context.customer.open_account()
    context.account.deposit(float(n))


@when('we add a new account')
def step_impl(context):
    context.account = context.customer.open_account()


@when('we deposit {n} to the account')
def step_impl(context, n):
    context.account.deposit(float(n))


@when('we withdraw {n} from the account')
def step_impl(context, n):
    try:
        context.account.withdraw(float(n))
    except Exception as ex:
        context.ex = ex


@when('we close the account')
def step_impl(context):
    try:
        context.account.close()
    except Exception as ex:
        context.ex = ex


@then('the account should be closed')
def step_impl(context):
    assert context.account.state == 'Closed',\
           'Actual: ' + context.account.state


@then('the customer should have {n} accounts')
def step_impl(context, n):
    assert len(context.customer.accounts) == int(n)


@then('the account should have {n} balance')
def step_impl(context, n):
    assert context.account.balance == float(n),\
           "Expected: {0}, actual: {1}.".format(n, context.account.balance)


@then('the {operation} should fail with {message}')
def step_impl(context, operation, message):
    message = message.strip('"')
    assert context.ex is not None
    assert context.ex.message == message
