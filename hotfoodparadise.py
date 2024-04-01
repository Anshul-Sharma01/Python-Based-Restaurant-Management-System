dash=("--------------------------------------------------------------")
ndash=("______________________________________________________________")
eq=("==============================================================")
combo=("""______________________________________________________________
==============================================================""")
megadash=("----------------------------------------------------------------------------------------------------------------------------")
megacombo=("""____________________________________________________________________________________________________________________________
----------------------------------------------------------------------------------------------------------------------------""")
fence=("===========================================**************************************===========================================")
megaeq=("============================================================================================================================")
sfence=("==================**************************==================")
s1=(" ")
s2=(" ")
s3=(" ")
def signup():
        global s1
        l1=[]
        for a in r1 :
            if a  == []:
                pass
            else:
                l1.append(a[0])
        print("\n\t\t\t   SIGN IN\n")
        print(eq)
        nm=input("Enter your name                :   ")
        s1=s1+nm
        eid=input("--------------------------------------------------------------\nEnter email ID (must contain '@gmail.com')                :   ")
        while eid  in l1:
            print("--------------------------------------------------------------\nAn account already exists with the ID", eid ,".\Please log in or enter another email ID! \n ----------------------------------------------------------------")
            eid = input("Enter ID(must contain '@gmail.com')-------------->")
            continue
                
            


            

        
        pw=" "
        pwc=""
        while pw!=pwc:
            pw=input("--------------------------------------------------------------\nEnter Password                 :   ")
            pwc=input("--------------------------------------------------------------\nConfirm your password          :   ")
            print(eq)
            if pw!=pwc:
                print("Incorrect password. \nPlease re-enter your password.")
        print("WELCOME TO HOTFOODPARADISE,",nm.title(),".\nYOUR ACCOUNT HAS BEEN SUCCESSULLY CREATED WITH THE EMAIL ID\n" , eid,".\n==============================================================")
        if pw==pwc:
            rec=[eid,pw,nm]
            w1.writerow(rec )


def login():
    global s2
    global s3
    l1=[]
    l2=[]
    for a in r1 :
       if a  == []:
            pass
       else:
            l1.append(a[0])
            l2.append(a)
            
    for tr in range(3):
        print("\n\t\t\tLOG IN\n")
        print(eq)
        eid=input("Enter email ID                 :   ")
        if eid in l1:
            lo=l1.index(eid)
            break
        elif tr==2:
                print("--------------------------------------------------------------\nIncorrect Password.\nWe're sorry to take you out of the program.")
                print(eq)
                quit()
        else:
            print("------------------------------------------------------------\nNo account exists for ",eid,".\nPlease enter a valid email ID.\n\n")
            continue
    for tr in range(3):
        ps=input("---------------------------------------------------------------\nEnter your password            :   ")
        if l2[lo][1]==ps:
             print(eq,"\nWelcome to HOTFOODPARADISE.\nYou have successfully logged into your account with the email \nID ", eid,"and \nname:-",l2[lo][2],".")
             s2=s2+l2[lo][2]
             s3=s3+eid
             
             print(eq)
             break
        else:
            if tr!=2:
                print(eq,"\nWrong Password. Try again.")
            elif  tr==2:
                print("--------------------------------------------------------------\nIncorrect Password.\nWe're sorry to take you out of the program.")
                print(eq)
                quit()


def Intro():
    print(combo)
    print("\t          WELCOME TO HOTFOODPARADISE\n\t     THE NO.1 FOOD DELIVERY APP OF INDIA!")
    print("==============================================================\nIf you already have an account :   (Enter 1 to Log In)\n--------------------------------------------------------------\nTo create a new account        :   (Enter 2 to Sign In)")
    print("==============================================================")
    ch1=int(input("Enter your choice              :   "))
    print("==============================================================")
    return ch1



# _main_
import csv
f1=open(r"IdPass.csv","a+",newline="")
w1=csv.writer(f1)

f1.seek(0)
r1=csv.reader(f1)




while True:
    try:
        ch1=Intro()
        if ch1==1:
            login()
            break
        if ch1==2:
            signup()
            break
        else:
            print("\n\n\n\nPLEASE ENTER VALID INPUT!!!!\n\n")
            continue

    except ValueError:
        print("\n\n\n\nPLEASE ENTER VALID INPUT!!!!\n\n")
    
            
    

