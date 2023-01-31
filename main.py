import sys


def main_menu():
    print("\n\nMain menu: \n\nChoose a feature or enter 0 to exit the program: \n1) List of keyboards (view all keyboards in database) "
          "\n0) Exit the program\n")
    choice = input()

    if int(choice) == 0:
        sys.exit()
    return int(choice)


def menu_options(menu_choice):
    test = 1
    if int(menu_choice) == 1:
        test = k_list()

    return test


def k_list():
    keyboard_brand = ["IBM", "IBM", "IBM", "IBM", "Apple", "Apple", "Apple", "NeXT", "Zenith", "Zenith"]
    keyboard_switches = ["IBM Membrane Buckling Springs", "IBM Capacitive Buckling Springs",
                         "IBM Capacitive Buckling Springs", "IBM Beamsprings", "Alps SKCM Orange or Salmon",
                         "Alps SKCM Salmon, Cream Dampened, or White Dampened", "Alps SKCM Orange or Salmon",
                         "Alps SKCM Cream or Black (pine)", "Alps SKCL Green or Yellow", "Alps SKCL Green or Yellow"]
    keyboard_keycaps = ["Dye-sublimated PBT", "Dye-sublimated PBT", "Dye-sublimated PBT", "Doubleshot ABS",
                        "Dye-sublimated PBT", "Dye-sublimated PBT", "Dye-sublimated PBT", "Doubleshot ABS",
                        "Dye-sublimated PBT or Doubleshot ABS", "Doubleshot ABS"]
    keyboard_build = ["PVC plastic, metal backplate", "Painted plastic, metal back case, metal plates",
                      "Painted plastic, metal plates", "Painted plastic with extremely thick metal chassis",
                      "ABS plastic, metal plate", "ABS plastic, metal plate", "ABS plastic, metal plate",
                      "ABS plastic, metal plate", "ABS plastic with metal back case, metal plate",
                      "ABS plastic with metal back case, metal plate"]
    keyboard_connections = ["AT, PS/2, various terminal connections", "XT", "AT", "proprietary terminal", "ADB", "ADB",
                            "ADB", "Proprietary connector", "XT or AT", "AT switchable"]
    keyboard_rarity = ["Extremely common (rare models exist)", "Extremely common", "Common", "Uncommon",
                       "Extremely common", "Extremely common", "Extremely common", "Rare", "Common", "Common"]
    keyboard_prices = ["70-120", "100-150", "200-250", "700-900", "90-130", "40-80", "70-90", "250-350", "180-220",
                       "150-200"]

    print("List of keyboards: \n\n1) IBM Model M\n2) IBM Model F XT\n3) IBM Model F AT\n4) IBM 5251\n5) Apple Extended Keyboard (M0115)"
          "\n6) Apple Extended Keyboard II (M3501)\n7) Apple Standard Keyboard (M0116)\n8) NeXT Non-ADB\n9) Zenith Z-150"
          "\n10) Zenith ZKB-2\n0) Return to main menu")
    print("Enter the number of the keyboard you wish to learn more about, or 0 to go back to the main menu: ")
    choice = input()

    if int(choice) == 0:
        return 1
    print("|Brand:       | " + str(keyboard_brand[int(choice)-1]) + " |"
          "\n|Switches:    | " + str(keyboard_switches[int(choice)-1]) + " |"
          "\n|Keycaps:     | " + str(keyboard_keycaps[int(choice)-1]) + " |"
          "\n|Build:       | " + str(keyboard_build[int(choice)-1]) + " |"
          "\n|Connections: | " + str(keyboard_connections[int(choice)-1]) + " |"
          "\n|Rarity:      | " + str(keyboard_rarity[int(choice)-1]) + " |")

    print("\nWould you like to view prices (1) or return to the main menu (0):")
    keyboard_choice = input()

    if int(keyboard_choice) == 0:
        return 1
    elif int(keyboard_choice) == 1:
        print("| Price: | $" + str(keyboard_prices[int(choice)-1]) + " |")
        return 1


def more_topics():
    print("\nWhich topics would you like to learn more about: \n1) Switches \n2) Brands \n3) Tips for finding keyboards "
          "\n0) Continue to main menu\n")
    choice = input()
    return int(topics(choice))


def topics(topic_choice):
    if int(topic_choice) == 1:
        print("The primary reason people tend to choose a vintage board over a modern one is the switches. Vintage switches, "
              "when in good condition, offer a completely unique feeling to the more commonly found switches today. "
              "\nThey are also significantly more diverse. While modern keyboard users are probably familiar with Cherry MX and its clones, "
              "Cherry MX is only one small part of the options available in vintage boards. "
              "\nThis program primarily organizes boards based on the switches they contain.")
        return 1
    elif int(topic_choice) == 2:
        print("You may be surprised at the brands that built high quality keyboards back in the day. For example, Apple. "
              "Apple may have a negative reputation for keyboards today, but in the 1980s they built some of the best keyboards around. "
              "\nDue to Apple’s popularity, their old keyboards can be found very often, and for good prices. Another major player was IBM. "
              "Perhaps the most famous vintage board is the IBM Model M, which was supplied with many of their PCs that dominated the market. "
              "\nIBM also produced earlier keyboards like their Model F series, and even earlier, their Beamspring series, "
              "which are some of the most coveted (and expensive) boards around. \nOther common brands include Zenith, "
              "Leading Edge, NeXT, Northgate, Focus, Chicony, Dell, SGI, NMB, and many more. ")
        return 1
    elif int(topic_choice) == 3:
        print("Use this program to find a target price for the board you are looking for. \nOnce you find a board at a "
              "good price, look thoroughly through the description and photos. How dirty is it? Dirty keyboards will "
              "require restoration. Other conditional factors are scratches and cracks, keycap wear (shine), and yellowing. "
              "\nIs it tested and working? Untested keyboards can be bargains, but have the potential for trouble. "
              "\nDoes the seller have good feedback (96% positive and above on eBay) and use secure payment methods? "
              "Paypal is a must, and only through the Goods & Services payment method.")
        return 1
    else:
        return 0


print("Would you like to learn the basics of vintage keyboards? This feature is best for people with no experience with "
      "vintage keyboards. Enter 1 for yes, or 0 to continue to the main menu: ")
choice1 = input()
while int(choice1) == 1:
    choice1 = more_topics()

choice2 = 1
while int(choice2) == 1:
    choice2 = main_menu()
    choice2 = menu_options(choice2)





