import math

import manim
from manim import *

config.media_width = "100%"


class CircleToSquare(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        self.play(Create(blue_circle))
        self.wait()

        self.play(Transform(blue_circle, green_square))
        self.wait()


class MovingDots(Scene):
    def construct(self):
        d1, d2 = Dot(color=BLUE), Dot(color=GREEN)
        dg = VGroup(d1, d2).arrange(RIGHT, buff=1)
        l1 = Line(d1.get_center(), d2.get_center()).set_color(RED)
        x = ValueTracker(0)
        y = ValueTracker(0)
        d1.add_updater(lambda z: z.set_x(x.get_value()))
        d2.add_updater(lambda z: z.set_y(y.get_value()))
        l1.add_updater(lambda z: z.become(Line(d1.get_center(), d2.get_center())))
        self.add(d1, d2, l1)
        self.play(x.animate.set_value(5))
        self.play(y.animate.set_value(4))
        self.wait()

        self.wait(2)


#
class myNN(Scene):

    def construct(self):
        # INPUT LAYER
        inputLayer_faux = []
        inputLayer_faux2 = []
        for x in range(-5, 5):
            inputLayer_faux.append(Dot(point=np.array([-5.0, x / 6, 0.0]), radius=0.05, color=GREEN))
            inputLayer_faux2.append(Dot(point=np.array([-5.0, x / 6, 0.0]), radius=0.05, color=GREEN))
        inputLayer_faux_group = VGroup(*inputLayer_faux)
        inputLayer_faux_group2 = VGroup(*inputLayer_faux2)


        inputLayer = []
        for x in range(-5, 5):
            inputLayer.append(Dot(point=np.array([0.0, 0.0, 0.0])))
        inputLayer_group = VGroup(*inputLayer)

        # HIDDEN LAYER 1
        hiddenLayer1_faux = []
        for x in range(-20, 20):
            hiddenLayer1_faux.append(Dot(point=np.array([-2.0, x / 6, 0.0]), radius=0.05))
        hiddenLayer1_faux_group = VGroup(*hiddenLayer1_faux)

        hiddenLayer1_faux2 = []
        for x in range(-20, 20):
            hiddenLayer1_faux2.append(Dot(point=np.array([-2.0, x / 6, 0.0]), radius=0.05))
        hiddenLayer1_faux_group2 = VGroup(*hiddenLayer1_faux2)

        hiddenLayer1 = []
        for x in range(-20, 20):
            hiddenLayer1.append(Dot(point=np.array([0.0, 0.0, 0.0])))
        hiddenLayer1_group = VGroup(*hiddenLayer1)

        # HIDDEN LAYER 2
        hiddenLayer2_faux = []
        for x in range(-15, 15):
            hiddenLayer2_faux.append(Dot(point=np.array([-1.0, x / 6, 0.0]), radius=0.05))
        hiddenLayer2_faux_group = VGroup(*hiddenLayer2_faux)

        hiddenLayer2 = []
        for x in range(-15, 15):
            hiddenLayer2.append(Dot(point=np.array([0.0, 0.0, 0.0])))
        hiddenLayer2_group = VGroup(*hiddenLayer2)

        # HIDDEN LAYER 3
        hiddenLayer3_faux = []
        for x in range(-20, 20):
            hiddenLayer3_faux.append(Dot(point=np.array([0.0, x / 6, 0.0]), radius=0.05))
        hiddenLayer3_faux_group = VGroup(*hiddenLayer3_faux)

        hiddenLayer3 = []
        for x in range(-20, 20):
            hiddenLayer3.append(Dot(point=np.array([0.0, 0.0, 0.0])))
        hiddenLayer3_group = VGroup(*hiddenLayer3)

        # HIDDEN LAYER 4
        hiddenLayer4_faux = []
        for x in range(-10, 10):
            hiddenLayer4_faux.append(Dot(point=np.array([1.0, x / 6, 0.0]), radius=0.05))
        hiddenLayer4_faux_group = VGroup(*hiddenLayer4_faux)

        hiddenLayer4 = []
        for x in range(-10, 10):
            hiddenLayer4.append(Dot(point=np.array([0.0, 0.0, 0.0])))
        hiddenLayer4_group = VGroup(*hiddenLayer4)

        # HIDDEN LAYER 5
        hiddenLayer5_faux = []
        for x in range(-15, 15):
            hiddenLayer5_faux.append(Dot(point=np.array([2.0, x / 6, 0.0]), radius=0.05))
        hiddenLayer5_faux_group = VGroup(*hiddenLayer5_faux)

        hiddenLayer5 = []
        for x in range(-15, 15):
            hiddenLayer3.append(Dot(point=np.array([0.0, 0.0, 0.0])))
        hiddenLayer5_group = VGroup(*hiddenLayer5)

        # OUTPUT LAYER
        outputLayer_faux = []
        for x in range(-16, 16):
            outputLayer_faux.append(Dot(point=np.array([5.0, x / 6, 0.0]), radius=0.05))
        outputLayer_faux_group = VGroup(*outputLayer_faux)

        outputLayer = []
        for x in range(-16, 16):
            outputLayer.append(Dot(point=np.array([0.0, 0.0, 0.0]), color=GREEN))
        outputLayer_group = VGroup(*outputLayer)


        #LINE FROM INPUT LAYER TO HIDDEN LAYER 1
        L_IN_HIDDEN1 = []
        for l1 in inputLayer_faux_group:
            for l2 in hiddenLayer1_faux_group:
                line = self.createLine(l1, l2)
                L_IN_HIDDEN1 .append(line)

        L_IN_HIDDEN1_Group = VGroup(*L_IN_HIDDEN1)

        # LINE FROM HIDDEN LAYER 1 TO HIDDEN LAYER 2
        L_HIDDEN1_HIDDEN2 = []
        for l1 in hiddenLayer1_faux_group:
            for l2 in hiddenLayer2_faux_group:
                line = self.createLine(l1, l2)
                L_HIDDEN1_HIDDEN2.append(line)

        L_HIDDEN1_HIDDEN2_Group = VGroup(*L_HIDDEN1_HIDDEN2)

        # LINE FROM HIDDEN LAYER 2 TO HIDDEN LAYER 3
        L_HIDDEN2_HIDDEN3 = []
        for l1 in hiddenLayer2_faux_group:
            for l2 in hiddenLayer3_faux_group:
                line = self.createLine(l1, l2)
                L_HIDDEN2_HIDDEN3.append(line)

        L_HIDDEN2_HIDDEN3_Group = VGroup(*L_HIDDEN2_HIDDEN3)

        # LINE FROM HIDDEN LAYER 3 TO HIDDEN LAYER 4
        L_HIDDEN3_HIDDEN4 = []
        for l1 in hiddenLayer3_faux_group:
            for l2 in hiddenLayer4_faux_group:
                line = self.createLine(l1, l2)
                L_HIDDEN3_HIDDEN4.append(line)

        L_HIDDEN3_HIDDEN4_Group = VGroup(*L_HIDDEN3_HIDDEN4)

        # LINE FROM HIDDEN LAYER 4 TO HIDDEN LAYER 5
        L_HIDDEN4_HIDDEN5 = []
        for l1 in hiddenLayer4_faux_group:
            for l2 in hiddenLayer5_faux_group:
                line = self.createLine(l1, l2)
                L_HIDDEN4_HIDDEN5.append(line)

        L_HIDDEN4_HIDDEN5_Group = VGroup(*L_HIDDEN4_HIDDEN5)

        # LINE FROM HIDDEN LAYER 5 TO OUTPUT LAYER
        L_HIDDEN5_OUTPUT = []
        for l1 in hiddenLayer5_faux_group:
            for l2 in outputLayer_faux_group:
                line = self.createLine(l1, l2)
                L_HIDDEN5_OUTPUT.append(line)

        L_HIDDEN5_OUTPUT_Group = VGroup(*L_HIDDEN5_OUTPUT)



        # self.add(L_IN_HIDDEN1_Group)

        self.play(Transform(inputLayer_group, inputLayer_faux_group))
        self.play(Transform(inputLayer_faux_group2, L_IN_HIDDEN1_Group), Transform(inputLayer_faux_group, hiddenLayer1_faux_group))

        # self.play(Transform(hiddenLayer1_faux_group, L_IN_HIDDEN1_Group))
        self.play(Transform(hiddenLayer1_faux_group2, L_HIDDEN1_HIDDEN2_Group))

        self.play(Transform(hiddenLayer2_group, hiddenLayer2_faux_group))
        self.play(Transform(hiddenLayer2_faux_group, L_HIDDEN2_HIDDEN3_Group))

        self.play(Transform(hiddenLayer3_group, hiddenLayer3_faux_group))
        self.play(Transform(hiddenLayer3_faux_group, L_HIDDEN3_HIDDEN4_Group))

        self.play(Transform(hiddenLayer4_group, hiddenLayer4_faux_group))
        self.play(Transform(hiddenLayer4_faux_group, L_HIDDEN4_HIDDEN5_Group))

        self.play(Transform(hiddenLayer5_group, hiddenLayer5_faux_group))
        self.play(Transform(hiddenLayer5_faux_group, L_HIDDEN5_OUTPUT_Group))

        self.play(Transform(outputLayer_group, outputLayer_faux_group))

        self.wait(5)

    def createLine(self, neuron1, neuron2):
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            stroke_width=0.15,
            stroke_opacity=0.5
        )
