'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
investor = False
balance = 200 #similiar to the canteen
stamina = 100 #stamina
rent = 40 #thirst but mandatory
revenue = 50 #miles in this game
rival_revenue = 50 #how close your enemies are
income = 50
employees = 0
month = 0
quit = "n"

print("Instructions")
print()
print("During the lowest point of your life, you decide to start a company.")
print("You rent a dirty and cramped apartment in a crowded city for 40 cash.")
print("You don't have a job since you applied to every place nearby so this company has to fully support you.")
print("So be determined!")
print()
print("But there's a problem...")
print("A rival of yours has decided to create a similar company")
print("Your goal is to grow your company's REVENUE and avoid being taken over by your rival and don't be bankrupt!")
print()
print("You have to take care of your BALANCE which you don't have a lot of.")
print("Your RENT also takes off from your balance every day so beware of that.")
print("Take care of yourself since you still can get tired so watch your STAMINA and take a vacation or hire more EMPLOYEES to take part of the work for you.")
print("Alright you're good to go!")
company_name = input("What is your company name again? ")

print("Thank you and Good Luck! CEO of", company_name.upper())
print()

while quit == "n":
    print("----------------")
    print("-MONTHLY REPORT-")
    print("MONTH: ",month)
    print("INCOME: ",income)
    print("BALANCE: ", balance)
    print("YOUR REVENUE: ", revenue)
    print("RIVAL'S REVENUE: ", rival_revenue)
    print("REVENUE DIFFERENCES: ", revenue-rival_revenue)
    print("STAMINA: ", stamina)
    print("EMPLOYEES: ", employees)
    print("----WEEK PLAN----")
    print("A. Advertise your company (Increases REVENUE)")
    print("B. Buy smaller companies (Increases REVENUE more)")
    print("C. Hire more people (Adds EMPLOYEES)")
    print("D. Attract Investors (Increases BALANCE but decreases INCOME)")
    print("E. Take a vacation (Increases STAMINA)")
    print("Q. Sell your company (Quit)")
    plan = input("What's the plan this month? ")

    if plan.upper() == "A":
        if stamina<=10:
            print("You're too tired, get a vacation!")
        else:
            advertsuccess = random.randint(1, 4)
            revenue = revenue+revenue/advertsuccess
            income = revenue/2+income
            print("You advertised your company.")
            print("Your INCOME has grown to ", income,"!")
            print("Your REVENUE has grown to ", revenue,"!")
    elif plan.upper() == "B":
        if stamina<=10:
            print("You're too tired, get a vacation!")
        else:
            if revenue<=10000:
                print("You're to small to buy companies. Your REVENUE has to be at least 10,000.")
                print("Your REVENUE: ", revenue)
            else:
                revenue = revenue*2
                income = revenue/2+income
                print("You brought a company and merged it into yours.")
            print("Your INCOME has grown to ", income, "!")
            print("Your REVENUE has grown to ", revenue, "!")
    elif plan.upper() == "C":
        if stamina<=10:
            print("You're too tired, get a vacation!")
        else:
            if income<100:
                print("You can't afford any more employees right now.")
                print("Your INCOME: ", income)
            else:
                employees = employees+1
                print("You have hired an employee!")
                print("You now have ",employees," employees")
    elif plan.upper() == "D":
        if stamina<=10:
            print("You're too tired, get a vacation!")
        else:
            investor = True
            investmentnum = random.randint(5,6)
            investment= income/investmentnum
            balance = balance+investment
            income = income-investment
            print("You have attracted an investor")
            print("Your BALANCE is now ",balance,)
            print("But your investors now own ",investment," out of your INCOME!")
            print("Your INCOME is now ",income)
    elif plan.upper() == "E":
        if employees == 0:
            print("You don't have anyone to run the company while you're gone!")
        stamina = stamina+employees*10
        if stamina<100 and employees > 0:
            stamina = 110
        print("That vacation gave you a nice break")
        print("And your ",employees, "employees have ran your company while you were away!")
        print("Your STAMINA has grown to ", stamina,"!")
    elif plan.upper() == "Q":
        quit = "y"
    stamina = stamina-10
    stamina = stamina+employees*0.25
    rival_income = random.randint(2, 3)
    rival_revenue = rival_revenue+rival_revenue/rival_income
    balance = balance+income
    balance = balance-rent
    event = random.randint(1,7)
    if event == 1:
        print("----NOTHING HAPPENED----")
        print("Nothing happened, go home!")
    elif event == 2:
        print("----CELEBRITIES ENDORSES ",company_name,"!----")
        print("After posts from a few celebrities' social medias, people have flocked to ", company_name," to join the trend. It seems that this could be a sign of great success coming our way.")
        revenue = revenue+revenue/2
        rival_revenue = rival_revenue-rival_revenue/8
        print("Your REVENUE has grown to ", revenue, "!")
        print("Rival's REVENUE has shrunk to ,", rival_revenue, "!")
    elif event == 3:
        print("----CELEBRITIES ENDORSES RIVAL COMPANY!----")
        print("After posts from a few celebrities' social medias, people have flocked to our rival to join the trend. It seems that this could be a sign of great failure coming our way.")
        rival_revenue = rival_revenue + rival_revenue /2
        revenue = revenue-revenue/8
        print("Rival's REVENUE has grown to ", rival_revenue, "!")
        print("Your REVENUE has shrunk to ,", revenue, "!")
    elif event == 4:
        if investor == True:
            print("----OUR INVESTOR IS A TRAITOR!!!----")
            print("We recently have found out that one of our investors sold their share to our rival. That means a percentage of our revenue goes to them!")
            if balance >= investment:
                print("Don't worry, we brought the share back! But shouldn't that be illegal?")
                balance = balance-investment
                print("Your BALANCE has shrunk to ", balance,"!")
            else:
                print("I guess we have to live with this now since we have no money. We should take this to court!")
                rival_revenue = rival_revenue+investment
                print("Rival's REVENUE has grown to ", rival_revenue, "!")
        else:
            print("----NOTHING HAPPENED----")
            print("Nothing happened, go home!")
    elif event == 5:
        print("----SALES RISES----")
        print("This month has been our highest month yet! This is a major jump for our company! Guess we won't be poor anytime soon!")
        revenue = revenue+revenue*0.25
        income = income+income*0.25
        print("Your REVENUE has grown to ",revenue,"!")
        print("Your INCOME has grown to ", income, "!")
    elif event == 6:
        reviews = random.randint (1,20)
        print("----GREAT REVIEWS----")
        print("Our company has recieved ",reviews," good reviews! Good Job!")
        reviews = reviews*0.001
        revenue = revenue+revenue*reviews
        print("Your REVENUE has grown to ", revenue, "!")
    elif event == 7:
        print("----RAT IN OFFICE----")
        print("Numerous sighting of a rat have been circulating around in the company. You have been ignoring it for so long but then YOU saw it.")
        print("You panicked but it moved so fast, you hardly saw it. Minutes later, you hear screams froom outside your office.")
        revenue=revenue-revenue*0.02
        print("Your REVENUE has shrunk to ", revenue, "!")
    if stamina == -10:
        stamina = 60
        print("You took a month off")
    month = month+1