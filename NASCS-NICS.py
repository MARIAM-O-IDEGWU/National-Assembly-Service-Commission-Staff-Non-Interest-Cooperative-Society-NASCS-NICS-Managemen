# Import the required libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import Toplevel, Button, Tk, Menu
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import pymysql
import db_config
import os
import tempfile
import win32api
from tkcalendar import Calendar, DateEntry
from time import gmtime, strftime
from tkinter.filedialog import askopenfilename
from datetime import datetime
from collections import OrderedDict
from tkinter import Tk, Button, Text
from reportlab.pdfgen.canvas import Canvas
import win32print
from PIL import Image, ImageWin
import tkinter.ttk as ttk
import csv

class Bank:

    def __init__(self, master):

        self.master = master()
        self.master.title('BANK HALL')
        self.ws = 600
        self.hs = 500
        # self.ws = self.master.winfo_screenwidth()
        # self.hs = self.master.winfo_screenheight()
        # self.ws = self.master.winfo_screenwidth()
        # self.hs = self.master.winfo_screenheight()
        self.master.wm_minsize(self.ws, self.hs)
        self.master.configure(background='#74C365')
        self.udname = StringVar()
        self.udpass = StringVar()
        self.udacc = StringVar()
        self.udbal = StringVar()
        self.fnum = StringVar()
        # self.actype = StringVar()
        self.menu_forget = False

    def run(self):
        self.main_frame()

    def write(self):
        f1 = open("Accnt_Record.txt", 'r')
        self.user = int(f1.readline())
        # password += 1
        f1.close()

        f1 = open("Accnt_Record.txt", 'w')
        f1.write(str(self.user))
        f1.close()

        fdet = open(str(self.user) + ".txt", "w")
        fdet.write(self.user + "\n")
        # fdet.write(balance+ "\n")
        # fdet.write(str(password) + "\n")
        # fdet.write(name + "\n")
        fdet.close()

        frec = open(str(self.user) + "-rec.txt", 'w')
        frec.write("Date                             Credit      Debit     Balance\n")
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + + "              " + + "\n")
        frec.close()
        frec.write(str(self.user))
        # frec.write(str(password) + "\n")
        # frec.write(str(balance) + "\n")

    def menu(self):

        self.menu = tk.Frame(self.master, bg='#006600')

        self.m_l1 = Label(self.menu, text='Welcome {}'.format(self.user), bg='#006600',
                          font=('Times', '20', 'bold'),
                          fg="#ffffff")
        self.m_l1.grid(row=0, column=0, padx=60, pady=10)

        self.m_b1 = tk.Button(self.menu, text='DEBIT', bg='#006600', width=10, font=('Times', '20', 'bold'),
                              command=self.debframe, fg="white")
        self.m_b1.grid(row=1, column=0, padx=60, pady=10)

        self.m_b2 = tk.Button(self.menu, text='CREDIT', width=10, bg='#006600', font=('Times', '20', 'bold'),
                              command=self.credit_Balance, fg="white")
        self.m_b2.grid(row=2, column=0, padx=76, pady=20)

        self.m_b25 = tk.Button(self.menu, text='HISTORY', width=10, bg='#006600', font=('Times', '20',),
                               command=self.disp_tr_hist, fg="white")
        self.m_b25.grid(row=3, column=0, padx=76, pady=25)

        self.m_b3 = tk.Button(self.menu, text='Profile', bd=0, bg='#006600', font=('Times', '20', 'bold'),
                              command=self.show_profile, fg="#aadcba")
        self.m_b3.grid(row=0, column=1, padx=76, pady=25)

        self.m_b4 = tk.Button(self.menu, text='LOGOUT', width=10, bg='#006600', font=('Times', '18', 'bold'),
                              command=self.show_f, fg="#ff0000")

        self.m_b4.grid(row=3, column=1, padx=76, pady=15)
        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)

    def credit_Balance(self):

        self.menu.grid_forget()


        self.credframe = tk.Frame(self.master, bg="green")


        self.up_amnt_lbl1 = Label(self.credframe, text='Welcome {} to Credit Services'.format(self.user),
                                  bg="green",
                                  font=('Times', '20', 'bold'), fg="#ffffff")
        self.up_amnt_lbl1.grid(row=0, column=0, columnspan=2, pady=10)

        self.up_amnt_lbl2 = Label(self.credframe, text='Enter amount to credit', bg="green",
                                  font=('Times', '26', 'bold'), fg="#ffffff")
        self.up_amnt_lbl2.grid(row=1, column=0, columnspan=2, pady=10)

        self.up_amnt_lbl = Label(self.credframe, text='Amount', bg="green", font=('Times', '20', 'bold'),
                                 fg="#ffffff")
        self.up_amnt_lbl.grid(row=2, column=0, pady=10)
        self.up_amnt = Entry(self.credframe, bg='white', width=20, font=('Times', '20', 'bold'), fg='black')
        self.up_amnt.grid(row=2, column=1, pady=10, padx=30)

        self.fnamenum = Label(self.credframe, text='File-No', bg="green", font=('Times', '20', 'bold'),fg="#ffffff")
        self.fnamenum.grid(row=3, column=0, pady=10)

        self.fnum = Entry(self.credframe,  bg='white', width=20, font=('Times', '20', 'bold'), fg='black')
        self.fnum.grid(row=3, column=1, pady=10, padx=30)

        self.atype = Label(self.credframe, text='Account-Type', bg="green", font=('Times', '20', 'bold'),fg="#ffffff")
        self.atype.grid(row=4, column=0, pady=10)

        self.crdlap= tk.StringVar(self.credframe)
        self.crdlap.set( "SELECT")
        self.atypeopmenu = OptionMenu(self.credframe, self.crdlap, "Credit-SAVINGS", "Credit-TargetEMG", "Credit-Investment",
                                      "Credit-RetirementSAV")
        self.atypeopmenu.grid(row=4, column=1, pady=10, padx=30)
        self.atypeopmenu.configure(width=40)

        self.up_amnt_btn = tk.Button(self.credframe, text='update balance', bg="green", font=('Times', '20', 'bold'),
                                     width=15, command=self.credit, fg="#000000")
        self.up_amnt_btn.grid(row=5, column=1, pady=13, padx=72)

        self.up_amnt_btn1 = tk.Button(self.credframe, text='<<Back', bg="green", font=('Times', '18', 'bold'),
                                      command=self.show_m5, fg="#000000", width=10)
        self.up_amnt_btn1.grid(row=5, column=0, pady=16, padx=40)

        self.credframe.grid(padx=self.ws * .3, pady=self.hs * .2)


    def credit(self):
        global amount
        abtcrd=self.crdlap.get()
        abtfnocrd=self.fnum.get().upper()
        amnt = float(self.up_amnt.get())
        if self.up_amnt.get()and abtcrd=="Credit-SAVINGS":
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from user where name="{}"'.format(self.user))
                bal = c.fetchone()[0]
                cmd = "update user SET balance=balance+{} where name='{}'".format(amnt, self.user)
                c.execute(cmd)
                db.commit()
                c.close()
                db.close()
                scrd = 'Sucessfully {} NGN credited to your Savings account associated with {}.\nYour Updated Balance is now {}.'.format(amnt, self.user, amnt + bal)
                messagebox.showinfo("CREDIT", scrd)
                frec1 = open(str(self.user) + "-rec.txt", 'w')
                frec1.write(
                    str(strftime("%Y-%m-%d,%H:%M:%S ",gmtime())) + "," + str(amnt) + "," + str( bal + amnt) + "," + str(abtcrd) + "," + str(abtfnocrd))
                frec1.close()
        elif self.up_amnt.get()and abtcrd=="Credit-Investment":
                db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from investment where name="{}"'.format(self.user))
                balinv = c.fetchone()[0]
                sqlcmd = "update investment SET balance=balance+{} where name='{}'".format(amnt, self.user)
                c.execute(sqlcmd)
                db.commit()
                c.close()
                db.close()
                scrd1 = 'Sucessfully {} NGN credited to your Investment account associated with {}.\nYour Updated Balance is now {}.'.format(amnt, self.user, amnt + balinv)
                messagebox.showinfo("CREDIT", scrd1)
                frec1 = open(str(self.user) + "-rec.txt", 'w')
                frec1.write(
                    str(strftime("%Y-%m-%d,%H:%M:%S ",gmtime())) + "," + str(amnt) + "," + str( balinv + amnt) + "," + str(abtcrd) + "," + str(abtfnocrd))
                frec1.close()
        elif self.up_amnt.get() and abtcrd == "Credit-TargetEMG":
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from targetemg where name="{}"'.format(self.user))
                balemg = c.fetchone()[0]
                sqlemg = "update targetemg SET balance=balance+{} where name='{}'".format(amnt, self.user)
                c.execute(sqlemg)
                db.commit()
                c.close()
                db.close()
                scrd2 = 'Sucessfully {} NGN credited to your Target Emergency account associated with {}.\nYour Updated Balance is now {}.'.format(
                    amnt, self.user, amnt + balemg)
                messagebox.showinfo("CREDIT", scrd2)
                frec1 = open(str(self.user) + "-rec.txt", 'w')
                frec1.write(
                    str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(amnt) + "," + str( balemg + amnt) + "," + str(abtcrd) + "," + str(abtfnocrd))
                frec1.close()
        elif self.up_amnt.get() and abtcrd == "Credit-RetirementSAV":
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from retirementsav where name="{}"'.format(self.user))
                balrsav = c.fetchone()[0]
                sqlrsav = "update retirementsav SET balance=balance+{} where name='{}'".format(amnt, self.user)
                c.execute(sqlrsav)
                db.commit()
                c.close()
                db.close()
                scrd3 = 'Sucessfully {} NGN credited to your Retirement Savings account associated with {}.\nYour Updated Balance is now {}.'.format(
                    amnt, self.user, amnt + balrsav)
                messagebox.showinfo("CREDIT", scrd3)
                frec1 = open(str(self.user) + "-rec.txt", 'w')
                frec1.write(
                    str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(amnt) + "," + str(
                        balrsav + amnt) + "," + str(abtcrd) + "," + str(abtfnocrd))
                frec1.close()
                self.credframe.grid_forget()
                self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)


        db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

        c = db.cursor()
        with open(str(self.user) + "-rec.txt", 'r')as crd:
            all_values4 = []
            for crds in csv.reader(crd, delimiter=","):
                    value4 = (crds[0],crds[1],crds[2],crds[3],crds[4],crds[5])
                    all_values4.append(value4)
            query3 = "insert into history(DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO)values(%s,%s,%s,%s,%s,%s)"
            c.executemany(query3, all_values4)
            db.commit()
            db.close()


    def disp_tr_hist(self):
        global as_list
        global l
        db = pymysql.connect(host=db_config.DB_SERVER,
                             user=db_config.DB_USER,
                             password=db_config.DB_PASS,
                             database=db_config.DB)

        c = db.cursor()
        disp_wn = tk.Tk()
        disp_wn.geometry("900x600")
        disp_wn.title("Transaction History")
        disp_wn.configure(bg="green")
        fr1 = tk.Frame(disp_wn, bg="white")
        l_title = tk.Message(disp_wn, text="BANKING SYSTEM", relief="raised", width=2000, padx=600, pady=0,
                             fg="white",
                             bg="black", justify="center", anchor="center")
        l_title.config(font=("Courier", "50", "bold"))
        l_title.pack(side="top")
        fr1 = tk.Frame(disp_wn)
        fr1.pack(side="top")
        l1 = tk.Message(disp_wn, text="Your Transaction History:", padx=100, pady=20, width=1000, bg="white",
                        fg="black", relief="raised")
        l1.pack(side="top")
        fr2 = tk.Frame(disp_wn)
        fr2.pack(side="top")
        billhis = Label(disp_wn, text='HISTORY REPORT', font='arial 15 bold', bd=7, relief=GROOVE)
        billhis.pack(fill=X)
        element_header = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th']
        treeScrollhis = tk.Scrollbar(disp_wn)
        treeScrollhis.pack(side='right', fill='y')
        treehis = ttk.Treeview(disp_wn, columns=element_header, height=20, show="headings")
        treehis.configure(yscrollcommand=treeScrollhis.set)
        treehis.column('1st', width=100, minwidth=70, stretch=tk.NO)
        treehis.column('2nd', width=100, minwidth=70, stretch=tk.NO)
        treehis.column('3rd', width=100, minwidth=70, stretch=tk.NO)
        treehis.column('4th', width=100, minwidth=770, stretch=tk.NO)
        treehis.column('5th', width=170, minwidth=70, stretch=tk.NO)
        treehis.column('6th', width=100, minwidth=70, stretch=tk.NO)
        treehis.column('7th', width=250, minwidth=70, stretch=tk.NO)
        sqlchhis = "select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,COMMENT from historycomment union all select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,Null as COMMENT from  history"
        c.execute(sqlchhis, )
        treehis.delete(*treehis.get_children())
        fetchis = c.fetchall()
        for his in fetchis:
            treehis.insert('', 'end', values=(
                his[0], his[1], his[2], his[3], his[4], his[5], his[6]))
            treehis.heading("1st", text="DATE")
            treehis.heading("2nd", text="TIME")
            treehis.heading("3rd", text="DEBIT")
            treehis.heading("4th", text="BALANCE")
            treehis.heading("5th", text="ACCOUNTTYPE")
            treehis.heading("6th", text="FNO")
            treehis.heading("7th", text="COMMENT")
            treehis.pack(side='left', padx=0, pady=0)
            treeScrollhis.config(command=treehis.yview)
            c.close()

    def show_m5(self):
        self.credframe.grid_forget()
        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)

    def debframe(self):

        self.menu.grid_forget()
        self.debit_Balance = tk.Frame(self.master, bg="#777777")
        self.lap = StringVar()
        self.fno1 = StringVar()

        self.debit_Balance = tk.Frame(self.master, bg="green")

        self.up_amnt_lbl1 = Label(self.debit_Balance, text='Welcome {} to Debit Services'.format(self.user),
                                  font=('Times', '20', 'bold'), fg="#ffffff", bg='green')
        self.up_amnt_lbl1.grid(row=0, column=0, columnspan=2, pady=10, padx=30)

        self.up_amnt_lbl = Label(self.debit_Balance, text='Enter amount to debit ', font=('Times', '23', 'bold'),
                                 fg="#ffffff", bg='green')
        self.up_amnt_lbl.grid(row=1, column=0, columnspan=2, pady=10, padx=30)

        self.up_amnt_lbl2 = Label(self.debit_Balance, text='Amount', font=('Times', '23', 'bold'), fg="white",
                                  bg='green')
        self.up_amnt_lbl2.grid(row=2, column=0, pady=10, padx=30)

        self.up_amnt = Entry(self.debit_Balance, bg='white', width=20, font=('Times', '20'), fg='black')
        self.up_amnt.grid(row=2, column=1, pady=12, padx=55)
        self.fno = Label(self.debit_Balance, text='File-No',font=('Times', '20', 'bold'), fg="#ffffff",
                              bg='green')
        self.fno.grid(row=3, column=0,pady=10, padx=30)

        self.entryfno = Entry(self.debit_Balance,bg='white', width=20, font=('Times', '20'), fg='black')
        self.entryfno.grid(row=3, column=1, pady=10, padx=30)

        self.p_acty = Label(self.debit_Balance, text='Account-Type',font=('Times', '20', 'bold'), fg="#ffffff",
                              bg='green')
        self.p_acty.grid(row=4, column=0,pady=10, padx=30)

        self.lap= tk.StringVar(self.debit_Balance)
        self.lap.set( "SELECT")
        self.optmenu = OptionMenu(self.debit_Balance, self.lap, "Debit-SAVINGS","Debit-TargetEMG", "Debit-Investment", "Debit-RetirementSAV")
        self.optmenu.grid(row=4, column=1, pady=10, padx=30)
        self.optmenu.configure(width=40)

        self.up_amnt_btn = tk.Button(self.debit_Balance, text='update balance', bg="green", font=('Times', '20', 'bold'),
                                     command=self.update_balance, fg="#000000", width=12)
        self.up_amnt_btn.grid(row=5, column=1, pady=16)

        self.up_amnt_btn1 = tk.Button(self.debit_Balance, text='<<Back', bg="green", font=('Times', '18', 'bold'),
                                      command=self.show_m4, fg="#000000", width=10)
        self.up_amnt_btn1.grid(row=5, column=0, pady=17, padx=40)

        self.debit_Balance.grid(padx=self.ws * .3, pady=self.hs * .2)

    def show_m4(self):
        self.debit_Balance.grid_forget()
        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)

    def update_balance(self):
                global amnt
                abt=self.lap.get()
                abtfno=self.entryfno.get()
                self.up_amnt.get()
                amnt = float(self.up_amnt.get())

                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from investment where name="{}"'.format(self.user))
                bal9 = c.fetchone()
                if bal9 is None:
                    messagebox.showinfo("Empty report", "User not assigned to Investment Account")
                else:
                    if amnt<= bal9[0] and abt=="Debit-Investment":
                        cmd = "update investment SET balance=balance-{} where name='{}'".format(amnt, self.user)
                        c.execute(cmd)
                        db.commit()
                        s = '!!DEBITED SUCESSFULLY!! \n {}NGN debited from Your Investment Account\nYour Updated Balance is now {}.'.format(
                            amnt, bal9[0] - amnt,abt,abtfno)
                        print(bal9[0])
                        messagebox.showinfo("!!Sucess!!", s)
                        frec1 = open(str(self.user) + "-rec.txt", 'w')
                        frec1.write(
                            str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(amnt) + "," + str(
                                bal9[0] - amnt) + "," + str(abt) + "," + str(abtfno))
                        frec1.close()
                        with open(str(self.user) + "-rec.txt", 'r')as ret:
                            all_values3 = []
                            for rtar in csv.reader(ret, delimiter=","):
                                value3 = (rtar[0], rtar[1], rtar[2], rtar[3], rtar[4], rtar[5])
                                all_values3.append(value3)
                            query3 = "insert into history(DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO)values(%s,%s,%s,%s,%s,%s)"
                            c.executemany(query3, all_values3)
                            db.commit()
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from user where name="{}"'.format(self.user))
                bal1 = c.fetchone()
                if bal1 is None:
                    messagebox.showinfo("Empty report", "User not assigned to SAVINGS Account")
                else:
                    if amnt <= bal1[0] and abt == "Debit-SAVINGS":
                        cmd1 = "update user SET balance=balance-{} where name='{}'".format(amnt, self.user)
                        c.execute(cmd1)
                        db.commit()
                        s1 = '!!DEBITED SUCESSFULLY!! \n {}NGN debited from Your SAVINGS Account\nYour Updated Balance is now {}.'.format(
                                    amnt, bal1[0] - amnt, abt, abtfno)
                        messagebox.showinfo("!!Sucess!!", s1)
                        print(bal1[0])
                        frec1 = open(str(self.user) + "-rec.txt", 'w')
                        frec1.write(
                                    str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(amnt) + "," + str(
                                        bal1[0] - amnt) + "," + str(abt) + "," + str(abtfno))
                        frec1.close()
                        with open(str(self.user) + "-rec.txt", 'r')as ret:
                            all_values3 = []
                            for rtar in csv.reader(ret, delimiter=","):
                                value3 = (rtar[0], rtar[1], rtar[2], rtar[3], rtar[4], rtar[5])
                                all_values3.append(value3)
                            query3 = "insert into history(DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO)values(%s,%s,%s,%s,%s,%s)"
                            c.executemany(query3, all_values3)
                            db.commit()
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from targetemg where name="{}"'.format(self.user))
                bal2 = c.fetchone()
                if bal2 is None:
                    messagebox.showinfo("Empty report", "User not assigned to TargetEMG Account ")
                else:
                    if amnt <= bal2[0] and abt == "Debit-TargetEMG":
                        cmd2 = "update targetemg SET balance=balance-{} where name='{}'".format(amnt, self.user)
                        c.execute(cmd2)
                        db.commit()
                        s2 = '!!DEBITED SUCESSFULLY!! \n {}NGN debited from Your TargetEMG Account\nYour Updated Balance is now {}.'.format(
                            amnt, bal2[0] - amnt, abt, abtfno)
                        messagebox.showinfo("!!Sucess!!", s2)
                        print(bal2[0])
                        frec1 = open(str(self.user) + "-rec.txt", 'w')
                        frec1.write(
                            str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(amnt) + "," + str(
                                bal2[0] - amnt) + "," + str(abt) + "," + str(abtfno))
                        frec1.close()
                        with open(str(self.user) + "-rec.txt", 'r')as ret:
                            all_values3 = []
                            for rtar in csv.reader(ret, delimiter=","):
                                value3 = (rtar[0], rtar[1], rtar[2], rtar[3], rtar[4], rtar[5])
                                all_values3.append(value3)
                            query3 = "insert into history(DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO)values(%s,%s,%s,%s,%s,%s)"
                            c.executemany(query3, all_values3)
                            db.commit()
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select balance from retirementsav where name="{}"'.format(self.user))
                bal3 = c.fetchone()
                if bal3 is None:
                    messagebox.showinfo("Empty report", "User not assigned to Retirement-Savings Account")
                else:
                    if amnt <= bal3[0] and abt == "Debit-RetirementSAV":
                        cmd3 = "update retirementsav SET balance=balance-{} where name='{}'".format(amnt, self.user)
                        c.execute(cmd3)
                        db.commit()
                        s3 = '!!DEBITED SUCESSFULLY!! \n {}NGN debited from Your Retirement Account\nYour Updated Balance is now {}.'.format(
                            amnt, bal3[0] - amnt,abt,abtfno)
                        messagebox.showinfo("!!Sucess!!", s3)
                        frec1 = open(str(self.user) + "-rec.txt", 'w')
                        frec1.write(
                            str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(amnt) + "," + str(
                                bal3[0] - amnt) + "," + str(abt) + "," + str(abtfno))
                        frec1.close()
                        with open(str(self.user) + "-rec.txt", 'r')as ret:
                            all_values3 = []
                            for rtar in csv.reader(ret, delimiter=","):
                                value3 = (rtar[0], rtar[1], rtar[2], rtar[3], rtar[4], rtar[5])
                                all_values3.append(value3)
                            query3 = "insert into history(DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO)values(%s,%s,%s,%s,%s,%s)"
                            c.executemany(query3, all_values3)
                            db.commit()
                        self.debit_Balance.grid_forget()
                        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)


    def show_f(self):
        self.menu.grid_forget()
        self.menu_forget = True
        self.f.grid(padx=self.ws * .3, pady=self.hs * .2)

    def show_m(self):
        self.profframe.grid_forget()
        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)

    def show_profile(self):

        self.menu.grid_forget()
        self.profframe = tk.Frame(self.master, bg="gray")
        try:
            db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB)

            c = db.cursor()
            c.execute('select * from user where name="{}"'.format(self.user))
            data = c.fetchone()

            self.udname.set(data[1])
            self.udpass.set(data[2])
            self.udacc.set(data[0])
            self.udbal.set(data[3])
            # self.actype.set(data[4])



        except Exception as e:
            messagebox.showerror("DataBASE Connectivity", "!!Error!!Database Connection!!{}".format(e))
            exit(0)

        self.p_l1 = Label(self.profframe, text='Account No:{}'.format(self.udacc.get()), bg="gray",
                          font=('Times', '18', 'bold'), fg="#ffffff")
        self.p_l1.grid(row=0, column=0, columnspan=2, padx=64)

        self.p_l2 = Label(self.profframe, text='User Name:{}'.format(self.udname.get()), bg="gray",
                          font=('Times', '18', 'bold'), fg="#ffffff")
        self.p_l2.grid(row=1, column=0, columnspan=2, padx=64)

        self.p_l3 = Label(self.profframe, text='Balance:{}'.format(self.udbal.get()), bg="gray",
                          font=('Times', '18', 'bold'), fg="#ffffff")
        self.p_l3.grid(row=2, column=0, columnspan=2, padx=64)

        # self.p_acty = Label(self.profframe, text='ACOUNTTYPE:{}'.format(self.actype.get()), bg="gray",
        # font=('Times', '18', 'bold'), fg="#ffffff")
        # self.p_acty.pack()
        # self.p_acty.grid(row=3, column=0, columnspan=2, padx=64)

        self.p_b1 = tk.Button(self.profframe, text='Change Name', bg="#777777", font=('Times', '20', 'bold'),
                              width=13,
                              command=self.updatename, fg="#003b8b")
        self.p_b1.grid(row=4, column=0, padx=64, pady=19)

        self.p_b2 = tk.Button(self.profframe, text='Change Password', bg="#777777", font=('Times', '20', 'bold'),
                              width=13, command=self.change_password, fg="#003b8b")
        self.p_b2.grid(row=5, column=0, padx=64, pady=10)

        self.p_b3 = tk.Button(self.profframe, text='<<Back', width=10, bg="#777777", font=('Times', '18', 'bold'),
                              command=self.show_m, fg="#000000")
        self.p_b3.grid(row=6, column=1, padx=64, pady=18)

        self.profframe.grid(padx=self.ws * .3, pady=self.hs * .2)

    def update_password(self):
        old = self.Old_Password.get()
        new = self.New_Password.get()
        self.Old_Password.set('')
        self.New_Password.set('')
        if old and new:
            try:
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select * from user where name="{}"'.format(self.user))
                data = c.fetchone()
                if old != data[2]:
                    messagebox.showerror("!!Invalid Error!!", "!!Error!!\nOld Password does not\nPlease Try Again")
                elif old == new:
                    messagebox.showerror("!!Invalid Error!!",
                                         "!!Error!!\nPassword is Same as Old Password\nPlease Choose Different Password")
                elif old == data[2]:
                    c.execute('update user set password="{}" where name="{}"'.format(new, self.user))
                    db.commit()
                    c.close()
                    db.close()
                    messagebox.showinfo("!!Sucess!!", "Your Password is sucessfully updated")
                    self.show_m3()

                else:
                    messagebox.showerror("!!Invalid Error!!", "!!Error!!\nSomething Went Wrong\nTry Again")



            except Exception as e:
                messagebox.showerror("!!DataBase Error!!", "Error!!{}".format(e))

        else:
            messagebox.showerror("Input Error", "Error!!Please Fill Passwords Properly")

    def change_password(self):
        self.profframe.grid_forget()
        self.passupdate = tk.Frame(self.master, bg="gray")
        self.up_opass_lbl1 = Label(self.passupdate, text='Welcome to Password Update Service', bg="gray",
                                   font=('Times', '20', 'bold'), fg="#abcdef")
        self.up_opass_lbl1.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.up_opass_lbl = Label(self.passupdate, text='Old password:', bg="gray", font=('Times', '25', 'bold'),
                                  fg="#FFFFFF")
        self.up_opass_lbl.grid(row=1, column=0, padx=21, pady=22)

        self.Old_Password = StringVar()
        self.New_Password = StringVar()
        self.old_password = Entry(self.passupdate, textvariable=self.Old_Password, bg='#123456', show="*", width=20,
                                  font=('Times', '20', 'bold'), fg='#FFFFFF')
        self.old_password.grid(row=1, column=1, padx=31, pady=22)

        self.up_npass_lbl = Label(self.passupdate, text='New password:', bg="gray", font=('Times', '25', 'bold'),
                                  fg="#FFFFFF")
        self.up_npass_lbl.grid(row=2, column=0, padx=30, pady=20)

        self.new_password = Entry(self.passupdate, bg='#123456', textvariable=self.New_Password, width=20, show="*",
                                  font=('Times', '20', 'bold'), fg='#FFFFFF')
        self.new_password.grid(row=2, column=1, padx=30, pady=21)

        self.pass_b1 = tk.Button(self.passupdate, text="Update", width=10, bg="gray", font=('Times', '20', 'bold'),
                                 command=self.update_password, fg="#000000")
        self.pass_b1.grid(row=3, column=1, columnspan=2, padx=30, pady=22)

        self.pass_b2 = tk.Button(self.passupdate, text="<<Back", bg="gray", font=('Times', '18', 'bold'),
                                 command=self.show_m3, fg="#000000")
        self.pass_b2.grid(row=3, column=0, pady=15, padx=30)

        self.passupdate.grid(padx=self.ws * .3, pady=self.hs * .2)

    def show_m3(self):

        self.passupdate.grid_forget()
        self.profframe.grid(padx=self.ws * .3, pady=self.hs * .2)

    def change_name(self):
        try:
            if self.up_name.get():
                name = self.up_name.get().lower().strip()
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                if name != self.user:
                    c.execute("select name from user")
                    users = [user[0] for user in c.fetchall()]
                    if name in users:
                        messagebox.showinfo("!!USER Exists!!",
                                            "This name is already taken by another user so please choose a unique one")
                    else:

                        c.execute('update user set name="{}" where name="{}"'.format(name, self.user))
                        db.commit()
                        c.close()
                        db.close()
                        messagebox.showinfo("!!Sucess!!", "Updated User Name Sucessfully")
                        self.nameupdate.grid_forget()
                        self.user = name
                        self.udname.set(name)
                        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)
                else:
                    messagebox.showerror("NameError", "This is your old username choose new one")

            else:
                messagebox.showerror("NameError", "Error!!Please Enter new username")
        except Exception as e:
            messagebox.showerror("Error!!", e)

    def updatename(self):

        self.profframe.grid_forget()

        self.nameupdate = tk.Frame(self.master, bg="gray")

        self.up_name_lbl1 = Label(self.nameupdate, text="Welcome to Update Name Facility", bg="gray",
                                  font=('Times', '20', 'bold'), fg="#ffffff")
        self.up_name_lbl1.grid(row=0, column=0, columnspan=2, pady=18)

        self.up_name_lbl2 = Label(self.nameupdate, text="Your Current Name is : {}".format(self.user), bg="gray",
                                  font=('Times', '20', 'bold'), fg="#ffffff")
        self.up_name_lbl2.grid(row=1, column=0, columnspan=2, pady=20)

        self.up_name_lbl = Label(self.nameupdate, text='New UserName:', bg="gray", font=('Times', '20', 'bold'),
                                 fg="#ffffff")
        self.up_name_lbl.grid(row=2, column=0, padx=30)

        self.up_name = Entry(self.nameupdate, bg='#123456', width=20, font=('Times', '20', 'bold'), fg='#FFFFFF')
        self.up_name.grid(row=2, column=1, padx=40)

        self.name_b1 = tk.Button(self.nameupdate, text="Update", bg="gray", width=14, font=('Times', '20', 'bold'),
                                 command=self.change_name, fg="#000000")
        self.name_b1.grid(row=3, column=1, padx=67, pady=10, columnspan=2)
        self.name_b2 = tk.Button(self.nameupdate, text="<<Back", bg="gray", font=('Times', '20', 'bold'),
                                 command=self.show_m1, fg="#000000")
        self.name_b2.grid(row=4, column=0, pady=15, padx=10)

        self.nameupdate.grid(padx=self.ws * .3, pady=self.hs * .2)

    def show_m1(self):
        self.nameupdate.grid_forget()
        self.profframe.grid(padx=self.ws * .3, pady=self.hs * .2)

    def main_frame(self):

        self.f = Frame(self.master, bg='#006600')
        Bank.username = StringVar()
        Bank.password = StringVar()

        self.l0 = Label(self.f, text="WELCOME TO (NASCS-NICS) BANKING HALL", bg='#006600', font=('Times', '16', 'bold'),
                        fg='white')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.l1 = Label(self.f, text='UserName : ', bg='#006600', font=('Times', '20', 'bold'), fg='white')
        self.l1.grid(row=1, column=0, ipadx=40, pady=30)

        self.e1 = Entry(self.f, textvariable=Bank.username, bg='white', width=20, font=('Times', '20', 'bold'),
                        fg='black')
        self.e1.grid(row=1, column=1)

        self.l2 = Label(self.f, text='Password : ', bg='#006600', font=('Times', '20', 'bold'), fg='white')
        self.l2.grid(row=2, column=0)

        self.e2 = Entry(self.f, textvariable=Bank.password, show='*', bg='white', width=20,
                        font=('Times', '20', 'bold'), fg='black')
        self.e2.grid(row=2, column=1, padx=20)

        self.b3 = Button(self.f, bg='#006600', text='forget password ?', font=('Times', '12', 'bold'),
                         command=self.fpass, fg='red', width=30, bd=0)
        self.b3.grid(row=3, column=1)

        self.b1 = Button(self.f, bg='#006600', text='LOGIN',width=17, font=('Times', '20', 'bold'), command=self.login,
                         fg='white')
        self.b1.grid(row=4, column=1, columnspan=4, padx=19, pady=31)

        #self.b2 = Button(self.f, bg='#006600', text='SIGNUP', font=('Times', '20', 'bold'), command=self.signup,
                         #fg='white')
        #self.b2.grid(row=4, column=1, columnspan=4)
        self.f.grid(padx=self.ws * .3, pady=self.hs * .2)

    def fpass(self):
        messagebox.showinfo("PRIVACY",
                            "Due to your privacy reason you have to meet in person to nearest branch with all documents to update your password.")

    def show_sf(self):
        self.sp.grid_forget()
        self.menu_forget = True
        self.f.grid(padx=self.ws * .3, pady=self.hs * .2)

    def signup(self):

        self.bal = StringVar()
        self.uname = StringVar()
        self.creds = StringVar()

        self.f.grid_forget()
        self.sp = Frame(self.master, bg='#006600')

        self.sl1 = Label(self.sp, text='UserName : ', bg='#006600', font=('Times', '30', 'bold'), fg='white')
        self.sl1.grid(row=0, column=0, ipadx=40, pady=28)

        self.se1 = Entry(self.sp, textvariable=self.uname, bg='white', width=20, font=('Times', '20', 'bold'),
                         fg='black')
        self.se1.grid(row=0, column=1)

        self.sl2 = Label(self.sp, text='Password : ', bg='#006600', font=('Times', '30', 'bold'), fg='white')
        self.sl2.grid(row=1, column=0)

        self.se2 = Entry(self.sp, textvariable=self.creds, show='*', bg='white', width=20,
                         font=('Times', '20', 'bold'), fg='black')
        self.se2.grid(row=1, column=1, padx=20)

        self.sl3 = Label(self.sp, text='Balance : ', bg='#006600', font=('Times', '30', 'bold'), fg='white')
        self.sl3.grid(row=2, column=0, ipadx=42, pady=27)

        self.se3 = Entry(self.sp, textvariable=self.bal, bg='white', width=20, font=('Times', '20', 'bold'),
                         fg='black')
        self.se3.grid(row=2, column=1)

        self.sb2 = Button(self.sp, bg='#006600', text='SIGNUP', font=('Times', '20', 'bold'), command=self.mksignup,
                          fg='white')
        self.sb2.grid(row=3, column=1, columnspan=4)

        self.sb3 = tk.Button(self.sp, text='<<Back', width=10, bg="#006600", font=('Times', '18', 'bold'),
                             command=self.show_sf, fg="#000000")
        self.sb3.grid(row=3, column=0, padx=66, pady=17)
        self.sp.grid(padx=self.ws * .3, pady=self.hs * .2)

    def mksignup(self):

        uname = self.uname.get().lower().strip()
        password = self.creds.get()
        balance = self.bal.get()
        if uname and password and balance:
            try:
                balance = float(balance)
                db = pymysql.connect(host=db_config.DB_SERVER,
                                     user=db_config.DB_USER,
                                     password=db_config.DB_PASS,
                                     database=db_config.DB)

                c = db.cursor()
                c.execute('select * from user where name="{}"'.format(uname))
                d = c.fetchone()
                if d:
                    messagebox.showerror("UserExist",
                                         "User with this name is already exists.\n Please Login if you are already a user \nelse choose another name")
                else:
                    cmd = "insert into user(name,password,balance) values('{}','{}',{})".format(uname, password,
                                                                                                balance)
                    c.execute(cmd)
                    db.commit()
                    c.close()
                    db.close()
                    messagebox.showinfo("Account Created",
                                        "Congratulations!! Your Account is Successfully Created\nPlease LOGIN to Enjoy your services")
                    frec1 = open(str(uname) + "-rec.txt", 'a+')
                    frec1.write(str(uname) + "\n")
                    frec1.write(str(password) + "\n")
                    frec1.write(str(balance) + "\n")
                    frec1.close()
                    self.sp.grid_forget()
                self.f.grid(padx=self.ws * .3, pady=self.hs * .2)
            except ValueError as e:
                messagebox.showerror("ERROR", "Please Enter a Valid Amount to Deposit Initial")


            except Exception as e:
                messagebox.showerror("ERROR", "SOMETHING WENT WRONG\nError!!{}".format(e))

        else:
            messagebox.showerror("INPUT", "Please fill-in all the Details")

    def login(self, event=None):

        UserName = self.e1.get().lower().strip()
        Password = self.e2.get()

        try:

            db = pymysql.connect(host=db_config.DB_SERVER,
                                 user=db_config.DB_USER,
                                 password=db_config.DB_PASS,
                                 database=db_config.DB)

            c = db.cursor()
            #cmdur ="select * from userall where name = '{}'".format(UserName)
            cmdur = "select * from nasportal where FILENO = '{}'".format(UserName)
            c.execute(cmdur)
            data = c.fetchone()
            self.password.set('')
            if data:
                if Password == data[0]:
                    self.f.grid_forget()
                    self.user = UserName
                    if self.menu_forget:
                        self.menu.grid(padx=self.ws * .3, pady=self.hs * .2)

                    else:
                        self.menu()

                else:

                    messagebox.showerror("Error", "!!Invalid Password")

            else:

                messagebox.showerror("Error", "!!No such user exists")
                self.username.set('')

        except Exception as e:

            messagebox.showerror("Error", "!!Check Data BAse Connectivity {}".format(e))


