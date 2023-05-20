def main():
    title = r'''
     _____    _                                   _    __          __         _       _                       _         _____                                           _          _ 
    |  __ \  (_)                                 | |   \ \        / /        | |     | |                     | |       / ____|                                _        | |        | |
    | |  | |  _   ___    ___    ___    _ __    __| |    \ \  /\  / /    ___  | |__   | |__     ___     ___   | | __   | (___    _ __     __ _   _ __ ___    _| |_    __| |   ___  | |
    | |  | | | | / __|  / __|  / _ \  | '__|  / _` |     \ \/  \/ /    / _ \ | '_ \  | '_ \   / _ \   / _ \  | |/ /    \___ \  | '_ \   / _` | | '_ ` _ \  |_   _|  / _` |  / _ \ | |
    | |__| | | | \__ \ | (__  | (_) | | |    | (_| |      \  /\  /    |  __/ | |_) | | | | | | (_) | | (_) | |   <     ____) | | |_) | | (_| | | | | | | |   |_|   | (_| | |  __/ | |
    |_____/  |_| |___/  \___|  \___/  |_|     \__,_|       \/  \/      \___| |_.__/  |_| |_|  \___/   \___/  |_|\_\   |_____/  | .__/   \__,_| |_| |_| |_|          \__,_|  \___| |_|
                                                                                                                            | |                                                   
                                                                                                                            |_|  

											by NOM                                                 
    '''
    print(title)
    
    webhook_url = input("Enter the Discord webhook URL: ")
    num_messages = int(input("Enter the number of messages to send: "))

    for _ in range(num_messages):
        send_message(webhook_url, 'SCAM @everyone')

    delete_webhook(webhook_url)
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
    time.sleep(5)  # Delay for 5 seconds before exiting