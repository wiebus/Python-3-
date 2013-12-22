#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Programm : PyKicadSchematic-ID_Interchanger_RevC.py
# Python 3 Programm; Interchanger tool for Kicad schematic pages
# Autor: Dipl.-Ing. Bernd Wiebus
# Uedem den 06. March 2013
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
  
  
  stPfad = "" #Path to the actual schematic file. preset: empty
  iZeilenzahl = 0 # Counter for lines
  bSheetmarker = False
  bSheetnamemarker = False
  stZwischenspeicherPfad = ""
  #stSubsheetname =""
  iPosition1 = 0 
  stPosition1 = ""
  iPosition2 = 0 
  stPosition2 = ""
  iPosition3 = 0 
  stPosition3 = ""
  bErstePosition = False
  bZweitePosition = False
  iListlen = 0
  zaehler1 = 0
  liListline = ["", ""]
  liZwischenspeicher = [liListline]
  ililenZwischenspeicher = 0
  SemaphorGerman = False
  SemaphorEnglish = True
  stSubschematic1Leer = "Subschematic choosen: Empty"
  stSubschematic1insert = "Subschematic choosen:"
  stSubschematic2 = "insert before position "
  
  Programmname ="PyKicadSchematic-ID_Interchanger_RevB.py\n" #Defining.....
  Programmzweck ="Purpose: Interchanger tool for Kicad schematic pages.\n" #Defining.....
  Programmversion ="Version: Alpha Version \n"   #Defining.....
  Programmdatum ="from 06th March 2013 \n"  #Defining.....
  Pythonversion = "Written for Python 3.1. \n"   #Defining.....
  Programmautor ="Author: Bernd Wiebus alias DL1EIC \n"  #Defining.....
  ProgrammautorMail ="E-Mail: bernd.wiebus@gmx.de \n" #How to contact the author
  Programmlizenz ="GNU-GPL NO WARRANTY!\n"   #Defining.....

  stHelpLine1 ="With \u0022 Choose File wählen \u0022  open the schematic (*.sch).\n" #Defining.....
  stHelpLine2 ="The subsheets of the next hierarchical layer will bee shown.\n" #Defining.....
  stHelpLine3 ="if you want to interchange them:\n"   #Defining.....
  stHelpLine4 ="First: Choose the subschematick by a single click\n"  #Defining.....
  stHelpLine5 ="Second: Choose position, bevore this subschematic shall be moved.\n"   #Defining.....
  stHelpLine6 ="Third: Save with \u0022 Save \u0022\n"  #Defining.....
  stHelpLine7 ="It will be saved to \u0022 *Changed.sch\u0022 at the same folder like \u0022 *.sch \u0022.\n" #How to contact the author
  stHelpLine8 ="++++++++++++++++++++++++++++++++++++\n"   #Defining.....
  
  
  
  def __init__(self):
    pass