login_screen = Tk()
login_screen.title("(NASCS-NICS)")
login_screen.resizable(0, 0)
login_screen.geometry("500x250")
login_screen.config(bg="#03C04A")

USERNAME=StringVar()
PASSWORD=StringVar()

def close():
    login_screen.destroy()

def Login(event=None):
    if username.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=login_screen)
    else:
        try:
            con = pymysql.connect(host=db_config.DB_SERVER,
                                  user=db_config.DB_USER,
                                  password=db_config.DB_PASS,
                                  database=db_config.DB)
            cur = con.cursor()

            cur.execute("select * from Login where username=%s and password = %s",
                        (username.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=login_screen)

            else:
                messagebox.showinfo("Success", "WELCOME TO (NASCS-NICS) CONTRIBUTION SCHEME",parent=login_screen)
                close()
                con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=login_screen)


lbl_username = Label(login_screen,bg="#03C04A", text="Username:", font=('bold', 12), bd=15)
lbl_username.place(x=85,y=78)
lbl_password = Label(login_screen,bg="#03C04A", text="Password:", font=('bold', 12), bd=15)
lbl_password.place(x=85,y=115)


username = Entry(login_screen,textvariable=USERNAME,width=20, font=(14))
username.place(x=180,y=93)
password = Entry(login_screen,width=20,textvariable=PASSWORD, show="*", font=(14))
password.place(x=180,y=130)

btn_login = Button(login_screen,bg="#03C04A", text="Login",fg="#222831",command=Login,font=('bold', 10), width=20)
btn_login.place(x=180,y=170)
imglng = ImageTk.PhotoImage(Image.open("lng.png"))
panellng =Label(login_screen, image=imglng, font=('Verdana', 20))
panellng.place(x=0, y=0)

login_screen.mainloop()


con = pymysql.connect(host=db_config.DB_SERVER,
                      user=db_config.DB_USER,
                      password=db_config.DB_PASS,
                      database=db_config.DB)



win = tk.Tk()
win.maxsize(width=1250, height=700)
win.minsize(width=1250, height=700)
win.config(bg="green")
win.title('OjayITSolutions')
win.resizable(0, 0)
img = ImageTk.PhotoImage(Image.open("logo.png"))
panel =Label(win, image=img, font=('Verdana', 20))
panel.place(x=0, y=0)

search_text_var =StringVar()
fno=StringVar()
namecontri=StringVar()
dropma = StringVar()
dropma.set(0)
dropmf = StringVar()
dropmf.set(0)
home=StringVar()
mbno=StringVar()
email=StringVar()
dept=StringVar()
nextkin=StringVar()
rel=StringVar()
nxtno=StringVar()
nxtadd=StringVar()
dropmb = StringVar()
dropmb.set(0)
dropmc = StringVar()
dropmc.set(0)
dropmd = StringVar()
dropmd.set(0)
dropme = StringVar()
dropme.set(0)
dropvar = StringVar()
dropvar.set(0)
drpcmdt= StringVar()
drpcmdt.set(0)
creds = StringVar()
pyprd1 = StringVar()
nameacctp1 = StringVar()
entSTDT1 = StringVar()
entEDDT1 = StringVar()
cshvar=StringVar()
flevar=StringVar()
flevarcmt=StringVar()
cshvarcmt=StringVar()
txtcmt1=tk.StringVar()

#pix=StringVar()

#DATE AND TIME
StartUpDateTime    = datetime.now()
DefaultYear        = StartUpDateTime.year
DefaultMonthNumber = StartUpDateTime.month
DefaultDayOfMonth  = StartUpDateTime.day



