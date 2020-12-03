# Insta_DM_Logger
This program will go through unread DMs and insert the last DM into a google spreadsheet.

Input your own information for the following parameters:
insta_usrname,
insta_password,
spreadsheet_name,
chrome_path.


Must install gspread and selenium. Follow authentication steps for gspread here: https://gspread.readthedocs.io/en/latest/oauth2.html#for-end-users-using-oauth-client-id


Limitations:
Can't automatically detect when a new DM is available 

The starting row is hardcoded, so if there's data already there, the program will change it.



