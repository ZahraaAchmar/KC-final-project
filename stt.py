import tkinter as tk
import time
import threading
import random

class TypeSpeedGUI:

    def __init__(self):
        self.running = True
        self.stt = tk.Tk()
        self.stt.title("speed typing test")
        self.stt.geometry("800x600")
        self.stt.configure(bg="black")
        #keycode = event.keycode
        self.counter = 0.0
        self.started = False

        self.Texts = open("Texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.stt)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.Texts), font=("Helventica", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helventica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS", font=("Helventica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font= ("Helventica", 24))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        #self.counter = 0.0
        #self.started = False

        self.stt.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [20, 21, 22]:
                self.running = True
                t =threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget("text").startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")       
        if self.input_entry.get() == self.sample_label.cget("text"):
            self.running = False
            self.input_entry.config(fg="green") 

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.sample_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS")
        self.sample_label.config(text= random.choice(self.Texts))
        self.input_entry.delete(0, tk.END)
        
TypeSpeedGUI()