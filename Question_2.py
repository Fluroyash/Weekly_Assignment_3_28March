"""
### Title
**Automate Myntra Product Selection**

### Description
Open the Myntra website using Selenium WebDriver (https://www.myntra.com/).

Automate the process of navigating categories, selecting a product, applying filters, sorting products and adding to bag.

Perform the following steps:
- Launch the browser and open the Myntra website
- Maximize the browser window
- Hover over the **Genz** category
- Click on **"Jackets Under ₹899"**
- Select any 2 filter under the product filters (e.g., brand, size, or color)
- Click on the **Sort By** 'Popularity'
- Click on the any one product
- Select size (if mentioned)
- Add to bag
Use appropriate locator strategies such as **XPath / CSS Selectors** and implement **ActionChains** for hovering and clicking.

Students should ensure that:
- The website opens successfully
- The hover over the **Genz** category works correctly
- The correct subcategory is clicked
- Filters and sorting are applied successfully
- The specific product is selected and added to bag without errors

### Expected Outcome
- The browser launches and opens Myntra website
- Hovering over **Genz** displays the subcategory
- **Jackets Under ₹899** is clicked successfully
- 2 filter checkbox is selected
- Products are sorted according to the chosen option
- The specified product is clicked and displayed
- The product is added to bag
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
driver.get('https://www.myntra.com/') # Opening shopper stack website
driver.maximize_window() # Maximize the browser
actions = ActionChains(driver) #Creating object for action chains
ele=driver.find_element(By.XPATH,"(//div[@class='desktop-navContent'])[6]")#Creating an object for Genz button
actions.move_to_element(ele).pause(2).perform()#Hovering the Cursor over the button
driver.find_element(By.XPATH,"//a[text()='Jackets Under ₹899']").click()#Clicking on the Jacket Section
sleep(4)
driver.find_element(By.XPATH,"(//div[@class='common-checkboxIndicator'])[14]").click()#Clicking on the checkbox
sleep(4)
driver.find_element(By.XPATH,"(//div[@class='common-checkboxIndicator'])[20]").click()#Cliking on the second checkbox
sleep(4)
dropdown=driver.find_element(By.XPATH,"//div[@class='sort-sortBy']")#Creating a element for sortBy dropdown
actions.move_to_element(dropdown).perform()# Hovering on the dropdown
driver.find_element(By.XPATH,"(//label[@class='sort-label '])[3]").click()#Clicking on popularity
sleep(5)
driver.find_element(By.XPATH,"//a[@href='jackets/kashianxstyle/kashianxstyle-women-crop-denim-jacket/39201475/buy']").click()#Selecting the item
sleep(2)
driver.switch_to.window(driver.window_handles[1])#Switching the tab
driver.find_element(By.XPATH,"//button[@class='size-buttons-size-button size-buttons-size-button-default']").click()#Selecting the size
sleep(2)
driver.find_element(By.XPATH,"//div[text()='ADD TO BAG']").click()#Clicking on add to bag
sleep(5)
driver.quit()#Closing the browser