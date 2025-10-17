from customtkinter import *
from datetime import datetime
from PIL import Image
from data import *
from functools import partial


# set up app window interface
appwidth = 375
appheight = 812

# set app light theme mode
set_appearance_mode("light")
set_default_color_theme("./blue.json")
compound = "left"

# window app class
class App(CTk): 
    def __init__(self):
        CTk.__init__(self)
        self.title('SecondServings')
        self.geometry('375x812')
        self.minsize = (375,812)
        self.maxsize = (375,812)

        # for storing username, pw, grocery list text, food, date of today in fridge data
        self.username = ""
        self.pw = "" 
        self.grocerylist_txt = ""
        self.fridge_data = [] 
        # side note: this is the format of dict for each var listed in list
        # food_data = {
        #                 "name": foodname,
        #                 "quantity": int(qty),
        #                 "expiry_date": exp,
        #                 "storage_date": datestored
        #                 }
        self.today = datetime.today().date() 

        # app fonts
        self.titlefont = CTkFont("SF Pro", size=33, weight="bold")
        self.subtitlefont = CTkFont("SF Pro", size=20, weight="bold")
        self.normalfont = CTkFont("SF Pro", size=14, weight="normal")
        self.normalboldfont = CTkFont("SF Pro", size=14, weight="bold")
        self.subnormalfont = CTkFont("SF Pro", size=13, weight="normal")
        self.smallfont = CTkFont("SF Pro", size=12, weight="normal")

        self.curr_frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        # the (self) below refers to class App, for inputting as 'master' in other classes
        new_frame = frame_class(self) 
        if self.curr_frame is not None:
            self.curr_frame.destroy()

        self.curr_frame = new_frame
        self.curr_frame.pack() 
        self.curr_frame.pack_propagate(False)


# interface for log in page
class LoginPage(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master,width=appwidth,height=appheight)
        self.errorstate = False
        
        # top part widget, for image
        top_frame = CTkFrame(self,fg_color="#9DB074") 

        # bottom part widget, for user input sign in/up
        bottom_frame = CTkFrame(self)
        # title bottom part
        title = CTkLabel(bottom_frame,text="Log in", font=master.titlefont)
        
        # labels
        left_frame = CTkFrame(bottom_frame)
        userlabel = CTkLabel(left_frame,text="Username", font=master.normalfont)
        pwlabel = CTkLabel(left_frame,text="Password", font=master.normalfont)
        
        # entry fields, right of bottom
        rightbottom_frame = CTkFrame(bottom_frame)

        user_entry = CTkEntry(rightbottom_frame,placeholder_text="Enter your username.", font=master.subnormalfont)
        pw_entry = CTkEntry(rightbottom_frame,placeholder_text="Enter your password.", font=master.subnormalfont)

        # log in
        login_b = CTkButton(self, 
                  text="Log in",
                  font=master.normalboldfont,
                  command=lambda: self.error(self))
        
        # switch to other page for creating account     
        switch_b = CTkButton(self, 
                  text="No account? Click me to create one!",
                  font=master.subnormalfont,
                  command=lambda: master.switch_frame(SignupPage))
        
        
        # --------------------
        # top layout
        top_frame.pack(side="top",expand=True, fill="both", padx=20, pady=20)

        # bottom layout 
        title.pack(padx=30, pady=10, anchor="nw")
        bottom_frame.pack(side="top",fill="both", expand=True, padx=20, pady=20)

        userlabel.pack(fill="x", padx=5,pady=10)
        pwlabel.pack(fill="x", padx=5,pady=5)
        left_frame.pack(side="left",fill="both", expand=True)
        
        user_entry.pack(fill="x",pady=10)
        pw_entry.pack(fill="x",pady=5)
        rightbottom_frame.pack(side="left",fill="both", expand=True)

        login_b.pack(side="top")

        switch_b.pack(side="bottom", expand=True, pady=20)
    
    def error(self, master):
        # because we're not using databases, just act as if the user hasnt signed in yet.
        # this is to prevent error text piling up
        if self.errorstate == False:
            errorlabel = CTkLabel(master,text="No such user found.",text_color="#FF5733",font=app.subnormalfont)
            errorlabel.pack()
            self.errorstate = True


