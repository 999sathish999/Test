from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to chromedriver.exe
driver_path = "path_to_chromedriver.exe"

# Initialize Chrome driver
driver = webdriver.Chrome(driver_path)

# Go to "https://amazon.in"
driver.get("https://amazon.in")

# Search for "Wrist Watches"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Wrist Watches")

# Click on the search button
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

# Select "Analogue" from the display filter
display_filter = driver.find_element(By.XPATH, "//span[text()='Analogue']")
display_filter.click()

# Select "Leather" from the material filter
material_filter = driver.find_element(By.XPATH, "//span[text()='Leather']")
material_filter.click()

# Select "Titan" from the brand filter
brand_filter = driver.find_element(By.XPATH, "//span[text()='Titan']")
brand_filter.click()

# Select "25% Off or more" from the discount filter
discount_filter = driver.find_element(By.XPATH, "//span[text()='25% Off or more']")
discount_filter.click()

# Get the fifth element from the search
search_results = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
fifth_element = search_results[4].text

print(fifth_element)

# Close the browser
driver.quit()