f1.close()



####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS) !!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS)!!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS)!!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS)!!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS)!!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS) !!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS)!!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS)!!!!!!!!!!!####################################
####################################!!!!!!!!!!!!HELP AND SUPPORT(FUNCTIONS) !!!!!!!!!!!####################################

def FAQs():
    def qs():
        print("FREQUENTLY ASKED QUESTIONS:")
        print(sfence)
        print("01",q1,"\n--------------------------------------------------------------")
        print("02",q2,"\n--------------------------------------------------------------")
        print("03",q3,"\n--------------------------------------------------------------")
        print("04",q4,"\n--------------------------------------------------------------")
        print("05",q5,"\n--------------------------------------------------------------")
        print("06",q6,"\n--------------------------------------------------------------")
        print("07",q7,"\n--------------------------------------------------------------")
        print("08",q8,"\n--------------------------------------------------------------")
        print("09",q9,"\n--------------------------------------------------------------")
        print("10",q10,"\n--------------------------------------------------------------")
        print("11",q11,"\n--------------------------------------------------------------")
        print("12",q12,"\n--------------------------------------------------------------")
        print("13",q13,"\n--------------------------------------------------------------")
        print("14",q14,"\n--------------------------------------------------------------")
        print("15",q15)
        print(sfence)
        print("""Please select your query from among the preceding Frequently \nAsked Questions. If your problem is not among these questions,\nplease enter 16.""")
        print(eq)
        ans=int(input("Enter your choice      :      "))
        print(eq)
        return ans
    A1=("""Offers shows up anytime you want, just choose "offers" from \nthe list.""")
    A2=("Offers might be outdated because they are showed according to \nfestive seasons. There is a slight possibility that the offers \nhave not been updated due to a prolonged season. They refresh \nevery once in a while. Please wait for them to refresh or \nwrite to the Help Desk for further help.")
    A3=("""For SIGNING IN, you have to first register yourself on the app \nby choosing the "Sign In" Option on the home page. Once you \nhave signed in, you can choose the "Log In"  option to LOG IN \nwhen you enter the app the next time. It's that simple.""")
    A4=("You can select items by just typing the serial numbers of the \nrespective items in the input area.")
    A5=("Yes. It is an automatic process. The items you choose move \ninto the cart by themselves, you you don't have to worry about \nit.")
    A6=("It is an automatic process. The items you choose move into \nthe cart by themselves, you you don't have to worry about it.")
    A7=("Recommendations are based on your interests. The items you \nview or select are considered for recommendations. That might \nbe the reason you are receiving same recommendations again and \nagain. For further help, please write to the Help Desk.")
    A8=("Locate the items through the categories in the maun menu. \nThe search option has not been made availabe yet.")
    A9=("Yes. You can purchase veg and non-veg items at the same time \nsince there are no restrictions regarding the same.")
    A10=("No, there is no such restriction, you can select any number of \nitems and quantity of food items.")
    A11=("""You can contact help and support by choosing the \n"Help and Support" option from any page.""")
    A12=("After selecting your desired food items you can pay through \nthe Billing WIndow, the option of which will appear after \nselecting the food items.")
    A13=("The Option to open the Billing Window will appear after you \nhave completed selecting the food items.")
    A14=("No, it is not mandatory to buy the items you have moved to the \ncart. To empty the cart, just close the app and open it again.")
    A15=("No, it is mandatory to pay for the items you have moved to the \ncart. No item can be purchased for free unless it is a special \noffer.")
    q1="Why are the offers not showing up?"
    q2="Why are the offers outdated?"
    q3="How do I Log-in / Sign-in?"
    q4="How can I select items?"
    q5="Do I need to put items in cart for purchasing?"
    q6="How do I move selected items to cart?"
    q7="Why I am getting same recommendations again and again?"
    q8="How do I search for items?"
    q9="Can I purchase both veg and non-veg items at the same time?"
    q10="Are there any restrictions in the number of selected items?"
    q11="How do I contact help and support?"
    q12="How do I pay ?"
    q13="How do I get to the billing window?"
    q14="Is is mandatory to buy the items I have put in the cart?"
    q15="Can I get any items for free?"
    
    while True:
        try:
            pb=qs()
            if pb==1:
                print(A1)
                print()
                break
            elif pb==2:
                print(A2)
                print()
                break
            elif pb==3:
                print(A3)
                print()
                break
            elif pb==4:
                print(A4)
                print()
                break
            elif pb==5:
                print(A5)
                print()
                break
            elif pb==6:
                print(A6)
                print()
                break
            elif pb==7:
                print(A7)
                print()
                break
            elif pb==8:
                print(A8)
                print()
                break
            elif pb==9:
                print(A9)
                print()
                break
            elif pb==10:
                print(A10)
                print()
                break
            elif pb==11:
                print(A11)
                print()
                break
            elif pb==12:
                print(A12)
                print()
                break
            elif pb==13:
                print(A13)
                print()
                break
            elif pb==14:
                print(A14)
                print()
                break
            elif pb==15:
                print(A15)
                print()
                break
            elif pb==16:
                sol=input("Please elaborate the problem here:")
                import csv
                f1=open("DEVELOPERSDATA.csv","a+",newline="")
                w1=csv.writer(f1)
                solu=("Issue from FAQs.")
                sloun=[solu,sol]
                w1.writerow(sloun)
                f1.close
                print("Sorry for inconveniece. The problem will be forwarded to the \nrespective teams. Thank you for your cooperation.")
                print()
                break
            else:
                print("Invalid input!!!!!!")
                continue
        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!!")

