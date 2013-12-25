#!/usr/bin/env python

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        """"""
        # Edith goes to the home page and accidentlly tries to submit
        # an empty list item. She hits Enter on the empty input box
        inputbox = self.browser.find_element_by_tag_name('input')
        inputbox.send_keys(Keys.ENTER)
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error_p = self.browser.find_element_by_id('id_error_message')
        self.assertEqual(
            error_p.text,
            'List items cannot be empty.'
        )
        # She tries again with some text for the item, which now works
        inputbox.send_keys('some text here.')
        inputbox.send_keys(Keys.ENTER)
        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in

