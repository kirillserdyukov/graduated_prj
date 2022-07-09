import random
import time

from generator.generator import person_generator
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    person_info = next(person_generator())
    full_name = person_info.full_name
    email = person_info.email
    current_address = person_info.current_address
    permanent_address = person_info.permanent_address

    def write_inside_all_forms(self, full_name=full_name, email=email, current_address=current_address, permanent_address=permanent_address):
        self.element_is_visible(TextBoxPageLocators.FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(TextBoxPageLocators.USER_EMAIL_FIELD).send_keys(email)
        self.element_is_visible(TextBoxPageLocators.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.element_is_visible(TextBoxPageLocators.PERMANENT_ADDRESS_FIELD).send_keys(permanent_address)
        self.element_is_visible(TextBoxPageLocators.SUBMIT_BUTTON).click()

    def check_created_forms(self, full_name=full_name, email=email, current_address=current_address, permanent_address=permanent_address):
        assert self.element_is_present(TextBoxPageLocators.CREATED_FULL_NAME_FIELD).text.split(':')[1] == full_name, "the full name not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_USER_EMAIL_FIELD).text.split(':')[1] == email, "the email not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_CURRENT_ADDRESS_FIELD).text.split(':')[1] == current_address, "the current_email not correct"
        assert self.element_is_present(TextBoxPageLocators.CREATED_PERMANENT_ADDRESS_FIELD).text.split(':')[1] == permanent_address, "the permanent_email not correct"


class CheckBoxPage(BasePage):
    def open_full_items_list(self):
        self.element_is_visible(CheckBoxPageLocators.EXPAND_BUTTON).click()

    def click_random_checkbox(self):
        checkbox_list = self.elements_are_visible(CheckBoxPageLocators.TITLE_ITEMS)
        count = 16
        while count != 0:
            checkbox = checkbox_list[random.randint(1, 16)]
            self.scroll_into_view(checkbox)
            checkbox.click()
            # print(checkbox.text)
            count -= 1

    def get_checked_checkbox(self):
        checked_list = self.elements_are_present(CheckBoxPageLocators.CHECKED_CHECKBOX)
        data = []
        for checkbox in checked_list:
            title_name = checkbox.find_element(*CheckBoxPageLocators.CHECKED_ITEM)
            data.append(title_name.text.lower().replace(" ", "").replace(".doc", ""))
        print(data)
        return data

    def get_output_selected_title(self):
        result_list = self.elements_are_present(CheckBoxPageLocators.RESULT_LIST)
        data = []
        for result in result_list:
            data.append(result.text.lower())
        print(data)
        return data

    def compare_checked_checkbox_with_selected_output_title(self):
        assert self.get_checked_checkbox() == self.get_output_selected_title(), "selected checkbox dont match with result output"