#Function LocaGerman : German localisation
def LocaGerman():
  File.SemaphorGerman = True
  File.SemaphorEnglish = False
  Pfadanzeige.configure(text = "Pfad: Leer")
  buttfunkt2.configure(text = "Wähle Kicad .sch Datei")
  buttfunkt4.configure(text = "Speichern")
  buEnd.configure(text = "Ende")
  buttonabout.configure(text = "Über")
  buttonhelp.configure(text = "Hilfe")
  File.stSubschematic1Leer = "Gewählter Unterschaltplan: Leer"
  File.stSubschematic1insert = "Gewählter Unterschaltplan: "
  File.stSubschematic2 = "einfügen vor Position "
  
  laSubschematic1.configure(text = File.stSubschematic1Leer)
  laSubschematic2.configure(text = File.stSubschematic2)
  
  File.Programmname ="PyKicadSchematic-ID_Interchanger_RevC.py\n" #Defining.....
  File.Programmzweck ="Zweck: Vertauschen der Reihenfolge von Kicad Unterschaltplänen.\n" #Defining.....
  File.Programmversion ="Version: Alpha Version \n"   #Defining.....
  File.Programmdatum ="vom 06. März 2013 \n"  #Defining.....
  File.Pythonversion = "Geschrieben für Python 3.1. \n"   #Defining.....
  File.Programmautor ="Autor: Bernd Wiebus alias DL1EIC \n"  #Defining.....
  File.ProgrammautorMail ="E-Mail: bernd.wiebus@gmx.de \n" #How to contact the author
  File.Programmlizenz ="GNU-GPL Keine Garantie!\n"   #Defining.....
  
  File.stHelpLine1 ="Mit \u0022 Datei wählen \u0022  den Schaltplan (*.sch) wählen.\n" #Defining.....
  File.stHelpLine2 ="Es werden die Subschaltpläne der hierarchischen Ebene darunter angezeigt.\n" #Defining.....
  File.stHelpLine3 ="Wenn einer verschoben werden soll:\n"   #Defining.....
  File.stHelpLine4 ="1. Subschaltplan Anklicken\n"  #Defining.....
  File.stHelpLine5 ="2. Die Position anklicken, vor die dieser Subschaltplan verschoben werden soll.\n"   #Defining.....
  File.stHelpLine6 ="3. \u0022 Save \u0022 wählen\n"  #Defining.....
  File.stHelpLine7 =" Es wird in \u0022 *Changed.sch\u0022 im gleichen Ordner wie \u0022 *.sch \u0022 gespeichert.\n" #How to contact the author
  File.stHelpLine8 ="++++++++++++++++++++++++++++++++++++\n"   #Defining.....
  
  
#Function LocaBritish : British localisation
def LocaBritish():
  File.SemaphorGerman = False
  File.SemaphorEnglish = True
  Pfadanzeige.configure(text = "Path: Empty")  
  buttfunkt2.configure(text = "Choose Kicad .sch file")
  buttfunkt4.configure(text = "SAVE") 
  buEnd.configure(text = "End")
  buttonabout.configure(text = "About")
  buttonhelp.configure(text = "help")
  File.stSubschematic1Leer = "Subschematic choosen: Empty"
  File.stSubschematic1insert = "Subschematic choosen: "
  File.stSubschematic2 = "insert before position "
  
  laSubschematic1.configure(text = File.stSubschematic1Leer)
  laSubschematic2.configure(text = File.stSubschematic2)
  
  File.Programmname ="PyKicadSchematic-ID_Interchanger_RevC.py\n" #Defining.....
  File.Programmzweck ="Purpose: Interchanger tool for Kicad schematic pages.\n" #Defining.....
  File.Programmversion ="Version: Alpha Version \n"   #Defining.....
  File.Programmdatum ="from 06 March 2013 \n"  #Defining.....
  File.Pythonversion = "Written for Python 3.1. \n"   #Defining.....
  File.Programmautor ="Author: Bernd Wiebus alias DL1EIC \n"  #Defining.....
  File.ProgrammautorMail ="E-Mail: bernd.wiebus@gmx.de \n" #How to contact the author
  File.Programmlizenz ="GNU-GPL NO WARRANTY!\n"   #Defining.....

  File.stHelpLine1 ="With \u0022 Choose File wählen \u0022  open the schematic (*.sch).\n" #Defining.....
  File.stHelpLine2 ="The subsheets of the next hierarchical layer will bee shown.\n" #Defining.....
  File.stHelpLine3 ="if you want to interchange them:\n"   #Defining.....
  File.stHelpLine4 ="First: Choose the subschematick by a single click\n"  #Defining.....
  File.stHelpLine5 ="Second: Choose position, bevore this subschematic shall be moved.\n"   #Defining.....
  File.stHelpLine6 ="Third: Save with \u0022 Save \u0022\n"  #Defining.....
  File.stHelpLine7 ="It will be saved to \u0022 *Changed.sch\u0022 at the same folder like \u0022 *.sch \u0022.\n" #How to contact the author
  File.stHelpLine8 ="++++++++++++++++++++++++++++++++++++\n"   #Defining.....
  
  
  
  
