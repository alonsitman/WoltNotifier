from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(800,600) 

# Navigate to a web page
driver.get("https://wolt.com/en/isr/tel-aviv/restaurant/vitrina-ibn-gvirol")
# driver.get("https://wolt.com/en/isr/tel-aviv/restaurant/meat-night-bursa")


# Find an element by name attribute
# element = driver.find_element("xpath", "//div[@data-test-value='The restaurant is temporarily offline']")

result = None
elements = driver.find_elements(By.XPATH, "//*[@id='mainContent']/div/div[5]/div/div")

if not elements:
    result = 'Open'
elif "Scheduled" in elements[0].text:
    result = 'Closed'
elif "Temporarily" in elements[0].text:
    result = 'Temp'

print(f'Result: {result}')

# Close the browser
driver.quit()




############################################################################################3
# if not element.text:
#     #msg = 'Go ahead with your order'
#     print('Go ahead with your order')
# elif element.text == 'The venue is closed' or 'The restaurant is currently closed':
#     #msg = 'Restaurant is completely closed, order from somewhere else'
#     print('Restaurant is completely closed, order from somewhere else')
# else:
#     while element.text == 'The restaurant is temporarily offline':
#         #msg = "They seem to be busy, you'll be notified once they go back online"
#         print("They seem to be busy, you'll be notified once they go back online")
      