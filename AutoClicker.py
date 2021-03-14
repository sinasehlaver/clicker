from pynput.mouse import Button, Controller, Listener
import tkinter as tk
import threading


def on_click(x, y, button, pressed):
	global pos_x, pos_y
	if pressed:
		pos_x = x
		pos_y = y
	else:
		return False


def set_pos():
	global pos_x, pos_y
	with Listener(on_click=on_click) as listener:
		listener.join()
	txt_pos_x.delete(1.0, "end")
	txt_pos_x.insert(1.0, pos_x)
	txt_pos_y.delete(1.0, "end")
	txt_pos_y.insert(1.0, pos_y)


def go_pos():
	try:
		x = float(txt_pos_x.get(1.0, "end"))
		y = float(txt_pos_y.get(1.0, "end"))
		mouse.position = (x,y)
		mouse.click(Button.left, 1)
	except Exception as e:
		print(e)


def rep():
	if var_txt_auto.get() == "Stop":
		sec = int(txt_interval.get(1.0, "end"))
		window.after(sec * 1000, rep)
		go_pos()


def auto_click():
	if var_txt_auto.get() == "Start":
		print("started")
		var_txt_auto.set("Stop")
		window.after(0, rep)
	elif var_txt_auto.get() == "Stop":
		print("stopped")
		var_txt_auto.set("Start")


mouse = Controller()

ticker = threading.Event()

pos_x = 0
pos_y = 0

filepath = "config.txt"

window = tk.Tk()
window.resizable(0,0)
window.title("Automated Clicker")

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

window.geometry("+{}+{}".format(positionRight, positionDown))

fr_buttons = tk.Frame(master=window, width=300, bg="white", borderwidth=4, relief="solid")
fr_buttons.pack(fill=tk.BOTH, side=tk.LEFT)

button_width = 12
button_pady = 22

set_var = tk.BooleanVar()

fr_periodic = tk.Frame(master=fr_buttons)
fr_periodic.grid(row=4, column=0, columnspan=2, sticky='nesw', padx=5)


# SETS THE MOUSE POSITION
btn_set_pos = tk.Button(fr_periodic, width=int(button_width / 2), text="Set", command= set_pos)
btn_set_pos.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# MOVES MOUSE TO SET POSITION
btn_go_pos = tk.Button(fr_periodic, width=int(button_width / 2), text="Go", command= go_pos)
btn_go_pos.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

# DISPLAYS MOUSE POSITION
lbl_pos = tk.Label(fr_periodic, text="Position")
lbl_pos.grid(row=2, column=1, sticky="ew")

txt_pos_x = tk.Text(fr_periodic, width=int(button_width / 2), height=1)
txt_pos_x.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
txt_pos_x.config(highlightthickness = 1, highlightbackground="black")

txt_pos_y = tk.Text(fr_periodic, width=int(button_width / 2), height=1)
txt_pos_y.grid(row=3, column=2, sticky="ew", padx=5, pady=5)
txt_pos_y.config(highlightthickness = 1, highlightbackground="black")

# CREATE INTERVAL
lbl_interval = tk.Label(fr_periodic, text="Interval")
lbl_interval.grid(row=4, column=1, sticky="ew")

txt_interval = tk.Text(fr_periodic, width=int(button_width / 2), height=1)
txt_interval.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
txt_interval.config(highlightthickness = 1, highlightbackground="black")

# PERIODIC CLICKER
var_txt_auto = tk.StringVar()
var_txt_auto.set("Start")
btn_auto = tk.Button(fr_periodic, width=int(button_width / 2), textvariable=var_txt_auto, command= auto_click)
btn_auto.grid(row=5, column=2, sticky="ew", padx=5, pady=5)

window.mainloop()

