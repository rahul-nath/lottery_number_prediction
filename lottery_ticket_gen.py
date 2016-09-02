import os
from numpy.random import randint

def gen_small():
    return randint(1,10)

def gen_mid_low():
    return randint(10,20)

def gen_mid():
    return randint(20,30)

def gen_mid_high():
    return randint(30,50)

def gen_high():
    return randint(50,70)

def gen_powerball():
    return randint(1,26)

ticket_type_1 = [gen_small, gen_mid_low, gen_mid, gen_high, gen_high] # gen_high dominant
ticket_type_2 = [gen_small, gen_small, gen_mid_low, gen_mid, gen_mid_high] # gen_small dominant
ticket_type_3 = [gen_mid_low, gen_mid_low, gen_mid, gen_mid_high, gen_high] # gen_mid_low dominant
ticket_type_4 = [gen_small, gen_mid_high, gen_mid_high, gen_high, gen_high] # mid_high, high dominants
ticket_type_5 = [gen_mid, gen_mid, gen_mid_low, gen_mid_high, gen_high] # gen_mid dominant
ticket_type_6 = [gen_small, gen_mid_low, gen_mid, gen_mid_high, gen_high] # no dominant

def gen_numbers(ticket_type):
    picked_nums = []
    # need to avoid duplicates
    for num_gen in ticket_type:
        picked = num_gen()
        while picked in picked_nums:
            picked = num_gen()
        picked_nums.append(picked)
    picked_nums.append(gen_powerball())
    print picked_nums

tickets = {"ticket_type_1": ticket_type_1, "ticket_type_2": ticket_type_2, 
           "ticket_type_3": ticket_type_3, "ticket_type_4": ticket_type_4, 
           "ticket_type_5": ticket_type_5, "ticket_type_6": ticket_type_6}

def gen_rand_tickets(num_tickets):
    print "\nRandomly selected:"
    ticket_set = []
    for i in range(0, num_tickets):
        print gen_numbers(tickets["ticket_type_{0}".format(randint(1, num_tickets+1))])
        

def gen_all_types():
    num_tickets = int(raw_input("How many tickets do you want?  "))
    print "\nRahul's types:"
    count = 1
    for k,v in tickets.items():
        gen_numbers(v)
        if count == num_tickets:
            break
        count += 1
    print "\n"

#gen_rand_tickets(5)
gen_all_types()
