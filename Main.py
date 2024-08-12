from flet import *
from router import views_handler

def main(page: Page):

  def route_change(route):
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )
  
  page.window_width=400
  page.window_height=750
  page.on_route_change = route_change
  page.go('/body')


app(target=main)
