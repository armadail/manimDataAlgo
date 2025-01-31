
from manim import *
import random


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screenf

class BubbleSortVisual(Scene):
     
    def construct(self):
        r = [] #store rectangle array here
        n = [] #store number array here
        
        nsz = 5; #size of array
        inArr = list(range(nsz))
        random.Random(604).shuffle(inArr)
        print(len(inArr))

        for i in range(nsz):

            # color gradient formula to map set of inputs into a red - blue colour gradient
            rect = Rectangle(
                height = 0.75, 
                width = 0.75, 
                fill_opacity = 0.35,
                color = ManimColor.from_rgb((255 * (1 - inArr[i] / nsz), 0, 255 * inArr[i] / nsz))
            )
            r.append(rect)

            num = Text(str(inArr[i]), font_size=24)
            n.append(num)
        
        # constructing visual vector of rects
        rectgroup = VGroup(*r)
        rectgroup.arrange(RIGHT)
        #rectgroup.set_color_by_gradient(RED,BLUE)

        # constructing visual vector of values
        numgroup = VGroup(*n)
        numgroup.arrange(RIGHT)


        # Move the numbers to the centers of the rectangles
        for rect, num in zip(rectgroup, numgroup):
            num.move_to(rect.get_center())

        self.play(Write(rectgroup))
        self.play(Write(numgroup))
        print(len(numgroup))
        
        self.bubblesort(rectgroup, numgroup)
    

        
        self.wait()

    # implementing swap handler
    def swap(self, numgroup,rectgroup, i, j):
        ntemp = numgroup[i]
        numgroup[i] = numgroup[j]
        numgroup[j] = ntemp
        
        rtemp = rectgroup[i]
        rectgroup[i] = rectgroup[j]
        rectgroup[j] = rtemp

        self.play(
            Swap(rectgroup[i], rectgroup[j]),
            Swap(numgroup[i], numgroup[j])
        )
    
    # implementing bubble sort
    def bubblesort(self,rectgroup, numgroup):
        completed = []
        
        for i in range(len(numgroup)):
            for j in range(0,len(numgroup) - i - 1):
                #animate a visual comparision between two elements
                self.play(Indicate(numgroup[j]),Indicate(rectgroup[j]),color = None)
                self.play(Indicate(numgroup[j+1]),Indicate(rectgroup[j+1]), color = None)
                if int(numgroup[j].text) > int(numgroup[j+1].text):
                    self.swap(numgroup,rectgroup, j, j+1)
            # last element from the right has been sorted;
            print(i)
            completed.append(SurroundingRectangle(rectgroup[len(rectgroup) - i - 1], color=PURE_GREEN))
            self.play(Write(completed[i]))



    



