# ---------------------------
#   Import Libraries
# ---------------------------
import os
import sys
import json
import codecs
import clr

# ---------------------------------------
# [Required]	Script Information
# ---------------------------------------
ScriptName = "Sim Commander"
Website = "twitch.tv/therustytigger"
Description = "Sims 4 Chat Control Bot"
Creator = "TheRustyTigger"
Version = "0.3"


# ---------------------------------------
#   Version Information
# ---------------------------------------
# Version:
# > 0.0.0.5 <
# Rewrote project from ground up following boilerplate examples,
# Began combining the various triggers into one script

# Version:
# > 0.0.1 <
# Began porting previous project into new project


# ---------------------------
#   Define Global Variables
# ---------------------------
global settings



# ---------------------------
#   [Required] Initialize Data (Only called on load)
# ---------------------------
def Init():
    # Get the path to the settings file
    settings_file = os.path.join(os.path.dirname(__file__), "settings.json")

    # Load the settings from the file
    with codecs.open(settings_file, encoding='utf-8-sig', mode='r') as file:
        global settings
        settings = json.load(file)
    return


# ---------------------------
#   [Required] Execute Data / Process messages
# ---------------------------
def Execute(data):
    find_command = settings["findcommand"]
    next_command = settings["nextcommand"]
    simone_command = settings["simonecommand"]
    simtwo_command = settings["simtwocommand"]
    simthree_command = settings["simthreecommand"]
    # simfour_command = settings["simfourcommand"]
    # simfive_command = settings["simfivecommand"]
    # simsix_command = settings["simsixcommand"]
    # simseven_command = settings["simsevencommand"]
    # simeight_command = settings["simeightcommand"]
    find_response = settings["findresponse"]
    next_response = settings["nextresponse"]
    simone_response = settings["simoneresponse"]
    simtwo_response = settings["simtworesponse"]
    simthree_response = settings["simthreeresponse"]
    username = data.UserName


    if data.GetParam(0) == "!sims" and data.GetParam(1) == find_command:
        response = username + ", " + find_response
        send_message(response)
        Parent.AddCooldown(ScriptName, find_command, settings["user_cd"])
        Parent.AddUserCooldown(ScriptName, find_command, data.User, settings["global_cd"])
        return

    if data.GetParam(0) == "!sims" and data.GetParam(1) == next_command:
        response = username + ", " + next_response
        send_message(response)
        return

    if data.GetParam(0) == "!sims" and data.GetParam(1) == simone_command:
        response = username + ", " + simone_response
        send_message(response)
        return

    if data.GetParam(0) == "!sims" and data.GetParam(1) == simtwo_command:
        response = username + ", " + simtwo_response
        send_message(response)
        return

    if data.GetParam(0) == "!sims" and data.GetParam(1) == simthree_command:
        response = username + ", " + simthree_response
        send_message(response)
        return

# ---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
# ---------------------------
def Tick():
    return


# ___________________________
#   MESSAGE HANDLING
# ___________________________
def send_message(message):
    Parent.SendStreamMessage(message)
    return


# ---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters)
# ---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter", "I am a cat!")

    return parseString


# ---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
# ---------------------------
# def ReloadSettings(jsonData):
#     # Execute json reloading here
#     settings.__dict__ = json.loads(jsonData)
#     settings.Save(SettingsFile)
#     return


# ---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
# ---------------------------
def Unload():
    return


# ---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
# ---------------------------
def ScriptToggled(state):
    return
# ___________________________________________________________________________________________________
# ______________________PREVIOUS CODE________________________________________________________________
# MainLogicScript__________________________________________________
#
# def Execute(data):
#     # get the command users name
#     username = data.UserName
#     command = data.GetParam(1)
#
#
# # HERE WE ARE DIVIDING UP THE COMMANDS FOR THE BOT TO MAKE AHK FILES
#
#     # !SIMS TRIGGERS THE BOT, THEN IT LOOKS FOR INFORMATION IN THE COMMAND
#     if data.GetParam(0).lower() != "!sims":
#         return
#
# # send stream message alert trigger
#     send_message("DEBUG PROCESS 1: " + username + " Triggered the script")
#
# # create the file for AHK to see in c:\simscript or wherever you put it
#     f = open("c:\simscript/command.txt", "w")
#     f.write("  Triggered the bot")
#     f.close()
#
# # _______________________________FIND NEXT SIM COMMAND____________________________________________________
#     if data.GetParam(1).lower() != "next":
#         return
#
#     # DEBUG stream message
#     send_message("NEXT DEBUG PROCESS 2: " + username + " Is looking for the next sim by using " + data.GetParam(1) + ".  Writing file.")
#
#     # create the file for AHK to see in c:\simscript or wherever you put it
#     f = open("c:\simscript/nextsim.txt", "w")
#     f.write("Trigger")
#     f.close()
#     # DEBUG stream message, file should be written
#     send_message("NEXT DEBUG PROCESS 3: I have successfully written the file. It is up to AHK now")
#
# # _______________________________CAMERA SIM 1____________________________________________________
#     if data.GetParam(1).lower() != "cam1":
#         return
#
#     # DEBUG stream message
#     send_message("CAMERA DEBUG PROCESS 2: " + username + " is " + data.GetParam(1) + ".  Writing file.")
#
#     # create the file for AHK to see in c:\simscript or wherever you put it
#     f = open("c:\simscript/test.txt", "w")
#     f.write("Trigger")
#     f.close()
#     # DEBUG stream message, file should be written
#     send_message("CAMERA DEBUG PROCESS 3: I have successfully written the file. It is up to AHK now")
#
#
# # _____________________END OF LOGIC______________________________________________________________
# def Tick():
#     return
#
#
# # message handling
# def send_message(message):
#     Parent.SendStreamMessage(message)
#     return
# # _______________________END OF PREVIOUS CODE_______________________________________________
# # __________________________________________________________________________________________
