import requests # get
import time # time
import os # clear screen
import urllib3 # disable stupid fucking warnings
from bs4 import BeautifulSoup # scraping
from colorama import Fore, init # color
from concurrent.futures import ThreadPoolExecutor, as_completed # multithreading
from datetime import datetime # date for filename

#Colorama init
init(autoreset=True)

# Disable InsecureRequestWarning for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logo = f"""
{Fore.BLUE}     ______   ______     ______     __  __     ______     __   __    
{Fore.BLUE}    /\\  == \\ /\\  == \\   /\\  __ \\   /\\_\\_\\_\\   /\\  __ \\   /\\ "-.\\ \\   
{Fore.LIGHTBLUE_EX}    \\ \\  _-/ \\ \\  __<   \\ \\ \\/\\ \\  \\/_/\\_\\/_  \\ \\ \\/\\ \\  \\ \\ \\-.  \\  
{Fore.LIGHTBLUE_EX}     \\ \\_\\    \\ \\_\\ \\_\\  \\ \\_____\\   /\\_\\/\\_\\  \\ \\_____\\  \\ \\_\\"\\_\\ 
{Fore.CYAN}      \\/_/     \\/_/ /_/   \\/_____/   \\/_/\\/_/   \\/_____/   \\/_/ \\/_/ 
                                                                 
    """

# faq screen
def faq():
    os.system("cls")
    print(logo)
    print("""
          
    [Scraper FAQ]
    The scraper will search through an assortment of different proxy websites (HTTP & HTTPS, for now)-
    and store them in a file called proxies.txt;
          
    We recommend you use the checker after the scraper, to make sure the fetched proxies are valid.

          
    [Checker FAQ]
    The checker will search for a file "proxies"-
    under the same directory as the checker;
          
    If it is found, the checker will validate the proxies.
    After it's done validating them, it'll create a new files (or find existing ones);
    called "http_proxies.txt", "https_proxies.txt", and store them there.

          
    (You will be returned to the main menu in 15 seconds)
    """)
    time.sleep(15)
    os.system("cls")
    main()

def scrape_from_github_http():
    url = "https://github.com/zloi-user/hideip.me/raw/refs/heads/master/http.txt"

    try:

        # Request the proxy list from the URL
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check if the request was successful
        proxies_list = response.text.splitlines()  # Split by line to get each proxy

        index = 0
        for proxy in proxies_list:
            proxies_list[index] = proxy.split(":")[0]+":"+proxy.split(":")[1]
            index+=1

        # Check if proxies.txt exists in the tool directory
        proxies_file_path = "proxies.txt"
        if os.path.exists(proxies_file_path):
            # Read the existing proxies.txt file
            with open(proxies_file_path, "r") as file:
                existing_proxies = file.read().splitlines()

            # Remove duplicates by combining and using a set
            combined_proxies = set(existing_proxies + proxies_list)

            # Write the combined proxies back into the file
            with open(proxies_file_path, "w") as file:
                for proxy in combined_proxies:
                    file.write(f"{proxy}\n")

            print(f"{Fore.YELLOW}Proxies have been added to {proxies_file_path}.")
            time.sleep(5)

        else:
            # If proxies.txt doesn't exist, create a new one and write the fetched proxies
            with open(proxies_file_path, "w") as file:
                for proxy in proxies_list:
                    file.write(f"{proxy}\n")
            print(f"{Fore.YELLOW}Proxies saved to {proxies_file_path}.")

    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching proxies: {e}")

def scrape_from_github_https():
    url = "https://github.com/zloi-user/hideip.me/raw/refs/heads/master/https.txt"

    try:

        # Request the proxy list from the URL
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check if the request was successful
        proxies_list = response.text.splitlines()  # Split by line to get each proxy

        index = 0
        for proxy in proxies_list:
            proxies_list[index] = proxy.split(":")[0]+":"+proxy.split(":")[1]
            index+=1
            #print(proxy)

        # Check if proxies.txt exists in the tool directory
        proxies_file_path = "proxies.txt"
        if os.path.exists(proxies_file_path):
            # Read the existing proxies.txt file
            with open(proxies_file_path, "r") as file:
                existing_proxies = file.read().splitlines()

            # Remove duplicates by combining and using a set
            combined_proxies = set(existing_proxies + proxies_list)

            # Write the combined proxies back into the file
            with open(proxies_file_path, "w") as file:
                for proxy in combined_proxies:
                    file.write(f"{proxy}\n")

            print(f"{Fore.YELLOW}Proxies have been added to {proxies_file_path}.")
            time.sleep(5)

        else:
            # If proxies.txt doesn't exist, create a new one and write the fetched proxies
            with open(proxies_file_path, "w") as file:
                for proxy in proxies_list:
                    file.write(f"{proxy}\n")
            print(f"{Fore.YELLOW}Proxies saved to {proxies_file_path}.")

    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching proxies: {e}")

def api_proxyscrape_com():

    url = "https://api.proxyscrape.com/?request=getproxies"

    try:

        # Request the proxy list from the URL
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check if the request was successful
        proxies_list = response.text.splitlines()  # Split by line to get each proxy

        # Check if proxies.txt exists in the tool directory
        proxies_file_path = "proxies.txt"
        if os.path.exists(proxies_file_path):
            # Read the existing proxies.txt file
            with open(proxies_file_path, "r") as file:
                existing_proxies = file.read().splitlines()

            # Remove duplicates by combining and using a set
            combined_proxies = set(existing_proxies + proxies_list)

            # Write the combined proxies back into the file
            with open(proxies_file_path, "w") as file:
                for proxy in combined_proxies:
                    file.write(f"{proxy}\n")

            print(f"{Fore.YELLOW}Proxies have been added to {proxies_file_path}.")
            time.sleep(5)

        else:
            # If proxies.txt doesn't exist, create a new one and write the fetched proxies
            with open(proxies_file_path, "w") as file:
                for proxy in proxies_list:
                    file.write(f"{proxy}\n")
            print(f"{Fore.YELLOW}Proxies saved to {proxies_file_path}.")

    except requests.RequestException as e:
        print(f"{Fore.RED}Error fetching proxies: {e}")


def socks_checker():
    pass

def check_proxy(proxy):
    test_url_http = "http://httpbin.org/ip"
    test_url_https = "https://www.google.com"
    proxies = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}",
    }
    
    http_valid = False
    https_valid = False
    
    try:
        response = requests.get(test_url_http, proxies={"http": proxies["http"]}, timeout=5, verify=False)
        response.raise_for_status()
        response_ip = response.json().get("origin", "")
        if proxy.split(":")[0] in response_ip:
            http_valid = True
    except requests.RequestException as e:
        pass  # Silences the error instead of printing it
    
    try:
        response = requests.get(test_url_https, proxies={"https": proxies["https"]}, timeout=5, verify=False)
        response.raise_for_status()
        https_valid = True  # If Google responds, HTTPS is working
    except requests.RequestException as e:
        pass  # Silences the error instead of printing it
    
    return proxy, http_valid, https_valid

def checker():

    proxies_fromfile = []
    has_proxiesFile = False

    if os.path.isfile("proxies.txt"):
        has_proxiesFile = True

    if has_proxiesFile:

        os.system("cls")

        with open("proxies.txt") as file:
            proxies_fromfile = [line.strip() for line in file.readlines()]

        valid_http_proxies = []
        valid_https_proxies = []
        
        thread_count = input(f"{Fore.LIGHTBLUE_EX}Thread Count?: ")
        try:
            thread_count = int(thread_count)
            if thread_count <= 0:
                print(f"{Fore.RED} Invalid thread amount provided, using the default amount of 10.")
                thread_count = 10
        except ValueError:
            print(f"{Fore.RED} Invalid thread input provided, using the default amount of 10.")
            thread_count = 10
        
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            future_to_proxy = {executor.submit(check_proxy, proxy): proxy for proxy in proxies_fromfile}

            for future in as_completed(future_to_proxy):
                proxy, is_http_valid, is_https_valid = future.result()

                if is_http_valid and is_https_valid:
                    print(f"{Fore.LIGHTBLUE_EX}{proxy} {Fore.CYAN}[HTTP] {Fore.BLUE}[HTTPS]")
                    valid_http_proxies.append(proxy)
                    valid_https_proxies.append(proxy)
                elif is_http_valid:
                    print(f"{Fore.LIGHTBLUE_EX}{proxy} {Fore.CYAN}[HTTP]")
                    valid_http_proxies.append(proxy)
                elif is_https_valid:
                    print(f"{Fore.LIGHTBLUE_EX}{proxy} {Fore.BLUE}[HTTPS]")
                    valid_https_proxies.append(proxy)
                else:
                    print(f"{Fore.LIGHTRED_EX}{proxy} {Fore.RED}[INVALID]")
        
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
        
        if valid_http_proxies:
            with open(f"proxies/http_proxies_{current_date}.txt", "w") as file:
                for proxy in valid_http_proxies:
                    file.write(f"{proxy}\n")
        
        if valid_https_proxies:
            with open(f"proxies/https_proxies_{current_date}.txt", "w") as file:
                for proxy in valid_https_proxies:
                    file.write(f"{proxy}\n")
        
        if valid_http_proxies or valid_https_proxies:
            print(f"\n{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}]{Fore.YELLOW} Valid proxies have been saved to 'proxies/' folder.")
        else:
            print(f"\n{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}]{Fore.YELLOW} No valid proxies found.")
        
        input(f"\nPress Enter to return to the main menu...")
        os.system("cls")
        main()

    else:
        print("\nYou don't have a proxies.txt file, please run the scraper first.")
        print("Returning you to the home screen in 5 seconds.")
        time.sleep(5)
        os.system("cls")
        main()

def scraper():
    os.system("cls")
    print("Please wait for the program to bring you back to the main menu.")
    api_proxyscrape_com()
    scrape_from_github_http()
    scrape_from_github_https()
    print("Returning to the main menu.")
    time.sleep(1)
    os.system("cls")
    main()


# main screen
def main():

    os.system(f"title PROXON Scraper : 0 CPM")

    print(f"""
    {logo}
      {Fore.CYAN}[1] Scraper

        {Fore.CYAN}[2] HTTP/S Checker         

          {Fore.LIGHTBLUE_EX}[3] Socks5 Checker (WIP)

            {Fore.BLUE}[0] FAQ
    """)

    choice = input(f"                {Fore.LIGHTCYAN_EX}[> ")
    if "1" in choice:
        scraper()
    elif "2" in choice:
        checker()
    elif "3" in choice:
        socks_checker()
    elif "0" in choice:
        faq()

if __name__ == '__main__':
    main()
