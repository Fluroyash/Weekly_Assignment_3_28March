"""

### Title
**Automate Product Selection and Delivery Check on ShoppersStack**

### Description
Open the ShoppersStack website using Selenium WebDriver (https://www.shoppersstack.com/).

Automate the process of selecting a product category and verifying delivery availability using a pincode.

Perform the following steps:
- Launch the browser and open the ShoppersStack website
- Maximize the browser window
- Click on the **"APPLE"** product category
- Locate the delivery input field and enter the pincode
- Click on the **"Check"** button

Use appropriate locator strategies such as **XPath / ID / CSS Selectors** for identifying elements.
Implement synchronization using both **Implicit Wait** and **Explicit Wait**.

Students should ensure that:
- The website loads successfully
- The **APPLE** category is clicked correctly
- The pincode is entered in the delivery field
- Explicit wait is properly implemented
- The script runs without timing issues or exceptions
- Proper locator strategies are used

### Expected Outcome
- The browser launches and opens the ShoppersStack website
- The **APPLE** category page is displayed
- The pincode  is entered successfully
- The **Check** button is clicked after becoming clickable
- Delivery check process is triggered
- Script executes smoothly without errors
"""
from time import sleep #Importing libraries
from selenium.webdriver.common.action_chains import ActionChains #Importing libraries
from selenium.webdriver import Edge, EdgeOptions #Importing libraries
from selenium.webdriver.common.by import By #Importing libraries
a = EdgeOptions() #Connecting with the browser
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.implicitly_wait(100)
driver.get('https://www.shoppersstack.com/') # Opening shopper stack website
driver.maximize_window() # Maximize the browser

actions = ActionChains(driver) #Creating object for action chains
ele = driver.find_element(By.XPATH,'//img[@alt="iphone"]') # Creating a elemment for the Apple product
actions.scroll_to_element(ele).pause(2).click(ele).perform()  # scrolling and clicking the element
driver.find_element(By.XPATH,'//input[@id="Check Delivery"]').send_keys('302022') # Entering the pincode
sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()# Clicking on submit
sleep(2)
driver.quit()#Closing the browser





