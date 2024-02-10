from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 
from bs4 import BeautifulSoup


driver = webdriver.Chrome()


driver.get("https://app.schoology.com/login")




assert "Schoology" in driver.title


sso_button = driver.find_element(By.CLASS_NAME,"sso-login-link")
ActionChains(driver).move_to_element(sso_button).click(sso_button).perform()

school_entry = driver.find_element(By.ID,"edit-school")
school_entry.send_keys("Rocklin High School")

time.sleep(1.5)
school_selector = driver.find_element(By.XPATH, "/html/body/div[2]/ul/li[1]/div[1]/strong")

school_selector.click()

#school_entry.send_keys(Keys.TAB)
school_entry.send_keys(Keys.ENTER)

time.sleep(2)



#driver_1 = webdriver.Chrome()
#driver_1.get("https://accounts.google.com/v3/signin/identifier?opparams=%253Fsuppress_webview_warning%253Dtrue&dsh=S2046830729%3A1707519578406154&client_id=138513641593.apps.googleusercontent.com&o2v=1&prompt=select_account&redirect_uri=https%3A%2F%2Fapp.schoology.com%2Flogin%2Fexternal_accounts%2Freceive%2Fgoogle_apps&response_type=code&scope=openid+email&service=lso&state=c2NoZW1lPWh0dHBzJmhvc3Q9c2Nob29sb2d5LnJvY2tsaW51c2Qub3JnJnBhdGg9JTJGbG9naW4lMkZleHRlcm5hbF9hY2NvdW50cyUyRnJlY2VpdmUlMkZnb29nbGVfYXBwcyZxdWVyeT1zY2hvb2xfbmlkJTNENDczMDEzMjEmc2Nob29sX25pZD00NzMwMTMyMSZzX2N1c3RvbV9kb21haW49aHR0cHMlM0ElMkYlMkZzY2hvb2xvZ3kucm9ja2xpbnVzZC5vcmcmZGVzdGluYXRpb249bG9naW4lMkZleHRlcm5hbF9hY2NvdW50cyUyRnNlbmQlMkZnb29nbGVfYXBwcyUzRnNjaG9vbF9uaWQlM0Q0NzMwMTMyMSZ0cz0xNzA3NTE5NTc4JnRva2VuPVo1QzVNT0RDMlJJS0tVWkVCMjc3MkUxMUJFMTk2NUIxOUEwRDU4QzcxNDhFM0FBRiZoYXNoPTUwY2ZhZDgzNDg2YWYyYjliZmY0NWM3OWIzNjgxMGIz&theme=glif&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAMGiOTyGHsbqpTPUJrnxwMHOWwb_4e-bsmhpXgQCE-GuxPf6EGLWu-XxgUR7Gk7CdVmaGOmLIMnSNtX4zPuf0GTbOn77fL7bKP1FoMLDezJor_Fm62d4CkvuBf_fuvTHzbGyANEr8w-KzfPlpv9CFPcgBSdq-SnEyHqjIBLrMTewJJxCaZQTto4AGAOfRU7X9t21rGAvPS2Ey1c7EUavROSV61DVmkSULQkAY7Zij7GpGjPciMN9V6QCpOeWuV0sEHixYx8Z91SyFOFxctfMPhnIjuTwF10MlCEs4EG7migwilBE6IRg9fEzN6UPPJ3Djr4U5ShY-c-gXbzzP5ky2b-1n5uLnEUuoNaD9KPWBZ1Xep85aIDYtthEri59TcX5zpxILpOThd5zIl90hFMbU5rh_v8hPmTkB-imqd9UO73vNz8S4Y%26as%3DS2046830729%253A1707519578406154%26client_id%3D138513641593.apps.googleusercontent.com%26theme%3Dglif%23&app_domain=https%3A%2F%2Fapp.schoology.com&rart=ANgoxcdbwdN_s_U-aAlqugFNVLjpHf_9cPvuA1v2QDS45XlewcFHCpVAuz57itqMXmCRZBMCRSRbmEEhEeu9Sg1nK6f3vv5IbTI9fBvc8bbe_18jgH5mcGk")


google_login = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
google_login.send_keys("john.malak@rocklinusd.org")

google_enter = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div")
google_enter.click()


time.sleep(2)
google_password = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
google_password.send_keys("Aim57575*")


time.sleep(2)
google_enter_password = driver.find_element(By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button")
google_enter_password.click()




time.sleep(10000)








