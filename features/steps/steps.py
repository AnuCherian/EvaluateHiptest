from behave import *

# This should be added to environment.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords()

@then(r'trial will test it for us!')
def impl(context):
    context.actionwords.trial_will_test_it_for_us()


@given(r'we have behave installed')
def impl(context):
    context.actionwords.we_have_behave_installed()


@then(r'the ninja should "{reaction}"')
def impl(context, reaction = ""):
    context.actionwords.the_ninja_should(reaction)


@given(r'the ninja has a "{achievement_level}"')
def impl(context, achievement_level):
    print("achievement_level:",achievement_level)
    context.actionwords.the_ninja_has_a(achievement_level)


@when(r'we implement a test')
def impl(context):
    context.actionwords.we_implement_a_test()


@when(r'attacked by  "{opponent_role}"')
def impl(context, opponent_role):
    context.actionwords.attacked_by(opponent_role)
