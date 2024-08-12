from flet import *
import sqlite3 as sql
import showContact


ShowContact="SELECT name || ' ' || Family AS full_name,phone,color,id FROM Contact ORDER BY name,family"
class Contact(UserControl):
    def __init__(self,color="#00aaff",number="0",name="a",contactId=1):
        super().__init__()
        self.number=number
        self.fullName=name
        self.profileColor=color
        self.contactId=contactId
        self.dlg = AlertDialog(
            modal=True,
            title=Text("توجه!!!",rtl=True),
            content=Text("این نوع اقدام تنها مخاطب را از این لیست پاک میکند و ربطی به دیتا بیس ندارد\n برای اینکه از دیتا بیس حذف شود باید روی مخاطب کلیک کنید و گزینه حذف را بزنید",rtl=True,text_align="right",weight="w400"),
            actions=[
                TextButton("بله",on_click=self.close_yes_dlg),
                TextButton("خیر",on_click=self.close_no_dlg),
            ],
            actions_alignment=MainAxisAlignment.CENTER,
            
        )
        self.contact=Dismissible(
                    Container(ElevatedButton(
                                        content=Row([
                                            CircleAvatar(#جای این container بود
                                                content=Text(
                                                    value=self.fullName[0].upper(),
                                                    weight=FontWeight.W_400,
                                                    size=30,
                                                    color="white"
                                                    # bgcolor="white",
                                                    ),
                                                width=45,
                                                height=45,
                                                bgcolor=self.profileColor,
                                                # border_radius=25,
                                                # alignment=alignment.center,
                                                # padding=padding.only(top=-5)
                                            ),
                                            Text(self.fullName,
                                                size=18,
                                                weight=FontWeight.W_400,
                                                color="black")
                                        ]),
                                    on_click=self.show,
                                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=border_radius.only(15,0,15)),
                                                    padding=padding.only(left=8),
                                                    shadow_color="transparent",
                                                    #   bgcolor="yellow",
                                                    surface_tint_color="white"),
                                    
                                ),
                    height=60),
                    dismiss_direction=DismissDirection.HORIZONTAL,
                    background=Container(content=Icon(icons.CALL,color="white"),bgcolor=colors.GREEN,alignment=alignment.center_left,padding=padding.only(10)),
                    secondary_background=Container(content=Icon(icons.DELETE_SWEEP,color="white"),bgcolor=colors.RED,alignment=alignment.center_right,padding=padding.only(10)),
                    # on_dismiss=self.handle_dismiss, 
                    on_update=self.handle_update,
                    on_confirm_dismiss=self.handle_confirm_dismiss,
                    dismiss_thresholds={
                        DismissDirection.END_TO_START: 0.3,
                        DismissDirection.START_TO_END: 1,
                    },
                                )
    def close_yes_dlg(self,e):
        self.page.close_dialog()
        self.dlg.data.confirm_dismiss(True)
        showContact.ShowContact.deleteContact

    def close_no_dlg(self,e):
        self.page.close_dialog()
        self.dlg.data.confirm_dismiss(False)
    def handle_confirm_dismiss(self,e: DismissibleDismissEvent):
        if e.direction == DismissDirection.END_TO_START: # right-to-left slide
            # save current dismissible to dialog's data
            self.dlg.data = e.control
            self.page.show_dialog(self.dlg)
        else: # left-to-right slide
            e.control.confirm_dismiss(True)
    def handle_update(self,e: DismissibleUpdateEvent):
        print(f"Update - direction: {e.direction}, progress: {e.progress}, reached: {e.reached}, previous_reached: {e.previous_reached}")
    def ins(self):
        con=sql.connect("Contact.db")
        con.execute("UPDATE ShowContact SET ShowId = ? WHERE id = ?;", (self.contactId, 1))
        con.commit()
        con.close()
    def show(self,e):
        self.ins()
        self.page.go('/showContact')
        print(self.contactId)
    
    def build(self):
        return self.contact
class ContactList(UserControl):
    def __init__(self):
        super().__init__()
        name="amir"
        family="esfahani"
        self.fullName=name+" "+family
        self.profileColor="#0000ff"
        
        
        self.listOfContact=ListView([
            
                        ],
                    # scroll=ScrollMode.ADAPTIVE,
                    spacing=1,
                    expand=True)
    def rebuild(self):
        BD.contactList.listOfContact.controls.clear()
        
        con=sql.connect("Contact.db")
        a=con.execute(ShowContact)
        for item in a:
            self.listOfContact.controls.append(Contact(number=item[1],name=item[0],color=item[2],contactId=str(item[3])))
            
        
        con.close()
        self.listOfContact.update()
        return self.listOfContact
    def build(self):
        con=sql.connect("Contact.db")
        a=con.execute(ShowContact)
        for item in a:
            self.listOfContact.controls.append(Contact(number=item[1],name=item[0],color=item[2],contactId=str(item[3])))
           
        
        con.close()
        
        return self.listOfContact
class Body(UserControl):
    def __init__(self):
        super().__init__()
        self.contactList=ContactList()
        
        self.body=Container(
            content=Column(
                [
                    Row([
                        Container(
                            content=Row(
                                [
                                    Icon(icons.SEARCH,color="black"),
                                    TextField(
                                        hint_text="Search Contact",
                                        border="none",
                                        on_change=self.search,
                                        text_style=TextStyle(weight=FontWeight.W_500,color="505050")
                                    ),
                                    IconButton(icons.MORE_VERT,icon_color="black")
                                ],
                                alignment="center"
                                ),
                            padding=padding.only(left=10,right=10),
                            height=55,
                            bgcolor="#dddddd",
                            expand=True,
                            border_radius=50
                        )
                        ],
                        ),
                    Stack([
                        Container(
                            content=self.contactList,
                            # bgcolor="red",
                            expand=True,
                            height=640,
                            bgcolor="white",
                            padding=padding.only(10,50)
                        ),
                        Container(
                            content=Row([
                                
                                IconButton(icon=icons.ADD,icon_color="black", on_click=lambda _: self.page.go('/insert')),
                                PopupMenuButton(items=[PopupMenuItem(text="select"),
                                                       PopupMenuItem(text="Select all")]),
                                
                                ]),
                            bgcolor="#ffffff",
                            shadow=BoxShadow(
                                spread_radius=0,
                                blur_radius=10,
                                color=colors.BLUE_GREY_600,
                                offset=Offset(0, 0),
                                
                                blur_style=ShadowBlurStyle.OUTER,
                            ),
                            expand=True,
                            height=50,
                            rtl=True,
                            margin=margin.only(-10,right=-10)
                            
                        ),
                    
                    
                        
                    
                        ]),
                    
                ],
                expand=True
            ),
            height=750,
            width=400,
            bgcolor="white"
        )
    def search(self,e):
        if e.control.value!="":
            searchText=e.control.value
            BD.contactList.listOfContact.controls.clear()
            BD.contactList.listOfContact.update()
            con=sql.connect("Contact.db")
            a=con.execute(f"""
                            SELECT name || ' ' || Family AS full_name, phone, color, id
                            FROM Contact
                            WHERE full_name LIKE '{searchText}%'
                            ORDER BY full_name;
                          """)
            for item in a:
                BD.contactList.listOfContact.controls.append(Contact(number=item[1],name=item[0],color=item[2],contactId=str(item[3])))
                BD.contactList.listOfContact.update()
        else:
            
            BD.contactList.rebuild()
    def build(self):
        
        return self.body
class OutPut(UserControl):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        
        global BD
        BD=Body()

    def build(self):
        return BD