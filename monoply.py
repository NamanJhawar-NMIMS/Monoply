import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd
import sys

# Create a game to replace Banking system in Monoply

# 1. Create a function to add users
# 2. Allocate Money
# 3. Transact
# 4. Balance


# variables
player_names = ['placeholder']
initial_balance = 0
monoply = {}




# display list of players
def display_players():
    print('\nList of Players in the system\n')
    count = 1
    for player in player_names:
        print(f'{count}. {player}')
        count += 1
    return player_names


# display players with their stats
def display_players_stats():
    print('\n', pd.DataFrame(monoply))
    return pd.DataFrame(monoply)


# Function to add new users

def add_users(name):
    if name.capitalize() in player_names:
        print('Player Exists!')
    else:
        player_names.append(name.capitalize())
        print(f'New player- {name}, added to the game')
    display_players()


# Add initial Balance to all players
def initial_balance(balance):
    initial_balance = balance
    print(f"Initial Balance to be allocated to all players is INR {initial_balance}")
    for player in player_names:
        monoply[player] = {'balance': initial_balance, 'player_status': 'Playing'}
    #display_players_stats()


# check for sufficient funds
def check_sufficient_funds(player, subtract_amount):
    if monoply[player]["balance"] - subtract_amount > 0:
        monoply[player]["player_status"] = "Playing".capitalize()
        return True
    else:
        monoply[player]["player_status"] = "Negative Balance".capitalize()
        return False


# Add/subtract balance to/from single player
def update_balance_singleUser(player_name, addOrSubtract, amount):
    player_name = player_name.capitalize()
    if addOrSubtract.capitalize() == 'Add'.capitalize():
        monoply[player_name]['balance'] += amount
    else:
        if check_sufficient_funds(player_name, amount):
            monoply[player_name]['balance'] -= amount
        else:
            monoply[player_name]['balance'] -= amount
            print(f"""
      *** TRANSACTION FAILED ***
      {player_name} does not have sufficient balance.
      Either Mortgage {player_name}'s properties or {player_name} loses!
      """)
            # monoply[player_name]['balance']+=amount

    #display_players_stats()


# Transfer amount from one player to another
def transfer_funds_between_players(fromPlayer, toPlayer, amount):
    fromPlayer = fromPlayer.capitalize()
    toPlayer = toPlayer.capitalize()
    if check_sufficient_funds(fromPlayer, amount):
        monoply[fromPlayer]['balance'] -= amount
        monoply[toPlayer]['balance'] += amount
    else:
        print(f'''
    *** TRANSACTION FAILED ***
    {fromPlayer} has insufficient funds!!!

    {toPlayer} has NOT received Funds!!!
    ''')
        # monoply[fromPlayer]['balance']-=amount
    #display_players_stats()


# add_users('Naman')
# add_users('prakshaal')

# initial_balance(1500)

root = tk.Tk()
root.title("Monoply")
root.geometry("400x600")
label1 = tk.Label(root, text="Enter player names that are going to play today",fg="purple")
label1.pack()

text_box = tk.Entry(root)
text_box.pack()


def on_click_addUser():
    print(f"Value entered in text box: {text_box.get()}")
    # print(f"Selected option: {dropdown_value.get()}")

    player_names.append(text_box.get().capitalize())
    if player_names[0] == 'placeholder':
        player_names.pop(0)

    dropdown1['values'] = player_names
    dropdown2['values'] = player_names
    dropdown3['values'] = player_names

    dropdown1.set(player_names[-1])
    dropdown2.set(player_names[-1])
    dropdown3.set(player_names[-1])

    text_box.delete(0, tk.END)
    initial_balance(1500)

    label_display['text'] = display_players_stats()




button_addUser = tk.Button(root, text="Add User", command=on_click_addUser)
button_addUser.pack()

label_fromPlayer = tk.Label(root, text="Send Money from")
label_fromPlayer.pack()

dropdown_value1 = tk.StringVar()
dropdown1 = ttk.Combobox(root, textvariable=dropdown_value1)
dropdown1['values'] = player_names
dropdown1.current(0)
dropdown1.pack()

label_toPlayer = tk.Label(root, text="Send Money To")
label_toPlayer.pack()
dropdown_value2 = tk.StringVar()
dropdown2 = ttk.Combobox(root, textvariable=dropdown_value2)
dropdown2['values'] = player_names
dropdown2.current(0)
dropdown2.pack()

text_box_amount_transferBetweenUsers = tk.Entry(root)
text_box_amount_transferBetweenUsers.pack()


def on_click_amount_transferBetweenUsers():
    amount = int(text_box_amount_transferBetweenUsers.get())
    fromTransfer = dropdown1.get()
    toTransfer = dropdown2.get()
    transfer_funds_between_players(fromTransfer, toTransfer, amount)
    label_display['text'] = display_players_stats()
    print(f'Amount {amount} has been transfered from {fromTransfer} to {toTransfer}')


button_amount_transferBetweenUsers = tk.Button(root,fg='purple',bg='yellow',text="Transfer Money",
                                               command=on_click_amount_transferBetweenUsers)
button_amount_transferBetweenUsers.pack()

# ---------------------------------------------------------------------------

# Single user

dropdown_value3 = tk.StringVar()
dropdown3 = ttk.Combobox(root, textvariable=dropdown_value3)
dropdown3['values'] = player_names
dropdown3.current(0)
dropdown3.pack()

text_box_amount_transferSingleUser = tk.Entry(root)
text_box_amount_transferSingleUser.pack()


def on_click_amount_add_transferSingleUser():
    amount = int(text_box_amount_transferSingleUser.get())
    player_name = dropdown3.get()
    update_balance_singleUser(player_name, 'Add', amount)
    label_display['text'] = display_players_stats()
    print(f'{amount} has been added to {player_name}')


button_amount_add_transferSingleUser = tk.Button(root, text="Add Money",bg="#90EE90", command=on_click_amount_add_transferSingleUser)
button_amount_add_transferSingleUser.pack()


# -----------------
# subtract
def on_click_amount_sub_transferSingleUser():
    amount = int(text_box_amount_transferSingleUser.get())
    player_name = dropdown3.get()
    update_balance_singleUser(player_name, 'sub', amount)
    label_display['text'] = display_players_stats()
    print(f'{amount} has been deducted from {player_name}')


button_amount_sub_transferSingleUser = tk.Button(root, text="Sub Money",bg="#FFCCCB", command=on_click_amount_sub_transferSingleUser)
button_amount_sub_transferSingleUser.pack()
# --------------------------------

# showcasing output

label_display = tk.Label(root, text="*** Game Stats ***")
label_display.place(x=600,y=400)
label_display.pack()

def on_click_passGo(player_name):
    print(player_name)
    pass
#label1.grid(row = 0, column = 0, pady = 2)

root.mainloop()

