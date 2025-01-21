from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@when('I visit the "Home Page"')
def step_impl(context):
    context.browser.get(context.base_url)

@then('I should see "{text}" in the title')
def step_impl(context, text):
    assert text in context.browser.title

@then('I should not see "404 Not Found"')
def step_impl(context):
    assert "404 Not Found" not in context.browser.page_source

@when('I set the "{field_name}" to "{value}"')
def step_impl(context, field_name, value):
    field = context.browser.find_element(By.NAME, field_name)
    field.clear()
    field.send_keys(value)

@when('I select "{value}" in the "{field_name}" dropdown')
def step_impl(context, value, field_name):
    dropdown = context.browser.find_element(By.NAME, field_name)
    for option in dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text == value:
            option.click()
            break

@when('I press the "{button_name}" button')
def step_impl(context, button_name):
    button = context.browser.find_element(By.NAME, button_name)
    button.click()

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.browser.page_source

@when('I copy the "{field_name}" field')
def step_impl(context, field_name):
    field = context.browser.find_element(By.NAME, field_name)
    context.copied_value = field.get_attribute('value')

@when('I press the "Clear" button')
def step_impl(context):
    button = context.browser.find_element(By.NAME, 'clear')
    button.click()

@then('the "{field_name}" field should be empty')
def step_impl(context, field_name):
    field = context.browser.find_element(By.NAME, field_name)
    assert field.get_attribute('value') == ''

@when('I paste the "{field_name}" field')
def step_impl(context, field_name):
    field = context.browser.find_element(By.NAME, field_name)
    field.clear()
    field.send_keys(context.copied_value)

@then('I should see "{value}" in the "{field_name}" field')
def step_impl(context, value, field_name):
    field = context.browser.find_element(By.NAME, field_name)
    assert field.get_attribute('value') == value