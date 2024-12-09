from behave import given, step, then, when
import selenium
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

@given (u'I open the url "{url}"')
def step_impl(context, url):
    context.behave_driver.open_url(url)

@given(u'I enter the method as {method}')
def step_impl(context, method):
    select = Select(context.behave_driver.find_element_by_id('decoder-setting'))
    
    select.select_by_value(method)
        
@given(u'I enter the Caesar shift as {caesar_shift}')
def step_impl(context, caesar_shift):
    select = Select(context.behave_driver.find_element_by_id('shift-amount'))
    
    select.select_by_value(caesar_shift)
    
@given(u'I enter the message {message}')
def step_impl(context, message):
    text_input = context.behave_driver.find_element_by_id('letters')
    text_input.clear()
    text_input.send_keys(message)
    
@when(u'I click the Translate Button')
def step_impl(context):
    translate_button = context.behave_driver.find_element_by_id('submit')
    translate_button.click()
    
@then(u'I should see the message {message}')
def step_impl(context, message):
    context.behave_driver.pause(1000)
    
    decoded_text_div = context.behave_driver.find_element_by_id('decoded_message')
    p_tag_in_div = decoded_text_div.find_element_by_tag_name('p')
    print("text", p_tag_in_div)
    print("message", message)
    
@then(u'I should see the decoded message {message}')
def step_impl(context, message):
    context.behave_driver.pause(1000)
    
    decoded_text_div = context.behave_driver.find_element_by_id('suggested_solution')
    p_tag_in_div = decoded_text_div.find_element_by_tag_name('p')
    print("text", p_tag_in_div)
    print("message", message)