from flet import *
import sqlite3 as sql
from random import randint
class ShowContact(UserControl):
    def __init__(self,page:Page):
        super().__init__()
        self.pageContact=Container(
            IconButton(icon=icons.ABC,on_click=lambda _:self.page.go("/body"))
        )
        
    def delete(self,e):
        con = sql.connect("Contact.db")
        con.execute("DELETE FROM Contact WHERE id = (SELECT ShowId FROM ShowContact WHERE Id = 1);")
        con.commit()
        con.close()
        self.page.go("/body")
    def close_dlg(self,e):
        self.dlg_modal.open = False
        self.page.update()
    def deleteContact(self,e):
        self.dlg_modal = AlertDialog(
        modal=True,
        title=Text("لطفا تایید کنید"),
        content=Text(f"اگه تا اینجا اومدی یعنی میخوای{self.name}  رو حذف کنی. از این کار مطمئنی؟",rtl=True),
        actions=[
            TextButton("Yes", on_click=self.delete),
            TextButton("No", on_click=self.close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
    )
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()
        

        
        


    def build(self):
        
        con=sql.connect("Contact.db")
        a=con.execute(f"""SELECT name || ' ' || Family AS full_name,Phone,Color FROM Contact WHERE Id = (SELECT ShowId FROM ShowContact WHERE Id = 1);""")
        for i in a:
            self.name=i[0]
            self.phone=i[1]
            self.color=i[2]
        con.close()
        self.fullName=Text(self.name,
                           size=30,
                           weight="w600")
        print(self.name,self.color,self.phone)
        self.pageInsert=Container(
            content=Column([
                Row([
                    IconButton(icons.ARROW_BACK,icon_color="black",on_click=lambda _: self.page.go('/body')),
                    
                    Container(width=215,height=50),
                    IconButton(icons.DELETE,icon_color="black",on_click=self.deleteContact),
                    IconButton(icons.EDIT,icon_color="black",on_click=lambda _: self.page.go('/editContact'))
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
                                
                                self.fullName
                            ],alignment="center"),
                            Divider(height=30,color="transparent"),
                            Row([
                                    Column([
                                        IconButton(icons.PHONE_OUTLINED,bgcolor="#C7C0F5",icon_color="black",width=50,height=50),
                                        ]),
                                    Column([
                                        IconButton(icons.SMS_OUTLINED,bgcolor="#C7C0F5",icon_color="black",width=50,height=50),
                                            ]),
                                    Column([
                                        IconButton(icons.VIDEO_CALL_OUTLINED,bgcolor="#C7C0F5",icon_color="black",width=50,height=50),
                                        ])
                                
                                
                            ],spacing=70,alignment="center"),
                            
                            Row([
                                Container(
                                    content=Column([
                                        Row([
                                            Text("  Contact info",
                                                 size=18,
                                                 weight="w600")
                                        ]),
                                        Divider(height=10,color="transparent"),
                                        Row([
                                            ElevatedButton(
                                            content=Row([
                                                Icon(icons.PHONE,color="black"),
                                                Text(self.phone+"\n"+"mobile"),
                                                Container(width=100)
                                                        ]),
                                            height=60,
                                            width=350,
                                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=0),
                                                              color="black",
                                                              shadow_color="#e0e0e0",
                                                              surface_tint_color="#e0e0e0",
                                                              bgcolor="#e0e0e0"
                                                            
                                                            )
                                            )
                                            ],alignment="center")
                                        ]),
                                    bgcolor="#e0e0e0",
                                    expand=True,
                                    height=135,
                                    margin=15,
                                    border_radius=20,
                                    padding=padding.only(top=18)
                                )
                                
                            ]),
                            ],
                                       ),
                        bgcolor="white",
                        expand=True,
                        height=700,
                        padding=padding.only(top=20)
                        ),
                    
                ])
            ]),
            
        )
        
        return self.pageInsert