# interface for sign up page
class SignupPage(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master, width=appwidth,height=appheight)
        # prevent duplicating error messages when appear
        self.errorstate = False
        
        # top part widget, for image
        top_frame = CTkFrame(self,fg_color="#9DB074")
        
        # bottom part widget, for user input sign in/up
        bottom_frame = CTkFrame(self)
        # title bottom part
        title = CTkLabel(bottom_frame,text="Create an account",font=master.titlefont)
        
        # labels
        left_frame = CTkFrame(bottom_frame)
        userlabel = CTkLabel(left_frame,text="Username",font=master.normalfont)
        pwlabel = CTkLabel(left_frame,text="Password",font=master.normalfont)
        
        # entry fields, right of bottom
        rightbottom_frame = CTkFrame(bottom_frame)

        self.user_entry = CTkEntry(rightbottom_frame,placeholder_text="Enter a username.",font=master.subnormalfont)
        self.pw_entry = CTkEntry(rightbottom_frame,placeholder_text="Enter a password.",font=master.subnormalfont)

        # log in
        login_b = CTkButton(self, text="Sign up", command=lambda: self.save_data(master),font=master.normalboldfont)
        
        # switch to other page for login account     
        switch_b = CTkButton(self, 
                  text="Already have an account? Click me to log in!",
                  font=master.subnormalfont,
                  command=lambda: master.switch_frame(LoginPage))
        
        
        # --------------------
        # top layout
        top_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # bottom layout 
        title.pack(padx=10, pady=10)
        bottom_frame.pack(fill="both", expand=True, padx=20, pady=20)

        userlabel.pack(fill="x", padx=5,pady=10)
        pwlabel.pack(fill="x", padx=5,pady=5)
        left_frame.pack(side="left",fill="both", expand=True)
        
        self.user_entry.pack(fill="x",pady=10)
        self.pw_entry.pack(fill="x",pady=5)
        rightbottom_frame.pack(side="left",fill="both", expand=True)

        login_b.pack(side="top")

        switch_b.pack(side="bottom", expand=True, pady=20)
    
    def save_data(self, master):
        master.username = self.user_entry.get()
        master.pw = self.pw_entry.get()
        if master.username == "" or master.pw == "":
            if self.errorstate == False:
                errorlabel = CTkLabel(self,text="Fill in your username and/or password!",text_color="#FF5733",font=app.subnormalfont)
                errorlabel.pack()
                self.errorstate = True
        else:
            master.switch_frame(InApp)


class SlidePanel(CTkFrame):
    def __init__(self, master, start_pos, end_pos): # 1, 0.6
        CTkFrame.__init__(self, master,height=appheight) 

        self.start_pos = start_pos # when it's hidden
        self.end_pos = end_pos # when it's visible to user
        self.width = abs(start_pos - end_pos) # abs for preventing negative results
        self.height = 0.04
        self.place(relx=self.start_pos, rely=self.height, relwidth=self.width, relheight=1)
 
        # animation logic
        self.curr_pos = start_pos # current position of panel
        self.in_startpos = True # hidden

        # widgets 
        home_b = CTkButton(self, text="Home", font=app.normalfont, 
                           image=home_img, compound=compound,
                           command=lambda: master.switchframe_inapp(Home))
        fridge_b = CTkButton(self, text="Fridge", font=app.normalfont,
                             image=fridge_img, compound=compound,
                             command=lambda: master.switchframe_inapp(Fridge))
        grocerylist_b = CTkButton(self, text="Grocery List", font=app.normalfont, 
                                  image=list_img, compound=compound,
                                  command=lambda: master.switchframe_inapp(GroceryList))
        guide_b = CTkButton(self, text="Guide", font=app.normalfont, 
                            image=guide_img, compound=compound,
                            command=lambda: master.switchframe_inapp(Guide))
        recipe_b = CTkButton(self, text="Recipe", font=app.normalfont, 
                             image=recipe_img, compound=compound,
                             command=lambda: master.switchframe_inapp(Recipe))

        # widget layout
        home_b.pack(fill="x", anchor="w",pady=16)
        fridge_b.pack(fill="x", anchor="w",pady=3)
        grocerylist_b.pack(fill="x", anchor="w",pady=3)
        guide_b.pack(fill="x", anchor="w",pady=3)
        recipe_b.pack(fill="x", anchor="w",pady=3)

    def animate(self):
        if self.in_startpos:
            self.animate_show()
        else:
            self.animate_hide()
    
    def animate_show(self):
        # reveals panel
        if self.curr_pos > self.end_pos:
            # update current panel pos if not yet reached set end_pos (visible)
            self.curr_pos -= 0.015
            self.place(relx=self.curr_pos, rely=self.height, relwidth=self.width, relheight=1)
            self.after(10, self.animate_show) # call function again after 10 ms to create an "animation"
        else:
            self.in_startpos = False # revealed

    def animate_hide(self):
        # hides panel
        if self.curr_pos < self.start_pos:
            self.curr_pos += 0.04
            self.place(relx=self.curr_pos, rely=self.height, relwidth=self.width, relheight=1)
            self.after(10, self.animate_hide) # call function again after some time to create an "animation"
        else:
            self.in_startpos = True 


