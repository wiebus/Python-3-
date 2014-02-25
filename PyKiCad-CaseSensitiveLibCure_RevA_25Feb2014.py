#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Programm : KiCad-CaseSensitiveLibCure_RevA_25Feb_2014.py
# Python 3 Programm; Tool for converting KiCad schematic from non case sensitive into case sensitive.
# Autor: Dipl.-Ing. Bernd Wiebus
# Uedem den 25. February 2014
# GNU-GPL

import tkinter as tk
from tkinter.filedialog import *
#from time import gmtime, strftime
#import datetime
import sys

class File(object):
  """
  Defining an objekt which contains all information about the used files and variables. 
  """
  
  
  stPath = "" #Path to the actual schematic file. preset: empty
  iZeilenzahl = 0 # Counter for lines
  bSheetmarker = False
  bSheetnamemarker = False
  stZwischenspeicherPath = ""
  #stSubsheetname =""
  iPosition1 = 0 
  stPosition1 = ""
  iPosition2 = 0 
  stPosition2 = ""
  iPosition3 = 0 
  iComponentCounter = 0 # Number of of components found in librarys
  stPosition3 = ""
  bErstePosition = False
  bZweitePosition = False
  iListlen = 0
  iLibListlen = 0
  zaehler1 = 0
  liListline = ["", ""]
  liZwischenspeicher = [liListline]
  liLibraryList = [liListline] # List of Librarys
  liComponentsInLibrary = [liListline] # List of components found in librarys
  ililenZwischenspeicher = 0
  iLiLenLibrary = 0
  SemaphorGerman = False
  SemaphorEnglish = True
  stSchematic1Leer = "Schematic choosen: Empty"
  stSchematic1insert = "Schematic choosen:"
  #stSchematic2 = "insert before position "
  
  
  Programmname ="PyKicad-CaseSensitiveLibCure_RevA_25Feb2014.py\n" #Defining.....
  Programmzweck ="Purpose: Converts old KiCad schematic files with pure upper case component names.\n" #Defining.....
  Programmversion ="Version: Alpha Version \n"   #Defining.....
  Programmdatum ="from 25th February 2014 \n"  #Defining.....
  Pythonversion = "Written for Python 3.1. \n"   #Defining.....
  Programmautor ="Author: Bernd Wiebus alias DL1EIC \n"  #Defining.....
  ProgrammautorMail ="E-Mail: bernd.wiebus@gmx.de \n" #How to contact the author
  Programmlizenz ="GNU-GPL NO WARRANTY!\n"   #Defining.....
  
  stHelpLine1 ="With \u0022 Choose File \u0022  you chose a schematic (*.sch) file you want to convert.\n" #Defining.....
  stHelpLine2 ="With \u0022 Choose Kicad Library  \u0022  you choose one or more library (.lib) files.\n" #Defining.....
  stHelpLine3 ="If you want to convert:\n"   #Defining.....
  stHelpLine4 ="Press Button \u0022 Convert \u0022. \n"  #Defining.....
  stHelpLine5 ="The converted file gets the suffix \u0022 -UpConverted.sch \u0022.\n"   #Defining.....
  stHelpLine6 ="Known problems: subschematics have to be converted by there own.\n"  #Defining.....
  stHelpLine7 ="Symbols starting with \u0022 ~ \u0022 will not be recognized.\n" #HDefining.......
  stHelpLine8 ="Do not forget to rename the files manually for proper working subschematics!\n"   #Defining...
  stHelpLine9 ="If you encounter problems: Please contact the author at:\n"   #Defining...
  stHelpLine10 ="bernd.wiebus@gmx.de\n"   #Defining...
  stHelpLine11 ="++++++++++++++++++++++++++++++++++++\n"   #Defining.....
  
  
  
  def __init__(self):
    pass

