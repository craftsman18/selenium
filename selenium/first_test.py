from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/user/Desktop/clarusway/workspace/port folio/selenium/chromedriver")
base_url = "https://toyota.com"
expected_title = "New Cars, Trucks, SUVs & Hybrids | Toyota Official Site"
actual_title = ""
driver.get(base_url)
actual_title = driver.title
if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test failed")
    print(actual_title)
driver.close()