# Funktion Button Ende
def end():
  Mainwindow.destroy()
  
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
  Aboutwindow.title ("PyKicadSchematic-ID_Interchanger_RevC.py")
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
  
def help():
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

def ReihenfolgeChanged(dummy):
  File.iPosition3 = File.iListlen - 1
  File.stPosition3 = SubsheetAnzeige1.get(END)
     
  if File.bErstePosition == False:
    File.iPosition2 = 0
    File.stPosition2 = ""
    tupel = SubsheetAnzeige1.curselection()
    File.iPosition1 = int(tupel[0])
    File.stPosition1 = SubsheetAnzeige1.get(SubsheetAnzeige1.curselection())
    File.bErstePosition = True
    laSubschematic1.configure(text = File.stSubschematic1insert + File.stPosition1)
    laSubschematic2.configure(text = "")
    return()
  if File.bErstePosition == True:
    tupel = SubsheetAnzeige1.curselection()
    File.iPosition2 = int(tupel[0])
    File.stPosition2 = SubsheetAnzeige1.get(SubsheetAnzeige1.curselection())
    File.bErstePosition = False
    File.bZweitePosition =True
    laSubschematic2.configure(text = File.stSubschematic2 + str(File.iPosition2))
    if File.iPosition1 == File.iPosition2:
      return()
    if File.iPosition1 != File.iPosition2:
      if File.iPosition1 > File.iPosition2:
        if File.iPosition2 == 0:
          File.iPosition3 = 0
          File.stPosition3 = SubsheetAnzeige1.get(0)
          SubsheetAnzeige1.delete(0)
          SubsheetAnzeige1.insert(File.iPosition2, File.stPosition1)
          SubsheetAnzeige1.insert(1, File.stPosition3)
          SubsheetAnzeige1.delete(File.iPosition1 +1)
          return()
        else:
          SubsheetAnzeige1.insert(File.iPosition2, File.stPosition1)
          SubsheetAnzeige1.delete(File.iPosition1 +1)
          return()
      if File.iPosition1 < File.iPosition2:
        SubsheetAnzeige1.insert(File.iPosition2, File.stPosition1)
        SubsheetAnzeige1.delete(File.iPosition1) 
        return()
        
      
    
    
  