# ------------------------------------------------------
# inside the app, with all our main features!
class InApp(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master, width=appwidth, height=appheight)
        self.curr_frame = None # the current frame inside InApp! not to be mistaken with App

        # bar appears from right side
        self.navbar = SlidePanel(self, 1, 0.6)

        # layout
        menu_b = CTkButton(self, 
                           text="☰",
                           command=self.navbar.animate)
        menu_b.pack(side="top",anchor="ne")

        self.switchframe_inapp(Home)


    def switchframe_inapp(self, frame_class):
        # Destroys current frame and replaces it with a new one
        # the (self) below refers to class App, for inputting as 'master' in other classes
      
        if self.curr_frame is not None and hasattr(self, "curr_frame"):
            self.curr_frame.destroy()              
        
        new_frame = frame_class(self) 
        self.curr_frame = new_frame
        self.curr_frame.pack(fill="x") # fill=both, expand=True
        self.curr_frame.pack_propagate(False)

        self.navbar.lift() # to prevent being buried under new frames when called
        self.navbar.animate_hide()


class Home(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master, width=appwidth, height=appheight)
        
        placeholdertext = CTkLabel(self, 
                           text=f"Welcome, {app.username}!",
                           font=app.titlefont)
        
        top_frame =  CTkFrame(self)

        # for home navigation menu, apart from side navigation panel
        bottom_frame = CTkFrame(self)
        leftbottom_frame = CTkFrame(bottom_frame)
        rightbottom_frame = CTkFrame(bottom_frame)

        menutitle = CTkLabel(bottom_frame, text = "Home", font=app.subtitlefont)

        fridge_b = CTkButton(leftbottom_frame, text="Fridge", font=app.normalfont, height=100,width=100,
                             image=fridge_img, compound=compound,
                             command=lambda: master.switchframe_inapp(Fridge))
        guide_b = CTkButton(leftbottom_frame, text="Guide", font=app.normalfont, height=100,width=100,
                             image=guide_img, compound=compound,
                             command=lambda: master.switchframe_inapp(Guide))
        grocerylist_b = CTkButton(rightbottom_frame, text="Grocery List", font=app.normalfont, height=100,width=100,
                             image=list_img, compound=compound,
                             command=lambda: master.switchframe_inapp(GroceryList))
        recipe_b = CTkButton(rightbottom_frame, text="Recipes",font=app.normalfont, height=100,width=100,
                             image=recipe_img, compound=compound,
                             command=lambda: master.switchframe_inapp(Recipe))

        # layout
        placeholdertext.pack(side="top",anchor="nw",padx=20,pady=20)

        top_frame.pack(fill="both")

        menutitle.pack(padx=20,pady=20, anchor="nw")

        fridge_b.pack(fill="both",padx=20,pady=18)
        guide_b.pack(fill="both",padx=20,pady=18)
        grocerylist_b.pack(fill="both",padx=20,pady=18)
        recipe_b.pack(fill="both",padx=20,pady=18)
        leftbottom_frame.pack(side="left",fill="both",expand=True)
        rightbottom_frame.pack(side="left",fill="both",expand=True)
        bottom_frame.pack(fill="both",expand=True)




