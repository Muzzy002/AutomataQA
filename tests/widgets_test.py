import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(selfs, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == "What is Lorem Ipsum?" and first_content > 0
            assert second_title == "Where does it come from?" and second_content > 0
            assert third_title == "Why do we use it?" and third_content > 0

    class TestAutoCompletePage:
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_data_before, value_date_after = date_picker_page.select_date()
            assert value_data_before != value_date_after

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_data_before, value_date_after = date_picker_page.select_date()
            print(value_date_after)
            print(value_data_before)
            assert value_data_before != value_date_after

    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            # value_before, value_after = progress_bar.change_progress_bar_value()
            value_before, value_after = progress_bar.change_progress_bar_value_100()
            assert value_before != value_after


class TestTabsPage:

    def test_tabs(self, driver):
        tabs = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs.open()
        what_content, origin_content, use_content = tabs.check_tabs()
        assert what_content != origin_content and what_content != use_content


class TestToolTips:
    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_selection = tool_tips_page.check_tool_tips()
        # print(tool_tip_text_button)
        # print(tool_tip_text_field)
        # print(tool_tip_text_contrary)
        print(tool_tip_text_selection)


class TestMenuPage:
    def test(self, driver):
        menu_page = MenuPage(driver, "https://demoqa.com/menu#")
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                        'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']


class TestSelectManuPage:

    def test_select_menu(self, driver):
        select_menu = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
        select_menu.open()
        output_result, input_result = select_menu.first_input()
        output_data, random_data = select_menu.second_input()
        color_input = select_menu.third_input()
        result_multi = select_menu.fourth_input()
        select_menu.five_multi_select()

        assert output_data == random_data
        assert output_result == input_result
        assert len(color_input) >= 1
        assert len(result_multi) == 1




