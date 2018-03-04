def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)