def Dateiwahl():
  """
  The subprogram "Dateiwahl()" is for choose an existing log file, read it into the list
  and continue this log.
  """
  global name
  File.iListlen = 0
  File.ililenZwischenspeicher = len(File.liZwischenspeicher)
  for iIndex in range(0, File.ililenZwischenspeicher -1, 1): #Clear the old list
      del File.liZwischenspeicher[0]
  name = askopenfilename(filetypes=[("Kicad-Schematics", ".sch"),("All files", "*")])
  if name: #Nur Wahr, wenn Pfad gewählt wurde. Sonst Leerstring/Tupel
    File.stPfad = name
    File.iZeilenzahl = 0
    stSZeile =""
    stUZeile =""
    stLesestring = ""
    stSubsheetname =""
    stBuchstabe = ""
    Pfad = ("Pfad: " + name)
    Pfadanzeige["text"] = Pfad
    SubsheetAnzeige1.delete(0, END) #Neue Datei, altes Listing...Clear 
    laSubschematic1.configure(text = File.stSubschematic1Leer) #Neue Datei, altes Daten...Clear 
    laSubschematic2.configure(text = "") #Neue Datei, altes Daten...Clear
    SchematicFile = open(File.stPfad, mode="rt")
    while True:
      Lesezeile = SchematicFile.readline()
      File.iZeilenzahl = File.iZeilenzahl +1
      if len(Lesezeile) ==0:
        break # EOF wenn lesezeile nicht mehr kommt.
      if Lesezeile.startswith("$Sheet"):
        File.bSheetmarker = True
      if Lesezeile.startswith("$EndSheet"):
        File.bSheetmarker = False
      if File.bSheetmarker == True:
        if Lesezeile.startswith("S"):
          stSZeile = Lesezeile
        if Lesezeile.startswith("U"):
          stUZeile = Lesezeile
        if Lesezeile.startswith("F0"):
          stLesestring = Lesezeile
          stLesestring = stLesestring[2:]
          while not stLesestring .startswith("\u0022"): # unicode für "
            stLesestring = stLesestring[1:]
          if stLesestring .startswith("\u0022"): # unicode für "
            stSubsheetname =""
            stLesestring = stLesestring[1:] 
            while not stLesestring .startswith("\u0022"): # unicode für "
              stBuchstabe = stLesestring[:1]
              stLesestring = stLesestring[1:]
              stSubsheetname = stSubsheetname + stBuchstabe
          SubsheetAnzeige1.insert(END, stSubsheetname) #Neues Listimng
          SubsheetAnzeige1.yview(END) #Anzeige zum Ende 
          File.iListlen = File.iListlen + 1
          File.liListline = [stSubsheetname, "$Sheet\n"]
          File.liZwischenspeicher.append(File.liListline[:])
          File.liListline = [stSubsheetname, stSZeile]
          File.liZwischenspeicher.append(File.liListline[:])
          File.liListline = [stSubsheetname, stUZeile]
          File.liZwischenspeicher.append(File.liListline[:])
          File.bSheetnamemarker = True
      if File.bSheetnamemarker == True:
        if not Lesezeile.startswith("$Sheet"):
          File.liListline = [stSubsheetname, Lesezeile]
          File.liZwischenspeicher.append(File.liListline[:])
      if File.bSheetmarker == False:
        if File.bSheetnamemarker == True:
          File.bSheetnamemarker = False
         
          
    
    SchematicFile.close()
  return()

   
        
  

# Function save
def Save():
    global name
    File.zaehler1 = 0
    File.bSheetmarker == False
    name = File.stPfad[:-4] + "Changed.sch"
    if name: #Nur Wahr, wenn Pfad gewählt wurde. Sonst Leerstring/Tupel
      stActPfad = ("Path: " + name) # Only local
      Pfadanzeige["text"] = stActPfad # Only local
      SchematicFile = open(File.stPfad, mode="rt")
      SaveFile = open(name, mode="w")
      while True:
        Lesezeile = SchematicFile.readline()
        if len(Lesezeile) ==0:
            break # EOF wenn lesezeile nicht mehr kommt.
        if Lesezeile.startswith("$Sheet"):
          File.bSheetmarker = True
          stSubsheetname = SubsheetAnzeige1.get(File.zaehler1)
          File.ililenZwischenspeicher = len(File.liZwischenspeicher)
          for iIndex in range(0, File.ililenZwischenspeicher, 1): #read list
            Listeneintrag = File.liZwischenspeicher[iIndex]
            stSubsheetnameRead = Listeneintrag[0]
            if stSubsheetnameRead == stSubsheetname:
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

# Mainwindowloop

Mainwindow = tk.Tk()
Mainwindow.title ("PyKicadSchematic-ID_Interchanger_RevC.py")
Mainwindow.protocol("WM_DELETE_WINDOW", end) # call end() when closing window

name = ""
IconBritish = """R0lGODlhJAAYAIQRAFIR+PgREewbItkwRNQyRtUzR+UwP+YxP9w+UOc/TdtCVOdGVOdHVOdHVelU
YP3n6ezw9////////////////////////////////////////////////////////////ywAAAAA
JAAYAAAFvmAQPE8UAWiKmo4jmqpqivRYnvEatS+ezzRg7xdhMIYxoGkZqcGSxWPgKWtOlzqnD2Bq
NJDCK1Fb9YKtyFxWzI0gEAIBs0dVr5+md3x+reuYgIAFBXSBhoeHg4WISwMDNZCRkpMijo6UmJmV
j5qdnp+gfYxLBASLo6hMpaeMdkpLCgpnaXYpryaxs2yuS2cLCwcHda+8xG2/wcNWfm1ktlEGBswQ
ELRhykbR09Vs11s6LQkJzHe9Qd9t4ePo5SEAOw=="""
IconDeutsch = """R0lGODlhJAAYAKEDAAAAAPgREfj2Ef///yH5BAEKAAMALAAAAAAkABgAAAI0hI+py+0Po5y02ouz
3jD4D4biSJbmiabqyrbuC8fyjAr2jef6zvf+DwwKh8Si8YhMKpfAAgA7"""



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

