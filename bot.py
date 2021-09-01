# Import the packages we need
import random
from time import sleep

from pynput.keyboard import Controller, Key
from selenium import webdriver

# Declare keyboard as Controller to control keys
keyboard = Controller()

# Driver
driver = webdriver.Firefox()

# Get to omegle and sleep
driver.get("https://www.omegle.com")
sleep(3)

# Click on text button
text_button = driver.find_element_by_xpath('//*[@id="textbtn"]')
text_button.click()

# Agree to terms of service
driver.find_element_by_xpath('/html/body/div[7]/div/p[1]/label/input').click()
driver.find_element_by_xpath('/html/body/div[7]/div/p[2]/label/input').click()
driver.find_element_by_xpath('/html/body/div[7]/div/p[3]/input').click()

# Declare the messages list in our messages.txt file
f = open("messages.txt")
messages = f.read().splitlines()

# Declare the random sleep delay
rdm_sleep = random.randint(5, 11)
# Make a while looop to make our program run forever
while True:
    # Make a try except to avoid our program to crash
    try:

        def send_message(message, messagebox):
            messagebox.send_keys(message)
            sleep(rdm_sleep)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)


        # Declare the Stop button to disconnect us
        stop_button = driver.find_element_by_css_selector('.disconnectbtn')
        # Press 3x the stop button to find a new user
        for x in messages:
            sleep(1)
            message_box = driver.find_element_by_class_name('chatmsg ')
            if x == "THE LAST BOT":
                for i in range(3):
                    sleep(0.4)
                    stop_button.click()
            else:
                send_message(x, message_box)


    except:
        print("User disconnected before us")
        stop_button = driver.find_element_by_css_selector('.disconnectbtn')
        stop_button.click()