def login_error():
    import csv
    f1=open("DEVELOPERSDATA.csv","a+",newline="")
    w1=csv.writer(f1)
    is1=("The program is not taking inputs.")
    is2=("The program is not responding to an input.")
    is3=("Unale to log in/sign in.")
    is4=("Not recognizing name/email id/password.")
    is5=("No response after logging/signing in.")
    is6=("Some other problem.")
    print("Choose the problem you are facing:")
    print(sfence)
    print("01. The program is not taking inputs.")
    print(dash)
    print("02. The program is not responding to an input.")
    print(dash)
    print("03. Unale to Log-In/Sign-In.")
    print(dash)
    print("04. Not recognizing Name/Email-id/Password.")
    print(dash)
    print("05. No response after Logging/Signing in.")
    print(dash)
    print("06.For some other problem,you can input any number (other than 1-5).")
    print(eq)
    while True:
        try:
            pb=int(input("Enter your choice      :      "))
            print(dash)
            pb=str(pb)
            if pb.isdigit():
                break
            
        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")
        
    sol=(input("Please elaborate your problem: "))
    print(eq)
    pb=int(pb)
    if pb==1:
        sol1=[is1,sol]
        w1.writerow(sol1)
                
    elif pb==2:
        sol1=[is2,sol]
        w1.writerow(sol1)
                
    elif pb==3:
        sol1=[is3,sol]
        w1.writerow(sol1)
                
    elif pb==4:
        sol1=[is4,sol]
        w1.writerow(sol1)
                
    elif pb==5:
        sol1=[is5,sol]
        w1.writerow(sol1)
                
    elif pb>=6:
        sol1=[is6,sol]
        w1.writerow(sol1)
                
    
    print("Sorry for inconveniece. The problem will be forwarded to the\nrespective teams. Thank you for cooperation.")
    print(sfence)
    print()
    f1.close()

def offer_recom():
    import csv
    f1=open("DEVELOPERSDATA.csv","a+",newline="")
    w1=csv.writer(f1)
    is1=("Offers are not being displayed.")
    is2=("Unable to select items.")
    is3=("Unable to add items to cart.")
    is4=("Unable to avail offers.")
    is5=("Recommendations are not good enough.")
    is6=("For some other problem,you can input any number (other than 1-5).")
    print("Choose the problem you are facing:")
    print(sfence)
    print("01.",is1)
    print(dash)
    print("02.",is2)
    print(dash)
    print("03.",is3)
    print(dash)
    print("04.",is4)
    print(dash)
    print("05.",is5)
    print(dash)
    print("06.",is6)
    print(eq)
    while True:
        try:
            pb=int(input("Enter your choice      :      "))
            print(dash)
            pb=str(pb)
            if pb.isdigit():
                break
            

        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")
    sol=(input("Please elaborate your problem: "))
    print(eq)
    pb=int(pb)
    if pb==1:
        sol1=[is1,sol]
        w1.writerow(sol1)
    elif pb==2:
        sol1=[is2,sol]
        w1.writerow(sol1)
    elif pb==3:
        sol1=[is3,sol]
        w1.writerow(sol1)       
    elif pb==4:
        sol1=[is4,sol]
        w1.writerow(sol1)
    elif pb==5:
        sol1=[is5,sol]
        w1.writerow(sol1)
    elif pb>=6:
        sol1=[is6,sol]
        w1.writerow(sol1)
   
      
    
    print("Sorry for inconveniece. The problem will be forwarded to the \nrespective teams. Thank you for cooperation.")
    print(sfence)
    print()
    f1.close()

