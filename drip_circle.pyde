points = []
radius = 200
trail_count = 125
trail_distance = 4
trail_chance = .2

w, h = 1000, 1000

def draw_drip():
    strokeWeight(1)
    for p in points:
        for i in range(0, int(trail_count + random(-trail_count, trail_count))):
            stroke(243, 240, 215, 255 - i*(255/trail_count))
            if (random(1) < trail_chance):
                circle(p[0], p[1] + i*trail_distance, 1)
                
def draw_drap():
    strokeWeight(1)
    print(points)
    for p in points:
        # if (random(1) < trail_chance * 100):
        for i in range(0, int(trail_count * 3)):
            stroke(243, 240, 215, 255)
            if (random(1) < trail_chance * 2):
                circle( p[0] - i*trail_distance, p[1] - i*trail_distance, 1)
    
def draw_circle(point_count):
    noFill()
    beginShape()
    for i in range(point_count):
        x = radius * sin(i * TWO_PI/point_count)
        y = radius * cos(i * TWO_PI/point_count)
        vertex(x, y)
        points.append((x, y))
    strokeWeight(1)
    stroke('#f3f0d7')
    endShape(CLOSE)
    
    
def draw_building(cen_x, cen_y, build_size):
    fill('#364547')
    
    orig_y = cen_y
    random_height = random(0, 30)
    cen_x -= random(-5, 5)
    cen_y -= random(0, 30)
    
    # Draw Top
    beginShape()
    vertex(cen_x - build_size, cen_y)
    vertex(cen_x, cen_y - build_size/2)
    vertex(cen_x + build_size, cen_y)
    vertex(cen_x, cen_y + build_size/2)
    endShape(CLOSE)
    
    #Draw Sides
    beginShape()
    vertex(cen_x - build_size, orig_y + 30)
    vertex(cen_x - build_size, cen_y)
    vertex(cen_x, cen_y + build_size/2)
    vertex(cen_x + build_size, cen_y)
    vertex(cen_x + build_size, orig_y + 30)
    endShape()
    # line(cen_x - build_size, cen_y, cen_x - build_size, orig_y + 30)
    line(cen_x, cen_y + build_size/2, cen_x, orig_y + build_size/2 + 30)
    # line(cen_x + build_size, cen_y, cen_x + build_size, orig_y + 30)
    
    
def draw_buildings():
    stroke('#f3f0d7')
    strokeWeight(1)
    total_rows = 60
    for i in range(total_rows):
        start_x = w
        end_x = 0
        if (i < total_rows - 1):
            start_y = h * .75 - ((total_rows - i) * 20) - w/2
            
            if (i%2 == 0):
                start_x += 22
                start_y -= 11
            for i in range(start_x, end_x, -44):
                draw_building(i, start_y, 11)
                start_y += 22
        
    
def draw_curvy():
    start_x = 0
    end_x = w
    start_y = h * .75
    end_y = h * .25
    
    stroke('#f3f0d7')
    beginShape()
    for i in range(start_x, end_x, 1):
        # vertex(i, start_y)
        points.append((i, start_y))
        start_y -= .5
    endShape()
    
def setup():
    pixelDensity(2)
    background('#364547')
    size(w, h)
    # translate(w/2, h/2)
    # draw_circle(4)
    strokeWeight(1)
    draw_curvy()
    draw_buildings()
    # draw_lines()
    draw_drip()
    # draw_drap()
    
    save("Examples/City/" + str(int(random(100000))) + ".png")
