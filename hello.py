from cProfile import label
from email.mime import base
from manim import *
import numpy as np

class RightTriangleScene(MovingCameraScene):
    def construct(self):
        # ----------------------------
        # TRIANGLE → CIRCLES (unchanged)
        # ----------------------------
        A = LEFT + DOWN
        B = LEFT + UP
        C = RIGHT + DOWN

        triangle = Polygon(A, B, C, color=BLUE)
        right_angle = RightAngle(Line(A, B), Line(A, C), length=0.3)

        self.play(Create(triangle), Create(right_angle) , run_time=9)
        triangle.save_state()
        self.wait(2)
        self.play(FadeOut(right_angle))

        circle1 = Circle(radius=2, color=RED).rotate(PI / 4)
        self.play(Transform(triangle, circle1))
        self.wait(1)
        self.play(FadeOut(triangle))

        # ----------------------------
        # POLAR GRID (CLEAN + SCALED)
        # ----------------------------
        origin = ORIGIN
        R = 3.5  # 🔥 MASTER SIZE CONTROL

        # concentric circles
        radii = [1, 2, 3]
        circles = VGroup(
            *[
                Circle(
                    radius=r,
                    color=BLUE,
                    stroke_width=1.5,
                    stroke_opacity=0.6
                )
                for r in radii
            ]
        )

        # faint radial grid lines (every 30°)
        grid_angles = [k * PI / 6 for k in range(12)]
        radial_lines = VGroup(
            *[
                Line(
                    origin,
                    R * np.array([np.cos(theta), np.sin(theta), 0]),
                    color=BLUE,
                    stroke_width=1.5,
                    stroke_opacity=0.6
                )
                for theta in grid_angles
            ]
        )

        self.play(Create(circles), Create(radial_lines))

        # ----------------------------
        # 🔥 BOLD ANGLE LINES (KEY FIX)
        # ----------------------------
        major_angles = [
            PI/6, PI/4, PI/3, PI/2,
            2*PI/3, 3*PI/4, 5*PI/6,
            PI,
            7*PI/6, 5*PI/4, 4*PI/3,
            3*PI/2, 5*PI/3, 7*PI/4
        ]

        major_lines = VGroup(
            *[
                Line(
                    origin,
                    R * np.array([np.cos(theta), np.sin(theta), 0]),
                    color=BLUE,
                    stroke_width=1.5,
                    stroke_opacity=0.6
                )
                for theta in major_angles
            ]
        )

        self.play(Create(major_lines))

        # ----------------------------
        # BRIGHT AXES (ON TOP)
        # ----------------------------
        x_axis = Line(
            LEFT * (R + 0.15),
            RIGHT * (R + 0.15),
            color=DARK_BLUE,
            stroke_width=2,
            stroke_opacity=2

        )

        y_axis = Line(
            DOWN * (R + 0.15),
            UP * (R + 0.15),
            color=DARK_BLUE,
            stroke_width=2,
            stroke_opacity=2

        )

        self.play(Create(x_axis), Create(y_axis))
                # ----------------------------
        # RADIUS LABELS ON X-AXIS
        # ----------------------------
        radii = [-3, -2, -1, 1, 2, 3]
        radius_labels = VGroup()

        for r in radii:  
           
            label = MathTex(str(r)).scale(0.6)
            label.next_to(RIGHT * r, DOWN, buff=0.1)
            radius_labels.add(label)

        self.play(FadeIn(radius_labels))



        # fake polarplane ONLY for coordinate conversion
        polarplane = PolarPlane(size=6)

        # ----------------------------
        # RADIAN LABELS
        # ----------------------------
        rad_angles = [
            (PI/6, r"\frac{\pi}{6}"),
            (PI/4, r"\frac{\pi}{4}"),
            (PI/3, r"\frac{\pi}{3}"),
            (PI/2, r"\frac{\pi}{2}"),
            (2*PI/3, r"\frac{2\pi}{3}"),
            (3*PI/4, r"\frac{3\pi}{4}"),
            (5*PI/6, r"\frac{5\pi}{6}"),
            (PI, r"\pi"),
            (7*PI/6, r"\frac{7\pi}{6}"),
            (5*PI/4, r"\frac{5\pi}{4}"),
            (4*PI/3, r"\frac{4\pi}{3}"),
            (3*PI/2, r"\frac{3\pi}{2}"),
            (5*PI/3, r"\frac{5\pi}{3}"),
            (7*PI/4, r"\frac{7\pi}{4}"),
            (11*PI/6, r"\frac{11\pi}{6}"),
            
        ]

        rad_labels = VGroup()
        for theta, tex in rad_angles:
            label = MathTex(tex).scale(0.8)
            label.move_to(polarplane.polar_to_point(R + 0.60, theta))
            label.shift(0.40 * np.array([np.cos(theta), np.sin(theta), 0]))
            rad_labels.add(label)

