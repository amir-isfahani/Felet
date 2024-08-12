from flet import *
import sqlite3 as sql
from random import randint
class Edit(UserControl):
    def __init__(self,page:Page):
        super().__init__()
        self.name='l'
        self.color='#202020'
        
        self.phone="09134099355"
    def edit(self,e):
        print(self.id)
        con=sql.connect("Contact.db")
        con.execute("UPDATE Contact SET name = ?, family = ?, phone = ? WHERE id = ?;", (self.fieldname.value,self.fieldfamily.value,self.fieldnumber.value, self.id))
        con.commit()
        con.close()
        self.page.go("/showContact")
    def build(self):
        con=sql.connect("Contact.db")
        a=con.execute(f"""SELECT name,Phone,Color,Family,id FROM Contact WHERE Id = (SELECT ShowId FROM ShowContact WHERE Id = 1);""")
        for i in a:
            self.name=i[0]
            self.phone=i[1]
            self.color=i[2]
            self.family=i[3]
            self.id=i[4]
        con.close()
        self.fieldname=TextField(value=self.name,label="First name")
        self.fieldfamily=TextField(value=self.family,label="Last name")
        self.fieldnumber=TextField(value=self.phone,label="Phone")
        
        print(self.name,self.color,self.phone)
        self.pageInsert=Container(
            content=Column([
                Row([
                    IconButton(icons.ARROW_BACK,icon_color="black",on_click=lambda _: self.page.go('/showContact')),
                    Text("Edit Contact",size=20,weight="w400"),
                    Container(width=90,height=50),
                    ElevatedButton("Save",width=80,
                                   height=40,
                                   style=ButtonStyle(color="black"),
                                   on_click=self.edit
                                   )
                    
                ]),
                Row([
                    Container(
                        content=Column([
                            Row([
                               Container(
                                        content=Text(
                                            value=self.name[0].upper(),
                                            weight=FontWeight.W_500,
                                            size=100,
                                            color="white"
                                            # bgcolor="white",
                                            ),
                                        width=150,
                                        height=150,
                                        bgcolor=self.color,#self.profileColor,
                                        border_radius=100,
                                        alignment=alignment.center,
                                        padding=padding.only(top=-18)
                                    ), 
                            ],alignment="center"),
                            
                            Row([
                                TextButton("Add picture",style=ButtonStyle(overlay_color="white")),
                                
                            ],alignment="center"),
                            Divider(height=30,color="transparent"),
                            # self.fullName
                            
                            Row([
                                Container(
                                    content=Column([
                                    
                                        Row([
                                            Icon(name=icons.PEOPLE,color="black"),
                                            self.fieldname
                                            ]),
                                        Row([
                                            Icon(),
                                            self.fieldfamily
                                            ]),
                                        Row([
                                            Icon(name=icons.PHONE,color="black"),
                                            self.fieldnumber
                                            ])
                                        ]),
                                    bgcolor="white",
                                    expand=True,
                                    
                                    margin=10,
                                    
                                    padding=padding.only(top=18)
                                )
                                
                            ]),
                            ],
                                       ),
                        bgcolor="white",
                        expand=True,
                        height=700,
                        padding=padding.only(top=30)
                        ),
                    
                ])
            ]),
            
        )
        
        return self.pageInsert
