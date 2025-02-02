
from manim import *
import random

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen



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
        
        #self.bubblesort(rectgroup, numgroup)
        self.insertsort(rectgroup, numgroup)

        
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

    def insertsort(self, rectgroup, numgroup):
        completed = []
        
        numkey = numgroup[0]
        rectkey = rectgroup[0]
        
        completedrect = None
    
        #typical insertion sort starts at i=0 but starting at 0 to animate the implied i=0 case;
        for i in range(0, len(numgroup)):

            numkey = numgroup[i]
            rectkey = rectgroup[i]
            emptySpot = numgroup[i].get_center()

            completed.append(rectgroup[i])
            
            # implementing expanding box animation
            new_completedrect = SurroundingRectangle(VGroup(*completed), color=PURE_GREEN)
            if completedrect:
                self.play(Transform(completedrect, new_completedrect))  # Expand animation
            else:
                completedrect = new_completedrect
                self.play(Write(completedrect))  # First time drawing it
            
            # move to bottom center of the screen
            self.play(Indicate(numkey),Indicate(rectkey), color = None)
            self.play(numkey.animate.move_to(ORIGIN + 2*DOWN),rectkey.animate.move_to(ORIGIN + 2*DOWN))
            

            j = i - 1
            while j >= 0 and int(numkey.text) < int(numgroup[j].text):
                # sorted elements scoot over to the right if the elements are greater than the key
                temp = rectgroup[j].get_center()
                self.play(numgroup[j].animate.move_to(emptySpot),rectgroup[j].animate.move_to(emptySpot))
                emptySpot = temp
                
                numgroup[j+1] = numgroup[j]
                rectgroup[j+1] = rectgroup[j]
                
                j -= 1

            numgroup[j+1] = numkey
            rectgroup[j+1] = rectkey

            self.play(numkey.animate.move_to(emptySpot),rectkey.animate.move_to(emptySpot))




