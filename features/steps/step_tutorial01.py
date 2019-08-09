from behave import *
import unittest
from actionwords import Actionwords

use_step_matcher('re')

@given('we have behave installed')
def step_impl(context):
    context.actionwords.we_have_behave_installed()

@when('we implement a test')
def step_impl(context):
    context.actionwords.we_implement_a_test()

@then('trial will test it for us!')
def step_impl(context):
    context.actionwords.trial_will_test_it_for_us()