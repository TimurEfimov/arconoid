import pygame
pygame.init()

back = (255, 255, 0)
window = pygame.display.set_mode((500, 500))
window.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x, y, w, h, src):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.image.load(src)
        self.image = pygame.transform.scale(image, (w, h))

    def fill(self):
        pygame.draw.rect(window, back, self.rect)

    def draw(self):
        pygame.draw.rect(window, back, self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

platform = Area(0, 400, 150, 40, 'C:/Users/tefim/Desktop/it/arcanoid/platform.png')
move_right = False
move_left = False

ball = Area(0, 200, 50, 50, 'C:/Users/tefim/Desktop/it/arcanoid/ball.png')
ball_speed_x = 3
ball_speed_y = 3

monsters = []
x = 0
y = 0
for i in range(3):
    for j in range(10):
        m = Area(x, y, 50, 50, 'C:/Users/tefim/Desktop/it/arcanoid/monster.png')
        monsters.append(m)
        x += 50
    x = 0
    y += 50

while True:
    platform.fill()
    ball.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right and platform.rect.x <=  500 - platform.rect.w:
        platform.rect.x += 10
    if move_left and platform.rect.x > 0:
        platform.rect.x -= 10

    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y

    if ball.colliderect(platform.rect):
        ball_speed_y *= -1
    if ball.rect.x >= 500 - ball.rect.w or ball.rect.x < 0:
        ball_speed_x *= -1 
    if ball.rect.y < 0:
        ball_speed_y *= -1
    if ball.rect.y > 500:
        pygame.quit()
    if len(monsters) == 0:
        print('You winner')
        pygame.quit()

    for i in monsters:
        i.draw()
        if ball.colliderect(i.rect):
            monsters.remove(i)
            i.fill()
            ball_speed_y *= -1
    ball.draw()
    platform.draw()
    pygame.display.update()
    clock.tick(60)