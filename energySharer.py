from bitcoinlib.wallets import Wallet, WalletTransaction
import tkinter as tk
from tkinter import ttk
w = Wallet.create("pop")
t = WalletTransaction(w)
address = ""
amount = "1234567890"
main_app = tk.Tk()
main_app.title("Synergy")
def showData():
    data_window = tk.Toplevel(main_app)
    data_window.title("Energy Data")
def send():
    send_window = tk.Toplevel(main_app)
    send_window.title("Send Payment to")
    amount_label = ttk.Label(send_window, text="Amount(BTC): ")
    amount_entry = ttk.Entry(send_window)
    address_label = ttk.Label(send_window, text="Address: ")
    address_entry = ttk.Entry(send_window)  
    confirm_button = ttk.Button(send_window, text="Send", command=actual_send)
    address = address_entry.get()
    amount = amount_entry.get()
    amount_label.pack()
    amount_entry.pack()
    address_label.pack()
    address_entry.pack()
    confirm_button.pack()
def actual_send():
    t = w.send_to(address, int(amount), w.key('change 0'))
def receive():
    receive_window = tk.Toplevel(main_app)
    receive_window.title("Transactions")
    info = tk.Text(receive_window)
    info.insert(tk.END, "Transaction Success")
data_button = ttk.Button(main_app, text="Energy Data", command=showData)
send_button = ttk.Button(main_app, text="Send Payment", command=send)
receive_button = ttk.Button(main_app, text="Receive", command=receive)
data_button.grid(column=0, row=0)
send_button.grid(column=0, row=1)
receive_button.grid(column=0, row=2)
main_app.mainloop()