def billinpay():
    print('Choose the problem you are facing:')
    print(sfence)
    pb1=("Wrong bill made.")
    print("1.",pb1)
    print("--------------------------------------------------------------")
    pb2=("Change in prices at the time of payment.")
    print("2.",pb2)
    print("--------------------------------------------------------------")
    pb3=("Suitable payment method not found.")
    print("3.",pb3)
    print("--------------------------------------------------------------")
    pb4=("Payment is not working.")
    print("4.",pb4)
    pb5=("For some other problem,you can input any number (other than 1-5).")
    print("5.",pb5)
    print(eq)
    while True:
        try:
            ch=int(input("Enter your choice      :      "))
            ch=str(ch)
            if ch.isdigit():
                break
            else:
                print("PLEASE ENTER VALID INPUT!!!!")
        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")
    print(eq)
    pb=str(pb5)
    if ch==1:
        import csv
        fh=open("DEVELOPERSDATA.csv","a+",newline="")
        fw=csv.writer(fh)
        print("You can cancel the bill and can go back to select it again.")
        print("If the above method is also not working , you can elaborate \nthe query below:-")
        print(eq)
        q1=input("Enter your query       :      ")
        ins=[pb1,q1]
        fw.writerow(ins)
        print(eq)
        print("Sorry for the inconvenience caused.\nYour query has been sent to the developers.")
        fh.close()
        print(sfence)
        print()
    elif ch==2:
        import csv
        fh=open("DEVELOPERSDATA.csv","a+",newline="")
        fw=csv.writer(fh)
        print("There might be a price increment or decrement after you put \nit in the cart, this mostly happens during festive seasons.")
        fh.close()
        print(sfence)
        print()
    elif ch==3:
        import csv
        fh=open("DEVELOPERSDATA.csv","a+",newline="")
        fw=csv.writer(fh)
        print("Sorry for the inconveninece caused,\nyou can specify the suitable payment method below and we will \ntry to work on it as soon as possible.")
        print(eq)
        q2=input("Enter your query       :      ")
        ins=[pb3,q2]
        fw.writerow(ins)
        print(eq)
        print("Your feedback has been forwarded.")
        print(sfence)
        print()
        fh.close()
    elif ch==4:
        import csv
        fh=open("DEVELOPERSDATA.csv","a+",newline="")
        fw=csv.writer(fh)
        print("Kindly specify below the problems you are facing during \npayment:-")
        print("--------------------------------------------------------------")
        q3=input("Enter your query       :      ")
        ins=[pb4,q3]
        fw.writerow(ins)
        print(eq)
        print("Sorry for the inconvenience caused!!!\nWe will ook into this matter.")
        print(sfence)
        print()
        fh.close()

    else:
        import csv
        fh=open("DEVELOPERSDATA.csv","a+",newline="")
        fw=csv.writer(fh)
        print("Kindly specify below the problems you are facing !!!!")
        print("--------------------------------------------------------------")
        q3=input("Enter your query       :      ")
        ins=[pb5,q3]
        fw.writerow(ins)
        print(eq)
        print("Sorry for the inconvenience caused!!!\nWe will ook into this matter.")
        print(sfence)
        print()
        fh.close()


##########                 HOME PAGE                 ########

ct=open("cart.csv","w",newline="")  #To Empty Cart
ct.close()
ct=open("cart.csv","a",newline="")
import csv
ct_r=csv.writer(ct)    #writer object for cart file



