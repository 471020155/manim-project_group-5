from manim import *

class ElectricFieldAnimation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR = "#0b132b"
        
        title = Text(
            "Have you ever wondered how an electric field is generated?",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        title.scale(0.6)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title))
        self.wait(1)
        
        
        positive_circle = Circle(
            radius=1.0,
            color=RED,
            stroke_width=10,
            fill_color=RED,
            fill_opacity=0.3
        )
        positive_circle.shift(LEFT * 2.5)  
        
       
        plus_sign = VGroup(
            Line(UP * 0.5, DOWN * 0.5, color=WHITE, stroke_width=15),
            Line(LEFT * 0.5, RIGHT * 0.5, color=WHITE, stroke_width=15)
        )
        plus_sign.move_to(positive_circle.get_center())
        
        
        positive_arrows = VGroup()
        arrow_length = 1.5  
        
        for i in range(10):
            angle = i * 36 * DEGREES  # 360/10 = 36 
            
            
            start_point = positive_circle.get_center() + \
                         np.array([np.cos(angle), np.sin(angle), 0]) * 1.0
            
            
            end_point = start_point + \
                       np.array([np.cos(angle), np.sin(angle), 0]) * arrow_length
            
            
            arrow = Arrow(
                start=start_point,
                end=end_point,
                color=RED,
                stroke_width=8,
                buff=0,
                max_tip_length_to_length_ratio=0.3
            )
            positive_arrows.add(arrow)
        
 
        
        negative_circle = Circle(
            radius=1.0,
            color=BLUE,
            stroke_width=10,
            fill_color=BLUE,
            fill_opacity=0.3
        )
        negative_circle.shift(RIGHT * 2.5) 
        
       
        minus_sign = Line(
            LEFT * 0.5, RIGHT * 0.5,
            color=WHITE,
            stroke_width=15
        )
        minus_sign.move_to(negative_circle.get_center())
        
        negative_arrows = VGroup()
        for i in range(10):
            angle = i * 36 * DEGREES  # 360/10 = 36 درجة لكل سهم
            
            start_point = negative_circle.get_center() + \
                         np.array([np.cos(angle), np.sin(angle), 0]) * (1.0 + arrow_length)
            
            end_point = negative_circle.get_center() + \
                       np.array([np.cos(angle), np.sin(angle), 0]) * 1.0
            
            arrow = Arrow(
                start=start_point,
                end=end_point,
                color=BLUE,
                stroke_width=8,
                buff=0,
                max_tip_length_to_length_ratio=0.3
            )
            negative_arrows.add(arrow)
        
        
        positive_label = Text("+", font="Arial Black", color=WHITE, weight=BOLD)
        positive_label.scale(1.5)
        positive_label.move_to(positive_circle.get_center())
        
        negative_label = Text("-", font="Arial Black", color=WHITE, weight=BOLD)
        negative_label.scale(1.5)
        negative_label.move_to(negative_circle.get_center())
        
       
        subtitle = Text(
            "We have two separate electric poles that affect their surroundings\nwith a force known as \"Electric Field\"",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        subtitle.scale(0.45)  
        subtitle.to_edge(DOWN, buff=0.5)  
        
       
        self.play(
            Create(positive_circle),
            Create(negative_circle),
            run_time=1.5
        )
        
        self.play(
            Create(plus_sign),
            Create(minus_sign),
            run_time=1
        )
        
        
        self.play(
            FadeIn(positive_label),
            FadeIn(negative_label),
            run_time=0.5
        )
        
        for i in range(10):
            self.play(
                Create(positive_arrows[i]),
                Create(negative_arrows[i]),
                run_time=0.3
            )
        
        
        self.play(Write(subtitle))
        
        
        for _ in range(3):
            self.play(
                positive_arrows.animate.set_stroke(opacity=1),
                negative_arrows.animate.set_stroke(opacity=1),
                run_time=0.5
            )
            self.play(
                positive_arrows.animate.set_stroke(opacity=0.7),
                negative_arrows.animate.set_stroke(opacity=0.7),
                run_time=0.5
            )
        
       
        self.wait(3)


# manim -pql electric_field.py ElectricFieldAnimation