import requests 


class App:
    def __init__(self):
        self.check_website()
    
    def program_loop(self):
        pass
    
    def check_website(self):
        URL = "https://www.google.com"
        
        response = requests.get(URL)
        
        print(response)



def main() -> None:
    App()