def about():
  """
  The subprogramm "about()" shows general info about the programm, 
  its purpose and the author.
  """
  if File.SemaphorEnglish == True:
    stButtonclipboard = "Copy info into clipboard"
  if File.SemaphorGerman == True:
    stButtonclipboard = "Kopiere Info in Zwischenablage"
  
  #Funktion close Aboutwindow
  def aboutok():
    """
    the subprogramm "aboutok()" is a subprogramm of the subprogramm "about()".
    Its funktion is just to close the window, which was opened by "about()".
    """
    
    Aboutwindow.destroy()
        
  def clipboardfill(): # copies the about text to the clipboard
    Aboutwindow.clipboard_clear() #First: clear clipboard!
    Aboutwindow.clipboard_append(Programmabout) #second: Write value to clipboard!
   
  
  Programmabout = File.Programmname + File.Programmzweck + File.Programmversion + File.Programmdatum + File.Pythonversion + File.Programmautor + File.ProgrammautorMail + File.Programmlizenz #And now putting all strings together.
  Aboutwindow = tk.Tk() #create Window
  Aboutwindow.title ("PyKicad-CaseSensitiveLibCure_RevA_25Feb2014.py --ABOUT--")
  Aboutanzeige = tk.Label(Aboutwindow, text = Programmabout, background = "#002040",foreground = "#FFFF5F")
  Aboutanzeige.pack(side = TOP, fill = X)
  # Rahmen für Aboutfenster OK Button
  AboutRahmen1 = Frame(Aboutwindow, background = "#002040")
  AboutRahmen1.pack(side = TOP, fill = X)
  # Button Aboutok
  buttonaboutok = tk.Button(AboutRahmen1, text = "OK", background = "#304000",  foreground = "#FFFF5F", command = aboutok) #closing about window
  buttonaboutok.pack(side = TOP)
  buttonclipboard = tk.Button(AboutRahmen1, text = stButtonclipboard, background = "#304000",  foreground = "#FFFF5F", command = clipboardfill) #copying the abouttext to clibboard.
  buttonclipboard.pack(side = TOP)
  
  
def helptext():
  """
  The subprogramm "help()" shows a help text.
  """
  if File.SemaphorEnglish == True:
    stButtonclipboard = "Copy info into clipboard"
  if File.SemaphorGerman == True:
    stButtonclipboard = "Kopiere Info in Zwischenablage"

  #Funktion close Aboutwindow
  def helpclose():
    """
    the subprogramm "helpclose()" is a subprogramm of the subprogramm "help()".
    Its funktion is just to close the window, which was opened by "help()".
    """
    
    Helpwindow.destroy()
        
  def clipboardfillhelp(): # copies the help text to the clipboard
    Helpwindow.clipboard_clear() #First: clear clipboard!
    Helpwindow.clipboard_append(stHelptext) #second: Write value to clipboard!
  stHelptext = File.stHelpLine1 + File.stHelpLine2 + File.stHelpLine3 + File.stHelpLine4 + File.stHelpLine5 + File.stHelpLine6 + File.stHelpLine7 + File.stHelpLine8 #And now putting all strings together.
  stHelptext = stHelptext + File.stHelpLine9 + File.stHelpLine10 + File.stHelpLine11
  Helpwindow = tk.Tk() #create Window
  Helpwindow.title ("Help")
  Helpanzeige = tk.Label(Helpwindow, text = stHelptext, background = "#002040",foreground = "#FFFF5F")
  Helpanzeige.pack(side = TOP, fill = X)
  # Rahmen für helpfenster OK Button
  HelpRahmen1 = Frame(Helpwindow, background = "#002040")
  HelpRahmen1.pack(side = TOP, fill = X)
  # Button helpok
  buttonhelpok = tk.Button(HelpRahmen1, text = "OK", background = "#304000",  foreground = "#FFFF5F", command = helpclose) #closing about window
  buttonhelpok.pack(side = TOP)
  buttonclipboard = tk.Button(HelpRahmen1, text = stButtonclipboard, background = "#304000",  foreground = "#FFFF5F", command = clipboardfillhelp) #copying the abouttext to clibboard.
  buttonclipboard.pack(side = TOP)
  
def ChooseSchematicFile():
  """
  The subprogram "ChooseSchematicFile()" is for choose an existing schematic file.
  """
  global name
  name = ""
  File.iListlen = 0
  File.ililenZwischenspeicher = len(File.liZwischenspeicher)
  for iIndex in range(0, File.ililenZwischenspeicher -1, 1): #Clear the old list
      del File.liZwischenspeicher[0]
  name = askopenfilename(filetypes=[("Kicad-Schematics", ".sch"),("All files", "*")])
  if name: #Nur Wahr, wenn Pfad gewählt wurde. Sonst Leerstring/Tupel
    File.stPath = name
  Pathanzeige["text"] = File.stPath 
  
  return()
  
  
