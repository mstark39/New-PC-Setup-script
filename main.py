import subprocess
import os
import shutil

# Keep the screen clear
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# The main menu
def display_menu(options):
    clear_screen()
    print("System Configuration Menu:")
    for key, value in options.items():
        print(f"{key}. {value}")
# The Sub menu for the apps
def install_apps_menu():
    apps_menu = {
        1: "Chrome",
        2: "Adobe",
        3: "ChildPlus",
        4: "MS Office",
        5: "RingCentral",
        6: "Savin Printer",
        'b': "Back to Main Menu"
    }

    while True:
        display_menu(apps_menu)
        choice = input("Enter your choice: ")

        if choice.lower() == 'b':
            break
        elif choice.isdigit() and int(choice) in apps_menu:
            install_app(int(choice))
        else:
            print("Invalid choice. Please select a valid option.")

def install_app(option):
    if option == 1:
        install_chrome()
    elif option == 2:
        install_adobe()
    elif option == 3:
        install_childplus()
    elif option == 4:
        install_office()
    elif option == 5:
        install_ringcentral()
    elif option == 6:
        install_savin_printer()
    else:
        print("Invalid option.")

def install_chrome():
    # Add Chrome installation logic here
    print("Installing Chrome...")
    # Edit to path: subprocess.run(['path/to/chrome_installer.exe'])

def install_adobe():
    # Add Adobe installation logic here
    print("Installing Adobe...")
    # Edit to path: subprocess.run(['path/to/adobe_installer.exe'])

def install_childplus():
    # Add ChildPlus installation logic here
    print("Installing ChildPlus...")
    # Edit to path: subprocess.run(['path/to/childplus_installer.exe'])

def install_office():
    # Add MS Office installation logic here
    print("Installing MS Office...")
    # Edit to path: subprocess.run(['path/to/office_installer.exe'])
    # Create shortcuts for Word, Excel, and Outlook on the desktop
    create_shortcuts(["Word", "Excel", "Outlook"], "~/Desktop")

def install_ringcentral():
    # Add RingCentral installation logic here
    print("Installing RingCentral...")
    # Edit to path: subprocess.run(['path/to/ringcentral_installer.exe'])

def install_savin_printer():
    # Add Savin Printer installation logic here
    print("Installing Savin Printer...")
    # Edit to path: subprocess.run(['path/to/savin_printer_installer.exe'])

def create_shortcuts(apps, location):
    for app in apps:
        shortcut_path = os.path.join(location, f"{app}.lnk")
        target_path = f"~/path/to/{app}.exe"  # Replace with actual path to the executable
        subprocess.run(['powershell.exe', '-Command', f'(New-Object -COM WScript.Shell).CreateShortcut("{shortcut_path}").TargetPath = "{target_path}"'])

# The main Menu
def main():
    options = {
        1: "Configure Windows Update",
        2: "Configure Network Settings",
        3: "Configure VPN",
        4: "Install Apps",
        'q': "Exit"
    }

    while True:
        display_menu(options)
        choice = input("Enter your choice: ")

        if choice.lower() == 'q':
            print("Exiting program.")
            break
        elif choice.isdigit() and int(choice) in options:
            option = int(choice)
            if option == 4:
                install_apps_menu()
            else:
                print("Option not implemented yet.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
