'''
    i
        print("mouse down")
    if event.type == pygame.MOUSEBUTTONUP:
        print("mouse up")
    if event.type == pygame.MOUSEMOTION:
        print(event.pos)
        
  get events with pygame.key or in a loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("jump")
        print(pygame.key.get_pressed())
        if playerRectangle.colliderect(snailRectangle) == 1:
            print("collision")
        mouse_pos = pygame.mouse.get_pos()
        if playerRectangle.collidepoint(mouse_pos):
            print(pygame.mouse.get_pressed() )
        '''
#pygame.draw.line(screen,"Gold", (0,0), (800,400), 10)
        #pygame.draw.ellipse(screen, "Brown", pygame.Rect(50,200,100,100))
        #pygame.draw.line(screen,"Gold", (0,0), pygame.mouse.get_pos() , 10)
#if event.type == pygame.MOUSEMOTION:
            #print(event.pos)
            #if event.type == pygame.KEYUP:
            #if event.key == pygame.K_SPACE:
            #test_surface = pygame.Surface((100, 200))
#test_surface.fill("Red")
#textSurface = testFont.render("My game", False, "Black")#rgb tuple
#STARTING VARIABLES
#scoreSurface = testFont.render("My game", False, (64,64,64))
#scoreRectangle = scoreSurface.get_rect(center=(400,50))
        #pygame.draw.rect(screen, "#c0e8ec", scoreRectangle)
        #pygame.draw.rect(screen, "#c0e8ec", scoreRectangle, 10)
        #screen.blit(scoreSurface,scoreRectangle)