# ---- 0 / 2π on positive x-axis ----
        theta = 0
        base = polarplane.polar_to_point(R + 0.60, theta)

        label_0_2pi = MathTex(r"0/2\pi").scale(0.8)
        label_0_2pi.move_to(base + 0.5 * RIGHT)

        rad_labels.add(label_0_2pi)

        self.play(FadeIn(rad_labels))
        rad_labels.save_state()
        self.wait(2)

        # ----------------------------
        # DEGREE LABELS
        # ----------------------------
        deg_angles = [
            (PI/6, r"30^\circ"),
            (PI/4, r"45^\circ"),
            (PI/3, r"60^\circ"),
            (PI/2, r"90^\circ"),
            (2*PI/3, r"120^\circ"),
            (3*PI/4, r"135^\circ"),
            (5*PI/6, r"150^\circ"),
            (PI, r"180^\circ"),
            (7*PI/6, r"210^\circ"),
            (5*PI/4, r"225^\circ"),
            (4*PI/3, r"240^\circ"),
            (3*PI/2, r"270^\circ"),
            (5*PI/3, r"300^\circ"),
            (7*PI/4, r"315^\circ"),
            (11*PI/6, r"330^\circ"),
        ]

        deg_labels = VGroup()
        for theta, tex in deg_angles:
            label = MathTex(tex).scale(0.8)
            label.move_to(polarplane.polar_to_point(R + 0.80, theta))
            label.shift(0.12 * np.array([np.cos(theta), np.sin(theta), 0]))
            deg_labels.add(label)

# ---- 0° / 360° on positive x-axis ----
        theta = 0
        base = polarplane.polar_to_point(R + 0.30, theta)

        label_0_360 = MathTex(r"0^\circ/360^\circ").scale(0.7)
        label_0_360.move_to(base + 0.8 * RIGHT)

        deg_labels.add(label_0_360)

        
        self.play(Transform(rad_labels, deg_labels))
        self.wait(2)
        self.play(Restore(rad_labels))
        # DOT MOVING AROUND CIRCLE
# ----------------------------
        r = 2.7       # radius of the circle (match your circle)
        dot = Dot(color=YELLOW)

# parametric function for a circle: x = r*cos(t), y = r*sin(t)
        circle_path = lambda t: polarplane.polar_to_point(r, t)
        
# 1️⃣ Line from origin to dot (radius vector)
        origin_to_dot = Line(ORIGIN, dot.get_center(), color=RED, stroke_width=2, stroke_opacity=1)
        origin_to_dot.add_updater(lambda m: m.become(
            Line(ORIGIN, dot.get_center(), color=RED, stroke_width=2, stroke_opacity=1)
        ))

# 3️⃣ Vertical line from x-axis up to the dot (touching x-axis)
        x_axis_line = Line(
            np.array([dot.get_center()[0], 0, 0]),  # start at x-axis
            dot.get_center(),                        # end at dot
            color=GREEN,
            stroke_width=2,
            stroke_opacity=1
        )
        x_axis_line.add_updater(lambda m: m.become(
            Line(
                np.array([dot.get_center()[0], 0, 0]),
                dot.get_center(),
                color=GREEN,
                stroke_width=2,
                stroke_opacity=1
            )
        ))

# Add all to the scene
        self.add(origin_to_dot, x_axis_line)


