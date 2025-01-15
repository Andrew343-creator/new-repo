from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import mysql.connector
import bcrypt
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

class InventoryApp(BoxLayout):
    def __init__(self, **kwargs):
        super(InventoryApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        # Set background color through Canvas instructions
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Light gray background color (RGB + Alpha)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Update the rectangle when the size or position changes
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.title_label = Label(text='Login', font_size=32, color=(0, 0, 0, 1))
        self.add_widget(self.title_label)

        self.username_label = Label(text='Username:', font_size=20, color=(0, 0, 0, 1))
        self.add_widget(self.username_label)

        self.username_input = TextInput(multiline=False, font_size=18, size_hint_y=None, height=40)
        self.username_input.background_color = (1, 1, 1, 0.8)  # Light background for input fields
        self.add_widget(self.username_input)

        self.password_label = Label(text='Password:', font_size=20, color=(0, 0, 0, 1))
        self.add_widget(self.password_label)

        self.password_input = TextInput(password=True, multiline=False, font_size=18, size_hint_y=None, height=40)
        self.password_input.background_color = (1, 1, 1, 0.8)  # Light background for input fields
        self.add_widget(self.password_input)

        # Buttons with styling
        self.login_button = Button(text='Login', font_size=18, background_color=(0.2, 0.6, 1, 1), size_hint_y=None, height=50)
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

        self.register_button = Button(text='Register', font_size=18, background_color=(0.6, 0.8, 0.2, 1), size_hint_y=None, height=50)
        self.register_button.bind(on_press=self.register)
        self.add_widget(self.register_button)

        self.forgot_password_button = Button(text='Forgot Password?', font_size=14, background_color=(1, 0.3, 0.3, 1), size_hint_y=None, height=40)
        self.forgot_password_button.bind(on_press=self.forgot_password)
        self.add_widget(self.forgot_password_button)

    # Update the rectangle's position and size when the layout changes
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def login(self, instance):
        try:
            username = self.username_input.text
            password = self.password_input.text

            if not username or not password:
                self.show_login_error_popup('Please enter all fields')
                return

            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            query = "SELECT password FROM Owner WHERE username = %s"
            cur.execute(query, (username,))

            result = cur.fetchone()
            if result:
                stored_password = result[0]
                if bcrypt.checkpw(password.encode(), stored_password.encode()):
                    self.show_login_success_popup()
                    self.clear_widgets()
                    self.post_login_window1()
                else:
                    self.show_login_error_popup('Incorrect username or password')
            else:
                self.show_login_error_popup('Incorrect username or password')

            cnx.close()
        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
    
    def back(self, instance):
    
        self.clear_widgets()
        self.post_login_window()

    def back1(self, instance):
    
        self.clear_widgets()
        self.post_login_window1()
    def Accounting(self, instance):
    
        self.clear_widgets()
        self.Accounting_form()

    

    def Accounting_form(self):
        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title label
        self.title_label = Label(text='Inventory Management', font_size=24, size_hint_y=None, height=50)
        layout.add_widget(self.title_label)

        # Profit calculations button
        self.profit_button = Button(text='Profit Calculations', font_size=18, size_hint_y=None, height=50)
        self.profit_button.bind(on_press=self.Profit_inventory)
        layout.add_widget(self.profit_button)

        # Sell item button
        self.sell_item_button = Button(text='Sell Item', font_size=18, size_hint_y=None, height=50)
        self.sell_item_button.bind(on_press=self.sell_item)
        layout.add_widget(self.sell_item_button)

        # Sales history button
        self.sales_button = Button(text='Sales History', font_size=18, size_hint_y=None, height=50)
        self.sales_button.bind(on_press=self.sales_history)
        layout.add_widget(self.sales_button)

        # discount button
        self.discount_button = Button(text='create discount code', font_size=18, size_hint_y=None, height=50)
        self.discount_button.bind(on_press=self.discount)
        layout.add_widget(self.discount_button)

        # Back button
        self.back_button = Button(text='Back', font_size=18, size_hint_y=None, height=50)
        self.back_button.bind(on_press=self.back1)
        layout.add_widget(self.back_button)

        # Add the layout to the main widget
        self.add_widget(layout)


    def post_login_window1(self):  # Renamed function
         # Background color
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Dark gray background
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_background_rect, pos=self.update_background_rect)  # Updated function name

        # Title Label
        self.title_label = Label(text='Inventory Management', font_size=24, color=(1, 1, 1, 1))
        self.add_widget(self.title_label)

        # Buttons Layout
        self.button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Inventory Management Button
        self.remove_item_button = Button(text='Inventory Management', font_size=18)
        self.remove_item_button.bind(on_press=self.back)
        self.remove_item_button.background_color = (0.1, 0.5, 0.8, 1)  # Blue color
        self.button_layout.add_widget(self.remove_item_button)

        # Accounting and Selling Button
        self.accounting_button = Button(text='Accounting and Selling', font_size=18)
        self.accounting_button.bind(on_press=self.Accounting)
        self.accounting_button.background_color = (0.1, 0.8, 0.5, 1)  # Green color
        self.button_layout.add_widget(self.accounting_button)

        # Logout Button
        self.logout_button = Button(text='Logout', font_size=18)
        self.logout_button.bind(on_press=self.logout)
        self.logout_button.background_color = (0.8, 0.1, 0.1, 1)  # Red color
        self.button_layout.add_widget(self.logout_button)

        self.add_widget(self.button_layout)

    def update_background_rect(self, instance, value):  # Updated function name
        self.rect.pos = self.pos
        self.rect.size = self.size
            

    def post_login_window(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.add_item_button = Button(text='Add Item', font_size=18)
        self.add_item_button.bind(on_press=self.add_item)
        self.add_widget(self.add_item_button)

        self.view_inventory_button = Button(text='View Inventory', font_size=18)
        self.view_inventory_button.bind(on_press=self.view_inventory)
        self.add_widget(self.view_inventory_button)

        self.update_item_button = Button(text='Update Item', font_size=18)
        self.update_item_button.bind(on_press=self.update_item)
        self.add_widget(self.update_item_button)

        self.remove_item_button = Button(text='Remove Item', font_size=18)
        self.remove_item_button.bind(on_press=self.remove_item)
        self.add_widget(self.remove_item_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.back1)
        self.add_widget(self.back_button)

    def logout(self, instance):
        self.clear_widgets()
        self.__init__()

    def add_item(self, instance):
        self.clear_widgets()
        self.add_form()
        
    def add_form(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.itemname_label = Label(text="Item name:")
        self.add_widget(self.itemname_label)

        self.itemname_input = TextInput(multiline=False)
        self.add_widget(self.itemname_input)

        self.quantity_label = Label(text="Quantity:")
        self.add_widget(self.quantity_label)

        self.quantity_input = TextInput(multiline=False)
        self.add_widget(self.quantity_input)

        self.order_price_label = Label(text="Order Price:")
        self.add_widget(self.order_price_label)

        self.order_price_input = TextInput(multiline=False)
        self.add_widget(self.order_price_input)

        self.selling_price_label = Label(text="Selling Price:")
        self.add_widget(self.selling_price_label)

        self.selling_price_input = TextInput(multiline=False)
        self.add_widget(self.selling_price_input)

        self.add_item_button = Button(text='Add', font_size=18)
        self.add_item_button.bind(on_press=self.add)
        self.add_widget(self.add_item_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.back)
        self.add_widget(self.back_button)
    
    
    def add(self,instance):
        try:
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            query2 = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query2, (self.username_input.text,))

            id_list = cur.fetchone()

            id = id_list[0]

            name = self.itemname_input.text
            quantity = int(self.quantity_input.text)
            order_price = float(self.order_price_input.text)
            selling_price = float(self.selling_price_input.text)
            date=datetime.now()
           

            cur.execute("select itemname from Items where ownerid=%s",(id,))

            results=cur.fetchall()

            for result in results:
                if name in result[0]:
                    
                    query="select Ordered_quantity,Available_quantity, order_price, selling_price from Items where itemname=%s and ownerid=%s"
                    cur.execute(query,(name,id))
                    output=cur.fetchone()

                    if order_price!=output[2] and selling_price!=output[3]:
                        logging.error(f"Information error")
                        self.show_login_error_popup('Order and selling price do not match with the previous orders!!')
                        return
                    else:
                        new_ordered=output[0]+quantity
                        new_available=output[1]+quantity

                        query2="UPDATE Items SET Ordered_quantity = %s, Available_quantity=%s, date=%s WHERE itemname =%s AND ownerid = %s"

                        cur.execute(query2,(new_ordered,new_available,date,name,id,))
                        
                        cnx.commit()
                        self.addition()
                        return
                        
                    
                    



            query4 = "INSERT INTO Items(ownerid, itemname, Ordered_quantity,Available_quantity, order_price,selling_price,date) VALUES (%s, %s, %s,%s, %s,%s,%s)"
            cur.execute(query4, (id, name, quantity,quantity, order_price,selling_price,date))

            cnx.commit()
            cnx.close()
            self.addition()
        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except ValueError:
            logging.error(f"Input Error.")
            self.show_login_error_popup('Please enter the correct details!')

       

    def view_inventory(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a database connection
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            query2 = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query2, (self.username_input.text,))
            id_list = cur.fetchone()

            if id_list is None:
                self.show_login_error_popup('User not found')
                return

            owner_id = id_list[0]

            # Fetch items associated with the owner ID
            query4 = "SELECT itemname, Ordered_quantity, Available_quantity, order_price, selling_price, date FROM Items WHERE ownerid = %s"
            cur.execute(query4, (owner_id,))
            result = cur.fetchall()

            # Clear existing widgets and display the inventory
            self.clear_widgets()

            # Create a main layout
            main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

            # Title Label
            self.title_label = Label(text='Ordered Inventory', font_size=24, bold=True, color=(0, 0, 0, 1))
            main_layout.add_widget(self.title_label)

            # Create a ScrollView for the inventory items
            scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
            grid_layout = GridLayout(cols=6, size_hint_y=None)
            grid_layout.bind(minimum_height=grid_layout.setter('height'))

            # Add header row
            headers = ["Item Name", "Ordered Quantity", "Available Quantity", "Order Price", "Selling Price", "Date"]
            for header in headers:
                header_label = Label(text=header, size_hint_y=None, height=40, bold=True)
                grid_layout.add_widget(header_label)

            # Add items to the grid layout
            for item in result:
                for value in item:
                    item_label = Label(
                        text=str(value),
                        size_hint_y=None,
                        height=40
                    )
                    grid_layout.add_widget(item_label)

            scroll_view.add_widget(grid_layout)
            main_layout.add_widget(scroll_view)

            # Back Button
            self.add_item_button = Button(text='Back', font_size=18, size_hint_y=None, height=50)
            self.add_item_button.bind(on_press=self.back)
            main_layout.add_widget(self.add_item_button)

            self.add_widget(main_layout)

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur is not None:
                cur.close()
            if cnx is not None:
                cnx.close()




    def update_item(self, instance):
        self.clear_widgets()
        self.update_form()
    
    def update_form(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.Uitemname_label = Label(text="Item name:")
        self.add_widget(self.Uitemname_label)

        self.Uitemname_input = TextInput(multiline=False)
        self.add_widget(self.Uitemname_input)

        self.new_quantity_label = Label(text="New Quantity:")
        self.add_widget(self.new_quantity_label)

        self.new_quantity_input = TextInput(multiline=False)
        self.add_widget(self.new_quantity_input)

        self.new_order_price_label = Label(text="New Order Price:")
        self.add_widget(self.new_order_price_label)

        self.new_order_price_input = TextInput(multiline=False)
        self.add_widget(self.new_order_price_input)

        self.new_selling_price_label = Label(text="New Selling Price:")
        self.add_widget(self.new_selling_price_label)

        self.new_selling_price_input = TextInput(multiline=False)
        self.add_widget(self.new_selling_price_input)

        self.add_item_button = Button(text='Update', font_size=18)
        self.add_item_button.bind(on_press=self.update)
        self.add_widget(self.add_item_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.back)
        self.add_widget(self.back_button)


    def update(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query_owner_id, (self.username_input.text,))
            owner_id_result = cur.fetchone()

            # Check if the owner ID was found
            if owner_id_result is None:
                self.item_does_not_exist()  # Handle case where username is not found
                return

            owner_id = owner_id_result[0]
            item_name = self.Uitemname_input.text.strip()
            new_quantity = self.new_quantity_input.text.strip()
            new_order_price = self.new_order_price_input.text.strip()
            new_selling_price = self.new_selling_price_input.text.strip()
            current_date = datetime.now().date()  # Get the current date

            # Validate inputs
            if not item_name or not new_quantity.isdigit() or not new_order_price.replace('.', '', 1).isdigit() or not new_selling_price.replace('.', '', 1).isdigit():
                self.show_login_error_popup('Invalid input. Please check your entries.')
                return

            # Check if the item exists for the given owner
            query_item_exists = "SELECT itemname FROM Items WHERE ownerid = %s AND itemname = %s"
            cur.execute(query_item_exists, (owner_id, item_name))
            item_exists = cur.fetchone()

            if item_exists is None:
                self.item_does_not_exist()  # Handle case where item does not exist
                return

            # Update the item
            update_query = """
            UPDATE Items 
            SET Ordered_quantity = %s, Available_quantity = %s, order_price = %s, selling_price = %s, date = %s 
            WHERE itemname = %s AND ownerid = %s
            """
            cur.execute(update_query, (new_quantity, new_quantity, new_order_price, new_selling_price, current_date, item_name, owner_id))

            # Commit the changes
            cnx.commit()
            self.updating()  # Notify user of successful update

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()


    def remove_item(self, instance):
        self.clear_widgets()
        self.remove_form()
    
    def remove_form(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.Ritemname_label = Label(text="Item name:")
        self.add_widget(self.Ritemname_label)

        self.Ritemname_input = TextInput(multiline=False)
        self.add_widget(self.Ritemname_input)


        self.add_item_button = Button(text='Remove', font_size=18)
        self.add_item_button.bind(on_press=self.remove)
        self.add_widget(self.add_item_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.back)
        self.add_widget(self.back_button)


    

    def remove(self, instance):
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            query2 = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query2, (self.username_input.text,))
            id_list = cur.fetchone()

            # Check if the owner ID was found
            if id_list is None:
                self.item_does_not_exist()  # Handle case where username is not found
                return

            owner_id = id_list[0]
            item_name = self.Ritemname_input.text

            # Check if the item exists for the given owner
            cur.execute("SELECT itemname FROM Items WHERE ownerid = %s", (owner_id,))
            results = cur.fetchall()

            # Check if the item name exists in the results
            item_exists = any(item_name == result[0] for result in results)

            if not item_exists:
                self.item_does_not_exist()  # Handle case where item does not exist
                return

            # Delete related records in Sold table first
            cur.execute("DELETE FROM Sold WHERE itemid = (SELECT id FROM Items WHERE itemname = %s AND ownerid = %s)", (item_name, owner_id))

            # Now delete the item
            query4 = "DELETE FROM Items WHERE itemname = %s AND ownerid = %s"
            cur.execute(query4, (item_name, owner_id))

            # Commit the changes
            cnx.commit()
            self.deleting()  # Notify user of successful deletion

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()



    def register(self, instance):
        self.clear_widgets()
        self.register_form()

    def register_form(self):
        self.title_label = Label(text='Register', font_size=24,color='black')
        self.add_widget(self.title_label)

        self.username_label = Label(text='Username:',color='black')
        self.add_widget(self.username_label)

        self.username_input = TextInput(multiline=False, font_size=18)
        self.add_widget(self.username_input)

        self.password_label = Label(text='Password:',color='black')
        self.add_widget(self.password_label)

        self.password_input = TextInput(password=True, multiline=False, font_size=18)
        self.add_widget(self.password_input)

        self.confirm_password_label = Label(text='Confirm Password:',color='black')
        self.add_widget(self.confirm_password_label)

        self.confirm_password_input = TextInput(password=True, multiline=False, font_size=18)
        self.add_widget(self.confirm_password_input)

        self.register_button = Button(text='Register', font_size=18)
        self.register_button.bind(on_press=self.register_user)
        self.add_widget(self.register_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.back_to_login)
        self.add_widget(self.back_button)

    def register_user(self, instance):
        try:
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()
            query2 = "SELECT username FROM Owner"
            cur.execute(query2)

            users = cur.fetchall()

            username = self.username_input.text
            password = self.password_input.text
            confirm_password = self.confirm_password_input.text

            if not username or not password or not confirm_password:
                self.show_register_error_popup('Please enter all fields')
                return
            for user in users:
                if username in user[0]:
                    self.show_user_exists_popup()
                    return

            if password != confirm_password:
                self.show_register_error_popup('Passwords do not match')
                return

            query = "INSERT INTO Owner(username, password) VALUES (%s, %s)"
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            cur.execute(query, (username, hashed_password))

            cnx.commit()
            cnx.close()

            self.show_register_success_popup()
        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_register_error_popup('Database error')

    def back_to_login(self, instance):
        self.clear_widgets()
        self.__init__()

    def forgot_password(self, instance):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Forgot Password', content=Label(text='Enter your email address to reset your password'), size_hint=(None, None), size=(400, 200))
        popup.open()
    

    def show_login_success_popup(self):
        popup = Popup(title='Login Success', content=Label(text='You have logged in successfully'), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_login_error_popup(self, message):
        popup = Popup(title='Login Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_register_success_popup(self):
        popup = Popup(title='Register Success', content=Label(text='You have registered successfully'), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_user_exists_popup(self):
        popup = Popup(title='Username already exists.', content=Label(text='Please enter another username.'), size_hint=(None, None), size=(400, 200))
        popup.open()
    
    def item_does_not_exist(self):
        popup = Popup(title='Item does not exist.', content=Label(text='Please enter valid item name.'), size_hint=(None, None), size=(400, 200))
        popup.open()
    def quantity_does_not_exist(self):
        popup = Popup(title='Quantity exceeded', content=Label(text='Please enter valid item quantity.'), size_hint=(None, None), size=(400, 200))
        popup.open()

    

    def show_register_error_popup(self, message):
        popup = Popup(title='Register Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
    def failure(self):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Code', content=Label(text='Code Already exists!.'), size_hint=(None, None), size=(400, 200))
        popup.open()
    
    def addition(self):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Items', content=Label(text='Item successfully added.'), size_hint=(None, None), size=(400, 200))
        popup.open()
    
    def sellation(self):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Items', content=Label(text='Item successfully sold.'), size_hint=(None, None), size=(400, 200))
        popup.open()
    
    
    def updating(self):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Items', content=Label(text='Item successfully updated.'), size_hint=(None, None), size=(400, 200))
        popup.open()
        self.clear_widgets()
        self.update_form()
    def deleting(self):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Items', content=Label(text='Item successfully removed.'), size_hint=(None, None), size=(400, 200))
        popup.open()
        self.clear_widgets()
        self.remove_form()
    def quantiting(self):
        # Show a popup to enter the email address to send the password reset link
        popup = Popup(title='Items', content=Label(text='Item quantity is has exceeded the ordered quantity.'), size_hint=(None, None), size=(400, 200))
        popup.open()
        
        

    def sell_item(self, instance):
        self.clear_widgets()
        self.sell_form()

    def sell_item_at_discount(self, instance):
        self.clear_widgets()
        self.sad_form()

    def discount(self, instance):
        self.clear_widgets()
        self.discount_form()



    def sell_form(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.sitemname_label = Label(text="Item name:")
        self.add_widget(self.sitemname_label)

        self.sitemname_input = TextInput(multiline=False)
        self.add_widget(self.sitemname_input)

        self.squantity_label = Label(text="Quantity:")
        self.add_widget(self.squantity_label)

        self.squantity_input = TextInput(multiline=False)
        self.add_widget(self.squantity_input)

        self.register_button = Button(text='Sell item At original price.', font_size=18)
        self.register_button.bind(on_press=self.sell)
        self.add_widget(self.register_button)

        self.register_button = Button(text='Sell item At Discount.', font_size=18)
        self.register_button.bind(on_press=self.sell_item_at_discount)
        self.add_widget(self.register_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.Accounting)
        self.add_widget(self.back_button)
    def sad_form(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.itemname_label = Label(text="Item name:")
        self.add_widget(self.itemname_label)
        self.itemname_input = TextInput(multiline=False)
        self.add_widget(self.itemname_input)

        self.quantity_label = Label(text="Quantity:")
        self.add_widget(self.quantity_label)
        self.quantity_input = TextInput(multiline=False)
        self.add_widget(self.quantity_input)

        self.code_label = Label(text="Discount Code:")
        self.add_widget(self.code_label)
        self.code_input = TextInput(multiline=False)
        self.add_widget(self.code_input)

        
        
        self.create_button = Button(text='Discount sell', font_size=18)
        self.create_button.bind(on_press=self.sell_at_discount)
        self.add_widget(self.create_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.Accounting)
        self.add_widget(self.back_button)

    def discount_form(self):
        self.title_label = Label(text='Inventory Management', font_size=24)
        self.add_widget(self.title_label)

        self.code1_label = Label(text="Code name:")
        self.add_widget(self.code1_label)

        self.code1_input = TextInput(multiline=False)
        self.add_widget(self.code1_input)

        self.amount1_label = Label(text="Amount:")
        self.add_widget(self.amount1_label)

        self.amount1_input = TextInput(multiline=False)
        self.add_widget(self.amount1_input)

        self.create_button = Button(text='Create', font_size=18)
        self.create_button.bind(on_press=self.discount1)
        self.add_widget(self.create_button)

        self.back_button = Button(text='Back', font_size=18)
        self.back_button.bind(on_press=self.Accounting)
        self.add_widget(self.back_button)

    def discount1(self,instance):
        try:
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            query2 = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query2, (self.username_input.text,))

            id_list = cur.fetchone()

            id = id_list[0]

            code = str(self.code1_input.text.strip())
            amount = int(self.amount1_input.text.strip())
            date=datetime.now()

            cur.execute("select code from Codes where ownerid=%s",(id,))

            code_list=cur.fetchall()

            for codes in code_list:
                if code in code_list[0]:                      
                    logging.error(f"Input Error.")
                    self.show_login_error_popup('Discount Code Exists!')
                    return
                    
            query4 = "INSERT INTO Codes(code, amount, ownerid, date) VALUES (%s, %s, %s, %s)"
            cur.execute(query4, (code,amount,id,date))

            cnx.commit()
            cnx.close()
            self.addition()
        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except ValueError:
            logging.error(f"Input Error.")
            self.show_login_error_popup('Please enter the correct details!')
    def sell_at_discount(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            username = self.username_input.text.strip()
            if not username:
                self.show_login_error_popup('Username cannot be empty.')
                return

            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query_owner_id, (username,))
            owner_id_result = cur.fetchone()

            if owner_id_result is None:
                self.item_does_not_exist()  # Handle case where username is not found
                return

            owner_id = owner_id_result[0]

            # Get item details from user input
            item_name = self.itemname_input.text.strip()
            quantity_to_sell = int(self.quantity_input.text.strip())
            discount_code=self.code_input.text.strip()
            current_date = datetime.now()
            
            #Get discount codes from user database and pair with amount
            cur.execute("select code from Codes where ownerid = %s ",(owner_id,))
            codes=cur.fetchone()
            if discount_code==codes[0]:
            
                    
                    cur.execute("select amount from Codes where ownerid=%s and code=%s",(owner_id,discount_code))
                    amount_list=cur.fetchone()
                    discount_amount=amount_list[0]

                    # Check if the item exists and get available quantity
                    query_item = "SELECT id, Available_quantity, selling_price FROM Items WHERE itemname = %s AND ownerid = %s"
                    cur.execute(query_item, (item_name, owner_id))
                    item_result = cur.fetchone()

                    if item_result is None:
                        self.item_does_not_exist()  # Handle case where item does not exist 
                        return
                    item_id, available_quantity,sell_price = item_result

                        # Check if there is enough quantity available
                    if quantity_to_sell > available_quantity:
                        self.quantity_does_not_exist()  # Handle case where quantity is insufficient
                        return
                    #Calculate the new sell price after discount
                    new_sell_price=sell_price-discount_amount
                    
                    # Insert the sale record
                    insert_query = "INSERT INTO Sold(itemid, sold_quantity,selling_price,discount_amount, date) VALUES (%s, %s, %s,%s,%s)"
                    cur.execute(insert_query, (item_id, quantity_to_sell, new_sell_price,discount_amount,current_date))

                    # Update the available quantity in the Items table
                    new_available_quantity = available_quantity - quantity_to_sell
                    update_query = "UPDATE Items SET Available_quantity = %s WHERE id = %s"
                    cur.execute(update_query, (new_available_quantity, item_id))

                    # Commit the changes
                    cnx.commit()
                    self.sellation()  # Notify user of successful sale
                    return
            else:
                    print("Not Good")
                    return
                
            
        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()
    
    def sell(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            username = self.username_input.text.strip()
            if not username:
                self.show_login_error_popup('Username cannot be empty.')
                return

            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query_owner_id, (username,))
            owner_id_result = cur.fetchone()

            if owner_id_result is None:
                self.item_does_not_exist()  # Handle case where username is not found
                return

            owner_id = owner_id_result[0]

            # Get item details from user input
            item_name = self.sitemname_input.text.strip()
            quantity_to_sell = int(self.squantity_input.text.strip())
            current_date = datetime.now()

            # Check if the item exists and get available quantity and selling price
            query_item = "SELECT id, Available_quantity,selling_price FROM Items WHERE itemname = %s AND ownerid = %s"
            cur.execute(query_item, (item_name, owner_id))
            item_result = cur.fetchone()

            if item_result is None:
                self.item_does_not_exist()  # Handle case where item does not exist
                return

            item_id, available_quantity, sell_price= item_result

            # Check if there is enough quantity available
            if quantity_to_sell > available_quantity:
                self.quantity_does_not_exist()  # Handle case where quantity is insufficient
                return

            # Insert the sale record
            insert_query = "INSERT INTO Sold(itemid, sold_quantity,selling_price,discount_amount, date) VALUES (%s, %s, %s, %s,%s)"
            cur.execute(insert_query, (item_id, quantity_to_sell,sell_price,0,current_date))

            # Update the available quantity in the Items table
            new_available_quantity = available_quantity - quantity_to_sell
            update_query = "UPDATE Items SET Available_quantity = %s WHERE id = %s"
            cur.execute(update_query, (new_available_quantity, item_id))
            
            # Commit the changes
            cnx.commit()
            self.sellation()  # Notify user of successful sale

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()
    def attained_profits(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            username = self.username_input.text.strip()
            if not username:
                self.show_login_error_popup('Username cannot be empty.')
                return

            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query_owner_id, (username,))
            owner_id_result = cur.fetchone()

            if owner_id_result is None:
                self.show_login_error_popup('User not found.')
                return

            owner_id = owner_id_result[0]

            # Fetch sales history
            query_sales_history = """
            SELECT Items.itemname, Sold.sold_quantity, Items.order_price,Sold.selling_price,Sold.discount_amount,Sold.date 
            FROM Items 
            INNER JOIN Sold ON Items.id = Sold.itemid 
            WHERE Items.ownerid = %s
            """
            cur.execute(query_sales_history, (owner_id,))
            sales_history_results = cur.fetchall()

            # Clear existing widgets
            self.clear_widgets()

            # Create a main layout
            main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

            # Title Label
            title_label = Label(text='Sales History', font_size=24, bold=True, color=(0, 0, 0, 1))
            main_layout.add_widget(title_label)

            # Create a ScrollView for the sales history items
            scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
            grid_layout = GridLayout(cols=6, size_hint_y=None)
            grid_layout.bind(minimum_height=grid_layout.setter('height'))

            # Add headers
            headers = ["Item Name","Sold Quantity","Order Price","Selling Price","Discount", "Date"]
            for header in headers:
                header_label = Label(text=header, size_hint_y=None, height=40, bold=True)
                grid_layout.add_widget(header_label)

            # Check if there are results and add sales history items to the grid layout
            if sales_history_results:
                for item in sales_history_results:
                    for value in item:
                        item_label = Label(
                            text=str(value),
                            size_hint_y=None,
                            height=40
                        )
                        grid_layout.add_widget(item_label)
            else:
                no_data_label = Label(text="No sales history found.", size_hint_y=None, height=40)
                grid_layout.add_widget(no_data_label)

            scroll_view.add_widget(grid_layout)
            main_layout.add_widget(scroll_view)
            #Attained  profit from selling 
            total_profit = 0
            for item in sales_history_results:
                sold_quantity=item[1]
                order_price=item[2]
                selling_price = item[3]
                profit_per_item = (selling_price - order_price) * sold_quantity
                total_profit += profit_per_item
            total_profit_label = Label(text=f'Total attained profit is K{total_profit}.', font_size=24, color=(0, 0.8, 0, 1))  # Green color
            main_layout.add_widget(total_profit_label)
            #Total Discounts given
            total_discount = 0
            for item in sales_history_results:
                sold_quantity=item[1]
                discount=item[4]
                discount_per_item = discount * sold_quantity
                total_discount += discount_per_item
            total_discount_label = Label(text=f'Discount: K{total_discount}',font_size=24, color=(0, 0.8, 0, 1))  # Green color
            main_layout.add_widget(total_discount_label)
                  
            # Back Button
            back_button = Button(text='Back', font_size=18, size_hint_y=None, height=50)
            back_button.bind(on_press=self.Accounting)
            main_layout.add_widget(back_button)

            self.add_widget(main_layout)

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()
    def Profit_inventory(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            username = self.username_input.text.strip()
            if not username:
                self.show_login_error_popup('Username cannot be empty.')
                return

            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query_owner_id, (username,))
            owner_id_result = cur.fetchone()

            if owner_id_result is None:
                self.show_login_error_popup('User not found.')
                return

            owner_id = owner_id_result[0]

            # Fetch profit-related data
            query_profit_data = "SELECT itemname, Ordered_quantity, order_price, selling_price FROM Items WHERE ownerid = %s"
            cur.execute(query_profit_data, (owner_id,))
            profit_data = cur.fetchall()

            # Clear existing widgets
            self.clear_widgets()

            # Create a main layout
            main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
            
            # Title Label
            title_label = Label(text='Profit', font_size=24, bold=True, color=(1, 0.5, 0, 1))  # Orange color
            main_layout.add_widget(title_label)

            # Create a ScrollView for profit data
            scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
            grid_layout = GridLayout(cols=4, size_hint_y=None)
            grid_layout.bind(minimum_height=grid_layout.setter('height'))

            # Add headers
            headers = ["Item Name","Ordered Quantity","Order Price","Selling Price"]
            for header in headers:
                header_label = Label(text=header, size_hint_y=None, height=40, bold=True)
                grid_layout.add_widget(header_label)

            # Check if there are results and add sales history items to the grid layout
            if profit_data:
                for item in profit_data:
                    for value in item:
                        item_label = Label(
                            text=str(value),
                            size_hint_y=None,
                            height=40
                        )
                        grid_layout.add_widget(item_label)
            else:
                no_data_label = Label(text="No sales history found.", size_hint_y=None, height=40)
                grid_layout.add_widget(no_data_label)


            scroll_view.add_widget(grid_layout)
            main_layout.add_widget(scroll_view)

            # Display total profit
            total_profit = 0
            for item in profit_data:
                item_name, ordered_quantity, order_price, selling_price = item
                profit_per_item = (selling_price - order_price) * ordered_quantity
                total_profit += profit_per_item
            total_profit_label = Label(text=f'Total Gross profit is K{total_profit}.', font_size=24, color=(0, 0.8, 0, 1))  # Green color
            main_layout.add_widget(total_profit_label)

            # Create buttons
            button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
            # Back Button
            back_button = Button(text='Attained Profit', font_size=18, size_hint_y=None, height=50)
            back_button.bind(on_press=self.attained_profits)
            main_layout.add_widget(back_button)
    
            back_button = Button(text='Back', font_size=18, size_hint_y=None, height=50)
            back_button.bind(on_press=self.Accounting)
            main_layout.add_widget(back_button)

            self.add_widget(main_layout)

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()

    def create_button(self, text, callback):
        button = Button(
            text=text,
            font_size=18,
            background_color=(0.2, 0.6, 0.8, 1),  # Blue color
            color=(1, 1, 1, 1),  # White text color
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'center_x': 0.5}  # Center the button horizontally
        )
        button.bind(on_press=callback)
        return button
    def sales_history(self, instance):
        cnx = None
        cur = None
        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(
                user='Practice',
                password='Root',
                host='localhost',
                database='inventory'
            )
            cur = cnx.cursor()

            # Fetch the owner ID based on the username
            username = self.username_input.text.strip()
            if not username:
                self.show_login_error_popup('Username cannot be empty.')
                return

            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cur.execute(query_owner_id, (username,))
            owner_id_result = cur.fetchone()

            if owner_id_result is None:
                self.show_login_error_popup('User not found.')
                return

            owner_id = owner_id_result[0]

            # Fetch sales history
            query_sales_history = """
            SELECT Items.itemname, Sold.sold_quantity, Sold.selling_price,Sold.discount_amount,Sold.date 
            FROM Items 
            INNER JOIN Sold ON Items.id = Sold.itemid 
            WHERE Items.ownerid = %s
            """
            cur.execute(query_sales_history, (owner_id,))
            sales_history_results = cur.fetchall()

            # Clear existing widgets
            self.clear_widgets()

            # Create a main layout
            main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

            # Title Label
            title_label = Label(text='Sales History', font_size=24, bold=True, color=(0, 0, 0, 1))
            main_layout.add_widget(title_label)

            # Create a ScrollView for the sales history items
            scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
            grid_layout = GridLayout(cols=5, size_hint_y=None)
            grid_layout.bind(minimum_height=grid_layout.setter('height'))

            # Add headers
            headers = ["Item Name","Sold Quantity","Selling Price","Discount", "Date"]
            for header in headers:
                header_label = Label(text=header, size_hint_y=None, height=40, bold=True)
                grid_layout.add_widget(header_label)

            # Check if there are results and add sales history items to the grid layout
            if sales_history_results:
                for item in sales_history_results:
                    for value in item:
                        item_label = Label(
                            text=str(value),
                            size_hint_y=None,
                            height=40
                        )
                        grid_layout.add_widget(item_label)
            else:
                no_data_label = Label(text="No sales history found.", size_hint_y=None, height=40)
                grid_layout.add_widget(no_data_label)

            scroll_view.add_widget(grid_layout)
            main_layout.add_widget(scroll_view)
                  
            # Back Button
            back_button = Button(text='Back', font_size=18, size_hint_y=None, height=50)
            back_button.bind(on_press=self.Accounting)
            main_layout.add_widget(back_button)

            self.add_widget(main_layout)

        except mysql.connector.Error as e:
            logging.error(f"Database error: {e}")
            self.show_login_error_popup('Database error')
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.show_login_error_popup('An unexpected error occurred')
        finally:
            # Ensure the cursor and connection are closed
            if cur:
                cur.close()
            if cnx:
                cnx.close()
    
    def calculate_daily_profit(self, instance):
        # Database connection parameters
        db_config = {
            'user': 'Practice',
            'password': 'Root',
            'host': 'localhost',
            'database': 'inventory'
        }

        # Fetch the owner ID based on the username
        username = self.username_input.text.strip()
        if not username:
            self.show_popup("Input Error", "Username cannot be empty.")
            return

        try:
            # Establish a connection to the database
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()

            # Query to fetch the owner ID
            query_owner_id = "SELECT id FROM Owner WHERE username = %s"
            cursor.execute(query_owner_id, (username,))
            owner_id_result = cursor.fetchone()

            if owner_id_result is None:
                self.show_popup("User Not Found", "User not found.")
                return

            owner_id = owner_id_result[0]

            # Get today's date
            today = datetime.now().date()

            # Query to calculate total profit for today
            query = """
            SELECT SUM((Items.selling_price - Items.order_price) * Sold.sold_quantity) AS total_profit
            FROM Sold
            INNER JOIN Items 
            WHERE DATE(Sold.date) = %s AND Items.ownerid = %s
            """
            cursor.execute(query, (today, owner_id))
            result = cursor.fetchone()

            total_profit = result[0] if result[0] is not None else 0
            self.result_label.text = f"Total profit for {today}: K{total_profit:.2f}"

        except mysql.connector.Error as e:
            self.show_popup("Database Error", f"Database error: {e}")
        except Exception as e:
            self.show_popup("Unexpected Error", f"Unexpected error: {e}")
        finally:
            # Ensure the cursor and connection are closed
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()


    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

    

class InventoryAppApp(App):
    def build(self):
        return InventoryApp()

if __name__ == '__main__':
    InventoryAppApp().run()


       
