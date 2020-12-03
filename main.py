from selenium import webdriver
import time
import gspread

driver = webdriver.Chrome(executable_path=r"chrome_path") # Replace my path with where your chromedriver is stored
insta_usrname = YOUR_USERNAME
insta_password = YOUR_PASSWORD
spreadsheet_name = YOUR SPREADSHEET_NAME

def accessInstagram():
    # Going to instagram's website then waiting 3 seconds before continuing
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    """Login Page"""
    # Getting username box and entering my username
    usernameBox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    usernameBox.send_keys(insta_usrname)

    # Getting password box and entering my password
    passwordBox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    passwordBox.send_keys(insta_password)

    # Getting the login box and clicking, then waiting 3 seconds to continue
    loginBox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    loginBox.click()
    time.sleep(5)

    """Home Page"""
    # Goes to dm page, then waits 3 seconds
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(3)

    # Gets past the turn on notifications pop up
    button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    button.click()


# Finds a workbook by name and open the first sheet
def access_sheet():
    client = gspread.oauth()
    return client.open(spreadsheet_name).sheet1


notification_class = "_41V_T.Sapc9.Igw0E.IwRSH.eGOV_._4EzTm"  # Class for the blue dot that appears for unread notification


# Finds the first box with an unread notification and clicks it, waits 1 second
def findDMs(sheet, i):
    print("Processing DMs")
    time.sleep(5)
    while True:
        try:
            notif = driver.find_element_by_class_name(notification_class)  # Gets next unread notification
        except:
            print("No notifications left")
            break
        notif.click()
        i += 1
        time.sleep(3)
        add_to_sheet(sheet, get_msg(), i)  # Adds message to specified cell


# Finds and the message text and copies it
def get_msg():
    messages = driver.find_elements_by_tag_name("span")
    return messages[len(messages) - 1].text  # Last span element is the last message sent


def add_to_sheet(sheet, message, row):
    sheet.update_cell(row, 1, message)  # Adds message to col A and row <row>




def main():
    start_row = 1  # The row you want to start on minus one
    sheet = access_sheet()  # Initiates access to spreadsheet
    accessInstagram()  # Initiates access to Instagram

    while True:
        findDMs(sheet, start_row)
        time.sleep(120)  # Waits 120 seconds before checking DMs again


if __name__ == '__main__':
    main()