# check fridge
class Fridge(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master, width=appwidth, height=appheight)

        # track if popup is open
        self.popup = None # adding data
        self.editpopup = None # edit data

        headerframe = CTkFrame(self,width=appwidth)
        title = CTkLabel(headerframe,text="Your Fridge",font=app.titlefont)
        add_b = CTkButton(headerframe, text="+ Add", font=app.normalboldfont, width=100,
                          command=self.input_popup)
        
        self.contentframe = CTkScrollableFrame(self,height=(appheight-200))

        # layout
        headerframe.pack(fill="x")
        title.pack(side="left",anchor="nw",fill="x", padx=20,pady=20)
        add_b.pack(side="left", anchor="e", padx=40,pady=30)
        
        self.contentframe.pack(fill="both")

        # updates whenever opening fridge
        self.update_display()

        self.contentframe.grid_columnconfigure((0,1),weight=1, uniform="a")

        

    def update_display(self):
        # destroy widgets being displayed
        for widget in self.contentframe.winfo_children():
            widget.destroy()

        # i = individual food data (list), food = details of a certain individual food data (dict)
        for i, food in enumerate(app.fridge_data):
            # manages storage date
            nstorage_date = datetime.strptime(food["storage_date"], "%Y-%m-%d").date()
            food["days_stored"] = abs(app.today - nstorage_date).days  # difference in days

            # manages expiry date 
            nexpiry_date = datetime.strptime(food["expiry_date"], "%Y-%m-%d").date()
            deadline = (app.today - nexpiry_date).days  # difference in days

            if app.today == nexpiry_date: 
                # difference in days
                food["days_left"] = "Expiring TODAY!"
            elif nexpiry_date < app.today:
                food["days_left"] = f"EXPIRED: {deadline} days"
            else: # if not expired
                food["days_left"] = f"{abs(deadline)} days left"

            nametext = f"{food["name"]}"
            qtytext = f"{food["quantity"]}x"
            exptext = f"{food["days_left"]}" 
            storedtext = f"{food["days_stored"]} days old"

            # create button to display info
            fakebtn = CTkFrame(self.contentframe, corner_radius=20,width=169, height=173,fg_color="#9DB074")
            detail1 = CTkLabel(fakebtn, text=nametext, font=app.normalboldfont, wraplength=100,justify="left",compound="left") # name
            detail2 = CTkLabel(fakebtn, text=qtytext, font=app.subnormalfont) # qty
            detail3 = CTkLabel(fakebtn, text=exptext, font=app.smallfont,height=16) # expiry
            detail4 = CTkLabel(fakebtn, text=storedtext, font=app.smallfont,height=16) # days old in storage
            
            # layout 
            row = i//2 # floor division. each row contains 2 box
            column = i%2 # remainder. two columns
            index = (row*2)+column

            fakebtn.grid(row=row, column=column, pady=3)
            fakebtn.grid_propagate(False)

            fakebtn.columnconfigure((0,1,2), weight=1)
            fakebtn.rowconfigure((0,1,2,3), weight=1)
            detail1.grid(row=0, column=0, columnspan=2, sticky="nw", padx=17,pady=15)
            detail2.grid(row=0, column=1, columnspan=2, sticky="ne", padx=16,pady=15)
            detail3.grid(row=2, column=0, columnspan=3, sticky="sw",padx=23)
            detail4.grid(row=3, column=0, columnspan=3, sticky="nw",padx=23,pady=7)

            # event click binding for left mouse click
            fakebtn.bind("<Button-1>", lambda event, index=index: self.edit_popup(index))
            detail1.bind("<Button-1>", lambda event, index=index: self.edit_popup(index))   # Allow clicking title
            detail2.bind("<Button-1>", lambda event, index=index: self.edit_popup(index)) 
            detail3.bind("<Button-1>", lambda event, index=index: self.edit_popup(index)) 
            detail4.bind("<Button-1>", lambda event, index=index: self.edit_popup(index)) 
            

    def update_frame(self):
        # redo buttons if deleted
        self.contentframe.destroy()
        self.contentframe = CTkScrollableFrame(self,height=(appheight-200))
        self.contentframe.pack(fill="both")

        self.update_display()

    def edit_popup(self, index_list):
        # Open a new window to edit the selected food item.
        if self.editpopup is None or not self.editpopup.winfo_exists():
            self.editpopup = EditFood(self,index_list)  # create window if its None or destroyed
        else:
            self.editpopup.focus()  # if window exists focus it

    def input_popup(self):
        # check if window still exists 
        if self.popup is None or not self.popup.winfo_exists():
            self.popup = InputFood(self)  # create window if its None or destroyed
            
        else:
            self.popup.focus()  # if window exists focus it
    
    def is_valid_date(self, date_string, format="%Y-%m-%d"):
        # check validity of date
        try:
            datetime.strptime(date_string, format)  # try to parse the date
            return True
        except ValueError:
            return False

