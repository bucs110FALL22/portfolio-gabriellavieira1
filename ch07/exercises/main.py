####### Requirements #######

# - Player is represented on screen by an image
# - Player has 3 health
# - Player can move using arrow keys
# - Player can shoot with space bar
# - 3 enemies that display on screen
# - enemies move vertically
# - when player shoots enemy enemy pauses
# - When player collides with the enemy, they fight
#   - either player or enemy loses
#   - player loses, lose 1 health
#   - enemy loses enemy dies

#### Models ####

# - player
# - enemy
# - projectile

from Player import Player
from Enemy import Enemy
from Projectile import Projectile

import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode()
    background = pygame.Surface(pygame.display.get_window_size())
    background_color = (200, 200, 250)
    background.fill(background_color)
    # held keys act like repeated strike
    pygame.key.set_repeat(50, 500)
    #create modle objects
    player = Player.Player()
    
    enemies = pygame.sprite.Group()
    num_enemies = 3
    for _ in range(0, num_enemies):
        enemies.add(Enemy.Enemy())

    projectiles = pygame.sprite.Group()

    # cast existing groups to a tuple to add them together with other sprites and make a new group
    all_sprites = pygame.sprite.Group(tuple(enemies) + (player, ))

    #mainloop
    while True:  # one time through the loop is one frame (picture)
        
        # check for events since the last time through the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move("U")
                if event.key == pygame.K_DOWN:
                    player.move("D")
                if event.key == pygame.K_LEFT:
                    player.move("L")
                if event.key == pygame.K_RIGHT:
                    player.move("R")
                if event.key == pygame.K_SPACE:
                    if len(projectiles.sprites()) <= 5:
                        p = Projectile.Projectile(pygame.display.get_window_size()[0])
                        pos = player.rect.midright
                        p.rect.x = pos[0]
                        p.rect.y = pos[1]
                        projectiles.add(p)
                        all_sprites.add(p)
                    else:
                        print("can't shoot ", len(projectiles.sprites()))

        # update models
        for enemy in enemies:
            enemy.update()
        for projectile in projectiles:  
          projectile.update()

        # detect and respond to collisions
        fight = pygame.sprite.spritecollide(player, enemies, False)
        if fight:
            for enemy in fight:
                if player.fight(enemy):
                    enemy.kill()
                else:
                    player.health -= 1
                    #add a bounce effect and visual cue
                    player.rect.x -= enemy.rect.w
                    background_color = (255, 0, 0)
                

        bullets = pygame.sprite.groupcollide(enemies, projectiles, False, True)
        if bullets:
            for enemy in bullets:
                enemy.pause()

        # check if we need to end the program
        if player.health == 0:
            return

        # redraw background
        background.fill(background_color)
        screen.blit(background, (0, 0))
        #reset the background to the default color
        background_color = (200, 200, 250)

        #redraw all models
        all_sprites.draw(screen)
        #projectiles.draw(screen)

        # update the screen
        pygame.display.flip()

main()
