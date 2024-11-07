import random
import os

# Function to create a random proxy
def generate_random_proxy():
    ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))  # Random IP
    port = random.randint(1000, 65535)  # Random port
    return f"{ip}:{port}"

# Function to generate a list of proxies
def generate_proxies(num_proxies):
    proxies = []
    for _ in range(num_proxies):
        proxy = generate_random_proxy()
        proxies.append(proxy)
    return proxies

# Function to save proxies to a file
def save_proxies_to_file(proxies, filename="proxies.txt"):
    try:
        with open(filename, "w") as file:
            for proxy in proxies:
                file.write(f"{proxy}\n")
        print(f"\033[1;32mProxies successfully saved to {filename}\033[0m")
    except Exception as e:
        print(f"\033[91mError saving proxies: {e}\033[0m")

# Function to display the banner with simple design
def display_banner():
    banner = """
    \033[1;32m██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ╚██████╔╝███████╗██║ ╚████║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """
    
    print(banner)

# Main function to handle user input and processing
def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for better UX

    # Display banner
    display_banner()

    try:
        # Ask user how many proxies they want
        num_proxies = int(input("\033[1;32mHow many proxies would you like to generate? \033[0m"))
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid number.\033[0m")
        return

    # Generate the proxies
    proxies = generate_proxies(num_proxies)

    print("\033[1;32mGenerated Proxies:\033[0m")
    for i, proxy in enumerate(proxies, 1):
        print(f"\033[1;32mProxy {i}:\033[0m {proxy}")

    # Ask if user wants to save the proxies
    save_choice = input("\033[1;32mDo you want to save the proxies to a file? (Y/N): \033[0m").strip().lower()
    if save_choice == 'y':
        save_proxies_to_file(proxies)
    else:
        print("\033[91mProxies not saved.\033[0m")

# Start the program
if __name__ == '__main__':
    main()

    # Wait for user input before closing
    input("\033[1;32mPress Enter to exit...\033[0m")
