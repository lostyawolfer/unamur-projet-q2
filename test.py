print("AAAAAAAAAAAAAAAAH")
print("BBBBBBBBBBBBBBBBH")
print("CCCCCCCCCCCCCCCCH")

from colorama import Fore

def scream():
    return Fore.YELLOW + "Saleté " * 10**6

print(scream())