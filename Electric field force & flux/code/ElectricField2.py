from manim import *

class ElectricFieldInteraction(Scene):
    def construct(self):
        self.camera.background_color = "#0b132b"
        
        big_positive = Circle(
            radius=0.9,
            color=RED,
            stroke_width=10,
            fill_color=RED,
            fill_opacity=0.3
        )
        big_positive.move_to(LEFT * 3 + UP * 1.5)
        
        big_plus = VGroup(
            Line(UP * 0.45, DOWN * 0.45, color=WHITE, stroke_width=15),
            Line(LEFT * 0.45, RIGHT * 0.45, color=WHITE, stroke_width=15)
        )
        big_plus.move_to(big_positive.get_center())
        
        big_label = Text("+", font="Arial Black", color=WHITE, weight=BOLD)
        big_label.scale(1.5)
        big_label.move_to(big_positive.get_center())
        
        self.play(
            Create(big_positive),
            Create(big_plus),
            FadeIn(big_label),
            run_time=1
        )
        
        arrow_length = 1.5
        positive_arrows = VGroup()
        for i in range(10):
            angle = i * 36 * DEGREES
            start_point = big_positive.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.9
            end_point = start_point + np.array([np.cos(angle), np.sin(angle), 0]) * arrow_length
            arrow = Arrow(
                start=start_point,
                end=end_point,
                color=RED,
                stroke_width=6,
                buff=0,
                max_tip_length_to_length_ratio=0.3
            )
            positive_arrows.add(arrow)
        
        self.play(Create(positive_arrows), run_time=1)
        
        small_positive = Circle(
            radius=0.3,
            color=RED,
            stroke_width=6,
            fill_color=RED,
            fill_opacity=0.7
        )
        small_positive.move_to(LEFT * 1.5 + UP * 1.5)
        
        small_label = Text("q", font="Arial Black", color=WHITE, weight=BOLD)
        small_label.scale(0.8)
        small_label.move_to(small_positive.get_center())
        
        text1 = Text(
            "Like charges repel each other",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text1.scale(0.6)
        text1.move_to(DOWN * 1.5)
        
        text2 = Text(
            "Positive charge moves in direction of electric field",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text2.scale(0.45)
        text2.next_to(text1, DOWN, buff=0.2)
        
        self.play(
            Create(small_positive),
            FadeIn(small_label),
            Write(text1),
            Write(text2),
            run_time=0.5
        )
        
        self.play(
            small_positive.animate.shift(RIGHT * 3 + UP * 0.3),
            small_label.animate.shift(RIGHT * 3 + UP * 0.3),
            run_time=2
        )
        
        self.wait(0.5)
        
        self.play(
            FadeOut(small_positive),
            FadeOut(small_label),
            FadeOut(text1),
            FadeOut(text2),
            run_time=1
        )
        
        small_negative = Circle(
            radius=0.3,
            color=BLUE,
            stroke_width=6,
            fill_color=BLUE,
            fill_opacity=0.7
        )
        small_negative.move_to(RIGHT * 2 + DOWN * 0.5)
        
        small_neg_label = Text("-q", font="Arial Black", color=WHITE, weight=BOLD)
        small_neg_label.scale(0.8)
        small_neg_label.move_to(small_negative.get_center())
        
        text3 = Text(
            "Opposite charges attract each other",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text3.scale(0.6)
        text3.move_to(DOWN * 1.5)
        
        text4 = Text(
            "Negative charge moves opposite to direction of electric field",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text4.scale(0.45)
        text4.next_to(text3, DOWN, buff=0.2)
        
        self.play(
            Create(small_negative),
            FadeIn(small_neg_label),
            Write(text3),
            Write(text4),
            run_time=0.5
        )
        
        self.play(
            small_negative.animate.shift(LEFT * 2.5 + UP * 0.8),
            small_neg_label.animate.shift(LEFT * 2.5 + UP * 0.8),
            run_time=2
        )
        
        self.wait(0.5)
        
        self.play(
            FadeOut(small_negative),
            FadeOut(small_neg_label),
            FadeOut(text3),
            FadeOut(text4),
            run_time=1
        )
        
        formula_title = Text(
            "Electric Force Formula:",
            font="Times New Roman",
            color=YELLOW,
            weight=BOLD
        )
        formula_title.scale(0.7)
        formula_title.move_to(DOWN * 1.5)
        
        formula = MathTex(
            r"\vec{F} = q \vec{E}",
            font_size=72,
            color=WHITE
        )
        formula.set_color_by_tex_to_color_map({
            r"\vec{F}": YELLOW,
            r"\vec{E}": GREEN,
            "q": WHITE
        })
        formula.next_to(formula_title, DOWN, buff=0.5)
        
        self.play(Write(formula_title), run_time=0.5)
        self.play(Write(formula), run_time=1)
        
        self.wait(2)
        
        self.play(
            FadeOut(big_positive),
            FadeOut(big_plus),
            FadeOut(big_label),
            FadeOut(positive_arrows),
            FadeOut(formula_title),
            FadeOut(formula),
            run_time=1
        )