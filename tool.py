import ipaddress
import requests
from colorama import Fore, Style, init

init(autoreset=True)


def print_title():
    title = r"""
@@@  @@@  @@@  @@@  @@@      @@@@@@    @@@@@@@   @@@@@@   @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@
@@@  @@@  @@@  @@@@ @@@     @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@
@@!  !@@  @@!  @@!@!@@@     !@@       !@@       @@!  @@@  @@!@!@@@  @@!@!@@@  @@!       @@!  @@@
!@!  @!!  !@!  !@!!@!@!     !@!       !@!       !@!  @!@  !@!!@!@!  !@!!@!@!  !@!       !@!  @!@
@!@@!@!   !!@  @!@ !!@!     !!@@!!    !@!       @!@!@!@!  @!@ !!@!  @!@ !!@!  @!!!:!    @!@!!@!
!!@!!!    !!!  !@!  !!!      !!@!!!   !!!       !!!@!!!!  !@!  !!!  !@!  !!!  !!!!!:    !!@!@!
!!: :!!   !!:  !!:  !!!          !:!  :!!       !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!: :!!
:!:  !:!  :!:  :!:  !:!         !:!   :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!
 ::  :::   ::   ::   ::     :::: ::    ::: :::  ::   :::   ::   ::   ::   ::   :: ::::  ::   :::
 :   :::  :    ::    :      :: : :     :: :: :   :   : :  ::    :   ::    :   : :: ::    :   : :
"""
    print(Fore.RED + title + Style.RESET_ALL)


def print_empty():
    print("")


def info(ip_address):
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        print(Fore.YELLOW + "IP address is not valid!" + Style.RESET_ALL)
        return

    try:
        r = requests.get(f'https://ipapi.co/{ip_address}/json/', timeout=5)
        if r.status_code == 200:
            data = r.json()
            network = data.get('network', 'N/A')
            version = data.get('version', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            region_code = data.get('region_code', 'N/A')
            country = data.get('country', 'N/A')
            country_name = data.get('country_name', 'N/A')
            country_code = data.get('country_code', 'N/A')
            country_code_iso3 = data.get('country_code_iso3', 'N/A')
            country_capital = data.get('country_capital', 'N/A')
            country_tld = data.get('country_tld', 'N/A')
            continent_code = data.get('continent_code', 'N/A')
            in_eu = data.get('in_eu', False)
            postal = data.get('postal', 'N/A')
            latitude = data.get('latitude', 0.0)
            longitude = data.get('longitude', 0.0)
            timezone = data.get('timezone', 'N/A')
            utc_offset = data.get('utc_offset', 'N/A')
            country_calling_code = data.get('country_calling_code', 'N/A')
            currency = data.get('currency', 'N/A')
            currency_name = data.get('currency_name', 'N/A')
            languages = data.get('languages', 'N/A')
            country_area = data.get('country_area', 0.0)
            country_population = data.get('country_population', 0)
            asn = data.get('asn', 'N/A')
            org = data.get('org', 'N/A')

            print(Fore.RED + f"Network: {network}" + Style.RESET_ALL)
            print(Fore.RED + f"Version: {version}" + Style.RESET_ALL)
            print(Fore.RED + f"City: {city}" + Style.RESET_ALL)
            print(Fore.RED + f"Region: {region}" + Style.RESET_ALL)
            print(Fore.RED + f"Region Code: {region_code}" + Style.RESET_ALL)
            print(Fore.RED + f"Country: {country}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Name: {country_name}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Code: {country_code}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Code ISO3: {country_code_iso3}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Capital: {country_capital}" + Style.RESET_ALL)
            print(Fore.RED + f"Country TLD: {country_tld}" + Style.RESET_ALL)
            print(Fore.RED + f"Continent Code: {continent_code}" + Style.RESET_ALL)
            print(Fore.RED + f"In EU: {in_eu}" + Style.RESET_ALL)
            print(Fore.RED + f"Postal Code: {postal}" + Style.RESET_ALL)
            print(Fore.RED + f"Latitude: {latitude}" + Style.RESET_ALL)
            print(Fore.RED + f"Longitude: {longitude}" + Style.RESET_ALL)
            print(Fore.RED + f"Timezone: {timezone}" + Style.RESET_ALL)
            print(Fore.RED + f"UTC Offset: {utc_offset}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Calling Code: {country_calling_code}" + Style.RESET_ALL)
            print(Fore.RED + f"Currency: {currency}" + Style.RESET_ALL)
            print(Fore.RED + f"Currency Name: {currency_name}" + Style.RESET_ALL)
            print(Fore.RED + f"Languages: {languages}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Area: {country_area}" + Style.RESET_ALL)
            print(Fore.RED + f"Country Population: {country_population}" + Style.RESET_ALL)
            print(Fore.RED + f"ASN: {asn}" + Style.RESET_ALL)
            print(Fore.RED + f"Organization: {org}" + Style.RESET_ALL)
            print(
                Fore.RED + f"Google Maps Link: https://www.google.com/maps/search/?api=1&query={latitude},{longitude}" + Style.RESET_ALL)
            print(Fore.RED + "WARNING: The Google Maps link is never 100% true." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"Error: Received status code {r.status_code}" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"Request error: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    print_title()
    print_empty()
    ip_address = input(Fore.RED + "Enter the IP address: " + Style.RESET_ALL)
    info(ip_address)
    input(Fore.RED +"Press Enter to exit..."+ Style.RESET_ALL)