YearAndMonthLengths =  [ 365, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
EnglishMonthNames = ( 'Entire Year', 'January', 'February', 'March',
                      'April', 'May', 'June', 'July', 'August', 'September',
                      'October', 'November', 'December' )
FrenchMonthNames  = ( 'annÃ©e entiÃ¨re', 'janvier', 'fÃ©vrier', 'mars',
                      'avril', 'mai', 'juin', 'juillet', 'aoÃ»t', 'septembre',
                      'octobre', 'novembre', 'dÃ©cembre' )


Month_Names = FrenchMonthNames
Month_Names = EnglishMonthNames



DaysInMonth = OrderedDict()
for i in range( 0, len( Month_Names ) ) :
    DaysInMonth[ Month_Names[ i ] ] = YearAndMonthLengths[ i ]

DefaultMonthName   = Month_Names[ DefaultMonthNumber ]
DefaultMonthLength = DaysInMonth[ DefaultMonthName ]
SelectedYear        = tk.IntVar(    value = DefaultYear )
SelectedMonthName   = tk.StringVar( value = DefaultMonthName )
SelectedMonthLength = tk.IntVar(    value = DefaultMonthLength )
SelectedDay         = tk.IntVar(    value = DefaultDayOfMonth )

def GetChosenMonthLength( *args ) :

    global SelectedMonthLength
    SelectedMonthLength.set( DaysInMonth[ SelectedMonthName.get()  ] )
    return

#-------------------------------------------------------------------------------

YearSpinBox  = tk.Spinbox( win,
                        from_ = 1800, to = 2050,
                        textvariable = SelectedYear,
                        wrap = True, state = 'readonly', width = 6,font=("century", 11) )
MonthSpinBox  = tk.Spinbox( win,
                         values = tuple( DaysInMonth.keys() )[1:],
                         textvariable = SelectedMonthName,
                         wrap = True, state = 'readonly', width = 9,font=("century", 11) )
DaySpinBox  = tk.Spinbox( win,
                       from_ = 1,
                       to = SelectedMonthLength.get(),
                       textvariable = SelectedDay,
                       wrap = True, state = 'readonly', width = 3,font=("century", 11)
                     )

def Logout():
    win.destroy()


#IMAGES DEFINATION
def image_path(file_path):
    global image
    open_image = Image.open(file_path)
    image = ImageTk.PhotoImage(open_image)
    return image

def load_photo_tab_one(file_path):
    image = image_path(file_path)
    imgLabelTabOne.configure(image=image)
    imgLabelTabOne.image = image

def database_error(err):
    messagebox.showinfo("Error", err)
    return False

def select_image():
    global image_selected
    global image_file_name
    global file_new_home
    global file_to_copy

    path_to_image = filedialog.askopenfilename(initialdir="/",
                                           title="Open File",
                                           filetypes=(("PNGs", "*.png"), ("GIFs", "*.gif"), ("All Files", "*.*")))

    if path_to_image:
        image_file_name = os.path.basename(path_to_image)
        file_new_home = db_config.PHOTO_DIRECTORY + image_file_name
        file_to_copy = path_to_image
        image_selected = True
        load_photo_tab_one(file_to_copy)

    try:
     if path_to_image:
        image_file_name = os.path.basename(path_to_image)
        file_new_home = db_config.PHOTO_DIRECTORY + image_file_name
        file_to_copy = path_to_image
        image_selected = True
        load_photo_tab_one(file_to_copy)
    except IOError as err:
     image_selected = False
     messagebox.showinfo("File Error",err)
buttonAddImage = tk.Button(win, text="Add Image",command=select_image,bg='green',fg='white')
buttonAddImage.place(x=1117,y=300)


def insert_into_database():
    global a, bcon, c1, c2, c3, d, e, f, g, h, i, j, k, l, m, n, o, p, q, photo_field

    try:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)

        a=fno.get().upper()
        bcon=namecontri.get().lower()
        c1 = SelectedYear.get()
        c2 = SelectedMonthName.get()
        c3 = SelectedDay.get()
        d=dropma.get().lower()
        e=dropmf.get().lower()
        f=home.get("1.0", "end-1c").lower()
        g=mbno.get().lower()
        h=email.get().lower()
        i=dept.get().lower()
        j=nextkin.get().lower()
        k=rel.get().lower()
        l=nxtno.get().lower()
        m=nxtadd.get("1.0", "end-1c").lower()
        n=dropmb.get().lower()
        o=dropmc.get().lower()
        p=dropmd.get().lower()
        q=dropme.get().lower()
        photo_field=image_file_name

        sql = "INSERT INTO nasportal (FILENO,NAME,Year,Month,Day,SEX,MARITAL,HOMEADD,MOBILE,EMAIL,DEPT,NXTKIN,RELATIONSHIP,NXTKINMOBILE,NXTKINADD,INVESTMENT,SAVINGS,TARGETEMG,RETIRESAVINS,PIX ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vals = (a, bcon, c1,c2,c3, d, e, f, g, h, i, j, k, l, m, n, o,p,q,photo_field)
        cursor = con.cursor()
        cursor.execute(sql, vals)
        con.commit()
        cursor.close()
        con.close()
        messagebox.showinfo("Database", "Record Added to Database")
    except pymysql.ProgrammingError as e:
      database_error(e)
    except pymysql.DataError as e:
      database_error(e)
    except pymysql.IntegrityError as e:
      database_error(e)
    except pymysql.NotSupportedError as e:
      database_error(e)
    except pymysql.OperationalError as e:
      database_error(e)
    except pymysql.InternalError as e:
      database_error(e)

imgar = PhotoImage(file="addr.png")
imgr = imgar.subsample(5, 5)
buttonCommit = tk.Button(win, text="Add Record", image=imgar, command=insert_into_database, anchor="w", bg='white',fg='green')
buttonCommit.place(x=200, y=660)
def update():
    global  row
    global result

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)
    cursor = con.cursor()
    var1 = fno.get()
    var2 = namecontri.get()  # updated school
    var3 = SelectedYear.get()  # updated grade
    var4 = SelectedMonthName.get()  # updated checkoutdate
    var5 = SelectedDay.get()  # updated bookcode
    var6 = dropma.get()  # updated ebookname
    var7 = dropmf.get()
    var8=home.get("1.0", "end-1c")
    var9 = mbno.get()
    var10= email.get()
    var11 = dept.get()
    var12=nextkin.get()
    var13=rel.get()
    var14=nxtno.get()
    var15=nxtadd.get("1.0", "end-1c")
    var16=dropmb.get()
    var17=dropmc.get()
    var18=dropmd.get()
    var19 =dropme.get()

    query = "UPDATE nasportal SET FILENO=%s,NAME=%s,Year=%s,Month=%s,Day=%s,SEX=%s,MARITAL=%s,HOMEADD=%s,MOBILE=%s,EMAIL=%s,DEPT=%s,NXTKIN=%s,RELATIONSHIP=%s,NXTKINMOBILE=%s,NXTKINADD=%s,INVESTMENT=%s,SAVINGS=%s,TARGETEMG=%s,RETIRESAVINS=%s WHERE FILENO=%s "
    cursor.execute(query,(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,search_family.get(),))
    tk.messagebox.showinfo("Updated", "Successfully Updated.")
    con.commit()
imgup = PhotoImage(file="update1.png")
imgu = imgup.subsample(5, 5)
updbut=tk.Button(win, text='UPDATE', image=imgup,command=update,anchor="w", bg='white',fg='green')
updbut.place(x=302, y=660)

def delete_records():
    a = fno.get().upper()
    bcon = namecontri.get().lower()
    c1 = SelectedYear.get()
    c2 = SelectedMonthName.get()
    c3 = SelectedDay.get()
    d = dropma.get().lower()
    e = dropmf.get().lower()
    f = home.get("1.0", "end-1c").lower()
    g = mbno.get().lower()
    h = email.get().lower()
    i = dept.get().lower()
    j = nextkin.get().lower()
    k = rel.get().lower()
    l = nxtno.get().lower()
    m = nxtadd.get("1.0", "end-1c").lower()
    n = dropmb.get().lower()
    o = dropmc.get().lower()
    p = dropmd.get().lower()
    q = dropme.get().lower()

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    if (search_family.get()):
        tk.messagebox.showinfo("Deleted", "Successfully Deleted.")
    else:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)

        cursor = con.cursor()
    sql2 = "INSERT INTO achievemember (FILENO,NAME,Year,Month,Day,SEX,MARITAL,HOMEADD,MOBILE,EMAIL,DEPT,NXTKIN,RELATIONSHIP,NXTKINMOBILE,NXTKINADD,INVESTMENT,SAVINGS,TARGETEMG,RETIRESAVINS ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vals2 = (a, bcon, c1, c2, c3, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
    cursor = con.cursor()
    cursor.execute(sql2, vals2)
    cursor.execute("Delete from nasportal WHERE FILENO='" + search_family.get() + "'")
    entry15.delete(0,'end')
    entry_1an.delete(0,'end')
    dropma.set(0)
    dropmf.set(0)
    home.delete("1.0", "end")
    entry_5.delete(0,'end')
    entrynas1.delete(0,'end')
    entrynas2.delete(0,'end')
    entrydia.delete(0,'end')
    entrydiarel.delete(0,'end')
    entrydiakinmb.delete(0,'end')
    nxtadd.delete("1.0", "end")
    dropmb.set(0)
    dropmc.set(0)
    dropmd.set(0)
    dropme.set(0)
    load_photo_tab_one(db_config.PHOTO_DIRECTORY + "default.png")
    con.commit()
imgdel = PhotoImage(file="delete1.png")
imgdg = imgdel.subsample(5, 5)
delbut=tk.Button(win, text='DELETE',image=imgdel,command=delete_records,anchor="w", bg='white',fg='green').place(x=402, y=660)

def Clear_records():
    entry15.delete(0, END)
    entry_1an.delete(0, END)
    dropma.set(0)
    dropmf.set(0)
    home.delete("1.0", "end")
    entry_5.delete(0, END)
    entrynas1.delete(0, END)
    entrynas2.delete(0, END)
    entrydia.delete(0, END)
    entrydiarel.delete(0, END)
    entrydiakinmb.delete(0, END)
    nxtadd.delete("1.0", "end")
    dropmb.set(0)
    dropmc.set(0)
    dropmd.set(0)
    dropme.set(0)
    load_photo_tab_one(db_config.PHOTO_DIRECTORY + "default.png")

imgcel = PhotoImage(file="clear.png")
imgcss = imgcel.subsample(5, 5)
clrbut=tk.Button(win, text='CLEAR', image=imgcel,command= Clear_records,anchor="w", bg='white',fg='green').place(x=502, y=660)