class InputFood(CTkToplevel):
    def __init__(self, master):
        super().__init__(master=master)
        # settings
        self.geometry("350x400")
        self.title("Adding food to your fridge...")

        self.error_save = False

        # widgets
        title = CTkLabel(self, text="What do you want to add?",font=app.subtitlefont)

        labels = CTkFrame(self)
        foodname_txt = CTkLabel(labels, text="Name",font=app.normalfont)
        qty_txt = CTkLabel(labels, text="Quantity",font=app.normalfont)
        expiry_txt = CTkLabel(labels, text="Expiry date",font=app.normalfont)
        datestored_txt = CTkLabel(labels, text="Date stored",font=app.normalfont)
        
        entries = CTkFrame(self)
        self.foodname = CTkEntry(entries, placeholder_text= "e.g., Salmon", font=app.subnormalfont)
        self.qty = CTkEntry(entries, placeholder_text= "e.g., 1 (whole numbers only)", font=app.subnormalfont)
        self.expiry = CTkEntry(entries, placeholder_text= "format: YYYY-MM-DD", font=app.subnormalfont)
        self.datestored = CTkEntry(entries, placeholder_text= "format: YYYY-MM-DD", font=app.subnormalfont)

        save_b = CTkButton(self, text="Save", font=app.normalfont,
                           command=lambda:self.save_data(master))

        # layout
        title.pack(fill='both',anchor="nw",padx=20,pady=10)

        labels.pack(side="left",fill="both")
        foodname_txt.pack(fill="x",padx=15)
        qty_txt.pack(fill="x",padx=15)
        expiry_txt.pack(fill="x",padx=15)
        datestored_txt.pack(fill="x",padx=15)

        entries.pack(fill='both',padx=10)
        self.foodname.pack(fill="x")
        self.qty.pack(fill="x")
        self.expiry.pack(fill="x")
        self.datestored.pack(fill="x")

        self.datestored.insert(0,str(app.today))

        save_b.pack(anchor="se", padx=10, pady=20)

    def delete_window(self):
        # if window exists, delete
        if self.winfo_exists():
            self.destroy()

    def save_data(self, master):
        # get the input data and remove any unnecessary white space
        foodname = self.foodname.get().strip()
        qty = self.qty.get().strip()
        exp = self.expiry.get().strip()
        datestored = self.datestored.get().strip()

        # input validity tracker
        can_save = False

        # input validity, check for empty/none/blankspace-only value 
        templist = (foodname,qty,exp,datestored)
        for x in templist:
            if x is None or x == "":
                can_save = False
                break
            else:
                can_save = True

        # check if qty input is an integer 
        if not qty.isdigit() or not master.is_valid_date(exp) or not master.is_valid_date(datestored):
            can_save = False

        # proceed when input is valid
        if can_save == True: 
            # store data into dictionary
            food_data = {
                    "name": foodname,
                    "quantity": int(qty),
                    "expiry_date": exp,
                    "storage_date": datestored
                    }
            # add dictionary to list
            app.fridge_data.append(food_data)

            # delete window after saving
            self.delete_window()

            # update display on fridge
            master.update_display()
        else:
            # prompt error to user if msg hasnt shown up before
            if self.error_save == False:
                self.error = CTkLabel(self,text="There are mistake(s) in your input.\nCheck again.",text_color="#FF5733", font=app.subnormalfont)
                self.error.pack(anchor="w",padx=10)
                self.error_save = True

