from time import sleep

from behave import then, given
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "[aria-label='dark khaki selected'],[aria-label='black/gum'],[aria-label='stone/grey'],[aria-label='white/gum']")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")

@given("Open Target product {product_id} page")
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then ("Verify user can click through colors")
def verify_colors(context):
    expected_colors = ["dark khaki", 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        # print('current_color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, \
        f'expected {expected_colors} does not match actual {actual_colors}'