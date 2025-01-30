from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# ✅ Open IRCTC Website
driver.get("https://www.irctc.co.in/nget/train-search")

# ✅ Wait for the page to fully load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# ✅ Click the "Login" button (Top Right)
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'LOGIN')]"))
)
login_button.click()

# ✅ Wait for the Login Modal to Appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='userid']"))
)

# ✅ Find the Username and Password Fields
username = driver.find_element(By.XPATH, "//input[@formcontrolname='userid']")
password = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")

# ✅ Enter Username and Password
username.send_keys("jithuldevaraj01")  # Replace with your actual IRCTC username
password.send_keys("Aa.jgdw2@")  # Replace with your actual IRCTC password

# ✅ Handle CAPTCHA Manually (Wait for User Input)
input("Solve CAPTCHA and press Enter to continue...")

# ✅ Click the "Sign In" Button
sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'SIGN IN')]")
sign_in_button.click()

# ✅ Wait for Login Confirmation (Check for Profile Icon or Greeting)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Hi')]"))  # Adjust based on actual text
    )
    print("Login successful!")
except:
    print("Login might have failed. Check credentials or CAPTCHA.")

# ✅ Continue with booking or close browser
# driver.quit()