import pygame
from .game import Game

class Scene:

    def __init__(self, game: Game, fps=60):
        self.game = game
        self.game.add_scene(self)
        
        self.screen = game.screen
        self.clock = pygame.time.Clock()
        self.running = False
        
        self.returnable = None
        self.fps = fps
    
    def launch(self, **metadata):
        self.metadata = metadata
        
        self.running = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        
        self.start()
        
        self.main_loop()
        return self.returnable
    
    def main_loop(self):
        while self.running:
            self.events()
            self.update_everything()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.end()
            
            self.event(event)
    
    def update_everything(self):
        self.update()
        self.all_sprites.update()
    
    def draw(self):        
        self.all_sprites.draw(self.screen)
        
        self.clock.tick(self.fps)
        pygame.display.update()
    
    def start(self):
        pass
    
    def update(self):
        pass

    def event(self, event):
        pass
    
class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, scene: Scene, layer: int, groups=None):
        self.scene = scene
        self._layer = layer
        
        self.groups = []
        self.groups.append(self.scene.all_sprites)
        if groups is not None: self.groups.extend(groups)
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.start()
    
    def start(self):
        pass
    
    def update(self):
        pass