def VIEWRECORDS():
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    cursor = con.cursor()
    win2 = tk.Toplevel(relief=GROOVE, bd=10,bg='light green')
    #message = "MEMBERS REPORT"
    tk.Label(win2, text='MEMBERS REPORT').pack(padx=0, pady=0)
    element_header = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th',
                      '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th'
                     ]
    treeScroll = tk.Scrollbar(win2)
    treeScroll.pack(side='bottom', padx=0, pady=0)

    def mambersaveme():
        def Close():
            F3M.destroy()

        global userM, win, rown
        F3M = Frame(relief=GROOVE, bd=10, bg='green')
        F3M.place(x=700, y=180, width=600, height=300)
        bill_M = Label(F3M, text='MEMBERS REPORT PRINTING IN PROGRESS', font='arial 15 bold', bg='white', bd=7,
                       relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F3M, orient=VERTICAL)
        textareaM = tk.Text(F3M, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=textareaM.yview)
        textareaM.pack()
        textareaM.tag_add("whole", "2.0", "end-1c")
        textareaM.tag_configure("whole", spacing3=10)
        userM = textareaM.get(1.0, "end-1c")
        textareaM.delete(1.0, END)

        with open("NASMem.csv", "w", newline='') as memfile:
            memwriter = csv.writer(memfile,delimiter='|')
            headerM = ['(NASCS-NICS) MEMBERSHIP REPORT']
            line = ['--------------------------------------------------------']
            dataM = [
                'FILENO NAME YEAR MONTH DAY SEX MARITAL HOMEADD MOBILE EMAIL DEPT NXTKIN RELATIONSHIP NXTKINMOBILE NXTKINADD INVESTMENT SAVINGS TARGETEMG RETIRESAVINS']
            memwriter.writerow(headerM)
            memwriter.writerow(line)
            memwriter.writerow(dataM)
            memwriter.writerow(line)

            for row_id in treeM.get_children():
                row = treeM.item(row_id)['values']
                if row_id[0].isdigit():
                    memwriter.writerow(row_id)
                memwriter.writerow(line)
                print('save row:', row)
                memwriter.writerow(row)

        with open("NASMem.csv", "r") as f:
            datap = f.read()
        textareaM.insert("1.0", datap)
        q = textareaM.get("1.0", "end-1c")
        filename = tempfile.mktemp(".txt")
        open(filename, "w").write(q)
        win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
        close_button = Button(F3M, bg="green", fg="white", width=9, text="CLOSE", command=Close)
        close_button.place(x=2, y=4)

    treeM =ttk.Treeview(win2, columns=element_header, show="headings", yscrollcommand=treeScroll)
    treeM.column('1st', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('2nd', width=75, minwidth=50, stretch=tk.NO)
    treeM.column('3rd', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('4th', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('5th', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('6th', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('7th', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('8th', width=60, minwidth=50, stretch=tk.NO)
    treeM.column('9th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('10th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('11th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('12th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('13th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('14th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('15th', width=55, minwidth=20, stretch=tk.NO)
    treeM.column('16th', width=55, minwidth=50, stretch=tk.NO)
    treeM.column('17th', width=55, minwidth=50, stretch=tk.NO)
    treeM.column('18th', width=55, minwidth=50, stretch=tk.NO)
    treeM.column('19th', width=55, minwidth=50, stretch=tk.NO)

    btn23 = tk.Button(win2, text=" PRINT REPORT", anchor="w", bg='green', fg='white', command=mambersaveme).place(x=3,
                                                                                                                  y=270)
    sqlch = "SELECT * FROM nasportal"
    cursor.execute(sqlch, )
    treeM.delete(*treeM.get_children())
    fetch = cursor.fetchall()
    for data in fetch:
        treeM.insert('', 'end', values=(
            data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
            data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19]))
    treeM.heading("1st", text="FILENO")
    treeM.heading("2nd", text="NAME")
    treeM.heading("3rd", text="YEAR")
    treeM.heading("4th", text="MONTH")
    treeM.heading("5th", text="DAY")
    treeM.heading("6th", text="SEX")
    treeM.heading("7th", text="MARITAL")
    treeM.heading("8th", text="HOMEADD")
    treeM.heading("9th", text="MOBILE")
    treeM.heading("10th", text="EMAIL")
    treeM.heading("11th", text="DEPT")
    treeM.heading("12th", text="NXTKIN")
    treeM.heading("13th", text="RELATIONSHIP")
    treeM.heading("14th", text="NXTKINMOBILE")
    treeM.heading("15th", text="NXTKINADD ")
    treeM.heading("16th", text="INVESTMENT")
    treeM.heading("17th", text="SAVINGS")
    treeM.heading("18th", text="TARGETEMG")
    treeM.heading("19th", text="RETIRESAVINS")
    treeM.pack(side='left', padx=0, pady=0)
    treeScroll.config(command=treeM.yview)

imgvew = PhotoImage(file="view.png")
imgvew1 = imgvew.subsample(5, 5)

vwbut=tk.Button(win, text='VIEW-RECORDS',image=imgvew,command=VIEWRECORDS,anchor="w", bg='white',fg='green').place(x=1044, y=660)


user_in = str()

printer_name = win32print.GetDefaultPrinter ()
file_name = "but.png"


def printdoc():
    def Close():
        F3.destroy()
    def printsam():
        q = textarea.get("1.0", "end-1c")
        #m=textarea.image_create(tk.END,image=image)
        filename = tempfile.mktemp(".txt")
        open(filename, "w").write(q)
        win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)

    global user_in, win
    F3 = Frame(relief=GROOVE, bd=10)
    F3.place(x=700, y=180, width=500, height=500)
    bill_title = Label(F3, text='Contribution ', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
    scrol_y = Scrollbar(F3, orient=VERTICAL)
    textarea =tk.Text(F3, yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    submit_button = Button(F3,bg="grey",fg="black", width=20,text="PRINT INDIVIDUAL REPORT", command=printsam)
    submit_button.pack()
    close_button = Button(F3,bg="grey",fg="black", width=15,text="CLOSE", command=Close)
    close_button.pack()
    user_in= textarea.get(1.0, "end-1c")
    textarea.delete(1.0,END)
    textarea.insert(END,"\t  WELCOME TO (NASCS-NICS) CONTRIBUTION SCHEME")
    #textarea.image_create(tk.END,image=image)
    textarea.insert(END,f"\n\nFile No:-----\t\t{fno.get()}")
    textarea.insert(END,f"\nName:----------\t\t{namecontri.get()}")
    textarea.insert(END,f"\nYear:----------\t\t{SelectedYear.get()}")
    textarea.insert(END, f"\nMonth:--------\t\t{SelectedMonthName.get()}")
    textarea.insert(END, f"\nYear:---------\t\t{SelectedDay.get()}")
    textarea.insert(END,f"\nSex:-----------\t\t{dropma.get()}")
    textarea.insert(END, f"\nMarital Status:\t\t{dropmf.get()}")
    #textarea.insert(END, f"\nHome Address:\t\t{home.get()}")
    textarea.insert(END,f"\nNumber:--------\t\t{mbno .get()}")
    textarea.insert(END, f"\nEmail:---------\t\t{email.get()}")
    textarea.insert(END, f"\nDepartment:----\t\t{dept.get()}")
    textarea.insert(END,f"\nNext Of Kin:--\t\t{nextkin.get()}")
    textarea.insert(END, f"\nRelationship:--\t\t{rel.get()}")
    textarea.insert(END, f"\nNext Of Kin No:\t\t{nxtno.get()}")
    #textarea.insert(END,f"\nNext Of Kin Address:\t\t nxtadd .get("1.0", "end-1c")")
    textarea.insert(END, f"\nInvestment Account:\t{dropmb.get()}")
    textarea.insert(END, f"\nSavings Account:\t{dropmc.get()}")
    textarea.insert(END,f"\nTarget Emergency:\t{dropmd.get()}")
    textarea.insert(END, f"\nRetirement Account:\t{dropme.get()}")
    textarea.insert(END,f"\n\n======================================")
    textarea.insert(END,f"\n======================================\n")
    textarea.configure(font='arial 8 bold')

imgprnt = PhotoImage(file="print.png")
imgprnt1 =imgprnt.subsample(5, 5)
prntbut=tk.Button(win,text='PRINT',image=imgprnt,command=printdoc,anchor="w", bg='white',fg='green').place(x=1145, y=660)


def search_records():
    global  row
    global result

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    vals = search_text_var.get()
    sql = "SELECT * FROM nasportal WHERE FILENO=%s"
    cursor = con.cursor()
    Lenmem=(vals,)
    result=cursor.execute(sql, Lenmem)
    result = cursor.fetchall()
    if  result:

        for row in result:
            fno.set(result[0][0])
            namecontri.set(result[0][1])
            SelectedYear.set(result[0][2])
            SelectedMonthName.set(result[0][3])
            SelectedDay.set(result[0][4])
            dropma.set(result[0][5])
            dropmf.set(result[0][6])
            msg = ""
            msg = msg + (result[0][7])
            home.insert("end", msg)
            mbno.set(result[0][8])
            email.set(result[0][9])
            dept.set(result[0][10])
            nextkin.set(result[0][11])
            rel.set(result[0][12])
            nxtno.set(result[0][13])
            dmg = ""
            dmg = dmg + (result[0][14])
            nxtadd.insert("end", dmg)
            dropmb.set(result[0][15])
            dropmc.set(result[0][16])
            dropmd.set(result[0][17])
            dropme.set(result[0][18])
            ph_path = db_config.PHOTO_DIRECTORY + result[0][19]
            load_photo_tab_one(ph_path)
            #photo = row[4]  # image saved in the 5th column of database
            cursor.close()
        con.close()
imgsrc = PhotoImage(file="search1.png")
imgsrc1 = imgsrc.subsample(5, 5)
srcbut=tk.Button(win, text='SEARCH', image=imgsrc,command=search_records,anchor="w", bg='white',fg='green').place(x=842, y=666)

file_name = "default.png"
path = db_config.PHOTO_DIRECTORY + file_name
rows = None
num_of_rows = None
row_counter = 0
image_selected = False
image_file_name = None
file_to_copy = None
file_new_home = None
blank_textboxes_tab_two = True


openImageTabOne = Image.open(path)
imgTabOne = ImageTk.PhotoImage(openImageTabOne)
imgLabelTabOne = tk.Label(win, image=imgTabOne)
imgLabelTabOne.place(x=1100,y=200)


def inicmd():
    vapo = flevar.get().upper()
    vali = flevar.get().upper()
    vabo = cshvar.get()
    pabo = dropvar.get()
    if pabo == "Credit-SAVINGS":
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        c = con.cursor()
        cmdsav = "insert into user(name,password,balance) VALUES (%s,%s,%s)"
        cmdsvar = (vapo, vali, vabo)
        c.execute(cmdsav, (cmdsvar))
        con.commit()
        c.close()
        con.close()
        messagebox.showinfo("INITIAL DEPOSIT", "Savings Credited")
    elif pabo == "Credit-Investment":
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        c = con.cursor()
        cmdsav1 = "insert into investment(name,password,balance) VALUES (%s,%s,%s)"
        cmdsvar1 = (vapo, vali, vabo)
        c.execute(cmdsav1, (cmdsvar1))
        con.commit()
        c.close()
        con.close()
        messagebox.showinfo("INITIAL DEPOSIT", "Investment Credited")
    elif pabo == "Credit-TargetEMG":
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        c = con.cursor()
        cmdsav2 = "insert into targetemg(name,password,balance) VALUES (%s,%s,%s)"
        cmdsvar2 = (vapo, vali, vabo)
        c.execute(cmdsav2, (cmdsvar2))
        con.commit()
        c.close()
        con.close()
        messagebox.showinfo("INITIAL DEPOSIT", "Target/Emergency Credited")
    elif pabo == "Credit-RetirementSAV":
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        c = con.cursor()
        cmdsav3 = "insert into retirementsav(name,password,balance) VALUES (%s,%s,%s)"
        cmdsvar3 = (vapo, vali, vabo)
        c.execute(cmdsav3, (cmdsvar3))
        con.commit()
        c.close()
        con.close()
        messagebox.showinfo("INITIAL DEPOSIT", "Retirement Savings Credited")

def inicmtn():
    global fen
    vapocmt = flevarcmt.get().upper()
    valicmt = flevarcmt.get().upper()
    vabocmt = float(cshvarcmt.get())
    cmttxt=txtcmt1.get()
    pabocmt = drpcmdt.get()

    if pabocmt == "Credit-SAVINGS" and flevarcmt.get():
        con = pymysql.connect(host=db_config.DB_SERVER,
                                  user=db_config.DB_USER,
                                  password=db_config.DB_PASS,
                                  database=db_config.DB)
        c = con.cursor()
        seqld='select balance from user where name=%s'
        seld = (vapocmt)
        rchap = c.execute(seqld, seld)
        rchap = c.fetchone()
        if rchap:
                print('BALANCE FROM DB IS',rchap)
                cmdsavcmt = "update user set balance=balance + %s where name=%s"
                cmdsvarcmt = (vabocmt,vapocmt)
                c.execute(cmdsavcmt, (cmdsvarcmt))
                con.commit()
                messagebox.showinfo("COMMENTED TRANSACTION", "Savings Credited")
                print(vabocmt)
                print(cmttxt)
                frcmt = open("fen.txt", 'w')
                frcmt.write(
                str(strftime("%Y-%m-%d,%H:%M:%S ", gmtime())) + "," + str(vabocmt) + "," + str(rchap[0]+ vabocmt) + "," + str(pabocmt) + "," + str(vapocmt) + "," + str(cmttxt))
                frcmt.close()
                with open("fen.txt", 'r')as etr:
                    all_values5 = []
                    for rtar in csv.reader(etr, delimiter=","):
                        value5 = (rtar[0], rtar[1], rtar[2], rtar[3], rtar[4], rtar[5], rtar[6])
                        all_values5.append(value5)
                    query5 = "insert into historycomment(DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,COMMENT)values(%s,%s,%s,%s,%s,%s,%s)"
                    c.executemany(query5, all_values5)
                    con.commit()

def inidepcash():
    fminid =tk.Toplevel(relief=GROOVE,width=550, height=300, bd=10, bg='green')
    inilab1=tk.Label(fminid,text='MEMBER INITIAL DEPOSIT',width=25, font=("century", 11)).place(x=0,y=0)
    inidg = tk.Label(fminid, text='ACCOUNT TYPE-------------------FILE-NO-------------------AMOUNT',bg='green',fg='black', width=50, font=("century", 8)).place(x=3, y=31)
    incm = tk.Label(fminid, text='ACCOUNT TYPE-------------------FILE-NO-------------------AMOUNT',bg='green',fg='black', width=50,font=("century", 8)).place(x=3, y=125)
    cmtlab1 = tk.Label(fminid, text='COMMENTED TRANSACTIONS',width=27, font=("century", 11)).place(x=0, y=100)
    dropvar.set("SELECT")
    dropini = tk.OptionMenu(fminid, dropvar, "Credit-SAVINGS", "Credit-TargetEMG", "Credit-Investment", "Credit-RetirementSAV")
    dropini.place(x=3, y=50)
    dropini.config(width=20, height=0)
    numnid = tk.Entry(fminid, textvar=flevar, font=('bold', 15), width=9)
    numnid.place(x=170, y=50)
    entinid = tk.Entry(fminid, textvar=cshvar, font=('bold', 15), width=7,)
    entinid.place(x=275, y=50)
    drpcmdt.set("SELECT")
    cmdini = tk.OptionMenu(fminid, drpcmdt, "Credit-SAVINGS", "Credit-TargetEMG", "Credit-Investment","Credit-RetirementSAV")
    cmdini.place(x=3, y=147)
    cmdini.config(width=20, height=0)
    cdmnid = tk.Entry(fminid, textvar=flevarcmt, font=('bold', 15), width=9)
    cdmnid.place(x=170, y=147)
    entcnd = tk.Entry(fminid, textvar=cshvarcmt, font=('bold', 15), width=7,)
    entcnd.place(x=275, y=147)
    cmtxt=tk.Label(fminid,text='COMMENT',bg='green',fg='black',font=("century", 8)).place(x=3, y=180)
    txtb=tk.Entry(fminid, textvar=txtcmt1,font=('bold', 15), width=7,)
    txtb.place(x=3, y=197)
    #text = ScrolledText(fminid, width=20, height=3)
    #text.insert(END,)
    tk.Button(fminid, text="SUBMIT INITIAL DEPOSIT", anchor="w", bg='green', fg='white', command=inicmd).place(x=365, y=50)
    tk.Button(fminid, text="SUBMIT TRANSACTION", anchor="w", bg='green', fg='white', command=inicmtn).place(
        x=365, y=147)

label_0 =tk.Label(win, text="MEMBERSHIP APPLICATION  FORM", width=30, font=("century", 17), bg="green", fg="black")
label_0.place(x=478, y=190)
labelperdt=tk.Label(win, text="PERSONAL DETAILS", anchor="w",width=25, font=("century", 13),bg="green", fg="black")
labelperdt.place(x=200, y=267)
filenum =tk.Label(win, text="SEARCH FILE NO:",font=("century", 9))
filenum.place(x=650, y=675)
search_family =tk.Entry(win,textvariable=search_text_var,font=('bold', 13),width=8)
search_family.place(x=765, y=675)
label_15=tk.Label(win, text="FILE NUMBER", anchor="w",width=20, font=("century", 11))
label_15.place(x=200, y=300)
entry15=tk.Entry(win, textvar=fno,font=('bold', 12), width=20)
entry15.place(x=390, y=300)
label_1 =tk.Label(win, text="NAME:", width=20,anchor="w",font=("century", 11))
label_1. place(x=200, y=330)
entry_1an =tk.Entry(win, textvar=namecontri,font=('bold', 12), width=20)
entry_1an.place(x=390, y=330)
label_2 =tk.Label(win, text="DATE OF BIRTH:", anchor="w",width=20, font=("century", 11))
label_2.place(x=200, y=360)
MonthSpinBox.place(x=390, y=360)
DaySpinBox.place(x=475, y=360)
YearSpinBox.place(x=515, y=360)
SelectedMonthName.trace( 'w', GetChosenMonthLength )
label_10 =tk.Label(win, text="SEX:", anchor="w",width=20, font=("century", 11))
label_10.place(x=200, y=390)
dropma.set("SELECT") # default value
droplistproga1=tk.OptionMenu(win, dropma, "MALE","FEMALE")
droplistproga1.place(x=390, y=390)
droplistproga1.config(width=24)
label_11=tk.Label(win, text="MARITAL STATUS:", anchor="w",width=20, font=("century", 11))
label_11.place(x=200, y=420)
dropmf.set("SELECT") # default value
droplistproga=tk.OptionMenu(win, dropmf, "SINGLE", "MARRIED", "DEVIOUS")
droplistproga.place(x=390, y=420)
droplistproga.config(width=24)
label_4 =tk.Label(win, text="HOME ADDRESS", anchor="w",width=20,font=("century", 11))
label_4.place(x=200, y=450)
home =tk.Text(win, width=23, height=3)
home.place(x=390, y=453)
label_5 =tk.Label(win, text="MOBILE NUMBER:", anchor="w",width=20,font=("century", 11))
label_5.place(x=200, y=509)
entry_5 =tk.Entry(win, textvar=mbno, font=('bold', 12), width=20)
entry_5.place(x=390, y=509)
label_nas =tk.Label(win, text="EMAIL:", anchor="w",width=20,font=("century", 11))
label_nas.place(x=200, y=537)
entrynas1 =tk.Entry(win, textvar=email, font=('bold', 12), width=20)
entrynas1.place(x=390, y=537)
label_nas =tk.Label(win, text="DEPARTMENT:", anchor="w",width=20,font=("century", 11))
label_nas.place(x=200, y=566)
entrynas2 =tk.Entry(win, textvar=dept, font=('bold', 12), width=20)
entrynas2.place(x=390, y=566)
label_nas2 =tk.Label(win, text="NEXT OF KIN:", anchor="w",width=20,font=("century", 11))
label_nas2.place(x=200, y=596)
entrydia =tk.Entry(win,textvar=nextkin, font=('bold', 12), width=20)
entrydia.place(x=390, y=596)


#SECOND PHASE
label_nas21 =tk.Label(win, text="RELATIONSHIP:", anchor="w",width=20,font=("century", 11))
label_nas21.place(x=700, y=300)
entrydiarel =tk.Entry(win,textvar=rel, font=('bold', 12), width=20)
entrydiarel.place(x=890, y=300)
label_nas23 =tk.Label(win, text="NEXT OF KIN MOBILE:", anchor="w",width=20,font=("century", 11))
label_nas23.place(x=700, y=330)
entrydiakinmb =tk.Entry(win,textvar=nxtno, font=('bold', 12), width=20)
entrydiakinmb.place(x=890, y=330)
label_nas24 =tk.Label(win, text="NEXT OF KIN ADDRESS:", anchor="w",width=20,font=("century", 11))
label_nas24.place(x=700, y=360)
nxtadd =tk.Text(win, width=23, height=4)
nxtadd.place(x=890, y=360)
label_acctype =tk.Label(win, text="TYPE OF ACCOUNT:", anchor="w",width=18,font=("century", 11,'underline','bold'))
label_acctype.place(x=700, y=430)
label_nas2 =tk.Label(win, text="(I) Investment:", anchor="w",width=20,font=("century", 11))
label_nas2.place(x=700, y=460)
label_nas3 =tk.Label(win, text="(II)Savings:", anchor="w",width=20,font=("century", 11))
label_nas3.place(x=700, y=490)
label_nas4 =tk.Label(win, text="(III)Target/Emergency:", anchor="w",width=20,font=("century", 11))
label_nas4.place(x=700, y=520)
label_nas5 =tk.Label(win, text="(IV)Retirement Savings:", anchor="w",width=20,font=("century", 11))
label_nas5.place(x=700, y=550)
labinidepo =tk.Label(win, text="INITIAL DEPOSIT AND COMMENTED TRANSACTIONS:", anchor="w",width=44,font=("century", 10,'underline','bold'))
labinidepo.place(x=700, y=580)
#iniacc =tk.Label(win, text="Account:",anchor="w",width=20,font=("century", 11))
#iniacc.place(x=700, y=610)
dropmb.set("SELECT") # default value
droplistprogb=tk.OptionMenu(win, dropmb,"Nill", "Investment")
droplistprogb.place(x=890, y=460)
droplistprogb.config(width=25)
dropmc.set("SELECT") # default value
droplistprogc=tk.OptionMenu(win, dropmc,"Nill","Savings")
droplistprogc.place(x=890, y=490)
droplistprogc.config(width=25)
dropmd.set("SELECT") # default value
droplistprogd=tk.OptionMenu(win, dropmd,"Nill","Target/Emergency")
droplistprogd.place(x=890, y=520)
droplistprogd.config(width=25)
dropme.set("SELECT") # default value
droplistproge=tk.OptionMenu(win, dropme,"Nill","Retirement Savings")
droplistproge.place(x=890, y=550)
droplistproge.config(width=25)
fmenibut=tk.Button(win, text="INITIAL DEPOSIT AND COMMENTED TRANSACTIONS", anchor="w", bg='green', fg='white', command=inidepcash).place(x=700, y=610)
# Create two frames in the window

greet =tk.Frame(win,bg="green")
root =tk.Frame(win,bg="green")
loan =tk.Frame(win,bg="green")
contrfrq =tk.Frame(win,bg="green")
supplycon =tk.Frame(win,bg="green")
achievfrm =tk.Frame(win,bg="green")
labelframe =tk.LabelFrame(win)
seperator =tk.Frame(win,height=800, width=10, bg='white')
seperator.place(x=178, y=190)

img1 = ImageTk.PhotoImage(Image.open("logo.png"))
panel =tk.Label(root, image=img1, font=(
    'Verdana', 20))
panel.place(x=0, y=0)

img2 = ImageTk.PhotoImage(Image.open("logo.png"))
panel =tk.Label(loan, image=img2, font=(
    'Verdana', 20))
panel.place(x=0, y=0)

img33 = ImageTk.PhotoImage(Image.open("logo.png"))
panel =tk.Label(contrfrq, image=img33, font=(
    'Verdana', 20))
panel.place(x=0, y=0)

img4 = ImageTk.PhotoImage(Image.open("logo.png"))
panel =tk.Label(supplycon, image=img4, font=(
    'Verdana', 20))
panel.place(x=0, y=0)

img5 = ImageTk.PhotoImage(Image.open("logo.png"))
panel =tk.Label(achievfrm, image=img5, font=(
    'Verdana', 20))
panel.place(x=0, y=0)
# Define a function for switching the frames


def membershipform():
   greet.pack_forget()
   root.pack_forget()
   loan.pack_forget()
   contrfrq.pack_forget()
   supplycon.pack_forget()
   achievfrm.pack_forget()



def contribution():
    root = Bank(Tk)
    root.run()
   # order.pack(fill='both', expand=1)
    greet.pack_forget()
    loan.pack_forget()
    contrfrq.pack_forget()
    supplycon.pack_forget()
    #updbut.pack_forget()
    achievfrm.pack_forget()

def loanaccess():
   loan.pack(fill='both', expand=1)
   greet.pack_forget()
   supplycon.pack_forget()
   root.pack_forget()
   contrfrq.pack_forget()
   achievfrm.pack_forget()

def contrifreq():
    contrfrq.pack(fill='both', expand=1)
    greet.pack_forget()
    supplycon.pack_forget()
    root.pack_forget()
    loan.pack_forget()
    achievfrm.pack_forget()

def supplyconlink():
   supplycon.pack(fill='both', expand=1)
   loan.pack_forget()
   greet.pack_forget()
   root.pack_forget()
   contrfrq.pack_forget()
   achievfrm.pack_forget()

def achvstaff():
   achievfrm.pack(fill='both', expand=1)
   loan.pack_forget()
   greet.pack_forget()
   supplycon.pack_forget()
   root.pack_forget()
   contrfrq.pack_forget()


labnas1 = tk.Label(root, text="MONTHLY CONTRIBUTION", width=30, font=("century", 17), bg="green", fg="black")
labnas1.place(x=478, y=190)

con = pymysql.connect(host=db_config.DB_SERVER,
                      user=db_config.DB_USER,
                      password=db_config.DB_PASS,
                      database=db_config.DB)

cursor = con.cursor()
acclab =tk.Label(loan , text="LOAN REQUEST PAGE.", width=30, font=("century", 17), bg="green", fg="black")
acclab.place(x=478, y=190)
filenum =tk.Label(loan, text="CLICK BUTTON BELOW TO ACCESS LOAN:",anchor="w",width=38,font=("century", 11,'underline','bold'))
filenum.place(x=200, y=270)

label_4 =tk.Label(loan, text="CLICK  BUTTON BELOW TO REFUND LOAN:",anchor="w",width=38,font=("century", 11,'underline','bold'))
label_4.place(x=700, y=270)

#DEFINITING TREEVIEW
fmloan=tk.Frame(loan,bg="green",relief=GROOVE, bd=10,width=25,height=100)
fmloan.place(x=200, y=370)

bill_title = Label(fmloan, text='LOAN REPORT', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
element_header = ['1st', '2nd', '3rd', '4th', '5th', '6th']
treeScroll = tk.Scrollbar(fmloan)
treeScroll.pack(side='right', fill='y')


def memberLOAN():
    def Close():
        F3ML.destroy()
    global userL
    F3ML = Frame(relief=GROOVE, bd=10,bg='green')
    F3ML.place(x=700, y=180, width=600, height=300)
    bill_ML = Label(F3ML, text='MEMBERS LOAN REPORT SENT FOR PRINTING', font='arial 15 bold',bg='white', bd=7, relief=GROOVE).pack(fill=X)
    scrol_y = Scrollbar(F3ML, orient=VERTICAL)
    textareaML = tk.Text(F3ML, yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textareaML.yview)
    textareaML.pack()
    textareaML.tag_add("whole", "2.0", "end-1c")
    textareaML.tag_configure("whole", spacing3=10)
    userL = textareaML.get(1.0, "end-1c")
    textareaML.delete(1.0, END)

    with open("NASLoan.csv", "w", newline='') as memfile:
        csvwriter = csv.writer(memfile,delimiter='|')
        header = ['(NASCS-NICS) MEMBERSHIP LOAN PRINTING IN PROGRESS']
        line = ['--------------------------------------------------------']
        data = ['FILENO ACCOUNT-TYPE LOANAMOUNT MONTHLY-REFUND DATE']
        csvwriter.writerow(header)
        csvwriter.writerow(line)
        csvwriter.writerow(data)
        csvwriter.writerow(line)

        for row_id in treeML.get_children():
            row = treeML.item(row_id)['values']
            if row_id[0].isdigit():
                csvwriter.writerow(row_id)
            csvwriter.writerow(line)
            print('save row:', row)
            csvwriter.writerow(row)


    with open("NASLoan.csv", "r") as f:
     data = f.read()
    textareaML.insert("1.0", data)
    q = textareaML.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(q)
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
    close_button = Button(F3ML, bg="green", fg="white", width=9, text="CLOSE", command=Close)
    close_button.place(x=2, y=4)

btn23= tk.Button(fmloan, text=" PRINT LOAN REPORT", anchor="w", bg='green', fg='white', command=memberLOAN).place(x=97, y=3)


treeML =ttk.Treeview(fmloan, columns=element_header,height=10, show="headings")
treeML.configure(yscrollcommand=treeScroll.set)
treeML.column('1st', width=150, minwidth=70, stretch=tk.NO)
treeML.column('2nd', width=150, minwidth=70, stretch=tk.NO)
treeML.column('3rd', width=150, minwidth=70, stretch=tk.NO)
treeML.column('4th', width=150, minwidth=70, stretch=tk.NO)
treeML.column('5th', width=150, minwidth=70, stretch=tk.NO)


sqlch = "SELECT * FROM request"
cursor.execute(sqlch, )
treeML.delete(*treeML.get_children())
fetch = cursor.fetchall()
for data in fetch:
        treeML.insert('', 'end', values=(
            data[0], data[1], data[2], data[3], data[4]))
        treeML.heading("1st", text="FILENO")
        treeML.heading("2nd", text="ACCOUNT-TYPE")
        treeML.heading("3rd", text="LOANAMOUNT")
        treeML.heading("4th", text="MONTHLY-REFUND")
        treeML.heading("5th", text="DATE")
        treeML.pack(side='left', padx=0, pady=0)
        treeScroll.config(command=treeML.yview)
        cursor.close()
#btn_refresh = Button(fm, text='REFRESH REPORT').place(x=645, y=510)
def query_database():
    # Clear the Treeview
    for record in treeML.get_children():
        treeML.delete(record)

    # Create a database or connect to one that exists
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    # Create a cursor instance
    c = con.cursor()

    c.execute("SELECT * FROM request")
    records = c.fetchall()
    for record in records:
        treeML.insert(parent='', index='end',  text='',
                           values=(record[0], record[1], record[2], record[3], record[4]))
btnreset= tk.Button(fmloan, text=" REFRESH VIEW", anchor="w", bg='green', fg='white', command=query_database).place(x=3, y=3)


def LoanRequest():
    global Home
    Home =tk.Toplevel()
    Home.title("Login Admin")
    width = 700
    height = 350
    Home.transient()
    Home.config(bg="green")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    searchrequest = StringVar()
    fnorq = StringVar()
    accrq = StringVar()
    loanAmountVar = StringVar()
    numberOfYearsVarmonth = StringVar()
    global daterq
    daterq = StringVar()
    lbdatrq=StringVar()


    def insert_request():

        try:
            con = pymysql.connect(host=db_config.DB_SERVER,
                                  user=db_config.DB_USER,
                                  password=db_config.DB_PASS,
                                  database=db_config.DB)

            a1 = fnorq.get().upper()
            b2 = accrq.get().lower()
            e5 = loanAmountVar.get().lower()
            g7 = numberOfYearsVarmonth.get().lower()
            j10 = daterq.get()


            sqlrq = "INSERT INTO request (FNO,ACCOUNTYPE,LOANAMOUNT,MONTHLYPAY,DATE) VALUES (%s,%s,%s,%s,%s)"
            valsrq = (a1, b2, e5, g7, j10)
            cursor = con.cursor()
            cursor.execute(sqlrq, valsrq)
            con.commit()
            cursor.close()
            con.close()
            messagebox.showinfo("Database", "Record Added to Database")
        except pymysql.ProgrammingError as e:
            database_error(e)
        except pymysql.DataError as e:
            database_error(e)
        except pymysql.IntegrityError as e:
            database_error(e)
        except pymysql.NotSupportedError as e:
            database_error(e)
        except pymysql.OperationalError as e:
            database_error(e)
        except pymysql.InternalError as e:
            database_error(e)

            # Clear The Treeview Table
            treeML.delete(*treeML.get_children())

            # Run to pull data from database on start
            query_database()
    tk.Button(Home, text='SUBMIT RECORD', command=insert_request).place(x=9, y=300)


    def updatereq():
        global rowreq
        global resultreq2

        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        cursor = con.cursor()
        var1req = fnorq.get()
        var2req = accrq.get()
        var5req = loanAmountVar.get()
        var7req = numberOfYearsVarmonth.get()
        var10req = daterq.get()

        query = "UPDATE request SET FNO=%s,ACCOUNTYPE=%s,LOANAMOUNT=%s,MONTHLYPAY=%s,DATE=%s WHERE FNO=%s "
        cursor.execute(query, (var1req, var2req, var5req,var7req,var10req,search_famnas.get(),))
        tk.messagebox.showinfo("Updated", "Successfully Updated.")
        con.commit()
    tk.Button(Home, text='UPDATE RECORD', command=updatereq).place(x=115, y=300)

    def delete_recordsreq():
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)

        if (search_famnas.get()):
            tk.messagebox.showinfo("Deleted", "Successfully Deleted.")
        else:
            con = pymysql.connect(host=db_config.DB_SERVER,
                                  user=db_config.DB_USER,
                                  password=db_config.DB_PASS,
                                  database=db_config.DB)

        cursor = con.cursor()
        cursor.execute("Delete from request WHERE FNO='" + search_famnas.get() + "'")
        con.commit()
        entry15.delete(0, 'end')
        entryTYPE.delete(0, 'end')
        entryLA.delete(0, 'end')
        entryIR.delete(0, 'end')
        daterq.delete(0, 'end')
    tk.Button(Home, text='DELETE RECORD', command=delete_recordsreq).place(x=221, y=300)

    def Clear_recordsreq():
        if (search_famnas.get()):
            tk.messagebox.showinfo("Cleared Report", "Successfully Cleared.")
            entry15.delete(0, END)
            entryTYPE.delete(0, END)
            entryLA.delete(0, END)
            entryIR.delete(0, END)
            daterq.delete(0, END)
    tk.Button(Home, text='CLEAR RECORD', command=Clear_recordsreq).place(x=327, y=300)


    def search_recordsrequest():
        global rowreq
        global  rowg
        global resultln
        global resultreq2


        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)

        valsreq2 = searchrequest.get()
        sqlreq2 = "SELECT * FROM request WHERE FNO=%s"
        drreprt="SELECT Date FROM request WHERE FNO=%s"
        cursor = con.cursor()
        Lenmemreq = (valsreq2,)
        resultln = cursor.execute(drreprt,Lenmemreq)
        resultln = cursor.fetchone()
        resultreq2 = cursor.execute(sqlreq2, Lenmemreq)
        resultreq2 = cursor.fetchall()
        if resultreq2:

            for rowreq in resultreq2:
                fnorq.set(resultreq2[0][0])
                accrq.set(resultreq2[0][1])
                loanAmountVar.set(resultreq2[0][2])
                numberOfYearsVarmonth.set(resultreq2[0][3])

        if resultln:
            for rowg in resultln:
                lbdatrq.set(resultln)
                print(rowg)


    def loanreport():
        def Close():
            F4.destroy()
        def printsam():
            q = textarea.get("1.0", "end-1c")
            filename = tempfile.mktemp(".txt")
            open(filename, "w").write(q)
            win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
            # filename = tempfile.mktemp(".txt")
            # open(filename, "w").write(q)
            # os.startfile(filename, "print")

        global user_in, win
        F4 = Frame(relief=GROOVE, bd=10)
        F4.place(x=700, y=180, width=500, height=500)
        bill_title = Label(F4, text='LOAN REPORT', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F4, orient=VERTICAL)
        textarea = tk.Text(F4, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=textarea.yview)
        textarea.pack()
        submit_button = Button(F4, bg="grey", fg="black", width=15, text="SUBMIT", command=printsam)
        submit_button.pack()
        close_button = Button(F4, bg="grey", fg="black", width=15, text="CLOSE", command=Close)
        close_button.pack()
        user_in = textarea.get(1.0, "end-1c")
        textarea.delete(1.0, END)
        textarea.insert(END, "\t  (NASCS-NICS) LOAN REQUEST REPORT ")
        textarea.insert(END, f"\n\nFILE NO:------\t\t\t{fnorq.get()}")
        textarea.insert(END, f"\nACCOUNT TYPE:----\t\t{accrq.get()}")
        textarea.insert(END, f"\nLOAN AMOUNT:--------\t\t{loanAmountVar.get()}")
        textarea.insert(END, f"\nNUMBER OF MONTHS:--------\t\t{numberOfYearsVarmonth.get()}")
        textarea.insert(END, f"\nDATE:--------------------\t{lbdatrq.get()}")
        textarea.insert(END,                                                                                                                                                                f"\n\n======================================")
        textarea.insert(END, f"\n======================================\n")
        textarea.configure(font='arial 9 bold')
    tk.Button(Home, text='GENERATE REPORT', command=loanreport).place(x=433, y=300)

    fileln = tk.Label(Home, text="SEARCH FILE NO:", anchor="w", width=15, font=("century", 8))
    fileln.place(x=0, y=32)
    search_famnas = tk.Entry(Home, textvar=searchrequest , font=('bold', 12), width=7)
    search_famnas.place(x=112, y=32)
    srcbutfm3 = tk.Button(Home, text='CLICK',font=("century", 8), anchor="w",command=search_recordsrequest)
    srcbutfm3.place(x=180, y=29)
    label_15 = tk.Label(Home, text="FILE NUMBER", anchor="w", width=20, font=("century", 11))
    label_15.place(x=9, y=100)
    entry15 = tk.Entry(Home, textvar=fnorq,font=('bold', 12), width=20)
    entry15.place(x=200, y=100)
    labelacty = tk.Label(Home, text="ACCOUNT TYPE", anchor="w", width=20, font=("century", 11))
    labelacty.place(x=9, y=130)
    accrq.set("SELECT")
    entryTYPE = OptionMenu(Home, accrq,"Savings")
    entryTYPE.place(x=200, y=130)
    entryTYPE.configure(width=23)
    labelLA = tk.Label(Home, text="LOAN AMOUNT:", anchor="w", width=20, font=("century", 11))
    labelLA.place(x=9, y=160)
    entryLA = tk.Entry(Home,textvar=loanAmountVar, font=('bold', 12), width=20)
    entryLA.place(x=200, y=160)
    labelIR = tk.Label(Home, text="NUMBER OF MONTHS:", anchor="w", width=20, font=("century", 11))
    labelIR.place(x=9, y=190)
    entryIR = tk.Entry(Home,textvar=numberOfYearsVarmonth, font=('bold', 12), width=20)
    entryIR.place(x=200, y=190)
    label_date = tk.Label(Home, text="DATE:", anchor="w", width=20, font=("century", 11))
    label_date.place(x=9, y=220)
    daterq= DateEntry(Home, width=27, year=2019, month=6, day=22,
                        background='darkblue', foreground='white', borderwidth=14)
    daterq.place(x=200, y=220)
    Home.bind(daterq)
    entry_datel = tk.Label(Home,textvar=lbdatrq,anchor="w", width=20, font=("century", 11),state='disabled')
    entry_datel.place(x=9, y=250)
    lasi=tk.Label(Home, text="LOAN REQUEST", font=('times new roman', 17)).pack()
    ldn = tk.Button(Home, text='Back', command=LoanReq).pack(pady=20, fill=X)

imgsrcacloan = PhotoImage(file="loanrq.png")
imgsrcacloan1  = imgsrc.subsample(5, 5)
btnsamACLN =tk.Button(loan,text="REFUND REQUEST",image=imgsrcacloan,anchor="w", bg='white',fg='green',command=LoanRequest)
btnsamACLN.place(x=200, y=300)


def LoanReq():
    Home.destroy()





def LoanRefund():
    LoanRef =tk.Toplevel()
    LoanRef.title("Login Admin")
    width = 700
    height = 350
    LoanRef.config(bg="green")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    LoanRef.geometry("%dx%d+%d+%d" % (width, height, x, y))

    fnorfnd = StringVar()
    Amountrfnd =StringVar()
    adminyr = IntVar()
    baladminyr=StringVar()
    sumamt=IntVar()
    serchrfnd=StringVar()
    dyr2=tk.StringVar()


    def insert_refund():

        try:
            con = pymysql.connect(host=db_config.DB_SERVER,
                                  user=db_config.DB_USER,
                                  password=db_config.DB_PASS,
                                  database=db_config.DB)

            a1rfnd = fnorfnd.get().upper()
            e5rfnd = Amountrfnd.get()
            jrfnd = dyr2.get()
            smamt=sumamt.get()
            delamnt=adminyr.get()
            delbal =baladminyr.get()

            sqlrfnd = "INSERT INTO refund (FNO,AMOUNT,DATE) VALUES (%s,%s,%s)"
            valrfnd = (a1rfnd, e5rfnd, jrfnd)
            cursor = con.cursor()
            cursor.execute(sqlrfnd, valrfnd)
            con.commit()
            messagebox.showinfo("Database", "Record Added to Database")
        except pymysql.ProgrammingError as e:
            database_error(e)
        except pymysql.DataError as e:
            database_error(e)
        except pymysql.IntegrityError as e:
            database_error(e)
        except pymysql.NotSupportedError as e:
            database_error(e)
        except pymysql.OperationalError as e:
            database_error(e)
        except pymysql.InternalError as e:
            database_error(e)
    tk.Button(LoanRef, text='SUBMIT RECORD',command=insert_refund).place(x=9, y=310)

    def search_refund():
        global row
        global result
        global dyr2
        dyr2=tk.StringVar()

        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)


        cap=sch_RFnd.get()
        valsrefund1 = serchrfnd.get()
        sqlrefund1 = "SELECT * FROM refund WHERE FNO=%s"
        sqlsum = "SELECT SUM(AMOUNT)FROM REFUND WHERE FNO='"+ sch_RFnd.get() +"'"
        amntln="SELECT LOANAMOUNT FROM REQUEST WHERE FNO='"+ sch_RFnd.get() +"'"
        cursor = con.cursor()
        Lenrfnd = (valsrefund1,)
        resultsum=cursor.execute(sqlsum)
        resultsum = cursor.fetchone()
        resultLON = cursor.execute(amntln)
        resultLON=cursor.fetchone()
        result=cursor.execute(sqlrefund1, Lenrfnd)
        result = cursor.fetchall()
        if result:

            for row in result:
                fnorfnd.set(result[0][0])
                Amountrfnd.set(result[0][1])
                dyr2.set(result[0][2])
        if resultsum:
            for user in resultsum:
                sumamt.set(user)
        if resultLON:
            for amnlon in resultLON:
                adminyr.set(amnlon)
        sp=adminyr.get()
        cp=sumamt.get()
        if cap:
            repbal=sp-cp
            baladminyr.set(repbal)

    def updaterfd():
        global rowrfd
        global resultrfd

        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        cursor = con.cursor()
        varno1rfd = fnorfnd.get()
        varno2rfd = Amountrfnd.get()
        varno5rfd = dyr2.get()


        queryrfd = "UPDATE refund SET FNO=%s,AMOUNT=%s,DATE=%s WHERE FNO=%s "
        cursor.execute(queryrfd, (varno1rfd , varno2rfd ,varno5rfd,sch_RFnd.get(),))
        tk.messagebox.showinfo("Updated", "Successfully Updated.")
        con.commit()
    tk.Button(LoanRef, text='UPDATE RECORD',command=updaterfd).place(x=115, y=310)


    def del_recordsrfd():
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)

        if (sch_RFnd.get()):
            tk.messagebox.showinfo("Deleted", "Successfully Deleted.")
        else:
            con = pymysql.connect(host=db_config.DB_SERVER,
                                  user=db_config.DB_USER,
                                  password=db_config.DB_PASS,
                                  database=db_config.DB)

        cursor = con.cursor()
        cursor.execute("Delete from refund WHERE FNO='" + sch_RFnd.get() + "'")
        con.commit()
        enRFND.delete(0, 'end')
        enamtty.delete(0, 'end')
        dyr2.delete(0, 'end')
    tk.Button(LoanRef, text='DELETE RECORD',command=del_recordsrfd).place(x=221, y=310)


    def Clear_refnd():
        if (sch_RFnd.get()):
            enRFND.delete(0, END)
            enamtty.delete(0, END)
            dyr2.delete(0, END)
            tk.messagebox.showinfo("Cleared Report", "Successfully Cleared.")
        else:
            tk.messagebox.showinfo("Declined.")
    tk.Button(LoanRef, text='CLEAR RECORD',command=Clear_refnd).place(x=327, y=310)


    def loanREFUNDreport():
        def Close1():
            F5.destroy()

        def printsam1():
            q = textarearfd.get("1.0", "end-1c")
            filerfd = tempfile.mktemp(".txt")
            open(filerfd, "w").write(q)
            win32api.ShellExecute(0, "print", filerfd, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)

        global user_in1, win
        F5 = Frame(relief=GROOVE, bd=10)
        F5.place(x=700, y=180, width=500, height=500)
        bill_title1 = Label(F5, text='LOAN REFUND REPORT', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y1 = Scrollbar(F5, orient=VERTICAL)
        textarearfd = tk.Text(F5, yscrollcommand=scrol_y1)
        scrol_y1.pack(side=RIGHT, fill=Y)
        scrol_y1.config(command=textarearfd.yview)
        textarearfd.pack()
        submit_button1 = Button(F5, bg="grey", fg="black", width=15, text="SUBMIT", command=printsam1)
        submit_button1.pack()
        close_button1 = Button(F5, bg="grey", fg="black", width=15, text="CLOSE", command=Close1)
        close_button1.pack()
        user_in1 = textarearfd.get(1.0, "end-1c")
        textarearfd.delete(1.0, END)
        textarearfd.insert(END, "\t  (NASCS-NICS) LOAN REFUND REPORT ")
        textarearfd.insert(END, f"\n\nFILE NO:------\t\t\t{fnorfnd.get()}")
        textarearfd.insert(END, f"\nAMOUNT:----\t\t{Amountrfnd.get()}")
        textarearfd.insert(END, f"\nDATE:--------\t\t{dyr2.get()}")
        textarearfd.insert(END, f"\nTOTAL REFUND:--------\t\t{sumamt.get()}")
        textarearfd.insert(END, f"\nAMOUNT-LOANED:--------------------\t{adminyr.get()}")
        textarearfd.insert(END, f"\nDEBT BALANCE:--------------------\t{baladminyr.get()}")
        textarearfd.insert(END,                                                                                                                                                                f"\n\n======================================")
        textarearfd.insert(END, f"\n======================================\n")
        textarearfd.configure(font='arial 9 bold')
    tk.Button(LoanRef, text='GENERATE REPORT',command=loanREFUNDreport).place(x=433, y=310)

    fileRFND = tk.Label(LoanRef, text="SEARCH FILE NO:", anchor="w", width=15, font=("century", 8))
    fileRFND.place(x=0, y=32)
    sch_RFnd = tk.Entry(LoanRef,textvar=serchrfnd, font=('bold', 12), width=7)
    sch_RFnd.place(x=112, y=32)
    srcRFnd = tk.Button(LoanRef, text='CLICK', font=("century", 8), anchor="w",command=search_refund)
    srcRFnd.place(x=180, y=29)
    labRFnd = tk.Label(LoanRef, text="FILE NUMBER", anchor="w", width=20, font=("century", 11))
    labRFnd.place(x=9, y=100)
    enRFND = tk.Entry(LoanRef, textvar=fnorfnd ,font=('bold', 12), width=20)
    enRFND.place(x=200, y=100)
    RFDAM = tk.Label(LoanRef, text="AMOUNT", anchor="w", width=20, font=("century", 11))
    RFDAM.place(x=9, y=130)
    enamtty = tk.Entry(LoanRef,textvar= Amountrfnd,font=('bold', 12), width=20)
    enamtty.place(x=200, y=130)
    dterfnd = tk.Label(LoanRef, text="DATE:", anchor="w", width=20, font=("century", 11))
    dterfnd.place(x=9, y=160)
    dyr2 =DateEntry(LoanRef, width=27,year=2019, month=6, day=22,
                        background='darkblue', foreground='white', borderwidth=14)
    dyr2.place(x=200, y=160)
    #LoanRef.bind(dyr2)
    labtlrfnd = tk.Label(LoanRef, text="AMOUNT REFUNDED:", anchor="w", width=20, font=("century", 11))
    labtlrfnd.place(x=9, y=190)
    enttlrfnd = tk.Entry(LoanRef, textvar= sumamt,font=('bold', 12), width=20, state='disabled')
    enttlrfnd.place(x=200, y=190)
    amntloaned = tk.Label(LoanRef, text="AMOUNT LOANED:", anchor="w", width=20, font=("century", 11))
    amntloaned.place(x=9, y=220)
    amntloanedent = tk.Entry(LoanRef,textvar=adminyr, width=20, font=("century", 11),state='disabled')
    amntloanedent.place(x=200, y=220)
    balandebt = tk.Label(LoanRef, text="DEBT BALANCE:", anchor="w", width=20, font=("century", 11))
    balandebt.place(x=9, y=250)
    balandebtent = tk.Entry(LoanRef,textvar=baladminyr, width=20, font=("century", 11),state='disabled')
    balandebtent.place(x=200, y=250)
    #btn_reportRF = Button(LoanRef, text='GENERATE REPORT').place(x=539, y=410)

    tk.Label(LoanRef, text="REFUND LOAN!", font=('times new roman', 17)).pack()
    tk.Button(LoanRef, text='Back', command=Refund).pack(pady=20, fill=X)

imgsrcfmLREF = PhotoImage(file="loanrq1.png")
imgsrc1fm2 = imgsrc.subsample(5, 5)
srcbutfm2=tk.Button(loan, text='LOAN REFUND', image=imgsrcfmLREF,command=LoanRefund,anchor="w", bg='white',fg='green').place(x=700, y=300)
#btn_rep=tk.Button(loan, text='LOAN REFUND',command=LoanRefund,anchor="w", bg='white',fg='green').place(x=700, y=300)
indivi=StringVar()


def Close2():
    F12.destroy()
def backup():
    global user_bk
    global treeb
    global  F12
    global entsrch
    F12 = Frame(relief=GROOVE, bd=10,bg='white')
    F12.place(x=600, y=350, width=600, height=300)
    bill_title1 = Label(F12, text='BACKUP', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
    bill_jh = Label(F12, text='SEARCH', font='arial 9').place(x=4,y=6)
    entsrch = tk.Entry(F12, textvariable=indivi, font=('bold', 12), width=7)
    entsrch.place(x=60,y=6)
    butcls = tk.Button(F12, text='CLOSE', bg='green', fg='white', command=Close2).place(x=520, y=4)
    element_headerb = ['1st', '2nd', '3rd', '4th', '5th']
    scrolb = Scrollbar(F12, orient=VERTICAL)
    treeb = ttk.Treeview(F12, columns=element_headerb, height=20, show="headings")
    treeb.configure(yscrollcommand=scrolb.set)
    treeb.column('1st', width=100, minwidth=50, stretch=tk.NO)
    treeb.column('2nd', width=150, minwidth=50, stretch=tk.NO)
    treeb.column('3rd', width=100, minwidth=50, stretch=tk.NO)
    treeb.column('4th', width=150, minwidth=50, stretch=tk.NO)
    treeb.column('5th', width=100, minwidth=50, stretch=tk.NO)

    global bal


    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)
    cursor = con.cursor()
    cursor.execute("select FNO,ACCOUNTYPE,LOANAMOUNT,MONTHLYPAY,DATE from request union all select FNO,Null as ACCOUNTYPE,AMOUNT,Null as MNTHPY,DATE from  refund ")
    resultb = cursor.fetchall()
    treeb.delete(*treeb.get_children())
    if resultb:
        for row1 in resultb:
            treeb.insert(parent='', index='end', values=(
                row1[0], row1[1], row1[2], row1[3], row1[4]))
            treeb.heading("1st", text="FILENO")
            treeb.heading("2nd", text="ACCOUNT-TYPE")
            treeb.heading("3rd", text="LOANAMOUNT")
            treeb.heading("4th", text="MONTHLY-REFUND")
            treeb.heading("5th", text="DATE")
            treeb.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()
            buttonsrch = tk.Button(F12, text='CLICK',bg='green',fg='white',command=search_recordsBK).place(x=130, y=4)
            buttonbzh = tk.Button(F12, text='RESET',bg='green',fg='white', command=backup).place(x=350, y=4)
            buttonwe = tk.Button(F12, text='BACKUP RECORD',bg='green',fg='white', command=Backuprecords).place(x=400, y=4)


def search_recordsBK():
    global  vals
    global  row
    global result

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    vals = indivi.get()
    valmil = indivi.get()
    sql = "select FNO,ACCOUNTYPE,LOANAMOUNT,MONTHLYPAY,DATE from request where FNO=%s union all select FNO,Null as ACCOUNTYPE,AMOUNT,Null as MNTHPY,DATE from  refund where FNO=%s"
    cursor = con.cursor()
    Lenmem=(vals,valmil)
    result=cursor.execute(sql, Lenmem)
    result = cursor.fetchall()
    treeb.delete(*treeb.get_children())
    if result:
        for row1 in result:
            treeb.insert(parent='', index='end', values=(
                row1[0], row1[1], row1[2], row1[3], row1[4]))
            treeb.heading("1st", text="FILENO")
            treeb.heading("2nd", text="ACCOUNT-TYPE")
            treeb.heading("3rd", text="LOANAMOUNT")
            treeb.heading("4th", text="MONTHLY-REFUND")
            treeb.heading("5th", text="DATE")
            treeb.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()


def Backuprecords():
    valp = indivi.get()
    if valp=='':
        tk.messagebox.showinfo("Empty Search", "Please insert a file No.")
    else:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        cursor = con.cursor()
        tk.messagebox.showinfo("Achieved", "Successfully Achieved.")
        for row_id in treeb.get_children():
            row = treeb.item(row_id)['values']
            value3 = (row[0], row[1], row[2], row[3], row[4])
            query3 = "insert into achieve (FNO,ACCOUNTYPE,LOANAMOUNT,MONTHLYPAY,DATE)values(%s,%s,%s,%s,%s)"
            cursor.execute(query3,value3)
            con.commit()

BKbutton1 = Button(fmloan, bg="green", fg="white", width=15, text="BACKUP ACHIEVE", command=backup)
BKbutton1.place(x=0,y=250)

def Refund():
    LoanRef.destroy()


# Create fonts for making difference in the frame
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='12')


def show_selected_record(self, event):
    self.clear_form()
    for selection in self.tvStudent.selection():
        item = self.tvStudent.item(selection)
        global roll_no
        roll_no, first_name, last_name, city, state, contact_no, dob = item["values"][0:7]
        self.entFName.insert(0, first_name)
        self.entLName.insert(0, last_name)
        self.entCity.insert(0, city)
        self.entState.insert(0, state)
        self.entContact.insert(0, contact_no)
        self.calDOB.insert(0, dob)
        return roll_no

global tf5
tf5 = Frame(supplycon,bg='green',bd=10)
tf5.place(x=200, y=230, width=1000, height=150)
svarn = StringVar()
svaran = StringVar()
svarbn = StringVar()
svarcn = StringVar()
svardn = StringVar()
svaren = StringVar()
svrn = StringVar()
svran = StringVar()
svrbn = StringVar()
svrcn = StringVar()
svrdn= StringVar()
pfnm= StringVar()
# COMMENTED AND NON COMMENTED REPORTS
global rumn
global ruman
global rumbn
global rumcn
global rumdn
global rumen
global rmn
global rman
global rmbn
global rmcn
global rmdn

con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

squmn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Credit-SAVINGS'"
squman = "SELECT SUM(BALANCE)FROM historycomment WHERE ACCOUNTTYPE='Credit-SAVINGS'"
squmbn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Credit-Investment'"
squmcn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Credit-TargetEMG'"
squmdn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='retirementsav'"
sqman = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-SAVINGS'"
sqmbn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-Investment'"
sqmcn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-TargetEMG'"
sqmdn = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-RetirementSAV'"
cursor = con.cursor()
rumn = cursor.execute(squmn)
rumn = cursor.fetchone()[0]
ruman = cursor.execute(squman)
ruman = cursor.fetchone()[0]
rumbn = cursor.execute(squmbn)
rumbn = cursor.fetchone()[0]
rumcn = cursor.execute(squmcn)
rumcn = cursor.fetchone()[0]
rumdn = cursor.execute(squmdn)
rumdn = cursor.fetchone()[0]
#rumen = cursor.execute(squmen)
#rumen = cursor.fetchone()[0]
rmn = cursor.execute(sqman)
rmn = cursor.fetchone()[0]
rman = cursor.execute(sqmbn)
rman = cursor.fetchone()[0]
rmbn = cursor.execute(sqmcn)
rmbn = cursor.fetchone()[0]
rmcn = cursor.execute(sqmdn)
rmcn = cursor.fetchone()[0]
top=(rumn or 0)+(ruman or 0)+(rumbn or 0)+(rumcn or 0)+(rumdn or 0)
dnasp=(rmn or 0)+(rman or 0)+(rmbn or 0)+(rmcn or 0)
svarn.set(rumn)
svaran.set(ruman)
svarbn.set(rumbn)
svarcn.set(rumcn)
svardn.set(rumdn)
svaren.set(top)
svrn.set(rmn)
svran.set(rman)
svrbn.set(rmbn)
svrcn.set(rmcn)
svrdn.set(dnasp)
#pfnm.set(rir)

labe35 =tk.Label(supplycon , text="COMMENTED AND NON COMMENTED REPORTS.", width=40, font=("century", 16), bg="green", fg="black")
labe35.place(x=465, y=190)
global tr35
icnm2=StringVar()
icn3=StringVar()

def nas_redb():
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    cursor = con.cursor()
    snsr = "select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,COMMENT from historycomment union all select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,Null as COMMENT from  history"
    cursor.execute(snsr, )
    tr35.delete(*tr35.get_children())
    fetchtr = cursor.fetchall()
    for rsttr in fetchtr:
        tr35.insert('', 'end',values=(rsttr[0],rsttr[1],rsttr[2],rsttr[3],rsttr[4],rsttr[5],rsttr[6]))
        tr35.pack(side='left', padx=0, pady=0)
        con.commit()

def cmd_mt():
    global  vcmds
    global  r8
    global rcmd4
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)
    cursor = con.cursor()
    vcmds = icnm2.get()
    vmd=icn3.get()
    scmdr = "select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,COMMENT from historycomment where FNO=%s union all select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,Null as COMMENT from  history where FNO=%s "
    Lcmdr=(vcmds,vmd)
    rcmd4=cursor.execute(scmdr, Lcmdr)
    rcmd4=cursor.fetchall()
    tr35.delete(*tr35.get_children())
    if rcmd4:
        for r8 in rcmd4:
            tr35.insert('', 'end',values=(r8[0], r8[1], r8[2], r8[3], r8[4],r8[5],r8[6]))
            tr35.heading("1st", text="DATE")
            tr35.heading("2nd", text="TIME")
            tr35.heading("3rd", text="DEBIT")
            tr35.heading("4th", text="BALANCE")
            tr35.heading("5th", text="ACCOUNTTYPE")
            tr35.heading("6th", text="FNO")
            tr35.heading("7th", text="COMMENT")
            tr35.pack(side='left', padx=0, pady=0)
            con.commit()

F35 = Frame(supplycon,bg='green',relief=GROOVE,bd=10)
F35.place(x=200, y=390, width=955, height=300)
bcmitle = Label(F35, text='REPORT', font='arial 15 bold', bd=7, relief=GROOVE)
bcmitle.pack(fill=X)
elheader = ['1st', '2nd', '3rd', '4th', '5th','6th','7th']
tr35pen = tk.Scrollbar(F35)
tr35pen.pack(side='right', fill='y')

lcm = Label(F35, text='SEARCH', font='arial 9').place(x=4,y=6)
lcmd = tk.Entry(F35, textvar=icnm2,font=('bold', 12), width=7)
lcmd.place(x=60,y=6)
mnde = tk.Button(F35, text='OK', bg='green', fg='white', command=cmd_mt).place(x=130, y=4)
cmde = tk.Button(F35, text="RESET", anchor="w", bg='green', fg='white', command=nas_redb).place(x=180, y=4)
def cmtrpt():
    def Closecm():
        f4p.destroy()

    global usr
    f4p = Frame(relief=GROOVE, bd=10,bg='green')
    f4p.place(x=700, y=180, width=600, height=300)
    bibi = Label(f4p, text='COMMENTED REPORT', font='arial 15 bold',bg='white', bd=7, relief=GROOVE).pack(fill=X)
    sc_y = Scrollbar(f4p, orient=VERTICAL)
    ttrns = tk.Text(f4p, yscrollcommand=sc_y)
    sc_y.pack(side=RIGHT, fill=Y)
    sc_y.config(command=ttrns.yview)
    ttrns.pack()
    ttrns.tag_add("whole", "2.0", "end-1c")
    ttrns.tag_configure("whole", spacing3=10)
    user_in = ttrns.get(1.0, "end-1c")
    ttrns.delete(1.0, END)

    with open("cmttrn.csv", "w", newline='') as mycmtr:
        csvwriter = csv.writer(mycmtr,delimiter='|')
        hder = ['(NASCS-NICS) COMMENTED REPORT']
        lne = ['--------------------------------------------------------']
        dta = ['DATE        TIME      DEBIT  BALANCE  ACCOUNTTYPE  FNO  COMMENT']
        csvwriter.writerow(hder)
        csvwriter.writerow(lne)
        csvwriter.writerow(dta)
        csvwriter.writerow(lne)

        for row_cm in tr35.get_children():
            row = tr35.item(row_cm)['values']
            if row_cm[0].isdigit():
                csvwriter.writerow(row_cm)
            csvwriter.writerow(lne)
            csvwriter.writerow(row)


    with open("cmttrn.csv", "r") as c:
     dtrc = c.read()
    ttrns.insert("1.0", dtrc)
    #textarea.insert(INSERT, dtrc)
    q = ttrns.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(q)
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
    close_button = Button(f4p, bg="green", fg="white", width=9, text="CLOSE", command=Closecm)
    close_button.place(x=2, y=4)

cmnn = tk.Button(F35, text="PRINT", anchor="w", bg='green', fg='white', command=cmtrpt).place(x=230, y=4)
con = pymysql.connect(host=db_config.DB_SERVER,
                      user=db_config.DB_USER,
                      password=db_config.DB_PASS,
                      database=db_config.DB)
cursor = con.cursor()

tr35 =ttk.Treeview(F35, columns=elheader,height=20, show="headings")
tr35.configure(yscrollcommand=tr35pen.set)
tr35.column('1st', width=100, minwidth=80, stretch=tk.NO)
tr35.column('2nd', width=100, minwidth=80, stretch=tk.NO)
tr35.column('3rd', width=100, minwidth=70, stretch=tk.NO)
tr35.column('4th', width=100, minwidth=70, stretch=tk.NO)
tr35.column('5th', width=150, minwidth=100, stretch=tk.NO)
tr35.column('6th', width=100, minwidth=70, stretch=tk.NO)
tr35.column('7th', width=270, minwidth=80, stretch=tk.NO)
scmh = "select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,COMMENT from historycomment union all select DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO,Null as COMMENT from  history"
cursor.execute(scmh, )
tr35.delete(*tr35.get_children())
fetch = cursor.fetchall()
for dcta in fetch:
        tr35.insert('', 'end', values=(
            dcta[0], dcta[1], dcta[2], dcta[3], dcta[4],dcta[5],dcta[6]))
        tr35.heading("1st", text="DATE")
        tr35.heading("2nd", text="TIME")
        tr35.heading("3rd", text="DEBIT")
        tr35.heading("4th", text="BALANCE")
        tr35.heading("5th", text="ACCOUNTTYPE")
        tr35.heading("6th", text="FNO")
        tr35.heading("7th", text="COMMENT")
        tr35.pack(side='left', padx=0, pady=0)
        tr35pen.config(command=tr35.yview)

varun=StringVar()
svar=StringVar()
svara=StringVar()
svarb=StringVar()
svarc=StringVar()
svard=StringVar()
svare=StringVar()
svr=StringVar()
svra=StringVar()
svrb=StringVar()
svrc=StringVar()
svrd=StringVar()


def transindicd():
    def Cse1():
        Ftrn.destroy()

    def printrans():
        t = textareartrn.get("1.0", "end-1c")
        fifd = tempfile.mktemp(".txt")
        open(fifd, "w").write(t)
        win32api.ShellExecute(0, "print", fifd, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)

    global usertran
    Ftrn = Frame(relief=GROOVE, bd=10)
    Ftrn.place(x=700, y=180, width=500, height=500)
    bill_title1 = Label(Ftrn, text="TRANSACTION REPORT.", font='arial 15 bold', bd=7,
                        relief=GROOVE).pack(fill=X)
    scry1 = Scrollbar(Ftrn, orient=VERTICAL)
    textareartrn = tk.Text(Ftrn, yscrollcommand=scry1)
    scry1.pack(side=RIGHT, fill=Y)
    scry1.config(command=textareartrn.yview)
    textareartrn.pack()
    subon1 = Button(Ftrn, bg="grey", fg="black", width=15, text="SUBMIT", command=printrans)
    subon1.pack()
    close_bon1 = Button(Ftrn, bg="grey", fg="black", width=15, text="CLOSE", command=Cse1)
    close_bon1.pack()
    usertran = textareartrn.get(1.0, "end-1c")
    textareartrn.delete(1.0, END)
    textareartrn.insert(END, "(NASCS - NICS) INDIVIDUAL CREDIT AND DEBIT TRANSACTION REPORT")
    textareartrn.insert(END, f"\t  CREDIT TRANSACTIONS USER:------\t\t\t{varun.get()}")
    textareartrn.insert(END, f"\n\nSAVINGS NON COMMENTED:------\t\t\t{svar.get()}")
    textareartrn.insert(END, f"\nSAVINGS COMMENTED:----\t\t\t\t{svara.get()}")
    textareartrn.insert(END, f"\nINVESTMENT:--------\t\t\t\t{svarb.get()}")
    textareartrn.insert(END, f"\nTARGET/EMERGENCY:--------\t\t\t{svarc.get()}")
    textareartrn.insert(END, f"\nRETIREMENT SAVINGS:--------------------\t\t{svard.get()}")
    textareartrn.insert(END, f"\nTOTAL CREDIT TRANSACTIONS:--------------------\t{svare.get()}")
    textareartrn.insert(END, f"\n\n======================================")
    textareartrn.insert(END, f"\n======================================\n")
    textareartrn.insert(END, "\t  DEBIT TRANSACTIONS.")
    textareartrn.insert(END, f"\n DEBIT-SAVINGS:------\t\t\t\t{svr.get()}")
    textareartrn.insert(END, f"\n DEBIT-INVESTMENT:----\t\t\t\t{svra.get()}")
    textareartrn.insert(END, f"\n DEBIT-TARGET-EMERGENCY:--------\t\t{svrb.get()}")
    textareartrn.insert(END, f"\n DEBIT-RETIREMENT SAVINGS:--------\t\t{svrc.get()}")
    textareartrn.insert(END, f"\nTOTAL DEBIT TRANSACTIONS:--------------------\t{svrd.get()}")
    textareartrn.configure(font='arial 9 bold')
bntinditn=tk.Button(tf5,text='PRINT INDIVIDUAL REPORT',bg='white',relief=GROOVE,width=40,font=("century", 5),command=transindicd).place(x=2, y=123)

def transnas():
    def Cse2():
        Ftnas.destroy()

    def prinnas():
        g = textnas.get("1.0", "end-1c")
        finas = tempfile.mktemp(".txt")
        open(finas, "w").write(g)
        win32api.ShellExecute(0, "print", finas, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)

    global usertran
    Ftnas = Frame(relief=GROOVE, bd=10)
    Ftnas.place(x=700, y=180, width=500, height=500)
    bilnas = Label(Ftnas, text="TRANSACTION REPORT.", font='arial 7 bold', bd=7,
                        relief=GROOVE).pack(fill=X)
    scry2 = Scrollbar(Ftnas, orient=VERTICAL)
    textnas = tk.Text(Ftnas, yscrollcommand=scry2)
    scry2.pack(side=RIGHT, fill=Y)
    scry2.config(command=textnas.yview)
    textnas.pack()
    subon1 = Button(Ftnas, bg="grey", fg="black", width=15, text="SUBMIT", command=prinnas)
    subon1.pack()
    close_bon2 = Button(Ftnas, bg="grey", fg="black", width=15, text="CLOSE", command=Cse2)
    close_bon2.pack()
    usertran = textnas.get(1.0, "end-1c")
    textnas.delete(1.0, END)
    textnas.insert(END, "(NASCS - NICS) CREDIT AND DEBIT TRANSACTION REPORT")
    textnas.insert(END, "\n\t CREDIT TRANSACTIONS.")
    textnas.insert(END, f"\n\nSAVINGS NON COMMENTED:------\t\t\t{svarn.get()}")
    textnas.insert(END, f"\nSAVINGS COMMENTED:----\t\t\t\t{svaran.get()}")
    textnas.insert(END, f"\nINVESTMENT:--------\t\t\t\t{svarbn.get()}")
    textnas.insert(END, f"\nTARGET/EMERGENCY:--------\t\t\t{svarcn.get()}")
    textnas.insert(END, f"\nRETIREMENT SAVINGS:--------------------\t\t{svardn.get()}")
    textnas.insert(END, f"\nTOTAL CREDIT TRANSACTIONS:--------------------\t{svaren.get()}")
    textnas.insert(END, f"\n\n======================================")
    textnas.insert(END, f"\n======================================\n")
    textnas.insert(END, "\t  DEBIT TRANSACTIONS.")
    textnas.insert(END, f"\n DEBIT-SAVINGS:------\t\t\t\t{svrn.get()}")
    textnas.insert(END, f"\n DEBIT-INVESTMENT:----\t\t\t\t{svran.get()}")
    textnas.insert(END, f"\n DEBIT-TARGET-EMERGENCY:--------\t\t{svrbn.get()}")
    textnas.insert(END, f"\n DEBIT-RETIREMENT SAVINGS:--------\t\t{svrcn.get()}")
    textnas.insert(END, f"\nTOTAL DEBIT TRANSACTIONS:--------------------\t{svrdn.get()}")
    textnas.configure(font='arial 9 bold')
bntnastn=tk.Button(tf5,text='PRINT (NASCS-NICS) REPORT',bg='white',relief=GROOVE,width=40,font=("century", 5),command=transnas).place(x=550, y=123)

def searchtrn():
    global rum
    global ruma
    global rumb
    global rumc
    global rumd
    global rume
    global rm
    global rma
    global rmb
    global rmc
    global rmd

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)
    mim=varun.get()
    valtn1 = varun.get()
    squm = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Credit-SAVINGS'and FNO=%s"
    squma = "SELECT SUM(BALANCE)FROM historycomment WHERE ACCOUNTTYPE='Credit-SAVINGS'and FNO=%s"
    squmb = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Credit-Investment'and FNO=%s"
    squmc = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Credit-TargetEMG'and FNO=%s"
    squmd = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='retirementsav'and FNO=%s"
    sqma = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-SAVINGS'and FNO=%s"
    sqmb = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-Investment'and FNO=%s"
    sqmc = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-TargetEMG'and FNO=%s"
    sqmd = "SELECT SUM(BALANCE)FROM history WHERE ACCOUNTTYPE='Debit-RetirementSAV'and FNO=%s"
    #dsn = "SELECT FNO FROM history where FNO=%s"
    cursor = con.cursor()
    #Lm = (mim,)
    #rir = cursor.execute(dsn, Lm)
    Lenrfnd = (valtn1,)
    rum = cursor.execute(squm,(Lenrfnd))
    rum = cursor.fetchone()[0]
    ruma = cursor.execute(squma,(Lenrfnd))
    ruma = cursor.fetchone()[0]
    rumb = cursor.execute(squmb,(Lenrfnd))
    rumb = cursor.fetchone()[0]
    rumc = cursor.execute(squmc,(Lenrfnd))
    rumc = cursor.fetchone()[0]
    rumd = cursor.execute(squmd,(Lenrfnd))
    rumd = cursor.fetchone()[0]
    totl = (rum or 0) + (ruma or 0) + (rumb or 0) + (rumc or 0) + (rumd or 0)
    svare.set(totl)
    rm = cursor.execute(sqma,(Lenrfnd))
    rm = cursor.fetchone()[0]
    rma = cursor.execute(sqmb,(Lenrfnd))
    rma = cursor.fetchone()[0]
    rmb = cursor.execute(sqmc,(Lenrfnd))
    rmb = cursor.fetchone()[0]
    rmc = cursor.execute(sqmd,(Lenrfnd))
    rmc = cursor.fetchone()[0]
    deb = (rm or 0) + (rma or 0) + (rmb or 0) + (rmc or 0)
    svar.set(rum)
    svara.set(ruma)
    svarb.set(rumb)
    svarc.set(rumc)
    svard.set(rumd)
    svr.set(rm)
    svra.set(rma)
    svrb.set(rmb)
    svrc.set(rmc)
    svrd.set(deb)

lbe36 =tk.Label(tf5, text="INDIVIDUAL CREDIT AND DEBIT TRANSACTION REPORT.",anchor="w", width=100, font=("century", 8), bg="green", fg="black").place(x=0, y=0)
lbe37 =tk.Label(tf5, text="CREDIT TRANSACTIONS.", width=25, font=("century", 7),anchor="w", bg="green", fg="black").place(x=0, y=15)
lbe38 =tk.Label(tf5, text="SAVINGS NON COMMENTED.", width=25, font=("century", 6), anchor="w",bg="green", fg="black").place(x=0, y=30)
lbe39 =tk.Label(tf5 ,text="SAVINGS COMMENTED.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=0, y=43)
lbe40 =tk.Label(tf5, text="INVESTMENT.", width=25, font=("century", 6), bg="green",anchor="w", fg="black").place(x=0, y=57)
lbe41 =tk.Label(tf5, text="TARGET/EMERGENCY.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=0, y=70)
lbe42 =tk.Label(tf5, text="RETIREMENT SAVINGS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=0, y=85)
lbe43 =tk.Label(tf5, text="TOTAL CREDIT TRANSACTIONS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=0, y=100)
#DEBIT TRANSACTIONS
lbe37d =tk.Label(tf5, text="DEBIT TRANSACTIONS.", width=25, font=("century", 7),anchor="w", bg="green", fg="black").place(x=280, y=15)
lbe38d =tk.Label(tf5, text="DEBIT-SAVINGS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=280, y=30)
#lbe39d =tk.Label(tf5, text="SAVINGS COMMENTED.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=280, y=43)
lbe40d =tk.Label(tf5, text="DEBIT-INVESTMENT.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=280, y=43)
lbe41d =tk.Label(tf5, text="DEBIT-TARGET-EMERGENCY.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=280, y=57 )
lbe42d =tk.Label(tf5, text="DEBIT-RETIREMENT SAVINGS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=280, y=70)
lbe43d =tk.Label(tf5, text="TOTAL DEBIT TRANSACTIONS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=280, y= 85)

# NAS TRANSACTION REPORT
lns6 =tk.Label(tf5, text="(NASCS-NICS) CREDIT AND DEBIT TRANSACTION REPORT.",anchor="w", width=100, font=("century", 8), bg="green", fg="black").place(x=550, y=0)
lns37 =tk.Label(tf5, text="CREDIT TRANSACTIONS.", width=25, font=("century", 7),anchor="w", bg="green", fg="black").place(x=550, y=15)
lns38 =tk.Label(tf5, text="SAVINGS NON COMMENTED.", width=25, font=("century", 6), anchor="w",bg="green", fg="black").place(x=550, y=30)
lns39 =tk.Label(tf5 ,text="SAVINGS COMMENTED.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=550, y=43)
lns40 =tk.Label(tf5, text="INVESTMENT.", width=25, font=("century", 6), bg="green",anchor="w", fg="black").place(x=550, y=57)
lns41 =tk.Label(tf5, text="TARGET/EMERGENCY.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=550, y=70)
lns42 =tk.Label(tf5, text="RETIREMENT SAVINGS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=550, y=85)
lns43 =tk.Label(tf5, text="TOTAL CREDIT TRANSACTIONS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=550, y=100)
#DEBIT TRANSACTIONS
lns37d =tk.Label(tf5, text="DEBIT TRANSACTIONS.", width=25, font=("century", 7),anchor="w", bg="green", fg="black").place(x=800, y=15)
lns38d =tk.Label(tf5, text="DEBIT-SAVINGS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=835, y=30)
#lns39d =tk.Label(tf5, text="SAVINGS COMMENTED.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=835, y=43)
lns40d =tk.Label(tf5, text="DEBIT-INVESTMENT.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=835, y=43)
lns41d =tk.Label(tf5, text="DEBIT-TARGET-EMERGENCY.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=835, y= 57)
lns42d =tk.Label(tf5, text="DEBIT-RETIREMENT SAVINGS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=835, y=70)
lns43d =tk.Label(tf5, text="TOTAL DEBIT TRANSACTIONS.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=835, y= 85)

#VARIABLE credit DECLARATION FOR INDIVIDUAL
lvr38 =tk.Label(tf5, textvariable=svar, width=25, font=("century", 6), anchor="w",bg="green", fg="black").place(x=150, y=30)
lvr39 =tk.Label(tf5 ,textvariable=svara, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=150, y=43)
lvr40 =tk.Label(tf5, textvariable=svarb, width=25, font=("century", 6), bg="green",anchor="w", fg="black").place(x=150, y=57)
lvr41 =tk.Label(tf5, textvariable=svarc, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=150, y=70)
lvr42 =tk.Label(tf5, textvariable=svard, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=150, y=85)
lvr43 =tk.Label(tf5, textvariable=svare, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=150, y=100)
#VARIABLE DEBIT TRANSACTIONS
lvr38d =tk.Label(tf5, textvariable=svr, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=420, y=30)
#lvr39d =tk.Label(tf5, textvariable=, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=420, y=43)
lvr40d =tk.Label(tf5, textvariable=svra, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=420, y=43)
lvr41d =tk.Label(tf5, textvariable=svrb, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=420, y= 57)
lvr42d =tk.Label(tf5, textvariable=svrc, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=420, y=70)
lvr43d =tk.Label(tf5, textvariable=svrd, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=420, y= 85)
#VARIABLE credit DECLARATION FOR NAS
vs38 =tk.Label(tf5, textvariable=svarn, width=25, font=("century", 6), anchor="w",bg="green", fg="black").place(x=700, y=30)
vs39 =tk.Label(tf5,textvariable=svaran, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=700, y=43)
vs40 =tk.Label(tf5, textvariable=svarbn, width=25, font=("century", 6), bg="green",anchor="w", fg="black").place(x=700, y=57)
vs41 =tk.Label(tf5, textvariable=svarcn, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=700, y=70)
vs42 =tk.Label(tf5, textvariable=svardn, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=700, y=85)
vs43 =tk.Label(tf5, textvariable=svaren, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=700, y=100)
#VARIABLE DEBIT TRANSACTIONS FOR NAS
lvb8d =tk.Label(tf5,textvariable=svrn, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=970, y=30)
#lvb9d =tk.Label(tf5, text="SD.", width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=970, y=43)
lvb0d =tk.Label(tf5, textvariable=svran, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=970, y=43)
lvb1d =tk.Label(tf5, textvariable=svrbn, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=970, y= 57)
lvb2d =tk.Label(tf5, textvariable=svrcn, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=970, y=70)
lvb3d =tk.Label(tf5, textvariable=svrdn, width=25, font=("century", 6),anchor="w", bg="green", fg="black").place(x=970, y=85)
lfno34 =tk.Label(tf5, text="SEARCH FNO:", width=15, font=("century", 10),anchor="w", bg="green", fg="black").place(x=200, y=123)
lent34 =tk.Entry(tf5,textvariable=varun,font='arial 9',width=10).place(x=294, y=122)
sr4ch = tk.Button(tf5, text='OK',bg='green', font=("century", 7),fg='black',command=searchtrn).place(x=374, y=122)

# Add a button to switch between two
imgc1 = PhotoImage(file="reg.png")
imgc = imgc1.subsample(5, 5)

imgc2 = PhotoImage(file="month.png")
imgd = imgc2.subsample(5, 5)

imgc3 = PhotoImage(file="loan.png")
imge = imgc3.subsample(5, 5)

imgc4 = PhotoImage(file="contrfq.png")
imgf = imgc4.subsample(5, 5)

imgc5 = PhotoImage(file="supply.png")
imgg = imgc5.subsample(5, 5)

imgc6 = PhotoImage(file="achieve.png")
imggA = imgc6.subsample(5, 5)

btnsam =tk.Button(win,text="MEMBERSHIP FORM",image=imgc1,anchor="w", bg='white',fg='green', command=membershipform)
btnsam.place(x=0, y=300)


btn2 =tk.Button(win, text="MONTHLY CONTRIBUTION",image=imgc2,anchor="w", bg='white',fg='green', command=contribution)
btn2.place(x=0, y=330)

btn3 =tk.Button(win, text="LOAN ACCESS",image=imgc3,anchor="w",bg='white',fg='green', command=loanaccess)
btn3.place(x=0, y=360)

btn4 =tk.Button(win, text="CONTRIBUTION FREQUENCY", image=imgc4,anchor="w",bg='white',fg='green', command=contrifreq)
btn4.place(x=0, y=390)

btn45 =tk.Button(win, text="COMMENTED REPORTS",image=imgc5,anchor="w", bg='white',fg='green',command=supplyconlink)
btn45.place(x=0, y=420)
btn46 =tk.Button(win, text="DELETED STAFF ",image=imgc6,anchor="w", bg='white',fg='green',command=achvstaff)
btn46.place(x=0, y=450)
con = pymysql.connect(host=db_config.DB_SERVER,
                      user=db_config.DB_USER,
                      password=db_config.DB_PASS,
                      database=db_config.DB)
cursor = con.cursor()
imglogt = PhotoImage(file="log.png")
imglogt1 =imglogt.subsample(5, 5)
logbut=tk.Button(win,text='LOGOUT',image=imglogt,command=Logout,anchor="w", bg='white',fg='green').place(x=4, y=200)

F5 = Frame(contrfrq,relief=GROOVE, bd=10)
F5.place(x=200, y=352, width=955, height=300)

def query_refrev():
    # Clear the Treeview
    for recd in tree.get_children():
        tree.delete(recd)

    # Create a database or connect to one that exists
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    # Create a cursor instance
    c = con.cursor()

    c.execute("SELECT * FROM history")
    recordsvw = c.fetchall()
    for recd in recordsvw:
        tree.insert(parent='', index='end',  text='',
                           values=(recd[0], recd[1], recd[2], recd[3], recd[4], recd[5]))

indnc=StringVar()
def searchnonc():
    global  vanc
    global  rnc
    global  rsnc
    global tree
    global tree2

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    vanc = indnc.get()
    sqcn = "select * from history where fno=%s"
    cursor = con.cursor()
    Lenv=(vanc)
    rsnc=cursor.execute(sqcn, Lenv)
    rsnc = cursor.fetchall()
    tree.delete(*tree.get_children())
    if rsnc:
        for rnc in rsnc :
            tree.insert(parent='', index='end', values=(
                rnc[0], rnc[1], rnc[2], rnc[3], rnc[4],rnc[5]))
            tree.heading("1st", text="DATE")
            tree.heading("2nd", text="TIME")
            tree.heading("3rd", text="DEBIT")
            tree.heading("4th", text="BALANCE")
            tree.heading("5th", text="ACCOUNTTYPE")
            tree.heading("6th", text="FNO")
            tree.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()


pyprd1 = StringVar()
nameacctp1 = StringVar()
entSTDT1 = StringVar()
entEDDT1 = StringVar()



bill_title = Label(F5, text='PAYMENT PERIOD REPORT', font='arial 15 bold', bd=7, relief=GROOVE)
bill_title.pack(fill=X)
ln1 = Label(F5, text='SEARCH', font='arial 9').place(x=4,y=6)
lnscn = tk.Entry(F5,textvar=indnc,font=('bold', 12), width=7).place(x=200,y=6)
element_header = ['1st', '2nd', '3rd', '4th', '5th','6th']
treeSpen = tk.Scrollbar(F5)
treeSpen.pack(side='right', fill='y')

label2 =tk.Label(contrfrq , text="PAYMENT PERIOD PROFILE.", width=30, font=("century", 17), bg="green", fg="black")
label2.place(x=478, y=190)
name =tk.Label(contrfrq , text="FILE-NO", anchor="w", width=18, font=("century", 9))
name.place(x=200, y=240)
entpyprd=tk.Entry(contrfrq,textvariable=pyprd1,font=('bold', 12), width=18)
entpyprd.place(x=351, y=240)
nameacctp =tk.Label(contrfrq , text="ACCOUNTTYPE", anchor="w", width=18, font=("century", 9))
nameacctp .place(x=200, y=270)
nameacctp1.set("SELECT")
entpyprd2= OptionMenu(contrfrq, nameacctp1,"Credit-SAVINGS","Credit-Investment","Credit-TargetEMG","Credit-RetirementSAV",
                          "Debit-SAVINGS","Debit-Investment","Debit-TargetEMG","Debit-RetirementSAV" )
entpyprd2.place(x=349, y=264)
entpyprd2.configure(width=21)
srtdt =tk.Label(contrfrq, text="START-DATE", anchor="w", width=18, font=("century", 9))
srtdt.place(x=530, y=240)
entSTDT=tk.Entry(contrfrq,textvariable=entSTDT1,font=('bold', 12), width=18)
entSTDT.place(x=678, y=240)
nameEDDT =tk.Label(contrfrq , text="END-DATE", anchor="w", width=18, font=("century", 9))
nameEDDT .place(x=530, y=270)
entEDDT=tk.Entry(contrfrq,textvariable=entEDDT1,font=('bold', 12), width=18)
entEDDT.place(x=678, y=270)
dtformt =tk.Label(contrfrq, text="DATE FORMAT(eg)= 2021-12-27",bg='green',fg='white',anchor="w", width=30, font=("century", 7)).place(x=678, y=220)

tree =ttk.Treeview(F5, columns=element_header,height=20, show="headings")
tree.configure(yscrollcommand=treeSpen.set)
tree.column('1st', width=150, minwidth=100, stretch=tk.NO)
tree.column('2nd', width=150, minwidth=100, stretch=tk.NO)
tree.column('3rd', width=150, minwidth=100, stretch=tk.NO)
tree.column('4th', width=150, minwidth=100, stretch=tk.NO)
tree.column('5th', width=150, minwidth=100, stretch=tk.NO)
tree.column('6th', width=150, minwidth=100, stretch=tk.NO)
sqlch = "select * from  history"
cursor.execute(sqlch, )
tree.delete(*tree.get_children())
fetch = cursor.fetchall()
for data in fetch:
        tree.insert('', 'end', values=(
            data[0], data[1], data[2], data[3], data[4],data[5]))
        tree.heading("1st", text="DATE")
        tree.heading("2nd", text="TIME")
        tree.heading("3rd", text="DEBIT")
        tree.heading("4th", text="BALANCE")
        tree.heading("5th", text="ACCOUNTTYPE")
        tree.heading("6th", text="FNO")
        tree.pack(side='left', padx=0, pady=0)
        treeSpen.config(command=tree.yview)
        cursor.close()
def saveme():
    def Close():
        F3p.destroy()

    global user_in, win,rown
    F3p = Frame(relief=GROOVE, bd=10,bg='green')
    F3p.place(x=700, y=180, width=600, height=300)
    bill_bil = Label(F3p, text='PAYMENT REPORT SENT FOR PRINTING', font='arial 15 bold',bg='white', bd=7, relief=GROOVE).pack(fill=X)
    scrol_y = Scrollbar(F3p, orient=VERTICAL)
    textarea = tk.Text(F3p, yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    textarea.tag_add("whole", "2.0", "end-1c")
    textarea.tag_configure("whole", spacing3=10)
    user_in = textarea.get(1.0, "end-1c")
    textarea.delete(1.0, END)

    with open("NASnew.csv", "w", newline='') as myfile:
        csvwriter = csv.writer(myfile,delimiter='|')
        header = ['(NASCS-NICS) LOAN REQUEST REPORT']
        line = ['--------------------------------------------------------']
        data = ['DATE        TIME      DEBIT  BALANCE  ACCOUNTTYPE  FNO']
        csvwriter.writerow(header)
        csvwriter.writerow(line)
        csvwriter.writerow(data)
        csvwriter.writerow(line)

        for row_id in tree.get_children():
            row = tree.item(row_id)['values']
            if row_id[0].isdigit():
                csvwriter.writerow(row_id)
            csvwriter.writerow(line)
            csvwriter.writerow(row)


    with open("NASnew.csv", "r") as f:
     data = f.read()
    textarea.insert("1.0", data)
    q = textarea.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(q)
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
    close_button = Button(F3p, bg="green", fg="white", width=9, text="CLOSE", command=Close)
    close_button.place(x=2, y=4)

biw = tk.Button(F5, text=" OK", anchor="w", bg='green', fg='white', command=searchnonc).place(x=300,y=3)
btn2= tk.Button(F5, text=" PRINT REPORT", anchor="w", bg='green', fg='white', command=saveme).place(x=3, y=3)
btnrviw = tk.Button(F5, text=" REFRESH VIEW", anchor="w", bg='green', fg='white', command=query_refrev).place(x=100,y=3)


def nutoh():
    F6.destroy()
    F5.pack_forget()

def search_payperiod():
    global F6
    global tree2
    def nutout():
        F6.destroy()
    F6 = Frame(contrfrq, relief=GROOVE, bd=10)
    F6.place(x=200, y=352, width=955, height=300)
    F5.pack_forget()
    global result
    global row
    bill_title = Label(F6, text='INDIVIDUAL PAYMENT REPORT', font='arial 15 bold', bd=7, relief=GROOVE)
    bill_title.pack(fill=X)
    element_header1 = ['1st', '2nd', '3rd', '4th', '5th', '6th']
    treeScroll2 = tk.Scrollbar(F6)
    treeScroll2.pack(side='right', fill='y')

    def indivi():
        def Close():
            F3ID.destroy()

        global userID
        F3ID = Frame(relief=GROOVE, bd=10, bg='green')
        F3ID.place(x=700, y=180, width=600, height=300)
        bill_ID = Label(F3ID, text='INDIVIDUAL PAYMENT LOAN REPORT SENT FOR PRINTING', font='arial 15 bold', bg='white',
                        bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F3ID, orient=VERTICAL)
        textareaID = tk.Text(F3ID, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=textareaID.yview)
        textareaID.pack()
        textareaID.tag_add("whole", "2.0", "end-1c")
        textareaID.tag_configure("whole", spacing3=10)
        userID = textareaID.get(1.0, "end-1c")
        textareaID.delete(1.0, END)

        with open("NASID.csv", "w", newline='') as memfile:
            csvwriter = csv.writer(memfile,delimiter='|')
            header = ['(NASCS-NICS) INDIVIDUAL PAYMENT PRINTING IN PROGRESS']
            line = ['--------------------------------------------------------']
            data = ['DATE        TIME      DEBIT  BALANCE  ACCOUNTTYPE  FNO']
            csvwriter.writerow(header)
            csvwriter.writerow(line)
            csvwriter.writerow(data)
            csvwriter.writerow(line)

            for row_id in tree2.get_children():
                row = tree2.item(row_id)['values']
                if row_id[0].isdigit():
                    csvwriter.writerow(row_id)
                csvwriter.writerow(line)
                print('save row:', row)
                csvwriter.writerow(row)

        with open("NASID.csv", "r") as f:
            data = f.read()
        textareaID.insert("1.0", data)
        q = textareaID.get("1.0", "end-1c")
        filename = tempfile.mktemp(".txt")
        open(filename, "w").write(q)
        win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
        close_button = Button(F3ID, bg="green", fg="white", width=9, text="CLOSE", command=Close)
        close_button.place(x=2, y=4)

    btnID = tk.Button(F6, text=" PRINT INDIVIDUAL REPORT", anchor="w", bg='green', fg='white', command=indivi).place(
        x=3, y=3)

    tree2 = ttk.Treeview(F6, columns=element_header1, height=20, show="headings")
    tree2.configure(yscrollcommand=treeScroll2.set)
    tree2.column('1st', width=150, minwidth=100, stretch=tk.NO)
    tree2.column('2nd', width=150, minwidth=100, stretch=tk.NO)
    tree2.column('3rd', width=150, minwidth=100, stretch=tk.NO)
    tree2.column('4th', width=150, minwidth=100, stretch=tk.NO)
    tree2.column('5th', width=150, minwidth=100, stretch=tk.NO)
    tree2.column('6th', width=150, minwidth=100, stretch=tk.NO)
    tk.Button(contrfrq, text="SWICTH TO MAIN REPORT", anchor="w", bg='white', fg='green', command=nutoh).place(x=850,y=270)
    global result
    global bal
    #abtcrd = pyprd1.get()
    #abtfnocrd = nameacctp1.get()
    srtdpypd = entSTDT1.get()
    endpypd = entEDDT1.get()
    abtfnocrd = nameacctp1.get()
    abtcrd1 = pyprd1.get()

    con = pymysql.connect(host=db_config.DB_SERVER,
                             user=db_config.DB_USER,
                             password=db_config.DB_PASS,
                             database=db_config.DB)
    cursor = con.cursor()
    sqlp="select * from history where FNO=%s and DATE(date) between %s and %s and ACCOUNTTYPE = %s"
    Ldmem = (abtcrd1,srtdpypd,endpypd,abtfnocrd)
    result = cursor.execute(sqlp, Ldmem)
    result = cursor.fetchall()
    tree2.delete(*tree2.get_children())
    if  result:
        for row1 in result:
             tree2.insert(parent='',index='end', values=(
                 row1[0], row1[1], row1[2], row1[3], row1[4], row1[5]))
             tree2.heading("1st", text="DATE")
             tree2.heading("2nd", text="TIME")
             tree2.heading("3rd", text="DEBIT")
             tree2.heading("4th", text="BALANCE")
             tree2.heading("5th", text="ACCOUNTTYPE")
             tree2.heading("6th", text="FNO")
             tree2.pack(side='left', padx=0, pady=0)
             treeScroll2.config(command=tree2.yview)
             con.commit()
             cursor.close()
btnPYPRD =tk.Button(contrfrq,text="GENERATE INDIVIDUAL REPORT",anchor="w", bg='white',fg='green',command=search_payperiod)
btnPYPRD.place(x=850, y=230)

global indipycntr
indipycntr = StringVar()

def ctrb_baserfs():
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    cursor = con.cursor()
    sqctr1 = "SELECT * FROM historyachieve"
    cursor.execute(sqctr1, )
    tcontr.delete(*tcontr.get_children())
    fetch = cursor.fetchall()
    for dcrt in fetch:
        tcontr.insert(parent='', index='end',  text='',
                           values=(dcrt[0],dcrt[1],dcrt[2],dcrt[3],dcrt[4],dcrt[5]))
        tcontr.pack(side='left', padx=0, pady=0)
    con.commit()
    cursor.close()
def Close3():
    F13.destroy()

def backupcontr():
    global user_bk
    global tcontr
    global F13
    global entcntr1
    F13 = Frame(relief=GROOVE, bd=10, bg='white')
    F13.place(x=600, y=350, width=600, height=300)
    bilcontr = Label(F13, text='BACKUP', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
    bilcont2 = Label(F13, text='SEARCH', font='arial 9').place(x=4, y=6)
    entcntr1 = tk.Entry(F13, textvariable=indipycntr, font=('bold', 12), width=7)
    entcntr1.place(x=60, y=6)
    butcontr3 = tk.Button(F13, text='CLOSE', bg='green', fg='white', command=Close3).place(x=520, y=4)
    elementcontr = ['1st', '2nd', '3rd', '4th', '5th','6th']
    scrolb = Scrollbar(F13, orient=VERTICAL)
    tcontr = ttk.Treeview(F13, columns=elementcontr, height=20, show="headings")
    tcontr.configure(yscrollcommand=scrolb.set)
    tcontr.column('1st', width=100, minwidth=50, stretch=tk.NO)
    tcontr.column('2nd', width=100, minwidth=50, stretch=tk.NO)
    tcontr.column('3rd', width=70, minwidth=50, stretch=tk.NO)
    tcontr.column('4th', width=70, minwidth=50, stretch=tk.NO)
    tcontr.column('5th', width=170, minwidth=50, stretch=tk.NO)
    tcontr.column('6th', width=70, minwidth=50, stretch=tk.NO)

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)
    cursor = con.cursor()
    cursor.execute("select * from history")
    contrres = cursor.fetchall()
    tcontr.delete(*tcontr.get_children())
    if contrres:
        for rres in contrres:
            tcontr.insert(parent='', index='end', values=(
                rres[0], rres[1], rres[2], rres[3], rres[4], rres[5]))
            tcontr.heading("1st", text="DATE")
            tcontr.heading("2nd", text="TIME")
            tcontr.heading("3rd", text="DEBIT")
            tcontr.heading("4th", text="BALANCE")
            tcontr.heading("5th", text="ACCOUNTTYPE")
            tcontr.heading("6th", text="FNO")
            tcontr.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()
            cntrsrch = tk.Button(F13, text='CLICK', bg='green', fg='white', command=search_contr).place(x=130, y=4)
            cntrbzh = tk.Button(F13, text='RESET', bg='green', fg='white', command=ctrb_baserfs).place(x=350, y=4)
            cntrnwe = tk.Button(F13, text='BACKUP RECORD', bg='green', fg='white', command=Bkupctr).place(x=400,y=4)
BKctr = Button(F5, bg="green", fg="white", width=15, text="BACKUP ACHIEVE", command=backupcontr)
BKctr.place(x=0, y=259)

def search_contr():
    global  valsctr
    global  r1
    global rsult4

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    valsctr = indipycntr.get()
    sqctr = "select * from history where fno=%s"
    cursor = con.cursor()
    Lenctr=(valsctr)
    rsult4=cursor.execute(sqctr, Lenctr)
    rsult4 = cursor.fetchall()
    tcontr.delete(*tcontr.get_children())
    if rsult4:
        for r1 in rsult4 :
            tcontr.insert(parent='', index='end', values=(
                r1[0], r1[1], r1[2], r1[3], r1[4],r1[5]))
            tcontr.heading("1st", text="DATE")
            tcontr.heading("2nd", text="TIME")
            tcontr.heading("3rd", text="DEBIT")
            tcontr.heading("4th", text="BALANCE")
            tcontr.heading("5th", text="ACCOUNTTYPE")
            tcontr.heading("6th", text="FNO")
            tcontr.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()


def Bkupctr():
    valp2 = indipycntr.get()
    if valp2=='':
        tk.messagebox.showinfo("Empty Search", "Please insert a file No.")
    else:
        con = pymysql.connect(host=db_config.DB_SERVER,
                              user=db_config.DB_USER,
                              password=db_config.DB_PASS,
                              database=db_config.DB)
        cursor = con.cursor()
        tk.messagebox.showinfo("Achieved", "Successfully Achieved.")
        for row_id in tcontr.get_children():
            roller = tcontr.item(row_id)['values']
            #vib3 = (roller[0], roller[1], roller[2], roller[3], roller[4],roller[5])
            vib3=(roller)
            que4 = "insert into historyachieve (DATE,TIME,DEBIT,BALANCE,ACCOUNTTYPE,FNO)values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(que4,vib3)
            con.commit()

def memreset_db():
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    cursor = con.cursor()
    acmem = "SELECT * FROM achievemember"
    cursor.execute(acmem, )
    trmem.delete(*trmem.get_children())
    fetch = cursor.fetchall()
    for mer in fetch:
        trmem.insert('', 'end', values=(mer[0],mer[1],mer[2],mer[3],mer[4],mer[5], mer[6], mer[7], mer[8], mer[9], mer[10],
                                   mer[11], mer[12], mer[13], mer[14], mer[15], mer[16], mer[17], mer[18]))
        trmem.pack(side='left', padx=0, pady=0)
    con.commit()
    cursor.close()
imembk=StringVar()
def memrp():
    global  valmem
    global  rmew
    global rmelt
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    valmem = imembk.get()
    sml = "SELECT * FROM achievemember where FILENO=%s"
    cursor = con.cursor()
    Ln=(valmem )
    rmelt=cursor.execute(sml, Ln)
    rmelt = cursor.fetchall()
    trmem.delete(*trmem.get_children())
    if rmelt:
        for rmew in rmelt:
            trmem.insert('', 'end', values=(rmew[0], rmew[1], rmew[2], rmew[3], rmew[4], rmew[5], rmew[6], rmew[7], rmew[8],
                        rmew[9], rmew[10],rmew[11], rmew[12], rmew[13], rmew[14], rmew[15], rmew[16], rmew[17], rmew[18], rmew[19]))
            trmem.heading('#1', text="FILENO")
            trmem.heading('#2', text="NAME")
            trmem.heading('#3', text="YEAR")
            trmem.heading('#4', text="MONTH")
            trmem.heading('#5', text="DAY")
            trmem.heading('#6', text="SEX")
            trmem.heading('#7', text="MARITAL")
            trmem.heading('#8', text="HOMEADD")
            trmem.heading('#9', text="MOBILE")
            trmem.heading('#10', text="EMAIL")
            trmem.heading('#11', text="DEPT")
            trmem.heading('#12', text="NXTKIN")
            trmem.heading('#13', text="RELATIONSHIP")
            trmem.heading('#14', text="NXTKINMOBILE")
            trmem.heading('#15', text="NXTKINADD")
            trmem.heading('#16', text="INVESTMENT")
            trmem.heading('#17', text="SAVINGS")
            trmem.heading('#18', text="TARGETEMG")
            trmem.heading('#19', text="RETIRESAVINS")
            trmem.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()
Fdem = Frame(achievfrm,bg="green",relief=GROOVE, bd=10)
Fdem.place(x=200, y=230, width=510, height=190)
labdel1 =tk.Label(achievfrm , text="DELETED STAFF PROFILE.", width=30, font=("century", 17), bg="green", fg="black")
labdel1.place(x=478, y=190)
bidem = Label(Fdem, text='MEMBERSHIP', font='arial 15 bold',relief=GROOVE, bd=7).pack(fill=X)
bdem1= Label(Fdem, text='SEARCH', font='arial 9').place(x=4,y=6)
entmem1 = tk.Entry(Fdem,textvar=imembk, font=('bold', 12), width=7)
entmem1.place(x=60,y=6)
element_mem = ['1st', '2nd', '3rd', '4th', '5th','6th','7th','8th','9th','10th', '11th','12th','13th','14th','15th','16th','17th','18th','19th']
treeSmem = tk.Scrollbar(Fdem)
treeSmem.pack(side='right', fill='y')
trmem =ttk.Treeview(Fdem, columns=element_mem , show="headings")
trmem.configure(yscrollcommand=treeSmem.set)
#trmem.column('#0', width=60, minwidth=50, stretch=tk.NO)
trmem.column('#1', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#2', width=70, minwidth=50, stretch=tk.NO)
trmem.column('#3', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#4', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#5', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#6', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#7', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#8', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#9', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#10', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#11', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#12', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#13', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#14', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#15', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#16', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#17', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#18', width=40, minwidth=20, stretch=tk.NO)
trmem.column('#19', width=40, minwidth=20, stretch=tk.NO)

con = pymysql.connect(host=db_config.DB_SERVER,
                      user=db_config.DB_USER,
                      password=db_config.DB_PASS,
                      database=db_config.DB)
cursor = con.cursor()
sqlmem = "SELECT * FROM achievemember"
cursor.execute(sqlmem, )
trmem.delete(*trmem.get_children())
fetch = cursor.fetchall()
for dta in fetch:
        trmem.insert('', 'end', values=(
            dta[0], dta[1], dta[2], dta[3], dta[4], dta[5], dta[6], dta[7], dta[8], dta[9], dta[10],
            dta[11], dta[12], dta[13], dta[14], dta[15], dta[16], dta[17], dta[18]))
trmem.heading('#1', text="FILENO")
trmem.heading('#2', text="NAME")
trmem.heading('#3', text="YEAR")
trmem.heading('#4', text="MONTH")
trmem.heading('#5', text="DAY")
trmem.heading('#6', text="SEX")
trmem.heading('#7', text="MARITAL")
trmem.heading('#8', text="HOMEADD")
trmem.heading('#9', text="MOBILE")
trmem.heading('#10', text="EMAIL")
trmem.heading('#11', text="DEPT")
trmem.heading('#12', text="NXTKIN")
trmem.heading('#13', text="RELATIONSHIP")
trmem.heading('#14', text="NXTKINMOBILE")
trmem.heading('#15', text="NXTKINADD")
trmem.heading('#16', text="INVESTMENT")
trmem.heading('#17', text="SAVINGS")
trmem.heading('#18', text="TARGETEMG")
trmem.heading('#19', text="RETIRESAVINS")
trmem.pack(side='left', padx=0, pady=0)
treeScroll.config(command=trmem.yview)
bmemln = tk.Button(Fdem, text="RESET", anchor="w", bg='green', fg='white',command=memreset_db,).place(x=350, y=4)
pmemn = tk.Button(Fdem, text="PRINT", anchor="w", bg='green', fg='white',).place(x=400, y=4)
bmensrch = tk.Button(Fdem, text='OK', bg='green', fg='white',command=memrp).place(x=130, y=4)


def loan_database():
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    cursor = con.cursor()
    sqldel1 = "SELECT * FROM achieve"
    cursor.execute(sqldel1, )
    trdel.delete(*trdel.get_children())
    fetch = cursor.fetchall()
    for dat in fetch:
        trdel.insert(parent='', index='end',  text='',values=(dat[0],dat[1],dat[2],dat[3],dat[4]))
        trdel.pack(side='left', padx=0, pady=0)
    con.commit()
    cursor.close()

def lonbk():
    def Close():
        F3bp.destroy()

    global user_inbp, win,rown
    F3bp = Frame(relief=GROOVE, bd=10,bg='green')
    F3bp.place(x=600, y=180, width=600, height=200)
    bill_bil = Label(F3bp, text='PAYMENT REPORT SENT FOR PRINTING', font='arial 6 bold',bg='white', ).pack(fill=X)
    scrol_y = Scrollbar(F3bp, orient=VERTICAL)
    textarea1 = tk.Text(F3bp, yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea1.yview)
    textarea1.pack()
    textarea1.tag_add("whole", "2.0", "end-1c")
    textarea1.tag_configure("whole", spacing3=10)
    user_inbp = textarea1.get(1.0, "end-1c")
    textarea1.delete(1.0, END)

    with open("lonbk.csv", "w", newline='') as myfilebk:
        csvwriter = csv.writer(myfilebk,delimiter='|')
        header = ['(NASCS-NICS) LOAN REQUEST REPORT']
        line1 = ['--------------------------------------------------------']
        datr =  ['FILENO  ACCOUNT-TYPE  LOANAMOUNT  MONTHLY-REFUND  DATE']
        csvwriter.writerow(header)
        csvwriter.writerow(line1)
        csvwriter.writerow(datr)
        csvwriter.writerow(line1)

        for row_id in trdel.get_children():
            row = trdel.item(row_id)['values']
            if row_id[0].isdigit():
                csvwriter.writerow(row_id)
            csvwriter.writerow(line1)
            csvwriter.writerow(row)


    with open("lonbk.csv", "r") as f:
     data = f.read()
    textarea1.insert("1.0", data)
    #textarea.insert(INSERT, data)
    q = textarea1.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(q)
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
    close_button = Button(F3bp, bg="green", fg="white", width=9, text="CLOSE", command=Close)
    close_button.place(x=2, y=4)
indilbk=StringVar()
def lnsr():
    global  valls
    global  row
    global result

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    valls = indilbk.get()
    sqel = "SELECT * FROM achieve where FNO=%s"
    cursor = con.cursor()
    Lemn=(valls)
    result=cursor.execute(sqel, Lemn)
    result = cursor.fetchall()
    trdel.delete(*trdel.get_children())
    if result:
        for row1 in result:
            trdel.insert(parent='', index='end', values=(
                row1[0], row1[1], row1[2], row1[3], row1[4]))
            trdel.heading("1st", text="FILENO")
            trdel.heading("2nd", text="ACCOUNT-TYPE")
            trdel.heading("3rd", text="LOANAMOUNT")
            trdel.heading("4th", text="MONTHLY-REFUND")
            trdel.heading("5th", text="DATE")
            trdel.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()
Fdel = Frame(achievfrm,bg="green",relief=GROOVE, bd=10)
Fdel.place(x=200, y=440, width=510, height=190)
bidel = Label(Fdel, text='LOAN REQUEST ', font='arial 15 bold',relief=GROOVE, bd=7).pack(fill=X)
bdl = Label(Fdel, text='SEARCH', font='arial 9').place(x=4,y=6)
entsr10 = tk.Entry(Fdel,textvar=indilbk, font=('bold', 12), width=7)
entsr10.place(x=60,y=6)
element_ln = ['1st', '2nd', '3rd', '4th', '5th','6th']
treeSln = tk.Scrollbar(Fdel)
treeSln.pack(side='right', fill='y')
trdel =ttk.Treeview(Fdel, columns=element_ln,height=20, show="headings")
trdel.configure(yscrollcommand=treeSln.set)
trdel.column('1st', width=100, minwidth=100, stretch=tk.NO)
trdel.column('2nd', width=100, minwidth=100, stretch=tk.NO)
trdel.column('3rd', width=100, minwidth=100, stretch=tk.NO)
trdel.column('4th', width=100, minwidth=100, stretch=tk.NO)
trdel.column('5th', width=100, minwidth=100, stretch=tk.NO)
trdel.column('6th', width=100, minwidth=100, stretch=tk.NO)
con = pymysql.connect(host=db_config.DB_SERVER,
                      user=db_config.DB_USER,
                      password=db_config.DB_PASS,
                      database=db_config.DB)
cursor = con.cursor()
sqldel1 = "SELECT * FROM achieve"
cursor.execute(sqldel1, )
trdel.delete(*trdel.get_children())
fetch = cursor.fetchall()
for dat in fetch:
        trdel.insert('', 'end', values=(
            dat[0], dat[1], dat[2], dat[3], dat[4]))
        trdel.heading("1st", text="FILENO")
        trdel.heading("2nd", text="ACCOUNT-TYPE")
        trdel.heading("3rd", text="LOANAMOUNT")
        trdel.heading("4th", text="MONTHLY-REFUND")
        trdel.heading("5th", text="DATE")
        trdel.pack(side='left', padx=0, pady=0)
        treeScroll.config(command=trdel.yview)

buttdelsrch = tk.Button(Fdel, text='OK',bg='green', fg='white',command=lnsr).place(x=130, y=4)
btnreln = tk.Button(Fdel, text="RESET", anchor="w", bg='green', fg='white',
                    command=loan_database).place(x=350, y=4)
pneln = tk.Button(Fdel, text="PRINT", anchor="w", bg='green', fg='white',
                    command=lonbk).place(x=400, y=4)

def contr_database():
    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    cursor = con.cursor()
    sctr = "SELECT * FROM historyachieve"
    cursor.execute(sctr, )
    trcr.delete(*trcr.get_children())
    fetch = cursor.fetchall()
    for ctrdt in fetch:
        trcr.insert(parent='', index='end',  text='',values=(ctrdt[0],ctrdt[1],ctrdt[2],ctrdt[3],ctrdt[4],ctrdt[5]))
        trcr.pack(side='left', padx=0, pady=0)
    con.commit()
    cursor.close()
indicntr2=StringVar()
def bk_ocontr():
    global  vals2k
    global  r5
    global rst4

    con = pymysql.connect(host=db_config.DB_SERVER,
                          user=db_config.DB_USER,
                          password=db_config.DB_PASS,
                          database=db_config.DB)

    vals2k = indicntr2.get()
    sqctr = "select * from historyachieve where fno=%s"
    cursor = con.cursor()
    Lctr=(vals2k)
    rst4=cursor.execute(sqctr, Lctr)
    rst4=cursor.fetchall()
    trcr.delete(*trcr.get_children())
    if rst4:
        for r5 in rst4 :
            trcr.insert(parent='', index='end', values=(
                r5[0], r5[1], r5[2], r5[3], r5[4],r5[5]))
            trcr.heading("1st", text="DATE")
            trcr.heading("2nd", text="TIME")
            trcr.heading("3rd", text="DEBIT")
            trcr.heading("4th", text="BALANCE")
            trcr.heading("5th", text="ACCOUNTTYPE")
            trcr.heading("6th", text="FNO")
            trcr.pack(side='left', padx=0, pady=0)
            con.commit()
            cursor.close()
def ctrprint():
    def Close():
        F13p.destroy()

    global user_in, win,rown
    F13p = Frame(relief=GROOVE, bd=10,bg='green')
    F13p.place(x=600, y=180, width=500, height=300)
    bisc = Label(F13p, text='BACKUP STAFF REPORT SENT FOR PRINTING', font='arial 15 bold',bg='white').pack(fill=X)
    scy = Scrollbar(F13p, orient=VERTICAL)
    textarea2 = tk.Text(F13p, yscrollcommand=scy)
    scy.pack(side=RIGHT, fill=Y)
    scy.config(command=textarea2.yview)
    textarea2.pack()
    textarea2.tag_add("whole", "2.0", "end-1c")
    textarea2.tag_configure("whole", spacing3=10)
    user_in = textarea2.get(1.0, "end-1c")
    textarea2.delete(1.0, END)

    with open("ctrbknew.csv", "w", newline='') as cnfile:
        csvwriter = csv.writer(cnfile,delimiter='|')
        header3 = ['(NASCS-NICS) LOAN REQUEST REPORT']
        line3 = ['--------------------------------------------------------']
        data3 = ['DATE        TIME      DEBIT  BALANCE  ACCOUNTTYPE  FNO']
        csvwriter.writerow(header3)
        csvwriter.writerow(line3)
        csvwriter.writerow(data3)
        csvwriter.writerow(line3)

        for row_id in trcr.get_children():
            row = trcr.item(row_id)['values']
            if row_id[0].isdigit():
                csvwriter.writerow(row_id)
            csvwriter.writerow(line3)
            print('save row:', row)
            csvwriter.writerow(row)


    with open("ctrbknew.csv", "r") as c:
     data = c.read()
    textarea2.insert("1.0", data)
    #textarea.insert(INSERT, data)
    q = textarea2.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(q)
    win32api.ShellExecute(0, "print", filename, '/d:"%s"' % win32print.GetDefaultPrinter(), ".", 0)
    betton = Button(F13p, bg="green", fg="white", width=9, text="CLOSE", command=Close)
    betton.place(x=2, y=4)

Fdln = Frame(achievfrm,bg="green",relief=GROOVE, bd=10)
Fdln.place(x=730, y=230, width=510, height=190)
lndrq = Label(Fdln, text='CONTRIBUTION', font='arial 15 bold',relief=GROOVE, bd=7).pack(fill=X)
lndrq1 = Label(Fdln, text='SEARCH', font='arial 9').place(x=4,y=6)
lnsr10 = tk.Entry(Fdln, textvar=indicntr2,font=('bold', 12), width=7)
lnsr10.place(x=60,y=6)
element_fdln = ['1st', '2nd', '3rd', '4th', '5th','6th']
treeScroll = tk.Scrollbar(Fdln)
treeScroll.pack(side='right', fill='y')
trcr =ttk.Treeview(Fdln, columns=element_fdln,height=20, show="headings")
trcr.configure(yscrollcommand=treeScroll.set)
trcr.column('1st', width=70, minwidth=50, stretch=tk.NO)
trcr.column('2nd', width=70, minwidth=50, stretch=tk.NO)
trcr.column('3rd', width=70, minwidth=50, stretch=tk.NO)
trcr.column('4th', width=70, minwidth=50, stretch=tk.NO)
trcr.column('5th', width=120, minwidth=50, stretch=tk.NO)
trcr.column('6th', width=70, minwidth=50, stretch=tk.NO)
sqlch = "SELECT * FROM  historyachieve"
cursor.execute(sqlch, )
trcr.delete(*trcr.get_children())
fetch = cursor.fetchall()
for data in fetch:
        trcr.insert(parent='', index='end',  text='', values=(data[0], data[1], data[2], data[3], data[4],data[5]))
        trcr.heading("1st", text="DATE")
        trcr.heading("2nd", text="TIME")
        trcr.heading("3rd", text="DEBIT")
        trcr.heading("4th", text="BALANCE")
        trcr.heading("5th", text="ACCOUNTTYPE")
        trcr.heading("6th", text="FNO")
        trcr.pack(side='left', padx=0, pady=0)
        treeScroll.config(command=trcr.yview)
        cursor.close()

hadelsrch = tk.Button(Fdln, text='OK',bg='green', fg='white',command=bk_ocontr).place(x=130, y=4)
hareln = tk.Button(Fdln, text="RESET", anchor="w", bg='green', fg='white',
                    command=contr_database).place(x=350, y=4)
cneln = tk.Button(Fdln, text="PRINT", anchor="w", bg='green', fg='white',
                   command=ctrprint ).place(x=400, y=4)
win.mainloop()


