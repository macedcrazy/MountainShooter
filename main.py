import pygame as pg

print('Setup Start')
pg.init()
window = pg.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # close window
            quit()  # end pygame
