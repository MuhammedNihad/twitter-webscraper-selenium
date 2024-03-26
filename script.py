from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = ""
password = ""
topic_name = input(" Please enter the topic name you want me to search for ")

driver = webdriver.Chrome()

driver.get("https://twitter.com/login")

wait = WebDriverWait(driver, 10)

username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="username"]')))
print("username entered")
username_input.send_keys(username)
username_input.send_keys(Keys.ENTER)

password_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
print("password entered")
time.sleep(3)
if "https://twitter.com/home" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")

print("searching tweets")

search_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')))
search_input.send_keys(topic_name)
search_input.send_keys(Keys.ENTER)

# Wait for the tweets to load


driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(6)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
# Wait for the like and engagement elements to load
like_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="like"]')))
engagement_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label*="views"]')))
tweets = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))
usernames = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="User-Name"]')))
hrefs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid=User-Name] a[role=link][href*=status]')))
print("getting tweets ...")
# Iterate over usernames and tweets and print them
for username, tweet,href_element, like_element, engagement_element in zip(usernames, tweets, like_elements, engagement_elements,hrefs):
    user_full_name = username.find_element(By.XPATH, '..').text.strip().rstrip('.')
    likes = like_element.text.split()[0] if like_element.text else "0"  # Extract the number of likes or default to 0 if not found
    engagement = engagement_element.text.split()[0] if engagement_element.text else "0"  # Extract the number of views or engagement or default to 0 if not found

    href=link = href_element.get_attribute('href')
    print(f'Username: {user_full_name}')
    print(f'Tweet: {tweet.text}')
    print(f'Likes: {likes}')
    print(f'Engagement: {engagement}')
    print("Link",href)
    print('---')
    time.sleep(5)

driver.quit()
