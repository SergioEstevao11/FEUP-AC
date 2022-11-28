import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


loans = pd.read_csv("./data/loan_dev.csv", sep=";",dtype=int)
transactions = pd.read_csv("./data/trans_dev.csv", sep=";",dtype={"trans_id":int,"account_id":int,"date":int,"type":str,"operation":str,"amount":float,"balance":float,"k_symbol":str,"bank":str,"account":str})
accounts = pd.read_csv("./data/account.csv", sep=";",dtype={"account_id":int,"district_id":int,"frequency":str,"date":int})
cards = pd.read_csv("./data/card_dev.csv", sep=";",dtype={"card_id":int,"disp_id":int,"type":str,"issued":int})
clients = pd.read_csv("./data/client.csv", sep=";",dtype=int)
dispositions = pd.read_csv("./data/disp.csv", sep=";",dtype={"disp_id":int,"client_id":int,"account_id":int,"type":str})
districts = pd.read_csv("./data/district.csv", na_values=['?'], sep=";",dtype={"code":int, "name":str, "region":str,"no. of inhabitants":int,"no. of municipalities with inhabitants < 499":int,"no. of municipalities with inhabitants 500-1999":int,"no. of municipalities with inhabitants 2000-9999":int, "no. of municipalities with inhabitants >10000": int, "no. of cities":int, "ratio of urban inhabitants":float, "average salary":float, "unemploymant rate '95":float, "unemploymant rate '96":float, "no. of enterpreneurs per 1000 inhabitants": float, "no. of commited crimes '95":int, "no. of commited crimes '96":int})
final_dataset = pd.read_csv("./data/merged_dataset.csv", na_values=['?'], sep=',', dtype={"age":int})



def accounts_plot():

        accounts_with_loans = len(loans["account_id"].unique())
        unique_accounts = len(accounts["account_id"].unique())

        sizes = [accounts_with_loans, unique_accounts]

        labels = ["Accounts with loans", "Accounts without\nloans"]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=30)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Ratio of accounts with loans to accounts without loans")
        plt.savefig('plots/accounts_with_loans.png', transparent=True)


def card_plot():

        cards_disp = pd.merge(cards, dispositions, on="disp_id")
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
        plt.savefig('plots/card_types_bar.png', transparent=True)


def plot_loans():
        plt.rcParams.update({'font.size': 16})

        num_nonpayed_loans = len(loans[loans["status"] == -1]["loan_id"].unique())
        num_payed_loans = len(loans[loans["status"] == 1]["loan_id"].unique())
        sizes = [num_payed_loans, num_nonpayed_loans]
        labels = ["1", "-1"]

        name = labels
        price = sizes
        
        # Figure Size
        fig, ax = plt.subplots(figsize =(11, 6))
        
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
        ax.set_title('Loan Type Distribution')
        
        
        # Show Plot
        plt.savefig('plots/loan_types_bar.png', transparent=True)


        
 
        nonpayed_loan_amount = loans[loans["status"] == -1]["amount"]
        payed_loan_amount = loans[loans["status"] == 1]["amount"]

        data = [nonpayed_loan_amount, payed_loan_amount]
        
        fig, ax = plt.subplots(figsize =(11, 6))
        
        
        # Creating plot
        bp = ax.boxplot(x=data, labels=["-1", "1"])

        plt.ylabel("Amount (czech crowns)")

        plt.title("Loan amount distribution")

        
        # show plot
        plt.savefig('plots/loan_amount_boxplot.png', transparent=True)


        durations = loans["duration"]
        amounts = loans["amount"]

        fig, ax = plt.subplots(figsize =(16, 9))

        plt.scatter(durations, amounts)
        plt.xlabel("Duration (months)") 
        plt.ylabel("Amount (czech crowns)")
        plt.title("Relation between loan amount and duration")

        plt.savefig('plots/loan_amount_duration_scatter.png', transparent=True)


        payments = loans["payments"]

        fig, ax = plt.subplots(figsize =(16, 9))

        sc = plt.scatter(payments, amounts, c=durations)
        plt.xlabel("Payments (czech crowns)")
        plt.ylabel("Amount (czech crowns)")
        cb = fig.colorbar(sc, ax=ax, label='Duration (months)')

        plt.title("Relation between loan amount, payments and duration")

        plt.savefig('plots/loan_amount_payments_duration_scatter.png', transparent=True)


