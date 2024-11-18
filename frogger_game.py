import os
import pygame 

class Settings:
    Window = pygame.rect.Rect(0,0,400,400)
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 800
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "Images_frogger")
    genereller_speed = 5  # Geschwindigkeit auf 5 für bessere Bewegung

class Rabbit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "rabbit.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # Setze die Startposition auf die Mitte unten
        self.rect.midbottom = (Settings.WINDOW_WIDTH // 2, Settings.WINDOW_HEIGHT - 10)

    def bewegen_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= Settings.genereller_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += Settings.genereller_speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= Settings.genereller_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += Settings.genereller_speed

        # Begrenze die Position des Hasen innerhalb des Bildschirms
        self.rect.x = max(0, min(self.rect.x, Settings.WINDOW_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, Settings.WINDOW_HEIGHT - self.rect.height))

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Frogger")
    clock = pygame.time.Clock()

    rabbit = Rabbit()  # Initialisiere den Hasen ohne x und y, da die Startposition in der Klasse definiert ist

    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "strasse.png")).convert()
    background_image = pygame.transform.scale(background_image, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        rabbit.bewegen_player()

        screen.blit(background_image, (0, 0))  # Hintergrundbild anzeigen
        screen.blit(rabbit.image, rabbit.rect.topleft)  # Hase anzeigen
        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()

if __name__ == "__main__":
     main()
