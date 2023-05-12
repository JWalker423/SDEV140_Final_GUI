# SDEV140_Final_GUI
Python shopping GUI with Tkinter


User Manual: Shopping GUI

Introduction:
The Shopping GUI is a graphical user interface developed using the tkinter library in Python. It offers a user-friendly interface for browsing and adding items to a shopping cart. The GUI consists of two modules: Hiking Gear and Camping Gear.

Hiking Gear Module:
Clicking on the "Hiking Gear" button opens a new window where users can view and select from a range of hiking gear items.
The items are displayed in a scrollable frame for easy navigation.
Each item is accompanied by an image, name, and a dropdown menu to choose the desired size and color.
Users can select an item and its specification from the dropdown menu in each category and add it to their cart.
The selected item and its size and color will be recorded for further processing.

Camping Gear Module:
Clicking on the "Camping Gear" button opens a new window where users can explore various camping gear items.
Like the Hiking Gear module, the items are presented in a scrollable frame.
An image and a name represent each item category.
Users can click the corresponding button to select items and specifications and add them to the cart.
The selected item will be captured and stored for future reference.

Cart Functionality:
The current implementation of the "Add to Cart" button only prints the selected item, size, and color to the console. To fully implement the cart functionality, you must modify the "add_to_cart" function according to your specific requirements.
For instance, you can enhance the function to store the selected items in a list or a database for later processing or purchase.

Exiting the Application:
To exit the application, you can close the main or any open module window. Doing so will terminate the GUI.

Note:
The provided code assumes the availability of image files (boots.jpeg, poles.jpeg, backpack.jpeg, hammock.jpeg, sleeping_bag.jpeg, stove.jpeg) in the same directory as the script.
If you wish to use different images, update the file paths in the code accordingly.

Example Usage:
To illustrate the usage, you can follow these steps:
1. Click on the "Hiking Gear" button.
2. Select a size and color for a desired item (e.g., "Boots" -> "Medium" -> "Brown").
3. Click the "Add to Cart" button.
4. The selected item, size, and color will be displayed in the console.
5. Repeat the same process for the "Camping Gear" module.

Disclaimer:
This user manual provides a general overview of the Shopping GUI and its functionality based on the provided code.
Feel free to customize and expand the code to meet your needs and requirements.
