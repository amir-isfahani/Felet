from flet import *

def main(page: Page):
    

    page.add(
        Container(
            Row([
                PopupMenuButton(items=[
                    PopupMenuItem(content=Text("item 1")),
                    PopupMenuItem(content=ElevatedButton(text="item 2",))
                ],
                                content=Icon(icons.ADS_CLICK,size=30))
            ]),
            bgcolor="red",
            width=300
        )
    )

app(target=main)