class EditFood(CTkToplevel):
    def __init__(self, master,index):
        super().__init__(master=master)
        # settings
        self.title("Editing Your Food Info...")
        self.geometry("350x400")
        
        self.food = app.fridge_data[index]  # Get the selected food dictionary

        # widgets
        title = CTkLabel(self, text="What do you want to add?",font=app.subtitlefont)

        labels = CTkFrame(self)
        foodname_txt = CTkLabel(labels, text="Name",font=app.normalfont)
        qty_txt = CTkLabel(labels, text="Quantity",font=app.normalfont)
        expiry_txt = CTkLabel(labels, text="Expiry date",font=app.normalfont)
        datestored_txt = CTkLabel(labels, text="Date stored",font=app.normalfont)
        
        entries = CTkFrame(self)
        self.foodname = CTkEntry(entries, placeholder_text= "e.g., Salmon)", font=app.subnormalfont)
        self.foodname.insert(0,str(self.food["name"])) 

        self.qty = CTkEntry(entries, placeholder_text= "e.g., 1 (whole numbers only)", font=app.subnormalfont)
        self.qty.insert(0, str(self.food["quantity"]))

        self.expiry = CTkEntry(entries, placeholder_text= "format: YYYY-MM-DD", font=app.subnormalfont)
        self.expiry.insert(0, str(self.food["expiry_date"]))

        self.datestored = CTkEntry(entries, placeholder_text= "format: YYYY-MM-DD", font=app.subnormalfont)
        self.datestored.insert(0, str(self.food["storage_date"]))

        save_b = CTkButton(self, text="Save", font=app.normalfont,
                           command=lambda:self.save_changes(master))
        delete_b = CTkButton(self, text="Remove food", font=app.normalfont,
                           command=lambda:self.delete_data(master,index))
        
        # layout
        title.pack(fill='both',anchor="nw",padx=20,pady=10)

        labels.pack(side="left",fill="both")
        foodname_txt.pack(fill="x",padx=15)
        qty_txt.pack(fill="x",padx=15)
        expiry_txt.pack(fill="x",padx=15)
        datestored_txt.pack(fill="x",padx=15)

        entries.pack(fill='both',padx=10)
        self.foodname.pack(fill="x")
        self.qty.pack(fill="x")
        self.expiry.pack(fill="x")
        self.datestored.pack(fill="x")

        save_b.pack(anchor="se", padx=10, pady=20)
        delete_b.pack(anchor="sw", padx=10, pady=20)

    # Save button to save updates to data
    def save_changes(self,master):
        foodname = self.foodname.get().strip()
        qty = self.qty.get().strip()
        exp = self.expiry.get().strip()
        datestored = self.datestored.get().strip()

        # tracker status 
        can_save = False

        # input validity, check for empty/none/blankspace-only value 
        templist = (foodname,qty,exp,datestored)
        for x in templist:
            if x is None or x == "":
                can_save = False
                break
            else:
                can_save = True

        # check if qty input is an integer 
        if not qty.isdigit() or not master.is_valid_date(exp) or not master.is_valid_date(datestored):
            can_save = False

        # proceed when input is valid
        if can_save == True: 
            # change into new data in the dictionary indexed
            self.food["name"] = foodname
            self.food["quantity"] = int(qty)
            self.food["expiry_date"] = exp
            self.food["storage_date"] = datestored
            
            # delete window after saving
            self.delete_window()

            # update display on fridge
            master.update_display()
        else:
            # prompt error to user if msg hasnt shown up before
            if self.error_save == False:
                self.error = CTkLabel(self,text="There are mistake(s) in your input.\nCheck again.",text_color="#FF5733", font=app.subnormalfont)
                self.error.pack(anchor="w",padx=10)
                self.error_save = True

    def delete_data(self,master,index):
        # remove food data from fridge data based on index of block being edited
        app.fridge_data.pop(index)

        # update display on fridge
        master.update_display()
        
        # delete window after deleting all data
        self.delete_window()


        

    def delete_window(self):
        # if window exists, delete
        if self.winfo_exists():
            self.destroy()




# read all kinds of guide on preventing food waste
class Guide(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=appwidth, height=appheight)

        title = CTkLabel(self,text="Guide",font=app.titlefont)
        desc = CTkLabel(self,text="How to Prevent Food Waste 101",font=app.normalfont)

        listframe = CTkScrollableFrame(self)
        b1 = CTkButton(listframe,height=150, text=guide_title1, font=app.subtitlefont,command=lambda: master.switchframe_inapp(Guide1))
        b2 = CTkButton(listframe,height=150, text=guide_title2, font=app.subtitlefont,command=lambda: master.switchframe_inapp(Guide2))
        b3 = CTkButton(listframe,height=150, text=guide_title3, font=app.subtitlefont,command=lambda: master.switchframe_inapp(Guide3))

        title.pack(side="top",anchor="nw",padx=20,pady=20)
        desc.pack(side="top",anchor="nw",padx=20,pady=10)

        listframe.pack(side="left",fill="both",expand=True)
        b1.pack(anchor="w", fill="x",padx=10,pady=10)
        b2.pack(anchor="w", fill="x",padx=10,pady=10)
        b3.pack(anchor="w", fill="x",padx=10,pady=10)