# animate the dot along the circle
        self.play(
            MoveAlongPath(dot, ParametricFunction(circle_path, t_range=[0, 2*PI])),
            run_time=5,
            rate_func=linear
            
        )
        # ----------------------------
        origin_to_dot.clear_updaters()
        x_axis_line.clear_updaters()
        self.wait(1)
        self.wait(2)
        self.play(
    FadeOut(dot),
    FadeOut(origin_to_dot),
    FadeOut(x_axis_line),
    run_time=2
)
        # --------------------------
        polar_group = VGroup(
            circles,
            radial_lines,
            major_lines,
            x_axis,
            y_axis,
            radius_labels,
            rad_labels
        )
        self.play(
            polar_group.animate
                .scale(0.75)
                .shift(4 * LEFT)
        )
        graph_origin = polarplane.polar_to_point(0, 0) * 0.75 + 4 * LEFT


        self.wait(0.5)
        # --------------------------
        Title = Text("What Does Polar Coordinates Actually Mean?", font_size=36, color=WHITE)
        Title.scale(0.7)
        Title.shift(3 * RIGHT)
        Title.to_edge(UP)
        self.play(FadeIn(Title, run_time=0.5))
        # ----------------------------
        question = MathTex("(", "r", ",", r"\theta", ")")
        question.shift(3 * RIGHT + 2 * UP)
        self.play(Write(question))

        r_def = Text("distance from the pole").scale(0.4)
        theta_def = Text("angle from polar axis").scale(0.4)

        r_def.next_to(question, DOWN + 1 * LEFT, buff=0.4)
        theta_def.next_to(r_def, 3 * RIGHT, buff=0.4)

        arrow_r = Arrow(question[1].get_bottom(), r_def.get_top(), buff=0.1, stroke_width=2,  max_tip_length_to_length_ratio=0.1, tip_length=0.15)
        arrow_theta = Arrow(question[3].get_bottom(), theta_def.get_top(), buff=0.1, stroke_width=2,  max_tip_length_to_length_ratio=0.1, tip_length=0.15)

        self.play(Write(r_def), GrowArrow(arrow_r))
        self.play(Write(theta_def), GrowArrow(arrow_theta))
        # ----------------------------
        self.wait(2)
        coord = MathTex("(","2",",",r"\frac{\pi}{4}",")")
        coord.shift(3 * RIGHT + 2 * UP)
        
        self.play(Write(coord, run_time=1), FadeOut(question))
        #----------------------------
        r_val = 2
        theta_val = PI / 4
        point_dot = Dot(
        polarplane.polar_to_point(r_val, theta_val),
        color=YELLOW
        )

        point_dot.scale(0.75).shift(3.95 * LEFT)
        
        self.play(Create(point_dot))
        self.add(point_dot)
        self.add_foreground_mobjects(point_dot)  # ensures dot is on top
        self.camera.frame.save_state()
        self.play(
            FadeOut(r_def),
            FadeOut(theta_def),
            FadeOut(arrow_r),
            FadeOut(arrow_theta),
        self.camera.frame.animate.scale(0.4).move_to(point_dot), run_time=2)

        # ----------------------------
# RIGHT TRIANGLE ATTACHED TO POLAR GRAPH
# ----------------------------

# Foot of perpendicular on polar x-axis
        # Foot of perpendicular on x-axis
        dot_pos = point_dot.get_center()
        foot = np.array([dot_pos[0], graph_origin[1], 0])  # add 0.2 to raise it


# Horizontal leg (r cos θ)
        horizontal_leg = Line(
            graph_origin,
            foot,
            color=GREEN,
            stroke_width=4
        )

# Vertical leg (r sin θ)
        vertical_leg = Line(
            foot,
            dot_pos,
            color=BLUE,
            stroke_width=4
        )

# Hypotenuse (radius r)
        hypotenuse = Line(
            graph_origin,
            dot_pos - np.array([0, 0, 0]),
            color=RED,
            stroke_width=4
        )

