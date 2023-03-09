'''
Author: Naor Or-Zion
State: Israel
Date: 08/03/2023

Brief: The code adds contacts to google contacts.
       Before adding the contacts - checks if they exists, if they do - ask if to still add the same user or cancel the opertaion.

       The code is using Google People API and supports OAuth 2.0 only, no need for an API key!
'''

import sys
import requests
import openpyxl
from time import sleep
from typing import Dict
from pathlib import Path
from PySide6 import QtWidgets
from gui import Ui_MainWindow
from bidi.algorithm import get_display
from PySide6.QtCore import QCoreApplication
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QListWidgetItem
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem


# Consts
# Local Paths
CLIENT_FILE = Path(r'client_secret.json')
TOKEN_FILE = Path("token.json")

# URLs
OAUTH_SCOPE = ['https://www.googleapis.com/auth/contacts']
CREATE_CONTACT_URL = "https://people.googleapis.com/v1/people:createContact"
SEARCH_CONTACT_URL = "https://people.googleapis.com/v1/people:searchContacts"

#TEXT
OPENING_TEXT = "Begins in 5 seconds from the moment you press the 'ok' button"
FINISH_TEXT = "All users have been added successfully"

# Network - Must use this proxy with any request
PROXY = {'http':'http://10.0.2.69:80'}
LOCAL_PORT_NUMBER = 62223
HTTP_OK_STATUS = 200


class ContactsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contacts")
        self.contacts_list = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Contacts added:"))
        layout.addWidget(self.contacts_list)
        self.setLayout(layout)

    def add_contact(self, name):
        item = QListWidgetItem(name)
        self.contacts_list.addItem(item)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.excel_file_path = ""
        self.ui.browse_button.clicked.connect(self.browse_for_file)
        self.ui.start_button.clicked.connect(self.start_process)


    def browse_for_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Excel files (*.xlsx)")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.ui.lineEdit.setText(file_path)
            self.excel_file_path = file_path


    def start_process(self):
        main(self.excel_file_path)


def get_credentials() -> Credentials:
    """
    This function gets the user's credentials from google with the help of the OAuth 2.0 Scope.
    OAuth 2.0 holds an access token. Remember - The access token replaces the API key.

    If user's credentials exists, use the existed credentials.
    Eventually this function will return the credentials(aspecially the access token) which 
    will grant the user a communication with the API servers.

    :return credentials
    """
    creds = None
    
    # Checks if the creds file is exists in the same directory.
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), OAUTH_SCOPE)

    # If the creds file is valid, return it.
    if creds and creds.valid:
        return creds
        
    # If the creds file is expired then refresh it - Request again    
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        return creds

    # Use a Client File in the OAuth flow to acquire an access token
    # associated with your project on behalf of a user's account.
    # @TODO Remove the secret from the json file, and then add it from an environment variable after you load it. 
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file=str(CLIENT_FILE), scopes=OAUTH_SCOPE)
    creds = flow.run_local_server(port=LOCAL_PORT_NUMBER)
    TOKEN_FILE.write_text(creds.to_json())

    return creds   


def add_contact(name: str, phone_number: str, current_course: str, credentials: Credentials, contacts_window: ContactsWindow) -> None:
    """
    This function creates a contact by a given name and a phone number.
    It first sets up the POST request parameters, then adds a contact.

    :param name: Given contact's name.
    :param phone_number: Given Contact's phone number.
    :param credentials: The user credentials, contains the access token held by the OAuth 2.0.
    :return None
    """

    # Set up the POST request parameters
    headers = {
        # 'credentials.token' is access token 
        'Authorization': f'Bearer {credentials.token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'names': [
            {
                'givenName': name
            }
        ],
        'phoneNumbers': [
            {
                'value': phone_number,
                'type': 'mobile'
            }
        ],
        "organizations": [
            {
                "title": current_course,
            }
        ]
    }

    is_contact_exists = False

    if not is_contact_exists:
        response = requests.post(CREATE_CONTACT_URL, headers=headers, json=data, proxies=PROXY)

        if response.status_code == HTTP_OK_STATUS:
            contacts_window.add_contact(f"{name} : {phone_number}  in course {current_course}")
            model_index = contacts_window.contacts_list.model().index(0, 0)
            contacts_window.contacts_list.update(model_index) 
            QCoreApplication.processEvents()         
        else:
            msg_box = QMessageBox()
            msg_box.setText(f"Failed to add contact '{get_display(name)}'. \nError: {response.text}")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()


