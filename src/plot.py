import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

loans = pd.read_csv("./data/loan_dev.csv", sep=";",dtype=int)
transactions = pd.read_csv("./data/trans_dev.csv", sep=";",dtype={"trans_id":int,"account_id":int,"date":int,"type":str,"operation":str,"amount":float,"balance":float,"k_symbol":str,"bank":str,"account":str})
accounts = pd.read_csv("./data/account.csv", sep=";",dtype={"account_id":int,"district_id":int,"frequency":str,"date":int})
cards = pd.read_csv("./data/card_dev.csv", sep=";",dtype={"card_id":int,"disp_id":int,"type":str,"issued":int})
clients = pd.read_csv("./data/client.csv", sep=";",dtype=int)
dispositions = pd.read_csv("./data/disp.csv", sep=";",dtype={"disp_id":int,"client_id":int,"account_id":int,"type":str})
districts = pd.read_csv("./data/district.csv", na_values=['?'], sep=";",dtype={"code":int, "name":str, "region":str,"no. of inhabitants":int,"no. of municipalities with inhabitants < 499":int,"no. of municipalities with inhabitants 500-1999":int,"no. of municipalities with inhabitants 2000-9999":int, "no. of municipalities with inhabitants >10000": int, "no. of cities":int, "ratio of urban inhabitants":float, "average salary":float, "unemploymant rate '95":float, "unemploymant rate '96":float, "no. of enterpreneurs per 1000 inhabitants": float, "no. of commited crimes '95":int, "no. of commited crimes '96":int})


#ACCOUNTS

accounts_with_loans = len(loans["account_id"].unique())
unique_accounts = len(accounts["account_id"].unique())

sizes = [accounts_with_loans, unique_accounts]

labels = ["Accounts with loans", "Accounts without\nloans"]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Ratio of accounts with loans to accounts without loans")
plt.savefig('plots/accounts_with_loans.pdf')


##CARD TYPES

cards_disp = pd.merge(cards, dispositions, on="disp_id")
print(cards_disp)
num_accounts_without_card =  len(accounts["account_id"].unique())  - len(cards_disp["account_id"].unique())
num_accounts_junior = len(cards_disp[cards_disp["type_x"] == "junior"]["account_id"].unique())
num_accounts_classic = len(cards_disp[cards_disp["type_x"] == "classic"]["account_id"].unique())
num_accounts_gold = len(cards_disp[cards_disp["type_x"] == "gold"]["account_id"].unique())

sizes = [num_accounts_without_card, num_accounts_classic, num_accounts_junior, num_accounts_gold]
labels = ["None", "Classic", "Junior", "Gold"]


name = labels
price = sizes
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(name, price)
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.4,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Number of accounts with specific card types')
 
# Show Plot
plt.savefig('plots/card_types_bar.pdf')