def ChooseLibraryFile():
  """
  The subprogram "ChooseLibraryFile()" is for choose existing library files and read it.
  """
  global name
  File.iLibListlen = 0
  File.iComponentCounter = 0
  File.iLiLenLibrary  = len(File.liLibraryList)
  for iIndex in range(0, File.iLibListlen -1, 1): #Clear the old list
      del File.liLibraryList[0]
  name = askopenfilenames(filetypes=[("Kicad-Libraries", ".lib"),("All files", "*")])
  if name: #Nur Wahr, wenn Pfad gewählt wurde. Sonst Leerstring/Tupel
    File.liLibraryList = name
    File.iLibListlen = len(File.liLibraryList)
    #print("LibListe: ", File.liLibraryList)
    LibraryList.delete(0, END) #Neues Listimng
    for iIndex in range(0, File.iLibListlen, 1):
      stLibName = File.liLibraryList[iIndex]
      LibraryList.insert(END, stLibName) #Neues Listimng
      LibraryList.yview(END) #Anzeige zum Ende 
      ReadFile = open(stLibName, mode="rt")
      while True:
        Lesezeile = ReadFile.readline()
        #print("Lesezeile: ", Lesezeile)
        File.iZeilenzahl = File.iZeilenzahl +1
        if len(Lesezeile) ==0:
          break # EOF wenn lesezeile nicht mehr kommt.
        stComponentName = ""
        stComponentNameUpper = ""
        tuComponentName = ("","")
        if Lesezeile.startswith("DEF "):
          stWorkline = Lesezeile
          #print("stWorkline Pos1: ", stWorkline)
          stWorkline = stWorkline[4:]
          while not stWorkline.startswith(" "):
            stComponentName = stComponentName + stWorkline[:1]
            stWorkline = stWorkline[1:]
          #print("ComponentName: ", "-" + stComponentName + "-")
          stComponentNameUpper = stComponentName.upper()
          tuComponentName = (stComponentNameUpper, stComponentName)
          File.liComponentsInLibrary.append(tuComponentName)
      ReadFile.close()
          
  #print("component Liste: ", File.liComponentsInLibrary)
  return()

# Function Convert
def Convert():
  if File.stPath == "":
    return()
  stWritepath = File.stPath[:-4] + "-UpConverted.sch"
  #print("Schreibpfaad: ", stWritepath)
  boComponentFlag = False
  ReadFile = open(File.stPath, mode="rt")
  WriteFile = open(stWritepath, mode="w")
  while True:
    Lesezeile = ReadFile.readline()
    if len(Lesezeile) ==0:
      break # EOF wenn lesezeile nicht mehr kommt.
    stWriteLine = Lesezeile
    if Lesezeile.startswith("$Comp"):
      boComponentFlag = True
    if Lesezeile.startswith("$EndComp"):
      boComponentFlag = False
    iWorkline = len(Lesezeile)
    iWorkcounter = 0
    if Lesezeile.startswith("L ") and boComponentFlag == True:
      stWorkline = Lesezeile
      #print("stWorkline Pos1: ", stWorkline)
      stWorkline = stWorkline[2:]
      iWorkcounter = 2
      stComponentNameSchematic = ""
      while not stWorkline.startswith(" "):
        stComponentNameSchematic = stComponentNameSchematic + stWorkline[:1]
        iWorkcounter = iWorkcounter + 1
        stWorkline = stWorkline[1:]
      iComponentListLen = len(File.liComponentsInLibrary)
      for iIndex in range(0, iComponentListLen, 1):
        tuComponent = File.liComponentsInLibrary[iIndex]
        #print("tupel0: ", tuComponent[0])
        #print("tupel1: ", tuComponent[1])
        if stComponentNameSchematic == tuComponent[0]:
          stComponentNameSchematic = tuComponent[1]
      stWriteLine = "L " + stComponentNameSchematic
      iLenWorkLine = len(stWorkline)
      for iIndex in range(0, iLenWorkLine):
        stWriteLine = stWriteLine + stWorkline[:1]
        stWorkline = stWorkline[1:]
      #print("Zeile: ", stWriteLine)
    WriteFile.write(stWriteLine)
  ReadFile.close()
  WriteFile.close()
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# Function save
def Save():
    global name
    File.zaehler1 = 0
    File.bSheetmarker == False
    name = File.stPath[:-4] + "Changed.sch"
    if name: #Nur Wahr, wenn Pfad gewählt wurde. Sonst Leerstring/Tupel
      stActPath = ("Path: " + name) # Only local
      Pathanzeige["text"] = stActPath # Only local
      SchematicFile = open(File.stPath, mode="rt")
      SaveFile = open(name, mode="w")
      while True:
        Lesezeile = SchematicFile.readline()
        if len(Lesezeile) ==0:
            break # EOF wenn lesezeile nicht mehr kommt.
        if Lesezeile.startswith("$Sheet"):
          File.bSheetmarker = True
          stSheetname = LibraryList.get(File.zaehler1)
          File.ililenZwischenspeicher = len(File.liZwischenspeicher)
          for iIndex in range(0, File.ililenZwischenspeicher, 1): #read list
            Listeneintrag = File.liZwischenspeicher[iIndex]
            stSheetnameRead = Listeneintrag[0]
            if stSheetnameRead == stSheetname:
              Lesezeile2 = Listeneintrag[1]
              SaveFile.write(Lesezeile2)
          File.zaehler1 = File.zaehler1 + 1
        if Lesezeile.startswith("$EndSheet"):
          File.bSheetmarker = False
        if File.bSheetmarker == False:
          if not Lesezeile.startswith("$EndSheet"):
            SaveFile.write(Lesezeile)
      SaveFile.close()
      SchematicFile.close()
        
   # newfile()

   # Funktion Button Ende
