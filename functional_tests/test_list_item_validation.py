#!/usr/bin/env python

from .base import FunctionalTest
#from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        """"""
        # Edith goes to the home page and accidentlly tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('\n')
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error_p = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(
            error_p.text,
            "You can't have an empty list item."
        )
        # She tries again with some text for the item, which now works
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('some text here.\n')
        self.check_for_row_in_list_table('1: some text here.')
        # Perversely, she now decides to submit a second blank list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('\n')

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: some text here.')
        error_p = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error_p.text, "You can't have an empty list item.")

        # And she can correct it by filling some text in
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: some text here.')
        self.check_for_row_in_list_table('2: Make tea')

