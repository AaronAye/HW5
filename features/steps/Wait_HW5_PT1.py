from time import sleep
from behave import then, when
from selenium.webdriver.common.by import By

@when("Enter search for item {search_text}")
def search_for_item(context, search_text):
    # Find the search input field and send keys
    context.driver.find_element(By.ID, 'search').send_keys(search_text)
    sleep(2)  # Adding sleep instead of explicit wait

    # Find and click the search button
    search_button = context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
    search_button.click()
    sleep(5)  # Adding sleep to wait for the search results to load


@when("Add item to cart")
def target_add_to_cart(context):
    # Wait for the add to cart button to be present and click it
    sleep(5)  # Adding sleep instead of explicit wait
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor16849682']")
    add_to_cart_button.click()
    sleep(5)  # Adding sleep to wait for the shipping option button to be clickable

    # Wait for the shipping option button to be present and click it
    shipping_option_button = context.driver.find_element(By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
    shipping_option_button.click()
    sleep(3)  # Adding sleep to wait for the shipping confirmation button to be clickable

    # Wait for the shipping confirmation button to be present and click it
    shipping_confirmation_button = context.driver.find_element(By.XPATH, "//button[@data-test='shippingButton']")
    shipping_confirmation_button.click()
    sleep(3)  # Adding sleep to wait for the view cart link to be clickable

    # Wait for the view cart link to be present and click it
    view_cart_link = context.driver.find_element(By.XPATH, "//a[contains(text(),'View cart')]")
    view_cart_link.click()
    sleep(5)  # Adding sleep to wait for the cart page to load


@then("Verify search item in cart")
def item_in_cart(context):
    sleep(5)  # Adding sleep to wait for the element to be present
    actual_text_element = context.driver.find_element(By.XPATH, "//div[contains(text(),'Lavazza Classico Medium Roast Ground Coffee - 12oz')]")
    actual_text = actual_text_element.text
    assert 'Lavazza Classico Medium Roast Ground Coffee - 12oz' in actual_text, f'{actual_text} is NOT in cart'
    print("Test case has passed")