# Right angle marker (NOW WORKS)
        right_angle = RightAngle(
            horizontal_leg,
            vertical_leg,
            length=0.2,
            quadrant=(-1, 1),
            color=WHITE
        )

        self.play(
            Create(horizontal_leg),
            Create(vertical_leg),
            Create(hypotenuse),
            Create(right_angle)
        )
        self.wait(4)
        
        reflect = Text("Now What?").scale(0.6)
        Title2 = Text("Finding The Components", font_size=36, color=WHITE)
        Title2.scale(0.8)
        Title2.move_to(Title)
        self.play(Transform(Title, Title2))
        reflect.shift(3 * RIGHT)
        self.play(Write(reflect, run_time=1))
        self.play(self.camera.frame.animate.scale(0.6).move_to(reflect), run_time=1)
        self.wait(2)
        self.play(
        FadeOut(reflect, run_time = 1),
        Restore(self.camera.frame, run_time=2),
        )
        rcos = MathTex(r"x = r\cos(\theta)").scale(0.8)
        rsin = MathTex(r"y = r\sin(\theta)").scale(0.8)

        rcos.next_to(coord, DOWN + 1 * LEFT, buff=0.4)
        rsin.next_to(rcos, 5 * RIGHT, buff=0.4)
        self.play(Write(rcos), Write(rsin))
        self.wait(4)
        xmath = MathTex(r"x = 2\cos\left(\frac{\pi}{4}\right)").scale(0.7)
        ymath = MathTex(r"y = 2\sin\left(\frac{\pi}{4}\right)").scale(0.7)
        xmath.next_to(rcos, DOWN, buff=0.4)
        ymath.next_to(rsin, DOWN, buff=0.4)
        self.play(Write(xmath), Write(ymath))
        self.wait(4)
        #---------------------------- 
        x_label = MathTex(r"1.41").scale(0.5)
        y_label = MathTex(r"1.41").scale(0.5).shift(0.1 * LEFT)
        r_label = MathTex(r"2").scale(0.5).shift(DOWN)
        x_label.set_color(GREEN)
        y_label.set_color(BLUE)
        r_label.set_color(RED)
        x_label.next_to(horizontal_leg, DOWN, buff=0.1)
        y_label.next_to(vertical_leg, RIGHT, buff=0.1)
        normal = hypotenuse.get_normal_vector()
        r_label.move_to(
            hypotenuse.get_midpoint() + 0.2 * UP
        )
        # ----------------------------
       
        xcord1 = MathTex(r"x = 2\left(\frac{1}{\sqrt{2}}\right)").scale(0.7)
        ycord1 = MathTex(r"y = 2\left(\frac{1}{\sqrt{2}}\right)").scale(0.7)
        xcord1.next_to(xmath, DOWN, buff=0.4)
        ycord1.next_to(ymath, DOWN, buff=0.4)
        self.play(Write(xcord1), Write(ycord1))
        self.wait(2)
        xcord2 = MathTex(r"x = \frac{2}{\sqrt{2}} \approx 1.41").scale(0.7)
        ycord2 = MathTex(r"y = \frac{2}{\sqrt{2}} \approx 1.41").scale(0.7)
        xcord2.next_to(xcord1, DOWN, buff=0.4)
        ycord2.next_to(ycord1, DOWN, buff=0.4)
        self.play(Write(xcord2), Write(ycord2))
        self.wait(4)
        #----------------------------
        self.play(Write(x_label), Write(y_label), Write(r_label), self.camera.frame.animate.scale(0.5).move_to(point_dot), run_time=2)

        self.wait(7)
        # self.play(Restore(self.camera.frame, run_time=2))
        #----------------------------
        reflect2 = Text("What About The Reverse?").scale(0.5)
        coord2 = MathTex(r"", r"\left(\frac{2}{\sqrt{2}}", ",", r"\frac{2}{\sqrt{2}}\right)", "")
        coord2.move_to(coord)
        final_pos = reflect2.get_center() + 4 * RIGHT + 2 * DOWN
        #----------------------------
        xcord3 = MathTex(r"x = \left(\frac{2}{\sqrt{2}}\right)").scale(0.7)
        ycord3 = MathTex(r"y = \left(\frac{2}{\sqrt{2}}\right)").scale(0.7)
        xcord3.move_to(xcord2)
        ycord3.move_to(ycord2)
        x_label2 = MathTex(r"\left(\frac{2}{\sqrt{2}}\right)").scale(0.4)
        x_label2.set_stroke(width=0.5)
        y_label2 = MathTex(r"\left(\frac{2}{\sqrt{2}}\right)").scale(0.4)
        y_label2.set_stroke(width=0.5)
        x_label2.move_to(x_label)
        x_label2.shift(0.2 * DOWN)

        y_label2.move_to(y_label)
        x_label2.set_color(GREEN)
        y_label2.set_color(BLUE)
        self.play(
        Transform(x_label, x_label2), 
        Transform(y_label, y_label2),
        Transform(coord, coord2),
        Transform(xcord2, xcord3),
        Transform(ycord2, ycord3),
        FadeOut(xcord1), FadeOut(ycord1), FadeOut(xcord2), FadeOut(ycord2),
        FadeOut(rcos), FadeOut(rsin),
        FadeOut(xmath), FadeOut(ymath),
        Transform(Title, Text("From Cartesian To Polar", font_size=36, color=WHITE).scale(0.8).move_to(Title)),
        Write(reflect2, run_time = 3),
        reflect2.animate.shift(4 * RIGHT + 2 * DOWN),
        FadeOut(r_label),
        self.camera.frame.animate.scale(0.6).move_to(final_pos),
        run_time=1
        )
        self.wait(4)

        self.play(
        FadeOut(reflect2),
        Restore(self.camera.frame),
        run_time=3
        )
        self.wait(2)
        xy = MathTex(r" r^2 = x^2 + y^2 ").scale(0.7)
        tan = MathTex(r" \theta = \arctan\left(\frac{y}{x}\right)").scale(0.7)
        xy.next_to(coord2, DOWN + 0.4 * LEFT, buff=0.4)
        tan.next_to(coord2, DOWN + 0.4 * RIGHT, buff=0.2)
        self.play(Write(xy), Write(tan))   
        self.wait(7)
        xy2 = MathTex(r" r^2 = \left(\frac{2}{\sqrt{2}}\right)^2 + \left(\frac{2}{\sqrt{2}}\right)^2 ").scale(0.6)
        tan2 = MathTex(r" \theta = \arctan\left(\frac{\frac{2}{\sqrt{2}}}{\frac{2}{\sqrt{2}}}\right)").scale(0.7)
        xy2.next_to(xy, DOWN, buff=0.4)
        tan2.next_to(tan, DOWN, buff=0.4)
        self.play(Write(xy2), Write(tan2))
        self.wait(3)
        xy3 = MathTex(r" r^2 = 2 + 2 = 4 ").scale(0.7)
        tan3 = MathTex(r" \theta = \arctan\left(1\right) = \frac{\pi}{4} ").scale(0.7)
        xy3.next_to(xy2, DOWN, buff=0.4)
        tan3.next_to(tan2, DOWN, buff=0.4)
        self.play(Write(xy3), Write(tan3))
        self.wait(1)
        xy4 = MathTex(r" r = \sqrt{4} = 2 ").scale(0.7)
        tan4 = MathTex(r" \theta = \frac{\pi}{4} ").scale(0.7)
        xy4.next_to(xy3, DOWN, buff=0.4)
        tan4.next_to(tan3, DOWN, buff=0.4)
        self.play(Write(xy4), Write(tan4))
        self.wait(1)
        self.play(Write(r_label), self.camera.frame.animate.scale(0.5).move_to(point_dot), run_time=2)
        self.wait(1)
        self.play(Transform(coord, MathTex(r"\left(2, \frac{\pi}{4}\right)").scale(0.8).move_to(coord)), self.camera.frame.animate.scale(0.5).move_to(coord), run_time=2)
        self.wait(1)
        self.play(
            FadeOut(x_label), FadeOut(y_label), FadeOut(coord), FadeOut(xy), FadeOut(tan), FadeOut(xy2), FadeOut(tan2), FadeOut(xy3), FadeOut(tan3), FadeOut(xy4), FadeOut(tan4), FadeOut(Title), 
            FadeOut(polar_group), FadeOut(horizontal_leg), FadeOut(vertical_leg), FadeOut(hypotenuse), FadeOut(right_angle),
            FadeOut(point_dot), FadeOut(r_label), FadeOut(Title), FadeOut(coord2), FadeOut(xcord3), FadeOut(ycord3), FadeOut(x_label2), FadeOut(y_label2),
            
            Restore(self.camera.frame, run_time=0.5)
        )
        

        # TITLE
        title = Text(
            "Why Engineers Care About Polar Coordinates",
            font_size=34
        ).to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        # SHARED ANGLE
        theta = ValueTracker(0)

        # LEFT: ROTATING SYSTEM
        demo_plane = PolarPlane(radius_max=1.5).scale(0.9).shift(3 * LEFT)
        unit_circle = Circle(radius=1, color=WHITE).move_to(demo_plane.get_origin())

        rotating_dot = Dot(color=YELLOW)
        rotating_dot.add_updater(
            lambda m: m.move_to(
                demo_plane.polar_to_point(1, theta.get_value())
            )
        )

        motor_label = Text(
            "Rotating System\n(Motor / Sensor)",
            font_size=22
        ).next_to(unit_circle, 4 * DOWN)

        # RIGHT: SINE WAVE OUTPUT
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=3,
            tips=False
        ).shift(3 * RIGHT)

        sine_wave = always_redraw(
            lambda: ParametricFunction(
                lambda t: axes.c2p(t, np.sin(t)),
                t_range=[0, max(theta.get_value(), 0.001)],
                color=BLUE,
                stroke_width=4
            )
        )

        wave_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    max(theta.get_value(), 0.001),
                    np.sin(max(theta.get_value(), 0.001))
                ),
                color=RED
            )
        )

        wave_label = Text(
            "Signal Output\n(Voltage / Sound)",
            font_size=22
        ).next_to(axes, UP)

        # PROJECTION LINE
        projection = always_redraw(
            lambda: DashedLine(
                rotating_dot.get_center(),
                axes.c2p(
                    max(theta.get_value(), 0.001),
                    np.sin(max(theta.get_value(), 0.001))
                ),
                color=GRAY,
                dash_length=0.15
            )
        )

        # ADD TO SCENE

        self.add(
            demo_plane,
            unit_circle,
            rotating_dot,
            motor_label,
            axes,
            sine_wave,
            wave_dot,
            projection,
            wave_label
        )
        # ANIMATE
        self.play(
            theta.animate.set_value(2 * PI),
            run_time=6,
            rate_func=linear
        )

        self.wait(2)

        # FINAL TAKEAWAY
      
        takeaway = Text(
            "Rotation → Oscillation → Signals",
            font_size=30,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(takeaway))
        self.wait(25)
        self.play(FadeOut(takeaway), FadeOut(title), FadeOut(motor_label), FadeOut(wave_label), FadeOut(demo_plane), FadeOut(unit_circle), FadeOut(rotating_dot), FadeOut(axes), FadeOut(sine_wave), FadeOut(wave_dot), FadeOut(projection), run_time=1)
        
        
        self.remove(triangle)

