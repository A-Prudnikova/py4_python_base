def open_browser(browser_name):
    pass


def go_to_companyname_homepage():
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]


def printing_name_and_args(args):
    for arg in args:
        print("Имя функции:", arg.__name__.capitalize().replace("_", " "), end='. ')
        if not any(arg.__code__.co_varnames):
            print("Аргументов нет")
        else:
            print("Аргумент/ы функции:", arg.__code__.co_varnames)


printing_name_and_args(functions)