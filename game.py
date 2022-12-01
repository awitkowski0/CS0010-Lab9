# Import and initialize the pygame library
import pygame

from vehicle import Vehicle
pygame.init()

screen = pygame.display.set_mode([1920, 1080])

clock = pygame.time.Clock()

# Define our vehicles
Tesla = Vehicle("Red", 4)
Motorcyle = Vehicle("Blue", 2)
Tri = Vehicle("Black", 3)

# Create a list with our vehicles
Vehicles = {Tesla, Motorcyle, Tri}

# Which one do we have selected? Default to the tesla
selected = 0

# Run until the user asks to quit
running = True
while running:
    clock.tick(5)
    # Did the user click the window close button?
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Check for keyboard input
    keys = pygame.key.get_pressed()

    font = pygame.font.SysFont('timesnewroman',  30)

    # create a text surface object,
    # on which text is drawn on it.
    # Tick our vehicles
    for vehicle in Vehicles:

        text = font.render(vehicle.gear, True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (0, 0))

        if keys[pygame.K_a]:
            vehicle.gas_pedal()
        if keys[pygame.K_d]:
            vehicle.break_pedal()
        if keys[pygame.K_UP]:
            vehicle.change_gears("P")
        if keys[pygame.K_LEFT]:
            vehicle.change_gears("R")
        if keys[pygame.K_RIGHT]:
            vehicle.change_gears("D")

        vehicle.tick()

        if vehicle.color == "Blue":
            # Draw a solid blue circle in the center
            pygame.draw.circle(screen, (0, 0, 255),
                               (vehicle.location_x, 100), 75)
        if vehicle.color == "Red":
            # Draw a solid blue circle in the center
            pygame.draw.circle(screen, (255, 0, 0),
                               (vehicle.location_x, 300), 75)
        if vehicle.color == "Black":
            # Draw a solid blue circle in the center
            pygame.draw.circle(screen, (0, 0, 0),
                               (vehicle.location_x, 500), 75)
    # Flip the display
    pygame.display.flip()

pygame.quit()