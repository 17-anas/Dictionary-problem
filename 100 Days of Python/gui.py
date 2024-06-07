import tkinter as tk

def on_configure(event):
    # Update scroll region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox('all'))

root = tk.Tk()
root.title("Scrollable Interface")

# Create a canvas and add a scrollbar
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# Configure the canvas to update scroll region when the size changes
frame.bind("<Configure>", on_configure)

# Add some widgets to the frame
for i in range(50):
    label = tk.Label(frame, text=f"Label {i}")
    label.pack(pady=10)

root.mainloop()
