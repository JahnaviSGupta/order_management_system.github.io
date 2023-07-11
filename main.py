from msilib.schema import Font
import tkinter as tk
from tkinter import Frame, Label, ttk
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from cProfile import label
from distutils.cmd import Command
from pydoc import text
from re import X
from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import datetime
import time
from tkinter import *
from tkinter.tix import X_REGION
from turtle import bgcolor
# import mysql.connector


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# from PIL import Image, ImageTK
class loginpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label = tk.Label(self, text="Welcome To My OMS", font=(FONT_NAME,30,"bold"))
        # Label.place(x=275, y=50)

        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.pack(side=TOP)
        L1 = tk.Label(self, text="Username", font=(FONT_NAME, 12,"bold"))
        L1.place(x=300, y=200)
        T1 = tk.Entry(self, width=30, bd=5)
        T1.place(x=400, y=200)
        L2 = tk.Label(self, text="Password", font=(FONT_NAME, 12, "bold"))
        L2.place(x=300, y=300)
        T2 =tk.Entry(self, show="*", width=30, bd=5)


        T2.place(x=400, y=300)
        def verify():
            if T1.get() == "Jahnavi" and T2.get()=="123":
                controller.show_frame(homepage)
                messagebox.showinfo("Login Successfull","Login Successfull")
            elif T1.get() == "Oscin" and T2.get()=="123":
                controller.show_frame(homepage)
                messagebox.showinfo("Login Successfull","Login Successfull")
            else:
                messagebox.showinfo("Error", "Invalid Username or Password")

        Button = tk.Button(self, text="Login", font=(FONT_NAME, 15),
                           command= verify)
        Button.place(x=440, y=400)






class homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label = tk.Label(self, text="Order Management System", font=(FONT_NAME, 30, "bold"))
        # Label.place(x=140, y=50)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="ORDER MANAGEMENT SYSTEM", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.pack(side=TOP)

        Label2 = tk.Label(self, text="What data would you like to access?", font=(FONT_NAME, 15, "bold"))
        Label2.place(x=300, y=150)
        Button = tk.Button(self, text="Employee", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Employee))
        Button.place(x=425, y=200)
        # Button = tk.Button(self, text="Customer", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Customer))
        # Button.place(x=425, y=250)
        # Button = tk.Button(self, text="Product", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Product))
        # Button.place(x=425, y=300)
        # Button = tk.Button(self, text="Suppliers", font=(FONT_NAME, 15),
        #                    command=lambda: controller.show_frame(Supplier))
        # Button.place(x=425, y=350)
        # Button = tk.Button(self, text="Order", font=(FONT_NAME, 15), command=lambda: controller.show_frame(Order))
        # Button.place(x=425, y=400)


class firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Employee Details", font=(FONT_NAME, 30, "bold"))
        Label.place(x=230, y=50)
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(homepage))
        Button.place(x=250, y=450)


class secondpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Customer Details", font=("Arial Bold", 30))
        Label.place(x=250, y=250)

        Button = tk.Button(self, text="Back", font=("Arial", 15),
                           command=lambda: controller.show_frame(homepage))
        Button.place(x=250, y=450)


class thirdpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Product Details", font=("Arial Bold", 30))
        Label.place(x=250, y=250)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(homepage))
        Button.place(x=250, y=450)


class fourthpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Suppliers Details", font=("Arial Bold", 30))
        Label.place(x=250, y=250)
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(homepage))
        Button.place(x=250, y=450)


class fifthpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Order Details", font=("Arial Bold", 30))
        Label.place(x=250, y=250)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(homepage))
        Button.place(x=250, y=450)