def plot_transactions():

        loans_accountid = loans["account_id"].unique()
        transactions_in_loans = transactions[transactions["account_id"].isin(loans_accountid)]

        transactions_to_plot = transactions_in_loans

        balances = [x for x in range(0, 190001, 5000)]
        amounts = [x for x in range(0, 90001,2500)]

        amount = transactions_to_plot["amount"]
        balance = transactions_to_plot["balance"]
        frequency = []

        balance_rebalance = list(map(lambda x: balances[int(x//5000)], balance))
        amount_rebalance = list(map(lambda x: amounts[int(x//2500)], amount))

        amount = amount_rebalance
        balance = balance_rebalance


        points = list(zip(amount, balance))

        points_dict = {}
        for point in points:
                if point in points_dict:
                        points_dict[point] += 1
                else:
                        points_dict[point] = 1
        
        for point in points:
                frequency.append(points_dict[point])


        fig, ax = plt.subplots(figsize =(16, 9))


        

        hb = plt.hexbin(x=amount, y=balance, C=frequency, gridsize=(30, 15), cmap="Reds", bins="log")
        cb = fig.colorbar(hb, ax=ax, label='Frequency')

        plt.title("Transaction amount related to balance")
        plt.xlabel("Amount")
        plt.ylabel("Balance")
        plt.savefig('plots/transaction_amount_balance.png', transparent=True)


def plot_districts():
        #nº habitants, urban ratio and average salary
        salary = districts["average salary "]
        habitants = districts["no. of inhabitants"]
        urban_ratio = districts["ratio of urban inhabitants "]
        num_enterporneurs = districts["no. of enterpreneurs per 1000 inhabitants "]
        unemployment_95 = districts["unemploymant rate '95 "]
        unemployment_96 = districts["unemploymant rate '96 "]
        num_crimes_95 = districts["no. of commited crimes '95 "]
        num_crimes_96 = districts["no. of commited crimes '96 "]
        avg_unemployment = (unemployment_95 + unemployment_96) / 2
        avg_num_crimes = (num_crimes_95 + num_crimes_96) / 2
        

        fig, ax = plt.subplots(figsize =(16, 9))
        sc = plt.scatter(habitants, urban_ratio, c=salary)
        plt.xlabel("Nº habitants")
        plt.ylabel("Ratio of Urban Inhabitants")
        cb = fig.colorbar(sc, ax=ax, label='Average Salary')
        plt.title("Relation between salary, habitants and urban ratio")
        plt.savefig('plots/salary_habitants_urbanratio_scatter.png', transparent=True)

        fig, ax = plt.subplots(figsize =(16, 9))
        sc = plt.scatter(habitants, num_enterporneurs, c=salary)
        plt.xlabel("Nº habitants")
        plt.ylabel("Nº enterpreneurs per 1000 habitants")
        cb = fig.colorbar(sc, ax=ax, label='Average salary')
        plt.title("Relation between salary, habitants and number of enterpreneurs")
        plt.savefig('plots/salary_habitants_enterpreneurs_scatter.png', transparent=True)

        fig, ax = plt.subplots(figsize =(16, 9))
        sc = plt.scatter(habitants, avg_unemployment, c=salary)
        plt.xlabel("Nº habitants")
        plt.ylabel("Averega Unemployment Rate in '95 and '96")
        cb = fig.colorbar(sc, ax=ax, label='Average salary')
        plt.title("Relation between salary, habitants and Averega Unemployment Rate")
        plt.savefig('plots/salary_habitants_unemployment_scatter.png', transparent=True)

        fig, ax = plt.subplots(figsize =(16, 9))
        sc = plt.scatter(habitants, avg_num_crimes, c=salary)
        plt.xlabel("Nº habitants")
        plt.ylabel("Averega number of crimes in '95 and '96")
        cb = fig.colorbar(sc, ax=ax, label='Average salary')
        plt.title("Relation between salary, habitants and Average number of crimes")
        plt.savefig('plots/salary_habitants_crime_scatter.png', transparent=True)


        fig = plt.figure(figsize =(16, 9))
        ax =plt.axes(projection ="3d")
        sc = ax.scatter3D(habitants, urban_ratio, num_enterporneurs, c=salary)
        plt.xlabel("Nº habitants")
        plt.ylabel("Ratio of Urban Inhabitants")
        ax.set_zlabel("Nº enterpreneurs per 1000 habitants")
        cb = fig.colorbar(sc, ax=ax, label='Average Salary')
        plt.title("Relation between salary, habitants, urban ratio and number of enterpreneurs")
        plt.savefig('plots/salary_habitants_urbanratio_enterpreneurs_scatter.png', transparent=True)


def plot_final_dataset():
        # importing diamond dataset from the library
        fig, ax = plt.subplots(figsize =(15, 10))
        # plotting histogram for carat using distplot()
        age_displot = sns.displot(final_dataset["age"], kde=True, bins=20, kde_kws=dict(cut=3))


        plt.savefig('plots/age_of_loan_displot.png', transparent=True)


        #avg salary and recent balance
        figure, axis = plt.subplots(nrows=2, ncols=2, figsize=(16, 11))
        axis[0][0].hist(final_dataset["average_balance_fluctuation_per_month"], bins=20, )
        axis[0][0].set_title("Balance variation per month frequency")
        axis[0][1].boxplot(final_dataset["average_balance_fluctuation_per_month"], labels=[""])
        axis[0][1].set_title("Balance variation per month Boxplot")
        axis[1][0].hist(final_dataset["recent_balance"], bins=20, )
        axis[1][0].set_title("Recent Balance Frequency")
        axis[1][1].boxplot(final_dataset["recent_balance"], labels=[""])
        axis[1][1].set_title("Recent Balance Boxplot")
        plt.savefig('plots/balanceVariation_balance_distributions.png', transparent=True)

        #salary and balance by sex

        males = final_dataset[final_dataset["sex"] == 1]
        females = final_dataset[final_dataset["sex"] == 0]

        fig, ax = plt.subplots(figsize =(16, 9))

        ax.scatter(males["average_balance_fluctuation_per_month"], males["recent_balance"], s=10, c="blue", marker="s", label="males")
        ax.scatter(females["average_balance_fluctuation_per_month"], females["recent_balance"], s=10, c="red", marker="o", label="females")
        
        b_male, a_male = np.polyfit(males["average_balance_fluctuation_per_month"], males["recent_balance"], deg=1)
        b_female, a_female = np.polyfit(females["average_balance_fluctuation_per_month"], females["recent_balance"], deg=1)
        xseq = np.linspace(0, 10, num=100)

        ax.plot(xseq, a_male + b_male * xseq, color="blue", lw=2.5)
        ax.plot(xseq, a_female + b_female * xseq, color="red", lw=2.5)

        
        plt.xlabel("Average Balance Fluctuation per month")
        plt.ylabel("Recent balance")
        plt.legend(loc="upper right")
        plt.title("Balance Variantion and Total Balance for men and women")
        plt.savefig('plots/BalanceVariation_balance_sex_scatter.png', transparent=True)



def main():
        plt.rcParams.update({'font.size': 12})
        accounts_plot()
        card_plot()
        plot_loans()
        plot_transactions()
        plot_districts()
        plot_final_dataset()
       


        
if __name__ == "__main__":
    main()