def end():
  Mainwindow.destroy()
   
# Mainwindowloop

Mainwindow = tk.Tk()
Mainwindow.title ("PyKicadSchematic-ID_Interchanger_RevC.py")
Mainwindow.protocol("WM_DELETE_WINDOW", end) # call end() when closing window

name = ""



# Rahmen1 
Rahmen1 = Frame(Mainwindow, background = "#002040")
Rahmen1.pack(side = TOP, fill = X)

#Rahmen2
Rahmen2 = Frame(Mainwindow, background = "#002040")
Rahmen2.pack(side = TOP, fill = X)

#Rahmen3
Rahmen3 = Frame (Mainwindow, background = "#002040")
Rahmen3.pack(side = TOP, fill = X)

#Rahmen4
Rahmen4 = Frame (Mainwindow, background = "#002040")
Rahmen4.pack(side = TOP, fill = X)

#Rahmen5
Rahmen5 = Frame (Mainwindow, background = "#002040")
Rahmen5.pack(side = TOP, fill = X)



# Button choose log file
buttfunkt2 = tk.Button(Rahmen1, text = "Choose Kicad .sch file", background = "#304000", foreground = "#FFFF5F", command = ChooseSchematicFile)
buttfunkt2.pack(side = LEFT)

# Button End
buEnd = tk.Button(Rahmen1, text = "End", background = "#304000", foreground = "#FFFF5F", command = end)
buEnd.pack(side = RIGHT)

# Button About
buttonabout = tk.Button(Rahmen1, text = "About", background = "#304000", foreground = "#FFFF5F", command = about)
buttonabout.pack(side = RIGHT)

# Button help
buttonhelp = tk.Button(Rahmen1, text = "help", background = "#304000", foreground = "#FFFF5F", command = helptext)
buttonhelp.pack(side = RIGHT)

#Pfadanzeige
Pathanzeige = tk.Label(Rahmen2, text = "Path: Empty", background = "#408000",foreground = "#FFFF5F")
Pathanzeige.pack(side = LEFT, fill = X)

#Choose libraries
buLibraryChoose = tk.Button(Rahmen3, text = "Choose Kicad Library .sch file", background = "#304000",foreground = "#FFFF5F", command = ChooseLibraryFile)
buLibraryChoose.pack(side = LEFT, fill = X)


# Listbox for Schematic
# Auch wenn der Scrollbar dem Textfeld zugeordnet ist,
# so wird er doch in das übergeordnete Fenster eingebaut!
scrollbarx = Scrollbar(Rahmen4, orient=HORIZONTAL) 
scrollbarx.pack(side= BOTTOM, fill=X)
scrollbary = Scrollbar(Rahmen4) 
scrollbary.pack(side= RIGHT, fill=Y)
LibraryList = tk.Listbox(Rahmen4, width = 100, height = 10, background = "#408000",foreground = "#FFFF5F")
LibraryList.pack(side= LEFT)

LibraryList.config(yscrollcommand=scrollbary.set)
scrollbary.config(command=LibraryList.yview)
LibraryList.config(xscrollcommand=scrollbarx.set)
scrollbarx.config(command=LibraryList.xview)
LibraryList.bind("<<ListboxSelect>>", end)

# Button Convert
buttfunkt4 = tk.Button(Rahmen1, text = "Convert", background = "#304000", foreground = "#FFFF5F", command = Convert)
buttfunkt4.pack(side = LEFT)

# Infinite mainlloop
Mainwindow.mainloop()