class Employee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Employee Details", fg="black", bg="white",
                            font=("Courier", 50, "bold"))
        lbltitle.pack(side=TOP)

        Dataframe = Frame(self, bd=15, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=950, height=250)
        DataframeCenter = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE,
                                     font=("times new roman", 12, "bold"), text="Employee Information")
        DataframeCenter.place(x=10, y=5, width=900, height=200)

        lblmember = Label(DataframeCenter, bg="powder blue", text="Employee Name", font=("times new roman", 15, "bold"),
                          padx=2, pady=2)
        lblmember.grid(row=0, column=0, sticky=W)
        textmember = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
        textmember.grid(row=0, column=1)

        lblid = Label(DataframeCenter, bg="powder blue", text="Employee ID", font=("times new roman", 15, "bold"),
                      padx=2, pady=2)
        lblid.grid(row=1, column=0, sticky=W)
        textid = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
        textid.grid(row=1, column=1)

        lblno = Label(DataframeCenter, bg="powder blue", text="Contact No", font=("times new roman", 15, "bold"),
                      padx=2, pady=2)
        lblno.grid(row=2, column=0, sticky=W)
        textno = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
        textno.grid(row=2, column=1)

        lbladd = Label(DataframeCenter, bg="powder blue", text="Address", font=("times new roman", 15, "bold"), padx=2,
                       pady=2)
        lbladd.grid(row=3, column=0, sticky=W)
        textadd = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
        textadd.grid(row=3, column=1)

        lblbranch = Label(DataframeCenter, bg="powder blue", text="Branch", font=("times new roman", 15, "bold"),
                          padx=2, pady=2)
        lblbranch.grid(row=4, column=0, sticky=W)
        textbranch = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
        textbranch.grid(row=4, column=1)

        Buttonframe = Frame(self, bd=10, relief=RIDGE)
        Buttonframe.place(x=5, y=440, width=950, height=50)

        btnadddata = Button(Buttonframe, text="Add", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
        btnadddata.grid(row=0, column=0)

        btnadddata = Button(Buttonframe, text="Delete", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
        btnadddata.grid(row=0, column=1)

        btnadddata = Button(Buttonframe, text="Update", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
        btnadddata.grid(row=0, column=2)

        btnadddata = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
        btnadddata.grid(row=0, column=4)

        btnadddata = Button(Buttonframe, text="Back", font=("arial", 12, "bold"), width=18, bg="blue", fg="white",
                            command=lambda: controller.show_frame(homepage))
        btnadddata.grid(row=0, column=3)

        Detailsframe = Frame(self, bd=10, relief=RIDGE)
        Detailsframe.place(x=20, y=500, width=1330, height=180)

        # yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.employee_table = ttk.Treeview(Detailsframe,
                                           column=("Employee ID", "Employee Name", "Contact No", "Address", "Branch"))

        self.employee_table.heading("Employee ID", text="Customer ID")
        self.employee_table.heading("Employee Name", text="Employee Name")
        self.employee_table.heading("Contact No", text="Contact No")
        self.employee_table.heading("Address", text="Address")
        self.employee_table.heading("Branch", text="Branch")
        self.employee_table["show"] = "headings"
        self.employee_table.pack(fill=BOTH, expand=1)



# class Customer(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Customer Details", fg="black", bg="white",
#                             font=("Courier", 50, "bold"))
#         lbltitle.pack(side=TOP)
#
#         Dataframe = Frame(self, bd=15, relief=RIDGE)
#         Dataframe.place(x=0, y=130, width=950, height=250)
#         DataframeCenter = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE,
#                                      font=("times new roman", 12, "bold"), text="Customer Information")
#         DataframeCenter.place(x=10, y=5, width=900, height=200)
#
#         lblmember = Label(DataframeCenter, bg="powder blue", text="Customer Name", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblmember.grid(row=0, column=0, sticky=W)
#         textmember = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textmember.grid(row=0, column=1)
#
#         lblid = Label(DataframeCenter, bg="powder blue", text="Customer ID", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblid.grid(row=1, column=0, sticky=W)
#         textid = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textid.grid(row=1, column=1)
#
#         lblno = Label(DataframeCenter, bg="powder blue", text="Contact No", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblno.grid(row=2, column=0, sticky=W)
#         textno = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textno.grid(row=2, column=1)
#
#         lbladd = Label(DataframeCenter, bg="powder blue", text="Company Name", font=("times new roman", 15, "bold"), padx=2,
#                        pady=2)
#         lbladd.grid(row=3, column=0, sticky=W)
#         textadd = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textadd.grid(row=3, column=1)
#
#         lblbranch = Label(DataframeCenter, bg="powder blue", text="Address", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblbranch.grid(row=4, column=0, sticky=W)
#         textbranch = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textbranch.grid(row=4, column=1)
#
#         Buttonframe = Frame(self, bd=10, relief=RIDGE)
#         Buttonframe.place(x=5, y=440, width=950, height=50)
#
#         btnadddata = Button(Buttonframe, text="Add", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=0)
#
#         btnadddata = Button(Buttonframe, text="Delete", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=1)
#
#         btnadddata = Button(Buttonframe, text="Update", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=2)
#
#         btnadddata = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=4)
#
#         btnadddata = Button(Buttonframe, text="Back", font=("arial", 12, "bold"), width=18, bg="blue", fg="white",
#                             command=lambda: controller.show_frame(homepage))
#         btnadddata.grid(row=0, column=3)
#
#         Detailsframe = Frame( bd=10, relief=RIDGE)
#         Detailsframe.place(x=20, y=500, width=1330, height=180)
#
#         yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
#
#         self.employee_table = ttk.Treeview(Detailsframe,
#                                            column=("Customer ID", "Customer Name", "Contact No", "Address","Company Name"))
#
#         self.employee_table.heading("Customer ID", text="Customer ID")
#         self.employee_table.heading("Customer Name", text="Customer Name")
#         self.employee_table.heading("Contact No", text="Contact No")
#         self.employee_table.heading("Address", text="Address")
#         self.employee_table.heading("Company Name", text="Company Name")
#         self.employee_table["show"] = "headings"
#         self.employee_table.pack(fill=BOTH, expand=1)
#
#         Detailsframe =Frame( bd=10, relief=RIDGE)
#         Detailsframe.place(x=0, y=500, width=1330, height=180)
#
#         yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
#
#         self.employee_table = ttk.Treeview(Detailsframe,
#                                            column=("Employee ID", "Employee Name", "Contact No", "Address", "Branch"))
#
#         self.employee_table.heading("Employee ID", text="Employee ID")
#         self.employee_table.heading("Employee Name", text="Employee Name")
#         self.employee_table.heading("Contact No", text="Contact No")
#         self.employee_table.heading("Address", text="Address")
#         self.employee_table.heading("Branch", text="Branch")
#         self.employee_table["show"] = "headings"
#         self.employee_table.pack(fill=BOTH, expand=1)
#

# class Supplier(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Supplier Details", fg="black", bg="white",
#                             font=("Courier", 50, "bold"))
#         lbltitle.pack(side=TOP)
#
#         Dataframe = Frame(self, bd=15, relief=RIDGE)
#         Dataframe.place(x=0, y=130, width=950, height=250)
#         DataframeCenter = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE,
#                                      font=("times new roman", 12, "bold"), text="Supplier Information")
#         DataframeCenter.place(x=10, y=5, width=900, height=200)
#
#         lblmember = Label(DataframeCenter, bg="powder blue", text="Supplier Name", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblmember.grid(row=0, column=0, sticky=W)
#         textmember = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textmember.grid(row=0, column=1)
#
#         lblid = Label(DataframeCenter, bg="powder blue", text="Supplier ID", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblid.grid(row=1, column=0, sticky=W)
#         textid = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textid.grid(row=1, column=1)
#
#         lblno = Label(DataframeCenter, bg="powder blue", text="Contact No", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblno.grid(row=2, column=0, sticky=W)
#         textno = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textno.grid(row=2, column=1)
#
#         lbladd = Label(DataframeCenter, bg="powder blue", text="Address", font=("times new roman", 15, "bold"), padx=2,
#                        pady=2)
#         lbladd.grid(row=3, column=0, sticky=W)
#         textadd = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textadd.grid(row=3, column=1)
#
#         lblbranch = Label(DataframeCenter, bg="powder blue", text="Supplier Branch", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblbranch.grid(row=4, column=0, sticky=W)
#         textbranch = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textbranch.grid(row=4, column=1)
#
#         Buttonframe = Frame(self, bd=10, relief=RIDGE)
#         Buttonframe.place(x=5, y=440, width=950, height=50)
#
#         btnadddata = Button(Buttonframe, text="Add", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=0)
#
#         btnadddata = Button(Buttonframe, text="Delete", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=1)
#
#         btnadddata = Button(Buttonframe, text="Update", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=2)
#
#         btnadddata = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=4)
#
#         btnadddata = Button(Buttonframe, text="Back", font=("arial", 12, "bold"), width=18, bg="blue", fg="white",
#                             command=lambda: controller.show_frame(homepage))
#         btnadddata.grid(row=0, column=3)
#
#         Detailsframe = Frame(parent,bd=10, relief=RIDGE)
#         Detailsframe.place(x=20, y=500, width=1330, height=180)
#
#         yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
#
#         self.employee_table = ttk.Treeview(Detailsframe,
#                                            column=("Employee ID", "Employee Name", "Contact No", "Address", "Branch"))
#
#         self.employee_table.heading("Employee ID", text="Employee ID")
#         self.employee_table.heading("Employee Name", text="Employee Name")
#         self.employee_table.heading("Contact No", text="Contact No")
#         self.employee_table.heading("Address", text="Address")
#         self.employee_table.heading("Branch", text="Branch")
#         self.employee_table["show"] = "headings"
#         self.employee_table.pack(fill=BOTH, expand=1)
#
#
# class Product(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Product Details", fg="black", bg="white",
#                             font=("Courier", 50, "bold"))
#         lbltitle.pack(side=TOP)
#
#         Dataframe = Frame(self, bd=15, relief=RIDGE)
#         Dataframe.place(x=0, y=130, width=950, height=250)
#         DataframeCenter = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE,
#                                      font=("times new roman", 12, "bold"), text="Product Information")
#         DataframeCenter.place(x=10, y=5, width=900, height=200)
#
#         lblmember = Label(DataframeCenter, bg="powder blue", text="Product Name", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblmember.grid(row=0, column=0, sticky=W)
#         textmember = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textmember.grid(row=0, column=1)
#
#         lblid = Label(DataframeCenter, bg="powder blue", text="Product ID", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblid.grid(row=1, column=0, sticky=W)
#         textid = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textid.grid(row=1, column=1)
#
#         lblno = Label(DataframeCenter, bg="powder blue", text="Contact No", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblno.grid(row=2, column=0, sticky=W)
#         textno = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textno.grid(row=2, column=1)
#
#         lbladd = Label(DataframeCenter, bg="powder blue", text="Address", font=("times new roman", 15, "bold"), padx=2,
#                        pady=2)
#         lbladd.grid(row=3, column=0, sticky=W)
#         textadd = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textadd.grid(row=3, column=1)
#
#         lblbranch = Label(DataframeCenter, bg="powder blue", text="Product Branch", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblbranch.grid(row=4, column=0, sticky=W)
#         textbranch = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textbranch.grid(row=4, column=1)
#
#         Buttonframe = Frame(self, bd=10, relief=RIDGE)
#         Buttonframe.place(x=5, y=440, width=950, height=50)
#
#         btnadddata = Button(Buttonframe, text="Add", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=0)
#
#         btnadddata = Button(Buttonframe, text="Delete", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=1)
#
#         btnadddata = Button(Buttonframe, text="Update", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=2)
#
#         btnadddata = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=4)
#
#         btnadddata = Button(Buttonframe, text="Back", font=("arial", 12, "bold"), width=18, bg="blue", fg="white",
#                             command=lambda: controller.show_frame(homepage))
#         btnadddata.grid(row=0, column=3)
#
#         Detailsframe = Frame( bd=10, relief=RIDGE)
#         Detailsframe.place(x=20, y=500, width=1330, height=180)
#
#         yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
#
#         self.employee_table = ttk.Treeview(Detailsframe,
#                                            column=("Employee ID", "Employee Name", "Contact No", "Address", "Branch"))
#
#         self.employee_table.heading("Employee ID", text="Employee ID")
#         self.employee_table.heading("Employee Name", text="Employee Name")
#         self.employee_table.heading("Contact No", text="Contact No")
#         self.employee_table.heading("Address", text="Address")
#         self.employee_table.heading("Branch", text="Branch")
#         self.employee_table["show"] = "headings"
#         self.employee_table.pack(fill=BOTH, expand=1)
#
#
# class Order(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         lbltitle = tk.Label(self, bd=20, relief=RIDGE, text="Order Details", fg="black", bg="white",
#                             font=("Courier", 50, "bold"))
#         lbltitle.pack(side=TOP)
#
#         Dataframe = Frame(self, bd=15, relief=RIDGE)
#         Dataframe.place(x=0, y=130, width=950, height=250)
#         DataframeCenter = LabelFrame(Dataframe, bd=10, padx=10, relief=RIDGE,
#                                      font=("times new roman", 12, "bold"), text="Order Information")
#         DataframeCenter.place(x=10, y=5, width=900, height=200)
#
#         lblmember = Label(DataframeCenter, bg="powder blue", text="Order Name", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblmember.grid(row=0, column=0, sticky=W)
#         textmember = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textmember.grid(row=0, column=1)
#
#         lblid = Label(DataframeCenter, bg="powder blue", text="Order ID", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblid.grid(row=1, column=0, sticky=W)
#         textid = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textid.grid(row=1, column=1)
#
#         lblno = Label(DataframeCenter, bg="powder blue", text="Contact No", font=("times new roman", 15, "bold"),
#                       padx=2, pady=2)
#         lblno.grid(row=2, column=0, sticky=W)
#         textno = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textno.grid(row=2, column=1)
#
#         lbladd = Label(DataframeCenter, bg="powder blue", text="Address", font=("times new roman", 15, "bold"), padx=2,
#                        pady=2)
#         lbladd.grid(row=3, column=0, sticky=W)
#         textadd = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textadd.grid(row=3, column=1)
#
#         lblbranch = Label(DataframeCenter, bg="powder blue", text="Order Branch", font=("times new roman", 15, "bold"),
#                           padx=2, pady=2)
#         lblbranch.grid(row=4, column=0, sticky=W)
#         textbranch = Entry(DataframeCenter, font=("arial", 12, "bold"), width=27)
#         textbranch.grid(row=4, column=1)
#
#         Buttonframe = Frame(self, bd=10, relief=RIDGE)
#         Buttonframe.place(x=5, y=440, width=950, height=50)
#
#         btnadddata = Button(Buttonframe, text="Add", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=0)
#
#         btnadddata = Button(Buttonframe, text="Delete", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=1)
#
#         btnadddata = Button(Buttonframe, text="Update", font=("arial", 12, "bold"), width=18, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=2)
#
#         btnadddata = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"), width=17, bg="blue", fg="white")
#         btnadddata.grid(row=0, column=4)
#
#         btnadddata = Button(Buttonframe, text="Back", font=("arial", 12, "bold"), width=18, bg="blue", fg="white",
#                             command=lambda: controller.show_frame(homepage))
#         btnadddata.grid(row=0, column=3)
#
#         Detailsframe = Frame( bd=10, relief=RIDGE)
#         Detailsframe.place(x=20, y=500, width=1330, height=180)
#
#         yscroll = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
#
#         self.employee_table = ttk.Treeview(Detailsframe,
#                                            column=("Employee ID", "Employee Name", "Contact No", "Address", "Branch"))
#
#         self.employee_table.heading("Employee ID", text="Employee ID")
#         self.employee_table.heading("Employee Name", text="Employee Name")
#         self.employee_table.heading("Contact No", text="Contact No")
#         self.employee_table.heading("Address", text="Address")
#         self.employee_table.heading("Branch", text="Branch")
#         self.employee_table["show"] = "headings"
#         self.employee_table.pack(fill=BOTH, expand=1)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.frames = {}
        for F in (loginpage, homepage, firstpage, secondpage, thirdpage, fourthpage, fifthpage, Employee):
                  # Customer, Supplier, Product, Order):
            Frame = F(window, self)
            self.frames[F] = Frame
            Frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(loginpage)

    def show_frame(self, page):
        Frame = self.frames[page]
        Frame.tkraise()


app = Application()
app.title("Order Management System")
# root = Tk()
# app = ABC(master=root)
# app.master.title("Simple Prog")
app.mainloop()
# root = Tk()
# # ob= Order(root)




# root.mainloop()

