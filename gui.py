import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('My first GUI')
window_surface = pygame.display.set_mode((800,600))
background = pygame.Surface((800,600))

manager = pygame_gui.UIManager((800,600))

button1 = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(500,400,100,30),
                            text='Click me 1',
                            manager=manager
                        )

button2 = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(500,200,100,30),
                            text='Click me 2',
                            manager=manager
                        )

label1 = pygame_gui.elements.UILabel(
                            relative_rect=pygame.Rect(150,100,200,100),
                            text="Value",
                            manager=manager
)


isRunning = True
clock = pygame.time.Clock()

while isRunning:

    time_delta = clock.tick(60)/1000.0
    window_surface.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    label1.set_text("click 1")
                if event.ui_element == button2:
                    label1.set_text("click 2")
    
        manager.process_events(event)
    
    manager.update(time_delta)
    manager.draw_ui(window_surface)
    pygame.display.update()