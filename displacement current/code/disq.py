from manim import *
import numpy as np

BACKGROUND_COLOR = "#0b132b"
TEXT_COLOR = WHITE
HIGHLIGHT_COLOR = YELLOW
QUESTION_COLOR = RED

class FluxQuestionFastV3(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Initial text lines - normal font (not Roman)
        line1 = Text(
            "Up to this point, we've connected the electric flux",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        )
        
        line2 = Text(
            "to the displacement field D instead of E,",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        )
        
        line3 = Text(
            "and we've seen how this gives a clearer description",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        )
        
        line4 = Text(
            "of free charges.",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        )
        
        # Group first part
        first_part = VGroup(line1, line2, line3, line4)
        first_part.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        first_part.center()
        
        # Animate first part faster
        self.play(Write(line1), run_time=0.6)
        self.wait(0.2)
        self.play(Write(line2), run_time=0.5)
        self.wait(0.2)
        self.play(Write(line3), run_time=0.5)
        self.wait(0.2)
        self.play(Write(line4), run_time=0.4)
        self.wait(1.5)  # PAUSE WHILE TEXT IS VISIBLE
        
        # Clear first part
        self.play(FadeOut(first_part, run_time=0.5))
        self.wait(0.3)  # Short pause before next
        
        # But here comes an important question…
        question_intro = Text(
            "But here comes an important question…",
            font_size=28,
            color=HIGHLIGHT_COLOR,
            font="Arial"
        )
        question_intro.center()
        
        self.play(Write(question_intro, run_time=0.8))
        self.wait(1.5)  # PAUSE WHILE TEXT IS VISIBLE
        
        # Clear question intro
        self.play(FadeOut(question_intro, run_time=0.5))
        self.wait(0.3)  # Short pause before next
        
        # Main question - normal font
        question_part1 = Text(
            "If D represents the effect of free charges,",
            font_size=26,
            color=QUESTION_COLOR,
            font="Arial"
        )
        
        question_part2 = Text(
            "then how does current flow in regions",
            font_size=26,
            color=QUESTION_COLOR,
            font="Arial"
        )
        
        question_part3 = Text(
            "where there are no free charges at all?",
            font_size=26,
            color=QUESTION_COLOR,
            font="Arial"
        )
        
        example = Text(
            "Like inside a capacitor?",
            font_size=26,
            color=YELLOW,
            font="Arial"
        )
        
        # Arrange question
        question_group = VGroup(question_part1, question_part2, question_part3, example)
        question_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        question_group.center()
        
        # Animate question
        self.play(Write(question_part1, run_time=0.6))
        self.wait(0.4)
        self.play(Write(question_part2, run_time=0.5))
        self.wait(0.3)
        self.play(Write(question_part3, run_time=0.6))
        self.wait(0.4)
        self.play(Write(example, run_time=0.5))
        self.wait(1.5)  # PAUSE AFTER ALL TEXT APPEARS
        
        # Highlight key parts
        highlight_rect1 = SurroundingRectangle(question_part1, color=YELLOW, buff=0.1)
        self.play(Create(highlight_rect1, run_time=0.5))
        self.wait(0.8)
        self.play(FadeOut(highlight_rect1, run_time=0.4))
        self.wait(0.5)
        
        highlight_rect2 = SurroundingRectangle(question_part3, color=YELLOW, buff=0.1)
        self.play(Create(highlight_rect2, run_time=0.5))
        self.wait(1.5)  # FINAL PAUSE WITH HIGHLIGHT
        
        # Final fade out
        self.play(FadeOut(highlight_rect2, run_time=0.4))
        self.play(FadeOut(question_group, run_time=0.8))
        self.wait(0.5)

if __name__ == "__main__":
    from manim import config
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    config.quality = "high_quality"
    scene = FluxQuestionFastV3()
    scene.render()