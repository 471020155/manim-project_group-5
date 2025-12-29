from manim import *

class ElectricDisplacementIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0b132b"
        
        title_font_size = 42
        question_font_size = 36
        text_font_size = 30
        
        # Line 1: So far, we've been describing...
        line1 = Text(
            "So far, we've been describing",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).shift(UP * 1.5)  # Center horizontally
        
        line1_cont = Text(
            "the electric flux using the electric field E.",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(line1, DOWN, buff=0.2)
        
        self.play(Write(line1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(line1_cont), run_time=0.8)
        self.wait(0.5)
        
        # Line 2: But is E always the best quantity...
        line2 = Text(
            "But is E always the best quantity",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(line1_cont, DOWN, buff=0.4)
        
        line2_cont = Text(
            "to describe flux — especially inside materials?",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(line2, DOWN, buff=0.2)
        
        self.play(Write(line2), run_time=0.8)
        self.play(Write(line2_cont), run_time=0.8)
        self.wait(0.8)
        
        # Fade out first section
        self.play(
            FadeOut(line1),
            FadeOut(line1_cont),
            FadeOut(line2),
            FadeOut(line2_cont),
            run_time=0.8
        )
        
        # Line 3: Or is there another field...
        line3 = Text(
            "Or is there another field",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).shift(UP * 1.5)
        
        line3_cont = Text(
            "that can describe it more naturally?",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(line3, DOWN, buff=0.2)
        
        self.play(Write(line3), run_time=0.8)
        self.play(Write(line3_cont), run_time=0.8)
        self.wait(1.0)
        
        # Fade out question
        self.play(
            FadeOut(line3),
            FadeOut(line3_cont),
            run_time=0.6
        )
        
        # Answer section
        answer_line1 = Text(
            "To answer this question, we need to introduce",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).shift(UP * 1.5)
        
        answer_line2 = Text(
            "a new field that separates the effect of free charges",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(answer_line1, DOWN, buff=0.2)
        
        answer_line3 = Text(
            "from the response of the material —",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(answer_line2, DOWN, buff=0.2)
        
        final_line = Text(
            "the electric displacement field, D.",
            font_size=question_font_size,
            color="#FF6B6B",
            font="Arial",
            weight="BOLD"
        ).next_to(answer_line3, DOWN, buff=0.3)
        
        self.play(Write(answer_line1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(answer_line2), run_time=0.8)
        self.wait(0.3)
        self.play(Write(answer_line3), run_time=0.8)
        self.wait(0.3)
        self.play(Write(final_line), run_time=0.8)
        
        self.wait(2.0)
        
        # Fade out everything
        self.play(
            FadeOut(answer_line1),
            FadeOut(answer_line2),
            FadeOut(answer_line3),
            FadeOut(final_line),
            run_time=1.0
        )