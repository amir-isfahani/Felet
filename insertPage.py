from flet import *
import sqlite3 as sql
from random import randint
class InsertPage(UserControl):
    def __init__(self,page:Page):
        super().__init__()
        self.firstName=TextField(hint_text="First Name",focused_border_color="black")
        self.lastName=TextField(hint_text="Last Name",focused_border_color="black")
        self.phone=TextField(hint_text="Phone",focused_border_color="black")
        self.pageInsert=Container(
            content=Column([
                Row([
                    IconButton(icons.CLOSE,icon_color="black",on_click=lambda _: self.page.go('/body')),
                    Text("Create contact",size=25),
                    Container(width=50,height=50),
                    ElevatedButton(text="Save",on_click=self.insert)
                ]),
                Row([
                    Container(
                        content=Column([
                            Container(content=IconButton(icon=icons.ADD_A_PHOTO_ROUNDED,
                                                         icon_color="black",
                                                         bgcolor="#e0e0e0",
                                                         width=150,height=150,
                                                         icon_size=70
                                                         ),
                                      alignment=alignment.center,
                                      margin=margin.only(left=-15,top=100,bottom=50)
                                      ),
                            
                            Row([
                                Icon(color="black",name=icons.PEOPLE),
                                self.firstName
                            ]),
                            Row([
                                Icon(),
                                self.lastName
                            ]),
                            Row([
                                Icon(name=icons.PHONE,color="black"),
                                self.phone
                                
                            ]),
                            ],
                                       ),
                        bgcolor="white",
                        expand=True,
                        height=700,
                        padding=padding.only(left=15)
                        ),
                    
                ])
            ]),
            
        )
    def insert(self,e):
        self.color=[
        "#f000f0",
        "#f05500",
        "#00aaff",
        "#565656",
        "#8C4EE6",
        "#50664A"
        ]
        indexColor=randint(0,5)
        profilecolor=self.color[indexColor]
        print(profilecolor)
        con=sql.connect("Contact.db")
        
        con.execute(f'insert into Contact(Phone,Name,family,color) values(?,?,?,?)',[self.phone.value,self.firstName.value,self.lastName.value,profilecolor])
        con.commit()
        con.close()
        self.phone.value=""
        self.firstName.value=""
        self.lastName.value=""
        self.firstName.update()
        self.lastName.update()
        self.phone.update()
        self.firstName.focus()
    def build(self):
        return self.pageInsert