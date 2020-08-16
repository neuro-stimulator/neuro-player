import pygame


communication_event_state = {
    0:  pygame.event.Event(pygame.USEREVENT, state = "READY"),
    1:  pygame.event.Event(pygame.USEREVENT, state = "UPLOADED"),
    2:  pygame.event.Event(pygame.USEREVENT, state = "INITIALIZED"),
    3:  pygame.event.Event(pygame.USEREVENT, state = "RUNNING"),
    4:  pygame.event.Event(pygame.USEREVENT, state = "PAUSED"),
    5:  pygame.event.Event(pygame.USEREVENT, state = "FINISHED"),
    6:  pygame.event.Event(pygame.USEREVENT, state = "CLEARED"),
}