def offers():
    with open("offerfood.csv",'r')as f1:
        fr=csv.reader(f1)
        from tabulate import tabulate
        fr=list(fr)
        print(megacombo)
        #scale-------------------------------------------------------------
        print("                                                            OFFERS")
        print(megacombo)
        print("                       Enjoy the below mentioned exciting offers on the tasty and delicious food items.")
        print(fence)
        print(tabulate(fr, headers=["S.No.", "Item_Name", "Quantity","Cost",
                                    "%_Off","Offer_Price","You_Save"]))
    print(fence)
    while True:
        try:
            ch=input("""Enter "Y"              :           Select items from OFFERS.
----------------------------------------------------------------------------------------------------------------------------
Enter "N"              :           Terminate and go back to the MAIN MENU.
============================================================================================================================
Enter your choice      :           """)
            print(megadash)
            if ch.strip() in"yY":
                while True:
                    try:
                        i=int(input("Enter S.No of the item :           "))
                        i=str(i)
                        if i.isdigit():
                            break

                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print(megadash)
                while True:
                    try:
                        j=int(input("Enter quantity         :           "))
                        j=str(j)
                        if j.isdigit():
                            break
                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                
                print(megaeq)
                f1=open("offerfood.csv",'r')
                fr=csv.reader(f1)
                for a in fr:
                    if a[0]==i.strip():
                        rec=[a[1],a[2],a[5],j]
                        ct_r.writerow(rec)
                f1.close()
                
            elif ch.strip() in "nN":
                print()
                break
            else:
                print("PLEASE ENTER VALID INPUT!!!!")
                continue

        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")

    f1.close()




def Recommendations():
    with open("Recommendations.csv",'r')as f2:
        file_r=csv.reader(f2)
        from tabulate import tabulate
        file_r=list(file_r)
        print("""________________________________________________________________________________________
----------------------------------------------------------------------------------------""")
        print("                                    RECOMMENDATIONS")
        print("""________________________________________________________________________________________
----------------------------------------------------------------------------------------""")
        print(tabulate(file_r, headers=["S.No.", "Item_Name", "Quantity","Cost","Veg/Non-veg"]))
    print("===============================**************************===============================")
    while True:
        try:
            ch=input("""Enter "Y"              :           Select items from RECOMMENDATIONS.
----------------------------------------------------------------------------------------
Enter "N"              :           Terminate and go back to the MAIN MENU.
========================================================================================
Enter your choice      :           """)
            print("----------------------------------------------------------------------------------------")
            if ch.strip() in"yY":
                
                while True:
                    try:
                        i=int(input("Enter S.No of the item :           "))
                        i=str(i)
                        if i.isdigit():
                            break

                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print(megadash)
                while True:
                    try:
                        j=int(input("Enter quantity         :           "))
                        j=str(j)
                        if j.isdigit():
                            break
                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print("========================================================================================")
                f1=open("Recommendations.csv",'r')
                fr=csv.reader(f1)
                for a in fr:
                    if a[0]==i.strip():
                        rec=[a[1],a[2],a[3],j]
                        ct_r.writerow(rec)
                f1.close()
                
            elif ch.strip() in "nN":
                print()
                break

            else:
                print("PLEASE ENTER VALID INPUT!!!!")
                continue

        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")

            

def nonveg():
    with open("efood.csv",'r')as f3:
        l1=[]
        f_e=csv.reader(f3)
        for p in f_e:
            if p[4]=="n":
                temp=[p[0],p[1],p[2],p[3]]
                l1.append(temp)
        print("""________________________________________________________________________________________
----------------------------------------------------------------------------------------""")
        print("""                                          NON-VEG""")
        print("""________________________________________________________________________________________
----------------------------------------------------------------------------------------""")
        print("                          All non-vegetarian food items available:")
        print("""===============================**************************===============================""")
        from tabulate import tabulate
        print(tabulate(l1, headers=["S.No.", "Item_Name", "Quantity","Cost"]))
        print("===============================**************************===============================")
    while True:
        try:
            ch=input("""Enter "Y"              :           Select items from NON_VEG.
----------------------------------------------------------------------------------------
Enter "N"              :           Terminate and go back to the MAIN MENU.
========================================================================================
Enter your choice      :           """)
            print("----------------------------------------------------------------------------------------")
            if ch.strip() in"yY":
                while True:
                    try:
                        i=int(input("Enter S.No of the item :           "))
                        i=str(i)
                        if i.isdigit():
                            break

                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print(megadash)
                while True:
                    try:
                        j=int(input("Enter quantity         :           "))
                        j=str(j)
                        if j.isdigit():
                            break
                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print("========================================================================================")
                f1=open("efood.csv",'r')
                fr=csv.reader(f1)
                for a in fr:
                    if a[0]==i.strip():
                        rec=[a[1],a[2],a[3],j]
                        ct_r.writerow(rec)
                f1.close()

            elif ch.strip() in "nN":
                print()
                break

            else:
                print("PLEASE ENTER VALID INPUT!!!!")
                continue


        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")




