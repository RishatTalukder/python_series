## Make a virtual environment

If you are on linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

If you are on windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## Install requirements

After activation of the virtual environment:

```bash
pip install -r pygame
```

Pygame should be installed and if you are on ubuntu or linux you might encounter this error:

![alt text](image.png)

All the sources suggest this is problem with the more recent versions of python. I got this error on a 3.14 environment. 

I downgraded to `3.12` and it worked.

Or if you dont want to downgrade, You can type installing the `pygame community edition`:

```bash
pip install pygame-ce
```

This installed properly in my python 3.14 environment.

Both libraries are largely indentical, So I dont think there would be any problem. Sometimes there might be some syntax differences but if you are using pygame-ce you can find the correct syntax in the official [documentation](https://pyga.me/docs/) or just one serach im google.

I'll be using `pygame-ce` going forward.

# Create a Pygame Window and respond to events

Make a new file named `main.py` and inside the file write the following:


```python 
import pygame


class Main():
    def __init__(self):
        # initialize pygame
        pygame.init()
        
        # set the screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space Defenders")
    
    def gmae_loop(self):
        
        # main game loop
        while True:

            # check for events
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    quit()
            
            # fill the screen with the background color
            self.screen.fill(self.bg_color)
            

if __name__ == "__main__":
    app = Main()
    app.gmae_loop()
```


## Setting thhe background


```python
#main.py
...
        pygame.display.set_caption("Space Defenders")

        # general attributes
        self.bg_color = (0,255,171)
    
    def gmae_loop(self):
        
        # main game loop
        while True:

            # check for events
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    quit()
            
            # fill the screen with the background color
            self.screen.fill(self.bg_color)

            ...

```