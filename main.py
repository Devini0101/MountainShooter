import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode(size=(600,400))
print("Setup end")

print("Loop Start")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting...")
            pygame.quit() #closes window
            quit() #end pygame