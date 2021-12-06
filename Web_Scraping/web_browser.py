import webbrowser
import sys

address = " "
if (len(sys.argv) > 1):
    address = ' '.join(sys.argv[1:])
    webbrowser.open("https://www.google.com/maps/place/" + address)
else:
    webbrowser.open("https://www.google.com/maps/place/")


