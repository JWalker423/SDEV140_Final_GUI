import tkinter as tk

from PIL import ImageTk, Image

# Create the main window
window = tk.Tk()
window.title("Shopping GUI")
window.geometry("500x400")
window.configure(bg="#662d15")

# Create the grid
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=100)
for i in range(4):
    window.rowconfigure(i, weight=1, minsize=100)

# Configuring labels
label1 = tk.Label(window, text="Live Wild Outdoors", font=("Brush Script MT", 28), fg="#c2a083", bg="#662d15")
label1.grid(row=0, column=1)

label2 = tk.Label(window, text="Shopping", font=("Nimbus Mono", 20), fg="#c2a083", bg="#662d15")
label2.grid(row=1, column=1)

label3 = tk.Label(window, text="Live Wild Outdoors, Inc\n© 2023", font=("Nimbus Mono", 10), fg="#c2a083", bg="#662d15", anchor="center")
label3.grid(row=3, column=1)

# Frame for buttons
button_frame = tk.Frame(window, bg="#662d15")
button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")

# Configure a grid layout
for i in range(3):
    button_frame.columnconfigure(i, weight=1)
button_frame.rowconfigure(0, weight=1)

#hiking gear module
def open_hiking_gear():
    hiking_gear_window = tk.Toplevel(window)
    hiking_gear_window.title("Hiking Gear")
    hiking_gear_window.geometry("400x400")
    hiking_gear_window.configure(bg="#662d15")

    # Create a scrollbar
    canvas = tk.Canvas(hiking_gear_window, bg="#662d15")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(hiking_gear_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create hiking gear frame
    hiking_gear_frame = tk.Frame(canvas, bg="#662d15")

    def update_frame(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas_frame = canvas.create_window((0, 0), window=hiking_gear_frame, anchor=tk.NW)
    hiking_gear_frame.bind("<Configure>", update_frame)

    label1 = tk.Label(hiking_gear_frame, text="Live Wild Outdoors", font=("Brush Script MT", 28), fg="#c2a083", bg="#662d15")
    label1.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

    label2 = tk.Label(hiking_gear_frame, text="Hiking Gear", font=("Nimbus Mono", 16), fg="#c2a083", bg="#662d15")
    label2.grid(row=1, column=1, padx=10, pady=30)

    # Load images for buttons
    boots_image = ImageTk.PhotoImage(Image.open("boots.jpeg"))
    poles_image = ImageTk.PhotoImage(Image.open("poles.jpeg"))
    hydration_image = ImageTk.PhotoImage(Image.open("backpack.jpeg"))

    # Create buttons with images
    boots_button = tk.Button(hiking_gear_frame, image=boots_image, bg="#662d15",
                             borderwidth=0, highlightthickness=0, highlightbackground="#662d15")
    boots_button.grid(row=2, column=1, pady=10, padx=30, sticky="nsew")
    boots_label = tk.Label(hiking_gear_frame, text="Boots", font=("Nimbus Mono", 12),
                           fg="#c2a083", bg="#662d15")
    boots_label.grid(row=3, column=1, pady=5, padx=30, sticky="nsew")

    poles_button = tk.Button(hiking_gear_frame, image=poles_image, bg="#662d15", borderwidth=0,
                             highlightthickness=0, highlightbackground="#662d15")
    poles_button.grid(row=4, column=1, pady=10, padx=30, sticky="nsew")
    poles_label = tk.Label(hiking_gear_frame, text="Poles", font=("Nimbus Mono", 12), fg="#c2a083",
                           bg="#662d15")
    poles_label.grid(row=5, column=1, pady=5, padx=30, sticky="nsew")

    hydration_button = tk.Button(hiking_gear_frame, image=hydration_image, bg="#662d15",
                                 borderwidth=0, highlightthickness=0, highlightbackground="#662d15")
    hydration_button.grid(row=6, column=1, pady=10, padx=30, sticky="nsew")
    hydration_label = tk.Label(hiking_gear_frame, text="Hydration\nPacks", font=("Nimbus Mono", 12),
                               fg="#c2a083", bg="#662d15")
    hydration_label.grid(row=7, column=1, pady=5, padx=30, sticky="nsew")

    def add_to_cart(item, size, color):
        # Implement the logic to add the selected item, size, and color to the cart
        # You can modify this function based on your specific requirements
        print(f"Added {size} {color} {item} to the cart.")

    # Add dropdown menu for boots button
    def boots_dropdown():
        sizes = ["Small", "Medium", "Large"]
        colors = ["Black", "Brown", "Gray"]
        boots_menu = tk.Menu(hiking_gear_frame, tearoff=False)
        for size in sizes:
            size_menu = tk.Menu(boots_menu, tearoff=False)
            for color in colors:
                size_menu.add_command(label=color, command=lambda s=size, c=color: add_to_cart("Boots", s, c))
            boots_menu.add_cascade(label=size, menu=size_menu)

        # Display the dropdown menu at the button's location
        boots_menu.post(boots_button.winfo_rootx(), boots_button.winfo_rooty() + boots_button.winfo_height())

    boots_button.configure(command=boots_dropdown)

    def poles_dropdown():
        pole_types = ["Telescoping", "Folding"]
        colors = ["Black", "Red", "Gray"]
        poles_menu = tk.Menu(hiking_gear_frame, tearoff=False)
        for pole_type in pole_types:
            type_menu = tk.Menu(poles_menu, tearoff=False)
            for color in colors:
                type_menu.add_command(label=color, command=lambda t=pole_type, c=color: add_to_cart("Boots", t, c))
            poles_menu.add_cascade(label=pole_type, menu=type_menu)

        # Display the dropdown menu at the button's location
        poles_menu.post(poles_button.winfo_rootx(), poles_button.winfo_rooty() + poles_button.winfo_height())

    poles_button.configure(command=poles_dropdown)

    def hydration_dropdown():
        sizes = ["10 Liter", "30 Liter", "50 Liter"]
        colors = ["Blue", "Purple", "Lime Green", "Orange", "Pink", "Red"]
        hydration_menu = tk.Menu(hiking_gear_frame, tearoff=False)
        for size in sizes:
            size_menu = tk.Menu(hydration_menu, tearoff=False)
            for color in colors:
                size_menu.add_command(label=color, command=lambda s=size, c=color: add_to_cart("Hydration Pack", s, c))
            hydration_menu.add_cascade(label=size, menu=size_menu)

        # Display the dropdown menu at the button's location
        hydration_menu.post(hydration_button.winfo_rootx(), hydration_button.winfo_rooty() + hydration_button.winfo_height())

    hydration_button.configure(command=hydration_dropdown)

    hiking_gear_window.mainloop()

# camping gear module
def open_camping_gear():
    camping_gear_window = tk.Toplevel(window)
    camping_gear_window.title("Camping Gear")
    camping_gear_window.geometry("400x400")
    camping_gear_window.configure(bg="#662d15")

    # Create a canvas with a scrollbar
    canvas = tk.Canvas(camping_gear_window, bg="#662d15")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(camping_gear_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create camping gear frame
    camping_gear_frame = tk.Frame(canvas, bg="#662d15")

    def update_frame(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas_frame = canvas.create_window((0, 0), window=camping_gear_frame, anchor=tk.NW)
    camping_gear_frame.bind("<Configure>", update_frame)

    label1 = tk.Label(camping_gear_frame, text="Live Wild Outdoors", font=("Brush Script MT", 28), fg="#c2a083", bg="#662d15")
    label1.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

    label2 = tk.Label(camping_gear_frame, text="Camping Gear", font=("Nimbus Mono", 16), fg="#c2a083", bg="#662d15")
    label2.grid(row=1, column=1, padx=10, pady=30)

    # assigning images for buttons
    tents_and_hammocks_image = ImageTk.PhotoImage(Image.open("hammock.jpeg"))
    sleeping_bags_image = ImageTk.PhotoImage(Image.open("sleeping_bag.jpeg"))
    cookware_and_stoves_image = ImageTk.PhotoImage(Image.open("stove.jpeg"))

    # Create buttons
    tents_and_hammocks_button = tk.Button(camping_gear_frame, image=tents_and_hammocks_image, bg="#662d15",
                                          borderwidth=0, highlightthickness=0, highlightbackground="#662d15",
                                          command=lambda: add_to_cart("Tents and Hammocks", "", ""))
    tents_and_hammocks_button.grid(row=2, column=1, pady=10, padx=30, sticky="nsew")
    tents_and_hammocks_label = tk.Label(camping_gear_frame, text="Tents and Hammocks", font=("Nimbus Mono", 12),
                                        fg="#c2a083", bg="#662d15")
    tents_and_hammocks_label.grid(row=3, column=1, pady=5, padx=30, sticky="nsew")

    sleeping_bags_button = tk.Button(camping_gear_frame, image=sleeping_bags_image, bg="#662d15", borderwidth=0,
                                     highlightthickness=0, highlightbackground="#662d15")
    sleeping_bags_button.grid(row=4, column=1, pady=10, padx=30, sticky="nsew")
    sleeping_bags_label = tk.Label(camping_gear_frame, text="Sleeping Bags", font=("Nimbus Mono", 12), fg="#c2a083",
                                   bg="#662d15")
    sleeping_bags_label.grid(row=5, column=1, pady=5, padx=30, sticky="nsew")

    cookware_and_stoves_button = tk.Button(camping_gear_frame, image=cookware_and_stoves_image, bg="#662d15",
                                           borderwidth=0, highlightthickness=0, highlightbackground="#662d15")
    cookware_and_stoves_button.grid(row=6, column=1, pady=10, padx=30, sticky="nsew")
    cookware_and_stoves_label = tk.Label(camping_gear_frame, text="Cookware and Stoves", font=("Nimbus Mono", 12),
                                         fg="#c2a083", bg="#662d15")
    cookware_and_stoves_label.grid(row=7, column=1, pady=5, padx=30, sticky="nsew")

    exit_button = tk.Button(camping_gear_frame, text="Exit", font=("Nimbus Mono", 12), bg="#c2a083",
                            command=camping_gear_window.destroy)
    exit_button.grid(row=8, column=1, padx=10, pady=10, ipadx=5, ipady=5)

    label3 = tk.Label(camping_gear_frame, text="Live Wild Outdoors, Inc\n© 2023", font=("Nimbus Mono", 10),
                      fg="#c2a083", bg="#662d15")
    label3.grid(row=9, column=1, pady=(20, 0), padx=30, sticky="nsew")

    # Setting the images as buttons
    tents_and_hammocks_button.image = tents_and_hammocks_image
    sleeping_bags_button.image = sleeping_bags_image
    cookware_and_stoves_button.image = cookware_and_stoves_image

    label3 = tk.Label(camping_gear_frame, text="Live Wild Outdoors, Inc\n© 2023", font=("Nimbus Mono", 10),
                      fg="#c2a083", bg="#662d15")
    label3.grid(row=9, column=1, pady=(20, 0), padx=30, sticky="ew")

    def add_to_cart(item, size, color):
        # Implement the logic to add the selected item, size, and color to the cart
        # You can modify this function based on your specific requirements
        print(f"Added {size} {color} {item} to the cart.")

    # Create a dropdown menu for shelter type
    def shelter_type_dropdown():
        shelter_types = ["Tent", "Hammock"]
        tent_sizes = ["2 Person", "6 Person", "10 Person"]
        hammock_sizes = ["Single", "Double"]
        colors = ["Black", "Brown", "Gray"]

        shelter_type_menu = tk.Menu(tents_and_hammocks_button, tearoff=False)
        for shelter_type in shelter_types:
            size_menu = tk.Menu(shelter_type_menu, tearoff=False)
            if shelter_type == "Tent":
                sizes = tent_sizes
            else:
                sizes = hammock_sizes
            for size in sizes:
                color_menu = tk.Menu(size_menu, tearoff=False)
                for color in colors:
                    color_menu.add_command(label=color, command=lambda s=size, c=color: add_to_cart(shelter_type, s, c))
                size_menu.add_cascade(label=size, menu=color_menu)
            shelter_type_menu.add_cascade(label=shelter_type, menu=size_menu)

        # Display the dropdown menu at the button's location
        shelter_type_menu.post(tents_and_hammocks_button.winfo_rootx(),
                               tents_and_hammocks_button.winfo_rooty() + tents_and_hammocks_button.winfo_height())

    tents_and_hammocks_button.configure(command=shelter_type_dropdown)

    # Create a dropdown menu for sleeping bag type
    def sleeping_bag_dropdown():
        sleeping_bag_types = ["Rectangular", "Semi-Rectangular", "Mummy", "Double"]
        seasons = ["Summer", "3 Season", "Cold Weather"]
        colors = ["Black", "Blue", "Red", "Green", "Yellow", "Orange", "Purple"]

        sleeping_bag_menu = tk.Menu(sleeping_bags_button, tearoff=False)
        for bag_type in sleeping_bag_types:
            season_menu = tk.Menu(sleeping_bag_menu, tearoff=False)
            for season in seasons:
                color_menu = tk.Menu(season_menu, tearoff=False)
                for color in colors:
                    color_menu.add_command(label=color,
                                           command=lambda t=bag_type, s=season, c=color: add_to_cart("Sleeping Bag", t,
                                                                                                     s, c))
                season_menu.add_cascade(label=season, menu=color_menu)
            sleeping_bag_menu.add_cascade(label=bag_type, menu=season_menu)

        # Display the dropdown menu at the button's location
        sleeping_bag_menu.post(sleeping_bags_button.winfo_rootx(),
                               sleeping_bags_button.winfo_rooty() + sleeping_bags_button.winfo_height())

    sleeping_bags_button.configure(command=sleeping_bag_dropdown)

    # Create dropdown menu for cookware and stove selection
    def cookware_stove_dropdown(c):
        options = ["Cookware", "Stove"]
        cookware_types = ["Cast Iron", "Aluminum", "Stainless Steel"]
        cast_iron_items = ["10in Pan", "Dutch Oven", "Griddle", "Deep Pan with Lid"]
        aluminum_items = ["Frypan", "Pot", "Tea Kettle", "Percolator"]
        stainless_steel_items = ["Frypan", "Pot", "Tea Kettle", "Percolator",
                                 "5 Piece Kit (2 Skillets/2 Pots/Percolator)"]
        stove_types = ["Canister Stove", "Liquid Stove", "Pellet/Tablet Stove", "Wood Stove"]

        cookware_stove_menu = tk.Menu(camping_gear_frame, tearoff=False)

        for option in options:
            if option == "Cookware":
                cookware_menu = tk.Menu(cookware_stove_menu, tearoff=False)
                for cookware_type in cookware_types:
                    if cookware_type == "Cast Iron":
                        cast_iron_menu = tk.Menu(cookware_menu, tearoff=False)
                        for item in cast_iron_items:
                            cast_iron_menu.add_command(label=item,
                                                       command=lambda c=cookware_type, i=item: add_to_cart("Cookware",
                                                                                                           c, i))
                        cookware_menu.add_cascade(label=cookware_type, menu=cast_iron_menu)
                    elif cookware_type == "Aluminum":
                        aluminum_menu = tk.Menu(cookware_menu, tearoff=False)
                        for item in aluminum_items:
                            aluminum_menu.add_command(label=item,
                                                      command=lambda c=cookware_type, i=item: add_to_cart("Cookware", c,
                                                                                                          i))
                        cookware_menu.add_cascade(label=cookware_type, menu=aluminum_menu)
                    elif cookware_type == "Stainless Steel":
                        stainless_steel_menu = tk.Menu(cookware_menu, tearoff=False)
                        for item in stainless_steel_items:
                            stainless_steel_menu.add_command(label=item,
                                                             command=lambda c=cookware_type, i=item: add_to_cart(
                                                                 "Cookware", c, i))
                        cookware_menu.add_cascade(label=cookware_type, menu=stainless_steel_menu)
                cookware_stove_menu.add_cascade(label=option, menu=cookware_menu)
            else:
                stove_menu = tk.Menu(cookware_stove_menu, tearoff=False)
                for stove_type in stove_types:
                    stove_menu.add_command(label=stove_type, command=lambda s=stove_type: add_to_cart("Stove", s, c))
                cookware_stove_menu.add_cascade(label=option, menu=stove_menu)

        # Display the dropdown menu at the button's location
        cookware_stove_menu.post(cookware_and_stoves_button.winfo_rootx(),
                                 cookware_and_stoves_button.winfo_rooty() + cookware_and_stoves_button.winfo_height())

    cookware_and_stoves_button.configure(command=lambda: cookware_stove_dropdown("No Color"))


# shopping cart
def open_shopping_cart():
    shopping_cart_window = tk.Toplevel(window)
    shopping_cart_window.title("Shopping Cart")
    shopping_cart_window.geometry("500x400")
    shopping_cart_window.configure(bg="#662d15")

    shopping_cart_frame = tk.Frame(shopping_cart_window, bg="#662d15")
    shopping_cart_frame.pack(pady=20)

    label1 = tk.Label(shopping_cart_frame, text="Live Wild Outdoors", font=("Brush Script MT", 28), fg="#c2a083", bg="#662d15")
    label1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(shopping_cart_frame, text="Shopping Cart", font=("Nimbus Mono", 16), fg="#c2a083", bg="#662d15")
    label2.grid(row=1, column=1, padx=10, pady=30)

    checkout_button = tk.Button(shopping_cart_frame, text="Checkout", font=("Nimbus Mono", 12), bg="#c2a083")
    checkout_button.grid(row=3, column=0, pady=10, ipadx=15, ipady=5)

    continue_shopping_button = tk.Button(shopping_cart_frame, text="Continue\nShopping", font=("Nimbus Mono", 12), bg="#c2a083", command=shopping_cart_window.destroy)
    continue_shopping_button.grid(row=3, column=2, pady=10, ipadx=15, ipady=5)

    from tkinter import IntVar, Entry

    quantity_label = tk.Label(shopping_cart_frame, text="Quantity:", font=("Nimbus Mono", 12), bg="#662d15", fg="#c2a083")
    quantity_label.grid(row=2, column=0, padx=5, pady=10)

    quantity_var = IntVar()
    quantity_entry = Entry(shopping_cart_frame, textvariable=quantity_var, font=("Nimbus Mono", 12), width=5)
    quantity_entry.grid(row=2, column=1, padx=5, pady=10)

    def increase_quantity():
        current_quantity = quantity_var.get()
        quantity_var.set(current_quantity + 1)

    def decrease_quantity():
        current_quantity = quantity_var.get()
        if current_quantity > 0:
            quantity_var.set(current_quantity - 1)

    increase_button = tk.Button(shopping_cart_frame, text="+", font=("Nimbus Mono", 12), bg="#c2a083", command=increase_quantity)
    increase_button.grid(row=2, column=1, sticky="e", padx=(0, 5), pady=10)

    decrease_button = tk.Button(shopping_cart_frame, text="-", font=("Nimbus Mono", 12), bg="#c2a083", command=decrease_quantity)
    decrease_button.grid(row=2, column=1, sticky="w", padx=(5, 0), pady=10)

    shopping_cart = []

    def add_to_cart(item, size, color):
        selected_item = f"{size} {color} {item}"
        shopping_cart.append(selected_item)
        print(f"Added {selected_item} to the cart.")

    def show_cart():
        for item in shopping_cart:
            print(item)

    show_cart_button = tk.Button(shopping_cart_frame, text="Show Cart", font=("Nimbus Mono", 12), bg="#c2a083",
                                 command=show_cart)
    show_cart_button.grid(row=5, column=1, pady=10)

    # Add a label to display the items in the shopping cart
    cart_label = tk.Label(shopping_cart_frame, text="Items in Cart:", font=("Nimbus Mono", 12), bg="#662d15",
                          fg="#c2a083")
    cart_label.grid(row=4, column=0, padx=5, pady=10, sticky="w")

    cart_content = tk.StringVar()
    cart_content_label = tk.Label(shopping_cart_frame, textvariable=cart_content, font=("Nimbus Mono", 12),
                                  bg="#662d15", fg="#c2a083")
    cart_content_label.grid(row=4, column=1, padx=5, pady=10, sticky="w")

    def update_cart_label():
        cart_items = "\n".join(shopping_cart)
        cart_content.set(cart_items)

    update_cart_label()

    shopping_cart_window.mainloop()



hiking_gear_image = Image.open("hiking_gear.jpeg")
hiking_gear_image = hiking_gear_image.resize((60, 60))
hiking_gear_photo = ImageTk.PhotoImage(hiking_gear_image)

camping_gear_image = Image.open("camping.jpeg")
camping_gear_image = camping_gear_image.resize((60, 60))
camping_gear_photo = ImageTk.PhotoImage(camping_gear_image)

shopping_cart_image = Image.open("cart.png")
shopping_cart_image = shopping_cart_image.resize((40, 40))
shopping_cart_photo = ImageTk.PhotoImage(shopping_cart_image)

#buttons with images
button1 = tk.Button(button_frame, image=hiking_gear_photo, text="Hiking Gear", font=("Nimbus Mono", 14),
                    bg="#c2a083", compound="top", command=open_hiking_gear)
button1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button2 = tk.Button(button_frame, image=camping_gear_photo, text="Camping Gear", font=("Nimbus Mono", 14),
                    bg="#c2a083", compound="top", command=open_camping_gear)
button2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

button3 = tk.Button(button_frame, image=shopping_cart_photo, text="Shopping Cart", font=("Nimbus Mono", 14),
                    bg="#c2a083", compound="top", command=open_shopping_cart)
button3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Start the GUI main loop
window.mainloop()