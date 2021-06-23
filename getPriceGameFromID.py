import urllib.request
import sys
import json
from colorama import init
init()

url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
response = urllib.request.urlopen(url).read()#.decode('utf-8')
steamGames = json.loads(response)

'''print(  "Name:", steamGames["applist"]["apps"][0]["name"],
        "\nSteamID:", steamGames["applist"]["apps"][0]["appid"])'''
# length json file elements
#print(len(steamGames['applist']['apps']))

def priceComparison(nameG, appID):
    steamStoreGame = 'https://store.steampowered.com/api/appdetails?appids='+str(appID)
    rSteamStoreGame = urllib.request.urlopen(steamStoreGame).read()
    getPriceSteam = json.loads(rSteamStoreGame)
    urlSteam = 'https://www.allkeyshop.com/api/latest/vaks.php?action=products&showOffers=1&showVouchers=false&locale=en_GB&currency=eur&apiKey=vaks_extension&search='+urllib.parse.quote_plus(nameG)
    rUrlSteam = urllib.request.urlopen(urlSteam).read()
    compare = json.loads(rUrlSteam)
    try:
        print("Prezzo Steam: ",getPriceSteam[str(appID)]['data']['price_overview']['final_formatted'], "\n")
        for i in range(5):
            print("Prezzo: ",compare['products'][0]['offers'][i]['price'])
            if(compare['products'][0]['offers'][i]['bestVoucher'] != None):
                print("Prezzo scontato del ",str(compare['products'][0]['offers'][i]['bestVoucher']['discount']['value']),str(compare['products'][0]['offers'][i]['bestVoucher']['discount']['type']))
                print("Prezzo scontato: ",compare['products'][0]['offers'][i]['bestVoucher']['priceWithVoucher'])
                print("Codice Voucher: ",compare['products'][0]['offers'][i]['bestVoucher']['code'])
            print("Nome sito: ",compare['products'][0]['offers'][i]['store']['name'], "\n")
    except KeyError:
        print("\033[1;31;40m" + "DLC o gioco gratuito\n")
    except IndexError:
        print("\033[1;31;40m" + "DLC o gioco gratuito\n")
        

try:
    while True:
        try:
            print('\033[39m')
            steamID = int(input("Steam ID (game): "))
            for appid in range(len(steamGames['applist']['apps'])):
                if(steamID == steamGames["applist"]["apps"][appid]["appid"]):
                    print(  "Name:", steamGames["applist"]["apps"][appid]["name"],
                            "\nSteamID:", steamGames["applist"]["apps"][appid]["appid"], "\n")
                    priceComparison(steamGames["applist"]["apps"][appid]["name"], steamGames["applist"]["apps"][appid]["appid"])
        except ValueError:
            print("Int Value\n")
except KeyboardInterrupt:
    # quit
    sys.exit()
