from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()
hp = 1

font = pygame.font.Font(None, 40)

hero = Hero(10,430,size_hero[0],size_hero[1],hero_image_list,3, 2)
bot1 = Bot(225, 240, size_bot[0], size_bot[1], bot_stay_image_list.copy(), 3, "vertical-left", radius = 230)
bot2 = Bot(495, 295, size_bot[0], size_bot[1], bot_stay_image_list.copy(), 3, "vertical-left", radius = 170)
bot3 = Bot(560, 28, size_bot[0], size_bot[1], bot_stay_image_list.copy(), 3, "horizontal-bottom", radius = 250)
bot4 = Bot(130, 30, size_bot[0], size_bot[1], bot_image_list.copy(), 3, "vertical-bottom", radius = 0)
bot5 = Bot(310, 200, size_bot[0], size_bot[1], bot_image_list, 3, "vertical", radius = 0)
bullet_4 = Bullet(bot4.x+15, bot4.y, 20, 20, RED, bot4.orientation,7)
bullet_5 = Bullet(bot5.x+17, bot5.y, 20, 20, RED, bot4.orientation,-3)

#ticket_list.append(Ticket(620, 455, 75, 75, ticket_image_list))
portal_list.append(Portal(620, 455, 75, 75, portal_image_list))

bot_list.append(bot1)
bot_list.append(bot2)
bot_list.append(bot3)
bot_list.append(bot4)
bot_list.append(bot5)
heart_list.append(Heart(780, 450, 75, 75, heart_image_list))
heart_list.append(Heart(315, 455, 75, 75, heart_image_list))

game = True

while game:
    events = pygame.event.get()
    window.fill(WHITE)

    render_text_hp = font.render(f"x{hero.hp}", True, RED) 
    window.blit(heart_image_list, (10,10))
    window.blit(render_text_hp, (65,25))


    for wall in wall_list:
        pygame.draw.rect(window, wall.color, wall)

    hero.move(window)
    bot1.guardian(window)
    bot2.guardian(window)
    bot3.guardian(window)
    bot4.stricker(window, bullet_4, hero)
    bot5.stricker(window, bullet_5, hero)

    for bot in bot_list:
        bot.colide_hero(hero)
    for heart in heart_list:
        heart.blit(window)
        heart.colide_hero(hero)

    for portal in portal_list:
        portal.blit(window)
        portal.colide_hero(hero)

    for heart in heart_list:
        heart.blit(window)

    for bot in bot_list:
        bot.colide_hero(hero)
    for heart in heart_list:
        heart.blit(window)
        heart.colide_hero(hero)

    for ticket in ticket_list:
        ticket.blit(window)

    for portal in portal_list:
        portal.blit(window)

    for event in events:
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.walk["up"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.walk["up"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                hero.walk["down"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                hero.walk["down"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero.walk["left"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                hero.walk["left"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hero.walk["right"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                hero.walk["right"] = False




    clock.tick(FPS)
    pygame.display.flip()
