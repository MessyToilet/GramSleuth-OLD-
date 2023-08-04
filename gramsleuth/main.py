from gramsleuth.instagramapi import *
from Frontend import printLogo
import sys
import pwinput

init()

# ---#   START login sequence
printLogo("green")

Uname = str(input("Username: "))
Upass = pwinput.pwinput(prompt="Password: ", mask="*")

login(Uname, Upass)
goHome()
# ---#   END login sequence

goProfile()

while True:
    choice = str(input(
        "\n1. Go Home\t\t4. Go Reels\t\t7. Go Create\n2. Go Search\t\t5. Go Messages\t\t6. Go Notifications\n3. Go "
        "Explore\t\t8. Go Profile\t\t9. Go More\n10. test (get followers) \t11. Quit (Q)\n\n"))
    if choice == '1':
        goHome()
    if choice == '2':
        goSearch()
    if choice == '3':
        goExplore()
    if choice == '4':
        goReels()
    if choice == '5':
        goMessages()
    if choice == '6':
        goNotifications()
    if choice == '7':
        goCreate()
    if choice == '8':
        goProfile()
    if choice == '9':
        goMore()
    if choice == '10':
        getFollowers()

    if choice.upper() in ['Q', 'QUIT']:
        quit()
        sys.exit()
