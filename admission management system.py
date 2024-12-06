import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password ="",
    database="project"
    )
mycursor=mydb.cursor()
option=0
try:
    while option<=3:  
        print("===============")
        print("|1. ADMISSION  |")
        print("|2. COURSES    |")
        print("|3. EXIT       |")
        print("---------------") 
        while True:
            try:
                option=int(input("enter your option:"))
                if option>0 and option<=3:
                    break
                else:
                    print("invalid input!!")
            except:
                print("invalid input,enter an integer")
        
        if option==1:
            print("1. NEW ADMISSION")
            print("2. EDIT ADMISSION")
            print("3. DELETE")
            print("4.VIEW")
            print("5. BACK")
            while True:
                    try:
                        option=int(input("enter your option:"))
                        if option>0 and option<=5:
                            break
                        else:
                            print("Invalid input!!")
                    except:
                        print("invalid input, enter an integer")   
            if option==1:  #new admission
                print("ENTER")
                print("------")
                name=input("enter your name:")
                while not name:
                    print("name should not empty,enter a name!")
                    name=input("enter a name")
                        
                while True:
                    try:
                        phone=int(input("enter your number:"))
                        break
                    except:
                        print("invalid,try again")
                address=input("enter your address:")
                while not address:
                        print("address should not be empty,enter address.")
                        address=input("enter address")
                gmail=input("enter your gmail:")
                while not gmail:
                    print("gmail should not be empty,enter a valid gmail")
                    gmail=input("enter gmail.")
                district=input("enter your district:")
                while not district:
                    print("district should not be empty,enter district")
                    district=input("enter district")
                mycursor.execute("SELECT * FROM courses")
                myresult=mycursor.fetchall()
                print(tabulate(myresult,headers=['id','name','fees','duration'],tablefmt='psql'))

                #for x in myresult:
                    #print(x)
                while True:
                    try:
                        enrolledcourse=int(input("enter course id:"))
                        for x in myresult:
                            if enrolledcourse==x[0]:
                                sql="INSERT INTO admission(name,phone,address,gmail,district,enrolledcourse) VALUES(%s,%s,%s,%s,%s,%s)"
                                val=(name,phone,address,gmail,district,x[1])
                                mycursor.execute(sql,val)
                                mydb.commit()
                                print("successfully added")
                                break
                        else:
                            print("id not found!!,try again")
                    except ValueError:
                        print("invalid..")
                    break
                    
            elif option==2:  #edit admission
                while option<=7:
                    print("EDIT")
                    print("-----")
                    print("0. VIEW(ID,NAME)")
                    print("1. NAME")
                    print("2. PHONE NUMBER")
                    print("3. ADDRESS")
                    print("4. GMAIL")
                    print("5. DISTRICT")
                    print("6. ENROLLED COURSE")
                    print("7. BACK")
                    while True:
                        try:
                            option=int(input("enter your option:"))
                            if option>=0 and option<=7:
                                break
                            else:
                                print("Invalid option!")
                        except:
                            print("invalid input,enter an integer")
                    if option==0: #view id and name
                        mycursor.execute("SELECT id,name FROM admission")
                        myresult=mycursor.fetchall()
                        print(tabulate(myresult,headers=['id','name'],tablefmt='psql'))
                        break
                    elif option==1:  #edit name
                        mycursor.execute("SELECT id FROM admission")
                        adm=mycursor.fetchall()
                        while True:
                            try:
                                id=int(input("enter the ID of the student,for edit:"))
                                for x in adm:
                                    if id==x[0]:
                                        new_name=input("enter the new name:")
                                        while not new_name:
                                            print("edited name should not empty,enter name.")
                                            new_name=input("enter new name.")
                                        sql="UPDATE admission SET name=%s WHERE id=%s"
                                        val=(new_name,id)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("successfully changed")
                                        break
                                else:
                                    print("ID not found")
                            except ValueError:
                                print("Invalid ID,please enter a valid id.")
                            try:
                                if id==x[0]:
                                    break
                            except:
                                pass
                    elif option==2:  #edit phone
                        mycursor.execute("SELECT id FROM admission")
                        adm=mycursor.fetchall()
                        while True:
                            try:
                                id=int(input("enter the ID of the student,for edit:"))
                                for x in adm:
                                    if id==x[0]:
                                        new_phn=int(input("enter new number:"))
                                        sql="UPDATE admission SET phone=%s WHERE id=%s"
                                        val=(new_phn,id)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("successfully changed")
                                        break
                                else:
                                    print("ID not found!")
                            except ValueError:
                                print("Invalid id,please enter a valid id.")
                            try:
                                if id==x[0]:
                                    break
                            except:
                                pass
                    elif option==3:#edit addr
                        mycursor.execute("SELECT id FROM admission")
                        adm=mycursor.fetchall()
                        while True:
                            try:
                                id=int(input("enter the ID of the student,for edit:"))
                                for x in adm:
                                    if id==x[0]:
                                        new_addr=input("enter the new address:")
                                        while not new_addr:
                                            print("addr should not be empty!")
                                            new_addr=input("enter new address")
                                        sql="UPDATE admission SET address=%s WHERE id=%s"
                                        val=(new_addr,id)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("successfully changed")
                                        break
                                else:
                                    print("ID not found!")
                            except ValueError:
                                print("Invalid id,please enter a valid id.")
                            try:
                                if id==x[0]:
                                    break
                            except:
                                pass
                    elif option==4: #edit mail
                        mycursor.execute("SELECT id FROM admission")
                        adm=mycursor.fetchall()
                        while True:
                            try:
                                id=int(input("enter the ID of the student,for edit:"))
                                for x in adm:
                                    if id==x[0]:
                                        new_mail=input("enter the new mail:")
                                        while not new_mail:
                                            print("gmail should not be empty!")
                                            new_mail=input("enter new gmail")
                                        sql="UPDATE admission SET gmail=%s WHERE id=%s"
                                        val=(new_mail,id)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("successfully changed")
                                        break
                                else:
                                    print("ID not found!")
                            except ValueError:
                                print("Invalid id,please enter a valid id.")
                            try:
                                if id==x[0]:
                                    break
                            except:
                                pass
                    elif option==5: #edit district
                        mycursor.execute("SELECT id FROM admission")
                        adm=mycursor.fetchall()
                        while True:
                            try:
                                id=int(input("enter the ID of the student,for edit:"))
                                for x in adm:
                                    if id==x[0]:
                                        new_dist=input("enter the new district:")
                                        while not new_dist:
                                            print("ditrict should not be empty!")
                                            new_dist=input("enter new district")
                                        sql="UPDATE admission SET district=%s WHERE id=%s"
                                        val=(new_dist,id)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("successfully changed")
                                        break
                                else:
                                    print("ID not found!")
                            except ValueError:
                                print("Invalid id,please enter a valid id.")
                            try:
                                if id==x[0]:
                                    break
                            except:
                                pass
                    elif option==6: #edit course
                        mycursor.execute("SELECT id FROM admission")
                        adm=mycursor.fetchall()
                        while True:
                            try:
                                id=int(input("enter the ID of the student,for edit:"))
                                for x in adm:
                                    if id==x[0]:
                                        new_course=input("enter the new course:")
                                        while not new_course:
                                            print("newly added course should not be empty")
                                            new_course=input("enter new course")
                                        sql="UPDATE admission SET enrolledcourse=%s WHERE id=%s"
                                        val=(new_course,id)
                                        mycursor.execute(sql,val)
                                        mydb.commit()
                                        print("successfully changed")
                                        break
                                else:
                                    print("ID not found!")
                            except ValueError:
                                print("Invalid id,please enter a valid id.")
                            try:
                                if id==x[0]:
                                    break
                            except:
                                pass
                            break
                    else:
                        if option==7:
                            break
                    break
                        
            elif option==3: #delete admission
                print("DELETE")
                print("-------")
                mycursor.execute("SELECT id FROM admission")
                abc=mycursor.fetchall()
                while True:
                    try:
                        id1=int(input("enter the id you want to delete:"))
                        for x in abc:
                            if id1==x[0]:
                                sql="DELETE FROM admission WHERE id=%s"
                                val=(id1,)
                                mycursor.execute(sql,val)
                                mydb.commit()
                                print("successfully deleted")
                                break
                        else:
                            print("id not found!")
                    except ValueError:
                        print("Invalid id,enter a valid id.")
                    try:
                        if id1==x[0]:
                            break
                    except:
                        pass
        
                    
            elif option==4: #view admission
                print("ID   NAME    PHONE   ADDRESS     GMAIL   DISTRICT    ENROLLEDCOURSE")
                print("<----*-------*-------*----------*-------*-----------*---------------->")
                mycursor.execute("SELECT * FROM admission")
                myresult=mycursor.fetchall()
                for admission in myresult:
                    print(admission)
                
            elif option==5: #back
                pass
             

        elif option==2:
            print("1. ADD COURSE")
            print("2. EDIT COURSE")
            print("3. AVAILABLE COURSES")
            print("4. DELETE COURSE")
            print("5. BACK")
            while True:
                try:
                    option=int(input("enter your option:"))
                    if option>0 and option<=5:
                        break
                    else:
                        print("Invalid option!!")
                except:
                    print("Invalid input,enter an integer.")
            while option<=5:
                if option==1: #add course
                    print("ENTER")
                    print("-----")
                    name=input("enter new course:")
                    while not name:
                        print("course name should not empty!!")
                        name=input("enter course name:")
                    while True:
                        try:
                            fees=int(input("enter fees:"))
                            break
                        except:
                            print("invalid try again")
                    duration=input("enter duration of the course:")
                    while not duration:
                        print("duration of the course should not empty!")
                        duration=input("enter duration of the course")
                    sql="INSERT INTO courses(name,fees,duration) VALUES(%s,%s,%s)"
                    val=(name,fees,duration)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("added successfully")
                    break
                elif option==2: #edit course
                    mycursor.execute("SELECT * FROM courses")
                    myresult=mycursor.fetchall()
                    print(tabulate(myresult,headers=['id','name','fees','duration'],tablefmt='psql'))
                    print("EDIT COURSE")
                    print("-------------")
                    print("1. EDIT COURSE NAME")
                    print("2. EDIT COURSE FEES")
                    print("3. EDIT COURSE DURATION")
                    while True:
                        try:
                            option=int(input("enter your option:"))
                            if option>0 and option<=3:
                                break
                            else:
                                print("Invalid option!")
                        except:
                            print("Invalid input,enter an integer.")
                    while option<=3:
                        if option==1: #edit course name
                            mycursor.execute("SELECT id FROM courses")
                            cse=mycursor.fetchall()
                            while True:
                                try:
                                    id2=int(input("enter the course id"))
                                    for x in cse:
                                        if id2==x[0]:
                                            c_name=input("enter edited name:")
                                            while not c_name:
                                                print("name of edited course should not empty")
                                                c_name=input("enter edited name.")
                                            sql="UPDATE courses SET name=%s WHERE id=%s"
                                            val=(c_name,id2)
                                            mycursor.execute(sql,val)
                                            mydb.commit()
                                            print("edit successfully")
                                            break
                                    else:
                                        print("ID not found!")
                                except ValueError:
                                    print("Invalid ID,please enter a valid id.")
                                try:
                                    if id2==x[0]:
                                        break
                                except:
                                    pass
                            break
                        elif option==2: #edit course fees
                            mycursor.execute("SELECT id FROM courses")
                            cse=mycursor.fetchall()
                            while True:
                                try:
                                    id2=int(input("enter the course id"))
                                    for x in cse:
                                        if id2==x[0]:
                                            c_fees=int(input("enter edited fees:"))
                                            sql="UPDATE courses SET fees=%s WHERE id=%s"
                                            val=(c_fees,id2)
                                            mycursor.execute(sql,val)
                                            mydb.commit()
                                            print("edit successfully")
                                            break
                                    else:
                                        print("ID not found!")
                                except ValueError:
                                    print("Invalid ID,please enter a valid id.")
                                try:
                                    if id2==x[0]:
                                        break
                                except:
                                    pass
                            break
                        elif option==3: #edit course duration
                            mycursor.execute("SELECT id FROM courses")
                            cse=mycursor.fetchall()
                            while True:
                                try:
                                    id2=int(input("enter the course id"))
                                    for x in cse:
                                        if id2==x[0]:
                                            c_duration=input("enter edited duration:")
                                            while not c_duration:
                                                print("duration should not empty,enter a valid course duration!")
                                                c_duration=input("enter edited duration")
                                            sql="UPDATE courses SET duration=%s WHERE id=%s"
                                            val=(c_duration,id2)
                                            mycursor.execute(sql,val)
                                            mydb.commit()
                                            print("edit successfully")
                                            break
                                    else:
                                        print("ID not found!")
                                except ValueError:
                                    print("Invalid ID,please enter a valid id.")
                                try:
                                    if id2==x[0]:
                                        break
                                except:
                                    pass
                            break
                        break
                        
                elif option==3:
                    mycursor.execute("SELECT * FROM courses")
                    myresult=mycursor.fetchall()
                    print(tabulate(myresult,headers=['id','name','fees','duration'],tablefmt='psql'))
                    break
                elif option==4:
                    print("DELETE")
                    print("-------")
                    mycursor.execute("SELECT id FROM courses")
                    cse=mycursor.fetchall()
                    while True:
                        try:
                            id3=int(input("enter the id of course you want to delete:"))
                            for x in cse:
                                if id3==x[0]:
                                    sql="DELETE FROM courses WHERE id=%s"
                                    val=(id3,)
                                    mycursor.execute(sql,val)
                                    mydb.commit()
                                    print("delete successfully")
                                    break
                            else:
                                print("ID not found!!")
                           
                        except ValueError:
                            print("Invalid!!!")
                        try:
                            if id3==x[0]:
                                break
                        except:
                            pass
                        
                    
                
                            
                elif option==5: #back
                    print("back")
                    break
                break
        elif option==3: #exit
            print("exit")
            break
except:
    pass



                        
                        
            







            








                


