# Unit3-HasanMajdi
Unit 3 Project for Computer Science. 

OEd Items Inventory 
==========================
An applictaion to track and identify the items exsists or lent in the OUT DOOR EDUCATION Program (OEd) in UWC ISAK Japan. 

![Unit3-Inventory](Cover.png)

Contents
---------
  1. [Planning](#planning)
  2. [SolutionOverview](#SolutionOverview)
  3. [Development](#development)
  4. [Evaluation](#evaluation)
  5. [References](#References)
  
  Planning
----------
### Definition of the problem 
The client is the OUT DOOR EDUCATION program in UWC ISAK Japan, they have a list of equipment for hikes and out door trips, such as tents, rucksacks, sleeping bags, and sleeping mats. these items can be lend to hikers for OEd organized trips, but most of the time the OEd team can lost the items beause of the lack of a system that allows them to know to who the equipments were lent to. Therefore, the client is asking to develop a desktop application that allows the team to control their equipments in a more manageable way, that make finding the items easy and simple, and tracking what the items are and to whom they were lent to, provided with an email of the indivisual who has them, so they won't have to buy new equipments everytime they lose, and decrease their monthly budget, and be more Sustainable. 
**fig.1** 
![Unit3-Inventory](OEdEmail.png)
***An email from the client (OEd Team), cleary what they want in the inventory from features.***

### Solution proposed
The solution is to create an application where the client can have all the requirments done, the developer decided to use Python programming language as a tool to develop this application as it is an avaliable language that is free to use and has a lot of resources to learn from, also because the developler is learning it now and can get support at anytime, **python;** is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991. 
for designing the application, we will be working on Qt Desinger combined with Python **(Pyqt5)** as it is an easy and avaliable tool to design and well documented. The application will be a tool to make what the client requires happen, the program would allow the users to have a security system where all their data is secured and only accessible by specific members of the team, it will store make the process of tracking equipments easier for the OEd team and to know to whom the equipments were lent for. 


### Feasibility Study 

**TELOS** is an acronym in project management used to define five areas of feasibility that determine whether
a project should run or not. 

**T - Technical** - Is the project technically possible?

Yes, the project is possible in the tecnical part and the developers are able to create such a thing.
__________________________________________________________________________________________________________________________
**E - Economic -** Can the project be afforded? Will it increase profit?

The project is affordable for the developers and does not require a budget.
__________________________________________________________________________________________________________________________
**L - Legal -** Is the project legal?

The project is legal, and does not have any conflicts with laws/rules. 
__________________________________________________________________________________________________________________________
**O - Operational -** How will the current operations support the change?

The operations are welling to support the project and they asked for us to develop it. 
__________________________________________________________________________________________________________________________
**S - Scheduling -** Can the project be done in time?

Yes, the developer is able to handle the project on the time required. 
__________________________________________________________________________________________________________________________

### Success criteria 
1. System can track the equipments lent. 
2. Be able to determine whether the equipments in the storage or lent out. 
3. Be able to identify who is the person that the equipment lent to and provide an email. 
4. items can be removed or added.  
5. system has a search method to make it easier to find items. 
6. items are categorised. 
7. system is secured and only accessible by specific members.
8. Client should be satisfied about the application and have their requirments done.

Development 
------------

### Design; paper-prototype : 

One of the simplest ways to start designing an application/website is to paper prototype. which means sketching it on a paper and try to combine ideas and put them down, one of its features is that it is easy to edit, so if the client changes their mind about the elements, you can easily edit it. it helps having an idea about the work before you acctually step over and design it.

**Fig.1**![Unit3-Inventory](Proto.jpg)


**Fig.1** is showing the first design for the OEd inventory, it is showing the Login secure page. 


**Fig.2**![Unit3-Inventory](Proto2.jpg)


**Fig.2** is showing the mainpage for the inventory, here is where the user woill get the news about the inventory and about the items lent. 


### Design; Qt Designiner : 

**Qt Designer and GUI Applications "Pyqt5"**

![Unit3-Inventory](python.png)

*What is Qt designer?*

Qt Designer is the Qt tool for designing and building graphical user interfaces (GUIs) with Qt Widgets. it can compose and customize windows or dialogs in a what-you-see-is-what-you-get (WYSIWYG) manner, and test them using different styles and resolutions. 

**After creating the paper-prototype, the meeting and going through it with the clients, we now have to make the paper prototype and actual application (User Interface), and will be developing with Qt designer and Python.**


 
