import random
import string
import time

class PassGen:
    def __init__(self):
      self.LINE_UP = '\033[1A'
      self.LINE_CLEAR = '\x1b[2K'  
        
    def program_loop(self):
        while True:
            self.print_welcome_msg()
            
            choice =  int(input('Enter your choice: '))
            
            # print(choice)
            
            self.reset_lines()
            
            if choice == 1:
                self.show_password()
                
            elif choice == 2:
                length = int(input('Enter the length of the password: '))
                self.show_password(length)
                self.clear_line()
                
            elif choice == 3:
                number = int(input('Enter the number of passwords you want to generate: '))
                length = int(input('Enter the length of the password: '))
                self.generate_multiple_passwords(number, length)
                self.clear_line()
            
            else:
                print('Invalid choice')
                time.sleep(1)
                self.clear_line()
            
            
    def go_back(self, lines = 1):
        for _ in range(lines):
            self.clear_line()
    
    def show_password(self, length=8):
        
        print()
        print(f"Your password is: {self.generate_password(length)}")
        print('----------------------')
        print()
        print('Press any key to go back')
        input()
        self.go_back(6)
            
    def generate_multiple_passwords(self, number = 1, length=8):
        print()
        print(f"Your password is:")
        for i in range(number):
            print(f"Password {i+1}: {self.generate_password(length)}")
        print('----------------------')
        print()
        print('Press any key to go back')
        input()
        self.go_back(6+number)

    def generate_password(self, length=8):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        
        digits = string.digits
        symbols = "!@#$%^&*"
        
        chars = upper + lower + digits + symbols
        
        password = "".join(random.choice(chars) for i in range(length))
        
        return password
    
    def print_welcome_msg(self):
        print()
        print('Hello USER, How May I Help You Today? ')
        print('--------------------------------------')
        print()
        print('1. Generate a password for me.')
        print('2. Generate a password of a given length.')
        print('3. Generate multiple passwords')
        print()
        print('----------------------')
        
    def clear_line(self):
        
        print(self.LINE_UP, end=self.LINE_CLEAR)
        
        
    def reset_lines(self):
        
        for _ in range(10):
            self.clear_line()

def main():
    app = PassGen()
    app.program_loop()

if __name__ == "__main__":
    main()