vegdash=("================================***************************================================")
def veg():
    with open("efood.csv",'r')as f3:
        l1=[]
        f_e=csv.reader(f3)
        for p in f_e:
            if p[4]=="v":
                temp=[p[0],p[1],p[2],p[3]]
                l1.append(temp)
                
#              ====================*************==================*****************===============********
        print("""___________________________________________________________________________________________
-------------------------------------------------------------------------------------------""")
        print("""                                          VEG""")
        print("""___________________________________________________________________________________________
-------------------------------------------------------------------------------------------""")
        print("                          All vegetarian food items available:")
        print(vegdash)
        from tabulate import tabulate
        print(tabulate(l1, headers=["S.No.", "Item_Name", "Quantity","Cost"]))
        print(vegdash)
    while True:
        try:
            ch=input("""Enter "Y"              :           Select items from VEG.
-------------------------------------------------------------------------------------------
Enter "N"              :           Terminate and go back to the MAIN MENU.
===========================================================================================
Enter your choice      :           """)
            print("-------------------------------------------------------------------------------------------")
            if ch.strip() in"yY":
                while True:
                    try:
                        i=int(input("Enter S.No of the item :           "))
                        i=str(i)
                        if i.isdigit():
                            break

                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print(megadash)
                while True:
                    try:
                        j=int(input("Enter quantity         :           "))
                        j=str(j)
                        if j.isdigit():
                            break
                    except ValueError:
                        print("PLEASE ENTER VALID INPUT!!!!")
                print("===========================================================================================")
                f1=open("efood.csv",'r')
                fr=csv.reader(f1)
                for a in fr:
                    if a[0]==i.strip():
                        rec=[a[1],a[2],a[3],j]
                        ct_r.writerow(rec)
                f1.close()

            elif ch.strip() in "nN":
                print()
                break

            else:
                print("PLEASE ENTER VALID INPUT!!!!")
        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")





#variables
dash=("--------------------------------------------------------------")
ndash=("______________________________________________________________")
eq=("==============================================================")
combo=("""______________________________________________________________
==============================================================""")
megadash=("----------------------------------------------------------------------------------------------------------------------------")
megacombo=("""____________________________________________________________________________________________________________________________
----------------------------------------------------------------------------------------------------------------------------""")
fence=("===========================================**************************************===========================================")
megaeq=("============================================================================================================================")
#home page
print(combo)
print("\t          WELCOME TO HOTFOODPARADISE\n\t     THE NO.1 FOOD DELIVERY APP OF INDIA!")
print("--------------------------------------------------------------")
print()
while True:
    print("\t                HOME PAGE")
    print(combo)
    print("OFFERS                 :      (Enter 1 for Offers)")
    print("--------------------------------------------------------------")
    print("RECOMMENDATIONS        :      (Enter 2 for Recommendations)")
    print("--------------------------------------------------------------")
    print("VEG                    :      (Enter 3 for Veg items)")
    print("--------------------------------------------------------------")
    print("NON-VEG                :      (Enter 4 for Non-Veg items)")
    print("--------------------------------------------------------------")
    print("HELP & SUPPORT         :      (Enter 5 for Help & Support)")
    print("--------------------------------------------------------------")
    print("BILLING                :      (Enter 6 for Billing & Payments)")
    print(eq)
    
    print(eq)
    try:
        ch=int(input("Enter your choice      :      "))
        if ch==1:
            offers()
        elif ch==2:
            Recommendations()
        elif ch==3:
            veg()
        elif ch==4:
            nonveg()
        elif ch==5:
            print(combo)
            print("\t          HELP AND SUPPORT")
            print(combo)
            while True:
                    print("FAQs                   :      (Enter 1 for FAQs)")
                    print("--------------------------------------------------------------")
                    print("TROUBLESHOOT           :      (Enter 2 for Glitch Reports)")
                    print("--------------------------------------------------------------")
                    print("HOME PAGE              :      (Enter 3 to Go Back)")
                    print(eq)
                    qc=int(input("Enter your choice      :      "))
                    print(eq)
                    if qc==1:
                            FAQs()
                    elif qc==2:
                            print("TROUBLESHOOT:")
                            print(sfence)
                            print("LOG-IN/SIGN-IN         :      (Enter 1)")
                            print("--------------------------------------------------------------")
                            print("OFFERS&RECOMMENDATIONS :      (Enter 2)")
                            print("--------------------------------------------------------------")
                            print("BILLING AND PAYMENT    :      (Enter 3)")
                            print("--------------------------------------------------------------")
                            print("GO BACK                :      (Enter 4)")
                            print("==============================================================")
                            qc1=int(input("Enter your choice      :      "))
                            print("==============================================================")
                            if qc1==1:
                                    login_error()
                            elif qc1==2:
                                    offer_recom()
                            elif qc1==3:
                                    billinpay()
                            else:
                                continue
                    else:
                            break
        
        elif ch==6:
            ct.close()
            break

        else:
            print("INVALID INPUT!!!!!")
    
    except ValueError:
        print("PLEASE ENTER VALID INPUT!!!!!")
            
    
    
        





