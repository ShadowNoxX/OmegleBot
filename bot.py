# Import the packages we need
import random
from time import sleep

from pynput.keyboard import Key, Controller
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

# Declare the messages list in our messages.txt file
f = open("messages.txt")
messages = f.read().splitlines()

# Declare the random sleep delay
rdm_sleep = random.randint(5, 11)
# Make a while looop to make our program run forever
while True:
    # Make a try except to avoid our program to crash
    try:
        # Declare the message text box
        sleep(2)
        message_box = driver.find_element_by_css_selector('.chatmsg')
        # Send the first message into the message box
        message_box.send_keys(messages[0])
        # Send the message by pressing enter and make a sleep to not be detected as a bot
        sleep(1.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the second message with the random sleep delay
        sleep(rdm_sleep)
        # Send the second message into the message box
        message_box.send_keys(messages[1])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the third message
        sleep(rdm_sleep)
        # Send the third message into the message box
        message_box.send_keys(messages[2])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the fourth message
        sleep(rdm_sleep)
        # Send the the fourth message into the message box
        message_box.send_keys(messages[3])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the fith message
        sleep(rdm_sleep)
        # Send the fith message into the message box
        message_box.send_keys(messages[4])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the sixth message
        sleep(rdm_sleep)
        # Send the sixth message into the message box
        message_box.send_keys(messages[5])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the seventh message
        sleep(rdm_sleep)
        # Send the seventh message into the message box
        message_box.send_keys(messages[6])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the eight message
        sleep(rdm_sleep)
        # Send the eight message into the message box
        message_box.send_keys(messages[7])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for the nineth message
        sleep(rdm_sleep)
        # Send the nineth message into the message box
        message_box.send_keys(messages[8])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Wait for last message
        sleep(rdm_sleep)
        # Send the last message into the message box
        message_box.send_keys(messages[9])
        # Send the message by pressing enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Declare the Stop button to disconnect us
        stop_button = driver.find_element_by_css_selector('.disconnectbtn')
        # Press 3x the stop button to find a new user
        # Make some sleeps to make that  and not suspect
        sleep(0.5)
        stop_button.click()
        sleep(0.5)
        stop_button.click()
        sleep(0.5)
        stop_button.click()
    # The except is when the user is disconnecting before us
    except:
        print("User disconnected before us")
        stop_button = driver.find_element_by_css_selector('.disconnectbtn')
        sleep(0.5)
        stop_button.click()