def add_contacts_from_excel(file_path: Path) -> None:
    """
    This function gets a file path to the excel file containing the data of the contacts.
    The data in the excel file MUST be 2 columns only while the first column is "Full name" and the second column is "Phone number".
    The file must be in a left-to-right alignment format.
    The data can be as many rows as you want.
    Example of how it should look like in excel:
    +--------------------+--------------------+--------------------+
    |      Full name     |     Phone Number   |   Current Course   |
    +--------------------+--------------------+--------------------+
    |    Lionel Messi    |      0501010101    |        Python      |
    +--------------------+--------------------+--------------------+
    |    Ryan Rynolds    |      0506942069    |         SQL        |
    +--------------------+--------------------+--------------------+

    :param file_path: The path to the excel file containing the contacts.
    :return None
    """

    # Load the Excel file
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active

    contacts_window = ContactsWindow()
    credentials = get_credentials()

    # Extract the name and phone number for each row in the sheet
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        name, phone_number, current_course = row
        contacts_window.show()
        add_contact(name, phone_number, current_course, credentials, contacts_window)
    
    
    # Create a message box to display the finish text
    msg_box = QMessageBox()
    msg_box.setText(FINISH_TEXT)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()

def main(excel_file_path: Path):
    add_contacts_from_excel(file_path=excel_file_path)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
    











# For future use

# def check_contact_exists(self, headers: Dict , contact_name: str, readmask: str) -> bool:
#     """
#     Checks if a contact exists in the user's Google Contacts using the
#     `people.searchContacts` API endpoint.

#     :param headers: The headers for the get request
#     :param contact_name: A string containing the search query for the contact.
#     :param readmask - The information's lists to retrieve from a contact.
#     :return True if the contact exists, False otherwise.
#     """

#     # Set up the GET request parameters
#     contact_name = quote(contact_name, safe='')

#     # Make the request
#     response = requests.get(f"{SEARCH_CONTACT_URL}?query='{contact_name}'&readMask={readmask}", headers=headers)

#     # Check the response status code
#     if response.status_code != HTTP_OK_STATUS:
#         print(f"Failed to check if contact '{get_display(contact_name)}' exists or not. \nError: {response.text}")
#         response.raise_for_status()
    
#     # If the response is successful, check if any contacts were found
#     search_results = response.json()
    
#     return search_results.get("results")


    # Display which contact was found in contacts list. If found, ask to create anyway.
    # if is_contact_exists:
    #     print(f"Contact '{get_display(name)}' was found in your contacts list already!")
    #     create_anyway = input(f"Do you want to create '{get_display(name)}' anyway? (yes/no)\n")

    #     if create_anyway.lower() == "yes":
    #         is_contact_exists = False
    #     else:
    #         print("No changes were applied.\n")

    # If contact is not exists or user chose to create it anyway then create contact.


    # Wakeup function call
    # The program sleeps for 5 seconds because the api needs to be "woken up", so Google advises to sleep 5 seconds
    # after sending the inital request
    # headers = {
    #     'Authorization': f'Bearer {credentials.token}',
    #     'Accept': 'application/json'
    # }
    # requests.get(SEARCH_CONTACT_URL, headers=headers, params={'query': '', 'readMask': 'names'})
    # sleep(5)



    # Not needed for now
    """
    # Get the full name from the headers and checks if that name exists in contacts.
    contact_full_name = data["names"][0]["givenName"]
    is_contact_exists = check_contact_exists(headers=headers, contact_name=contact_full_name, readmask="names")
    """