##########                  BILLING AND PAYMENT                   ##########

import csv
from datetime import date
from datetime import datetime
import csv



print("""________________________________________________________________________________________
----------------------------------------------------------------------------------------
                                   BILLING AND PAYMENT
________________________________________________________________________________________
----------------------------------------------------------------------------------------""")
ct=datetime.now().strftime("%H:%M:%S")
today=date.today()
print("Date:",today,"\t\t\t\t","                       Time:",ct)

def details():
    if ch1==2:
        file1=open("IdPass.csv",newline="\n")
        while True:
            try:
                pno=int(input("Enter phone number     :      "))
                pno=str(pno)
                if len(pno)==10:
                    break
                else:
                    print("PLEASE ENTER VALID PHONE NUMBER:---")
                    continue
            except ValueError:
                print("PLEASE ENTER VALID INPUT!!!!")

                
        print("----------------------------------------------------------------------------------------")
        add=input("Enter your address     :      ")
        print("========================================================================================")
        obj1=csv.reader(file1)
        for i in obj1:
                m=i[0]
        print("Name: ",s1,"\t\t\t\t\t","Email id: ",m,"\t"," \n","-"*103," \n","Address",add,"\t\t\t\t\t","Phone number",pno)
        
    if ch1==1:
        file1=open("IdPass.csv",newline="\n")
        while True:
            try:
                pno=int(input("Enter phone number     :      "))
                pno=str(pno)
                if len(pno)==10:
                    break
                else:
                    print("PLEASE ENTER VALID PHONE NUMBER---")
                    continue

            except ValueError:
                print("PLEASE ENTER VALID INPUT!!!!")
        print("----------------------------------------------------------------------------------------")
        add=input("Enter your address     :      ")
        print("========================================================================================")
        obj1=csv.reader(file1)
        print()
        print()
        print("         ======================**************************=======================")
        print("                                          BILL")
        print("         ======================**************************=======================")
        print("         Name          : ",s2)
        print("         -----------------------------------------------------------------------")
        print("         Email id      : ",s3)
        print("         -----------------------------------------------------------------------")
        print("         Phone number  :  ",pno)
        print("         -----------------------------------------------------------------------")
        print("         Address       :  ",add)
            
print("===============================**************************===============================")
details()


def billingsystem():
    file=open("cart.csv",newline="\n")
    s=csv.reader(file)
    global totalbill
    
    totalbill=0
    for i in s:
        d=float(i[2])*int(i[3])
        print("         =======================================================================")
        print("         Item Name     :  ",i[0])
        print("         -----------------------------------------------------------------------")
        print("         Item Quantity :  ",i[3],"plate(s)")
        print("         -----------------------------------------------------------------------")
        print("         Amount        :  ",d)
        totalbill+=d
    print("         =======================================================================")
    print("         Total amount  :   Rs",totalbill)
    print("         =======================================================================")
    print()
    print()
 
 


billingsystem()