class Guide1(CTkFrame):
    def __init__(self, master): 
        super().__init__(master=master, width=appwidth, height=appheight)
        
        title = CTkLabel(self,text=guide_title1,font=app.subtitlefont)
        
        back_b = CTkButton(self, 
                           text="Go back",
                           command=lambda: master.switchframe_inapp(Guide))
        self.textbox = CTkTextbox(self,scrollbar_button_color="#FFCC70",font=app.normalfont,
                             corner_radius=20, wrap="word", 
                             height=(appheight-395), width=appheight)
        
        # layout
        back_b.pack(side="top",anchor="ne")
        title.pack(side="top",anchor="nw",padx=20,pady=20)
        self.textbox.pack(fill="both",expand=True,padx=10,pady=15)

        self.textbox.insert("0.0", guide_txt1)
        self.textbox.configure(state="disabled")


class Guide2(CTkFrame):
    def __init__(self, master): 
        super().__init__(master=master, width=appwidth, height=appheight)
        
        title = CTkLabel(self,text=guide_title2,font=app.subtitlefont)
        
        back_b = CTkButton(self, 
                           text="Go back",
                           command=lambda: master.switchframe_inapp(Guide))
        
        self.textbox = CTkTextbox(self,scrollbar_button_color="#FFCC70",font=app.normalfont,
                             corner_radius=20, wrap="word", 
                             height=(appheight-395), width=appheight)
        
        
        
        # layout
        back_b.pack(side="top",anchor="ne")
        title.pack(side="top",anchor="nw",padx=20,pady=20)
        self.textbox.pack(fill="both",expand=True,padx=10,pady=15)

        self.textbox.insert("0.0", guide_txt2)
        self.textbox.configure(state="disabled")

class Guide3(CTkFrame):
    def __init__(self, master): 
        super().__init__(master=master, width=appwidth, height=appheight)
        
        title = CTkLabel(self,text=guide_title3,font=app.subtitlefont)
        
        back_b = CTkButton(self, 
                           text="Go back",
                           command=lambda: master.switchframe_inapp(Guide))
        
        self.textbox = CTkTextbox(self,scrollbar_button_color="#FFCC70",font=app.normalfont,
                             corner_radius=20, wrap="word",  
                             height=(appheight-395), width=appheight)
        # layout
        back_b.pack(side="top",anchor="ne")
        title.pack(side="top",anchor="nw",padx=20,pady=20)
        self.textbox.pack(fill="both",expand=True,padx=10,pady=15)

        self.textbox.insert("0.0", guide_txt3)
        self.textbox.configure(state="disabled")



# make a list for grocery shopping (or other things...)
class GroceryList(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master, width=appwidth, height=appheight)

        title = CTkLabel(self,text="Grocery List",font=app.titlefont)
        desc = CTkLabel(self,text="Write down your shopping list here!",font=app.normalfont)

        
        self.textbox = CTkTextbox(self,scrollbar_button_color="#FFCC70",font=app.normalfont,
                             corner_radius=20, wrap="word", height=(appheight-395), width=appheight)
        save_b = CTkButton(self,text="Save list", font=app.normalfont,
                           command=self.save_text)

        # layout 
        title.pack(anchor="nw",padx=20,pady=20)
        desc.pack(anchor="w",padx=20,pady=10)
        self.textbox.pack(side="top",expand=True,padx=15)
        save_b.pack(side="bottom",anchor="se",padx=20,pady=20)

         # restore list that user has made (if they did) every time this list is opened
        if app.grocerylist_txt != "":
            self.restore_text()

    def save_text(self):
        savedtext = self.textbox.get(0.0, 'end')
        app.grocerylist_txt = savedtext
    
    def restore_text(self):
        self.textbox.insert('end',app.grocerylist_txt)



class Recipe(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master, width=appwidth, height=appheight)

        title = CTkLabel(self,text="Recipes List",font=app.titlefont)
        desc = CTkLabel(self,text="List of recipes for leftovers, coming soon!",font=app.normalboldfont)

        title.pack(side="top",anchor="nw",padx=20,pady=20)
        desc.pack(side="top",anchor="nw",padx=20,pady=10)


# driver code — run app (the whole thing)
if __name__ == "__main__":
    app = App()
    app.mainloop()
