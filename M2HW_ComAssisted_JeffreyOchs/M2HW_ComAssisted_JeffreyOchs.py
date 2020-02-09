# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:37:54 2020

@author: ochsj6181
"""



def main():
    choice = 0
    while choice != 2:
        choice = menu()
        if choice == "1":
            get_randomNumbers()
            main()
        elif choice == "2":
            print("Exiting Program")
        else:
            print("Not an options please enter 1 or 2.")
        
        
        
    
    
    
    
    
    

def menu():

    print(' MENU')
    print("1.  Practice multiplicaiton.")
    print("2.  Quit")
    
if __name__ =="__main__":
    main()