def payment():
        
        print(combo)
        print("                        PAYMENT")
        print(combo)
        print("SELECT PAYMENT METHOD  :")
        print("--------------------------------------------------------------")
        #print("1.Credit Card\n2.Dredit card\n3.Google pay\n4.Paytm")
        print("CREDIT CARD            :      (Enter 1 for Credit Card)")
        print("--------------------------------------------------------------")
        print("DEBIT CARD             :      (Enter 2 for Debit Card)")
        print("--------------------------------------------------------------")
        print("GOOGLE PAY             :      (Enter 3 for Google Pay)")
        print("--------------------------------------------------------------")
        print("PAYTM                  :      (Enter 4 for Paytm)")
        print("--------------------------------------------------------------")
        print("CASH ON DELIVERY       :      (Enter 5 for COD")
        
        global choice
        print(eq)
        try:
            choice=int(input("Enter your choice      :      "))
            print(dash)
            if choice==1:
                v=int(input("Credit Card number     :      "))
                print(dash)
                b=int(input("Enter Password         :      "))
                print(eq)
                print()
                print()
                print(dash)
                print("Your bill of amount Rs",totalbill,"has been paid succesfully.")
                print(dash)
                print("Time of payment:",ct,"\tDate of payment:",today)
                print(dash)
                print()
            elif choice==2:
                v=int(input("Debit Card number      :      "))
                print(dash)
                b=int(input("Password               :      "))
                print(eq)
                print()
                print()
                print(dash)
                print("Your bill of amount Rs",totalbill,"has been paid succesfully.")
                print(dash)
                print("Time of payment:",ct,"\tDate of payment:",today)
                print(dash)
                print()
            elif choice==3:
                v=int(input("Google Pay number      :      "))
                print(dash)
                b=int(input("Password               :      "))
                print(eq)
                print()
                print()
                print(dash)
                print("Your bill of amount Rs",totalbill,"has been paid succesfully.")
                print(dash)
                print("Time of payment:",ct,"\tDate of payment:",today)
                print(dash)
                print()
            elif choice==4:
                v=int(input("Paytm number           :      "))
                print(dash)
                b=int(input("Password               :      "))
                print(eq)
                print()
                print()
                print(dash)
                print("Your bill of amount Rs",totalbill,"has been paid succesfully.")
                print(dash)
                print("Time of payment:",ct,"\tDate of payment:",today)
                print(dash)
                print()
            elif choice==5:
                print("YOUR ORDER WILL BE DELIVERED SOON!!!")
                print("STAY TUNED!!!")
                print(dash)
                print("Time of order:",ct,"\tDate of payment:",today)
                print(dash)
                print()

            elif choice>5:
                pass
                
                
        except ValueError:
            print("PLEASE ENTER VALID INPUT!!!!")  


payment()
print()

def pay():
        while choice>5:
                print(dash)
                print("Please enter valid input.")
                print(dash)
                payment()
        else:
                pass


pay()


print(sfence)
print("                  THANK YOU FOR PURCHASING")
print(sfence)
print("""We would be delighted to hear your experience:""")
print(dash)
print("YES                    :      (Enter 1 to share your feedback)")
print("--------------------------------------------------------------")
print("NO                     :      (Enter 2 to decline)")
F1=open("Feedback.csv","a")
Wr=csv.writer(F1)
print(eq)
while True:
    try:
        sug=int(input("Enter your choice      :      "))
        print(eq)
        if sug==1:
            import csv
            print(combo)
            print("                 FEEDBACK AND SUGGESTIONS")
            print(combo)
            sug1=input("""We will be pleased to know about your experience and hear
suggestions from you:
==============================================================\n""")
            lst1=list(sug1)
            print(eq)
            print()
            print(sfence)
            print("""Thank you for feedback.""")
            print(dash)
            print("We would always try to serve you in the best way we can.")
            print(sfence)
            print()
            print(sfence)
            print("                     HOPE TO SEE YOU AGAIN")
            print(sfence)
            print()
            Wr.writerow(lst1)
            break
        
        elif sug == 2:
            print()
            print(sfence)
            print("                     HOPE TO SEE YOU AGAIN")
            print(sfence)
            print()
            break
        else:
            print("PLEASE ENTER VALID INPUT!!!!")
            continue        
            
    except ValueError:
        print("PLEASE ENTER VALID INPUT!!!!")









        





