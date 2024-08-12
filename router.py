from flet import *
from insertPage import InsertPage
from Body import OutPut
from showContact import ShowContact
from EditContact import Edit

def views_handler(page):
    return {"/body": View(route="/body",controls=[OutPut(page)]),
            "/insert": View(route="/insert",controls=[InsertPage(page)]),
            "/showContact": View(route="/showContact",controls=[ShowContact(page)]),
            "/editContact": View(route="/editContact",controls=[Edit(page)]),
            }
    