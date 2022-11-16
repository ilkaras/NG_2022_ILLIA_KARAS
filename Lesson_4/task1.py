from rich.console import Console
import platform

console = Console()
entries = []

specification = {
    "Computer network name": platform.node(),
    "Machine type": platform.machine(),
    "Processor type": platform.processor(),
    "Platform type": platform.platform(),
    "Operating system": platform.system(),
    "Operating system": platform.release(),
    "Operating system release": platform.version()
}
for key in specification.keys():
    entries.append(key)

def log(type, message):
    print ("[" + str(type) + "]: " + str(message))

def info(message):
    log ("INFO", message)

def logicalToStrConverter(logic):
    return "y" if logic else "n"

def showMenu(modes):
    console.rule("[bold red] Menu")
    for entry in entries:
        print ("[" + str(entries.index(entry)) + "] / [ " + logicalToStrConverter(modes[entry]) + " ]: " + entry)
    print("[" + str(len(entries)) + "]: Proceed")
    
def getUserChoice(modes):
    showMenu(modes)
    return int(input("Choose the option "))

def buildModes():
    modes = {}
    for entry in entries:
        modes[entry] = False
    return modes

def startManager():
    modes = buildModes()
    while True:
        choice = getUserChoice(modes)
        if choice == len(entries):
            return modes
            break
        else:
            try:
                modes[entries[choice]] = not modes[entries[choice]]
            except Exception as e:
                info("Please, enter valid number")

def Result(modes):
    resultstr = ""
    for entry in entries:
        if modes[entry]:
            resultstr += (entry + ": "  + specification[entry]) + "\n"
    dataFile = open("Lesson4.txt", "w")
    dataFile.write(resultstr)
    dataFile.close()

def main():
    info("Program started")
    Result(startManager())

main()