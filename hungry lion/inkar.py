import pygame
import random
import time

pygame.init()
Wight, Height = 800, 600
screen = pygame.display.set_mode((Wight, Height))

font_small = pygame.font.SysFont("Verdana", 20)
font = pygame.font.SysFont("Verdana", 60)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 775)
        self.y = random.randint(0, 585)

    def move(self):
        if random.randint(0, 1) == 0:
            if self.x > 0:
                self.x -= random.randint(0, 5)
        else:
            if self.x + 25 < Wight:
                self.x += random.randint(0, 5)

        if random.randint(0, 1) == 0:
            if self.y > 0:
                self.y -= random.randint(0, 5)
        else:
            if self.y + 15 < Height:
                self.y += random.randint(0, 5)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 25, 15))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 775)
        self.y = random.randint(0, 550)

    def move(self):
        self.y += 5
        if self.y + 15 > Height:
            self.y = -15

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 25, 15))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.x -= 5
        if self.x + 15 < Wight:
            if pressed_keys[pygame.K_RIGHT]:
                self.x += 5
        if self.y > 0:
            if pressed_keys[pygame.K_UP]:
                self.y -= 7
        if self.y + 15 < Height:
            if pressed_keys[pygame.K_DOWN]:
                self.y += 7

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 15, 15))


def main():
    fps = pygame.time.Clock()
    pl = Player(random.randint(50, 850), random.randint(350, 550))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(pl)
    foods = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    for i in range(20):
        F = Food()
        E = Enemy()
        foods.add(F)
        enemys.add(E)
        all_sprites.add(F)
        all_sprites.add(E)

    coins = 0
    a = 0

    for i in enemys:
        if pl.x - 50 <= i.x <= pl.x + 65 or pl.x - 50 <= i.x + 25 <= pl.x + 65:
            if pl.y - 50 <= i.y <= pl.y + 65 or pl.y - 50 <= i.y + 15 <= pl.y + 65:
                i.y = -15

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                break
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    break

        screen.fill((255, 255, 255))
        for i in all_sprites:
            i.move()
            i.draw()

        for i in foods:
            if pl.x <= i.x <= pl.x + 15 or pl.x <= i.x + 25 <= pl.x + 15:
                if pl.y <= i.y <= pl.y + 15 or pl.y <= i.y + 15 <= pl.y + 15:
                    i.kill()
                    pygame.mixer.Sound('eda.wav').play()
                    coins += 1
                    a += 1

        for i in enemys:
            if pl.x <= i.x <= pl.x + 15 or pl.x <= i.x + 25 <= pl.x + 15:
                if pl.y <= i.y <= pl.y + 15 or pl.y <= i.y + 15 <= pl.y + 15:
                    i.y = -15
                    pygame.mixer.Sound('vrag.wav').play()
                    coins -= 1

        co = font_small.render("COINS:" + str(coins), True, (0, 0, 0))
        screen.blit(co, (10, 10))

        if coins < 0:
            screen.fill((240, 40, 5))
            pygame.mixer.Sound('lost.wav').play()
            ls = font.render("You Lost", True, (255, 255, 255))
            screen.blit(ls, (250, 250))
            pygame.display.update()
            time.sleep(3)
            break

        if a >= 20:
            screen.fill((40, 240, 5))
            pygame.mixer.Sound('win.wav').play()
            wn = font.render("You Win", True, (255, 255, 255))
            screen.blit(wn, (250, 250))
            pygame.display.update()
            time.sleep(3)
            break

        pygame.display.flip()
        fps.tick(30)

    pygame.quit()


main()