# Restore state (off-screen, not animated)
        triangle.restore()
        A, B, C = triangle.get_vertices()[:3]  # get triangle vertices
        line1 = Line(A, B)
        line2 = Line(A, C)

# Recreate right angle
        right_angle = RightAngle(line1, line2, length=0.3, quadrant=(1,1), color=WHITE)
        shape = VGroup(triangle, right_angle)

        self.play(
            FadeIn(shape),
            self.camera.frame.animate.move_to(shape.get_center()).scale(0.5),
            run_time=2
        )
        self.wait(5)
        self.play(
            FadeIn(polar_group),
            polar_group.animate.scale(0.5),
            shape.animate.shift(10 * LEFT),
            self.camera.frame.animate.move_to(polar_group),
        )
        final = VGroup(shape, polar_group)
        self.play(self.camera.frame.animate.move_to(final.get_center()).scale(1.5), run_time=2)
        self.wait(3)
        self.play(FadeOut(shape), FadeOut(polar_group), run_time=2)
        


        
        # theta = ValueTracker(0)

        # # Left: polar plane + unit circle
        # polarplane = PolarPlane(
        #     radius_max=1.5,
        #     azimuth_units="PI radians",
        # ).scale(1).shift(3 * LEFT)

        # circle = Circle(radius=1, color=WHITE).move_to(polarplane.get_origin())

        # # Rotating dot
        # dot = Dot(color=YELLOW)
        # dot.add_updater(
        #     lambda m: m.move_to(
        #         polarplane.polar_to_point(1, theta.get_value())
        #     )
        # )

        # # ----------------------------
        # # Right: Cartesian axes + sine wave
        # # ----------------------------
        # axes = Axes(
        #     x_range=[0, 2 * PI, PI / 2],
        #     y_range=[-1.5, 1.5, 1],
        #     x_length=6,
        #     y_length=3,
        #     tips=False,
        # ).shift(3 * RIGHT)

        # sine_curve = always_redraw(
        #     lambda: ParametricFunction(
        #         lambda t: axes.c2p(t, np.sin(t)),
        #         t_range=[0, theta.get_value()],
        #         color=BLUE,
        #         stroke_width=4,
        #     )
        # )

        # # Dot on the wave (records motion)
        # wave_dot = always_redraw(
        #     lambda: Dot(
        #         axes.c2p(theta.get_value(), np.sin(theta.get_value())),
        #         color=RED
        #     )
        # )

        # # ----------------------------
        # # Projection line (THE KEY IDEA)
        # # ----------------------------
        # projection = always_redraw(
        #     lambda: DashedLine(
        #         dot.get_center(),
        #         axes.c2p(theta.get_value(), np.sin(theta.get_value())),
        #         color=GRAY,
        #         stroke_width=2,
        #     )
        # )

        # # ----------------------------
        # # Labels (optional but clean)
        # # ----------------------------
        # theta_label = MathTex(r"\theta").next_to(circle, DOWN)
        # sine_label = MathTex(r"y=\sin(x)").next_to(axes, UP)

        # # ----------------------------
        # # ADD TO SCENE
        # # ----------------------------
        # self.add(
        #     polarplane,
        #     circle,
        #     dot,
        #     axes,
        #     sine_curve,
        #     wave_dot,
        #     projection,
        #     theta_label,
        #     sine_label,
        # )

        # # ----------------------------
        # # ANIMATE
        # # ----------------------------
        # self.play(
        #     theta.animate.set_value(2 * PI),
        #     run_time=6,
        #     rate_func=linear,
        # )

        # self.wait(2)

        
        
        

        
        
    

        

    
        # arrow_2 = Arrow(question[1].get_bottom(), coord[1].get_top(), buff=0.1, stroke_width=2,  max_tip_length_to_length_ratio=0.1, tip_length=0.15)
        # arrow_pi4 = Arrow(question[3].get_bottom(), coord[3].get_top(), buff=0.1, stroke_width=2,  max_tip_length_to_length_ratio=0.1, tip_length=0.15)
        # self.play(Write(coord), GrowArrow(arrow_2), GrowArrow(arrow_pi4))
        # self.wait(2)

        # ----------------------------
        # # POINT AT (2, 5π/4)
        # r_point = 2
        # theta_point = 5 * PI / 4
        # point_coords = polarplane.polar_to_point(r_point, theta_point)
        # point_dot = Dot(point_coords, color=YELLOW)
        # self.play(Create(point_dot))
        # self.wait(2)
        # # ----------------------------
        # # SHOW CARTESIAN COORDINATES
        # x_cartesian = r_point * np.cos(theta_point)
        # y_cartesian = r_point * np.sin(theta_point)
        # cartesian_coords = MathTex(f"\\left({x_cartesian:.2f}, {y_cartesian:.2f}\\right)")
        # cartesian_coords.scale(0.8)
        # cartesian_coords.shift(3 * RIGHT + DOWN)
        # self.play(Write(cartesian_coords, run_time=2))
        # self.wait(2)
        # # ----------------------------
        # self.play(FadeOut(point_dot), FadeOut(cartesian_coords), FadeOut(question), FadeOut(Title), FadeOut(polar_group))
        

