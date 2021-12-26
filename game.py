import pygame, sys

class Game:
    def __init__(self, screen_size, flags=0, depth=0, display=0, vsync=0):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size, flags, depth, display, vsync)
        self.scenes = []
        self.running_scene = None
    
    def add_scene(self, scene):
        self.scenes.append(scene)
    
    def start(self, scene, **metadata):
        if self.running_scene is not None:
            self.running_scene = None
        
        self.running_scene = scene
        return self.running_scene.launch(**metadata)
    
    def end(self):
        pygame.quit()
        sys.exit()