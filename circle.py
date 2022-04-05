import turtle
sc = turtle.Screen()
sc.bgcolor('black')
pen = turtle.Turtle()
pen.width(4)
def circle(col, rad, val):
   
    pen.color(col)
    pen.circle(rad)
    pen.up()
     
    pen.setpos(0, val)
    pen.down()
 

def text():
   
    pen.color('white')
    pen.up()
    pen.setpos(-100, 140)
    pen.down()
    pen.write("Concentric VIBGYOR",font = ("Verdana", 15))
    pen.up()
    pen.setpos(-82, -188)
    pen.down()
    pen.write("Using Turtle Graphics",font = ("Verdana", 12))
    pen.hideturtle()
 
if __name__ == "__main__" :
   
    col = ['violet', 'indigo', 'blue','green', 'yellow', 'orange','red']
for i in range(7):
    circle(col[i], -20*(i+1), 20*(i+1))
text()