#Pfadanzeige
Pfadanzeige = tk.Label(Rahmen1, text = "Path: Empty", background = "#408000",foreground = "#FFFF5F")
Pfadanzeige.pack(side = LEFT, fill = X)

# Button choose log file
buttfunkt2 = tk.Button(Rahmen2, text = "Choose Kicad .sch file", background = "#304000", foreground = "#FFFF5F", command = Dateiwahl)
buttfunkt2.pack(side = LEFT)

# Button save
buttfunkt4 = tk.Button(Rahmen2, text = "SAVE", background = "#304000", foreground = "#FFFF5F", command = Save)
buttfunkt4.pack(side = LEFT)

# Button End
buEnd = tk.Button(Rahmen2, text = "End", background = "#304000", foreground = "#FFFF5F", command = end)
buEnd.pack(side = RIGHT)

# Button About
buttonabout = tk.Button(Rahmen2, text = "About", background = "#304000", foreground = "#FFFF5F", command = about)
buttonabout.pack(side = RIGHT)

# Button Hilfe
buttonhelp = tk.Button(Rahmen2, text = "help", background = "#304000", foreground = "#FFFF5F", command = help)
buttonhelp.pack(side = RIGHT)

#Subschematic choosen
laSubschematic1 = tk.Label(Rahmen3, text = File.stSubschematic1Leer, background = "#304000",foreground = "#FFFF5F")
laSubschematic1.pack(side = LEFT, fill = X)

#Subschematic insert
laSubschematic2 = tk.Label(Rahmen3, text = "", background = "#304000",foreground = "#FFFF5F")
laSubschematic2.pack(side = LEFT, fill = X)

# Listbox für Subsheets
# Auch wenn der Scrollbar dem Textfeld zugeordnet ist,
# so wird er doch in das übergeordnete Fenster eingebaut!
scrollbarx = Scrollbar(Rahmen4, orient=HORIZONTAL) 
scrollbarx.pack(side= BOTTOM, fill=X)
scrollbary = Scrollbar(Rahmen4) 
scrollbary.pack(side= RIGHT, fill=Y)
SubsheetAnzeige1 = tk.Listbox(Rahmen4, width = 100, height = 10, background = "#408000",foreground = "#FFFF5F")
SubsheetAnzeige1.pack(side= LEFT)

SubsheetAnzeige1.config(yscrollcommand=scrollbary.set)
scrollbary.config(command=SubsheetAnzeige1.yview)
SubsheetAnzeige1.config(xscrollcommand=scrollbarx.set)
scrollbarx.config(command=SubsheetAnzeige1.xview)
SubsheetAnzeige1.bind("<<ListboxSelect>>", ReihenfolgeChanged)

# Button Deutsch
IconImageDeutsch=tk.PhotoImage(master = Mainwindow, data=IconDeutsch)
buttonDeutsch = tk.Button(Rahmen5, image = IconImageDeutsch, background = "#304000", foreground = "#FFFF5F", command = LocaGerman)
buttonDeutsch.image = IconImageDeutsch
buttonDeutsch.pack(side = RIGHT)

# Button British
IconImageBritish=tk.PhotoImage(master = Mainwindow, data=IconBritish)
buttonBritish = tk.Button(Rahmen5, image = IconImageBritish, background = "#304000", foreground = "#FFFF5F", command = LocaBritish)
buttonBritish.image = IconImageBritish
buttonBritish.pack(side = RIGHT)

# Infinite mainlloop
Mainwindow.mainloop()
