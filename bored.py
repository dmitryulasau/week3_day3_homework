from colorizer import *
from activity import Activity

def main():
    act = Activity()

    while True:
        clear_screen()
        option = input("*** Welcome to -= DO IT NOW! =- activity center ***\n"  
                       
                       "\nOPTIONS: "
                       "\n\t- (1) Search activity by PRICE"
                       "\n\t- (X) Search activity by TYPE - WORK IN PROGRESS... PLEASE SEARCH ACTIVITY BY PRICE (1)"
                       
                       "\n\t- (0) NOT BORED? - QUIT - enter '0' or 'q'\n"

                       "\nWHAT WOULD YOU LIKE? "
                        )
        
        # [ WRONG INPUT ] //////////////////////////////////////////////////////////////////////////////////////////+
        if option[0].lower() not in {'1', '2', '0', 'q'} or len(option) > 1:
            
            print("\n-* !WRONG INPUT! PLEASE FOLLOW THE INSTRUCTIONS *-\n")
            continue
        
        # [ QUIT ] ////////////////////////////////////////////////////////////////////////////////////////////////+
        if option[0].lower() == 'q' or option == "0":
            clear_screen()
            print_magenta("Bye Bye Berdie! \ (••) /")
            break
        
        elif option == "2":
            
            print("\n-* WORK IN PROGRESS... PLEASE SEARCH ACTIVITY BY PRICE (1) *-\n")
            continue
            
        
        # ACTIVITY BY PRICE
        if option == "1":
            
            clear_screen()
            print("Please enter a minimum and maximum price you would like to spend: "
                  "\n* Only numbers! *")
            
            #MIN
            min_price = input("\nWhat is the MINIMUM? MISER! ")
            if not min_price.isdigit():
                print("\n-* !WRONG INPUT! PLEASE FOLLOW THE INSTRUCTIONS *-\n")
                continue
            else:
                min_price = int(min_price)/1000
   
            #MAX
            max_price = input("What is the MAXIMUM?  Open you wallet! ")
            if not max_price.isdigit():
                print("\n-* !WRONG INPUT! PLEASE FOLLOW THE INSTRUCTIONS *-\n")
                continue
            else:
                max_price = int(max_price)/1000

            clear_screen()
            act.get_activity(min_price, max_price)
            act.show_activity()

        repeat = input("\nDo you like this activity? YES - main menu / 'NO' - show me more activities / 'Q' - quit ")
        
        if repeat[0].lower() == 'n':
            clear_screen()
            act.get_activity(min_price, max_price)
            act.show_activity()

        elif repeat[0].lower() == 'q':
            clear_screen()
            print_magenta("Bye Bye Berdie! \ (••) /")
            break

        elif repeat[0].lower() == 'y':
          continue

