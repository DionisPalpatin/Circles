import pygame as pg


size = 500
rad = 50
flag = False


circles = {
    "horizontal" : {"x" : rad, "y" : size // 2, "direction" : 1},
    "vertical" : {"x" : size // 2, "y" : rad, "direction" : 1},
    "top_corner" : {"x" : rad, "y" : rad, "direction" : 1},
    "bottom_corner" : {"x" : rad, "y" : size - rad, "direction" : 1},
    "jump" : {"x" : size // 2, "y" : size // 2, "direction" : 1}
}


pg.init()
window = pg.display.set_mode((size, size), pg.SHOWN)


for figure in circles:
    if figure == "horizontal":
        pg.draw.circle(window, (163, 31, 163), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
    elif figure == "vertical":
        pg.draw.circle(window, (57, 54, 175), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
    elif figure == "top_corner":
        pg.draw.circle(window, (0, 255, 0), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
    elif figure == "bottom_corner":
        pg.draw.circle(window, (158, 0, 8), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
    else:
        pg.draw.circle(window, (0, 0, 0), (circles[figure]["x"], circles[figure]["y"]), rad, 10)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.exit()
            exit()


    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE] and flag != True:
        flag = True
        step = 20
        memory = circles["jump"]["y"]
    elif flag != True:
        if keys[pg.K_RIGHT]:
            circles["jump"]["x"] += 1
        if keys[pg.K_LEFT]:
            circles["jump"]["x"] -= 1
        if keys[pg.K_DOWN]:
            circles["jump"]["y"] += 1
        if keys[pg.K_UP]:
            circles["jump"]["y"] -= 1


    for figure in circles:
        if figure == "horizontal":
            circles[figure]["x"] += circles[figure]["direction"]
            if circles[figure]["x"] == size - rad:
                circles[figure]["direction"] = -1
            elif circles[figure]["x"] == rad:
                circles[figure]["direction"] = 1

        elif figure == "vertical":
            circles[figure]["y"] += circles[figure]["direction"]
            if circles[figure]["y"] == size - rad:
                circles[figure]["direction"] = -1
            elif circles[figure]["y"] == rad:
                circles[figure]["direction"] = 1

        elif figure == "top_corner":
            circles[figure]["x"] += circles[figure]["direction"]
            circles[figure]["y"] += circles[figure]["direction"]
            if circles[figure]["x"] == size - rad:
                circles[figure]["direction"] = -1
            elif circles[figure]["x"] == rad:
                circles[figure]["direction"] = 1
        
        elif figure == "bottom_corner":
            circles[figure]["x"] += circles[figure]["direction"]
            circles[figure]["y"] -= circles[figure]["direction"]
            if circles[figure]["x"] == size - rad:
                circles[figure]["direction"] = -1
            elif circles[figure]["x"] == rad:
                circles[figure]["direction"] = 1

        elif flag == True:
            circles[figure]["y"] += -1 * step * circles[figure]["direction"]
            step += -1 * circles[figure]["direction"]
            if step == 0:
                circles[figure]["direction"] = -1
            if circles[figure]["y"] == memory:
                flag = False
                circles[figure]["direction"] = 1


    window.fill((255, 255, 255))
    for figure in circles:
        if figure == "horizontal":
            pg.draw.circle(window, (163, 31, 163), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
        elif figure == "vertical":
            pg.draw.circle(window, (57, 54, 175), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
        elif figure == "top_corner":
            pg.draw.circle(window, (0, 255, 0), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
        elif figure == "bottom_corner":
            pg.draw.circle(window, (158, 0, 8), (circles[figure]["x"], circles[figure]["y"]), rad, 10)
        else:
            pg.draw.circle(window, (0, 0, 0), (circles[figure]["x"], circles[figure]["y"]), rad, 10)


    pg.display.update()
    pg.time.delay(10)