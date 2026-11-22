# Import the tkinter library for creating a GUI.
import tkinter as tk
# Define the function that runs when the button is clicked.
def calculate_bmi():
    # use .get() to retrieve the value entered or selected by the user in a widget
    height = float(height_entry.get())
    # Get the weight from the Entry widget through .get () method.
    weight = float(weight_entry.get())
    # Add validation: Check whether height or weight is zero or negative.
    if height <= 0 or weight <= 0:
    # line below displays a message in the result Label.
        result_label.config(text="Enter positive values.")
    else:
    # Calculate BMI using the formula for U.S. units.
        bmi = weight / (height ** 2) * 703
    # Display BMI rounded to two decimal places.
    result_label.config(text=f"BMI = {bmi:.2f}")
# Create the main application window.
window = tk.Tk()
# Set the title of the window.
window.title("BMI Calculator")
# Set the window size (width x height).
window.geometry("360x220")
# Create the height Label.
height_label = tk.Label(window, text="Height (inches):")
# Position the Label in row 0, column 0.
# padx and pady add external spacing.
height_label.grid(row=0, column=0, padx=10, pady=8)
# Create an Entry widget for height.
height_entry = tk.Entry(window)
# Position the height Entry beside its Label.
height_entry.grid(row=0, column=1)
# Create the weight Label.
weight_label = tk.Label(window, text="Weight (pounds):")
# Position the Label in row 1, column 0.
weight_label.grid(row=1, column=0, padx=10, pady=8)
# Create an Entry widget for weight.
weight_entry = tk.Entry(window)
# Position the weight Entry beside its Label.
weight_entry.grid(row=1, column=1)
# Create a Button widget. Command=calculate_bmi calls the function when clicked.
calculate_button = tk.Button(window,text="Calculate BMI",command=calculate_bmi)
# Position the button in row 2. columnspan=2 spans both columns.
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
# Create an empty Label to display the BMI result.
result_label = tk.Label(window, text="")
# Position the result Label below the button.
result_label.grid(row=3, column=0, columnspan=2)
# Start the Tkinter event loop. This keeps the window open and responds to user actions.
window.mainloop()