from manim import *

class MaterialInField(Scene):
    def construct(self):
        self.camera.background_color = "#0b132b"
        
        title_font_size = 42
        question_font_size = 36
        text_font_size = 30
        
        free_space_text = Text(
            "All of this was in free space…",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).to_edge(UP + LEFT).shift(DOWN * 0.5 + RIGHT * 0.5)
        
        self.play(Write(free_space_text), run_time=1.0)
        self.wait(0.5)
        
        question1 = Text(
            "but what if we place a material",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(free_space_text, DOWN, buff=0.3).align_to(free_space_text, LEFT)
        
        question2 = Text(
            "between the charges?",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(question1, DOWN, buff=0.2).align_to(question1, LEFT)
        
        self.play(Write(question1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(question2), run_time=0.8)
        self.wait(0.5)
        
        main_question1 = Text(
            "Will the electric flux",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(question2, DOWN, buff=0.4).align_to(question2, LEFT)
        
        main_question2 = Text(
            "still remain the same?",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(main_question1, DOWN, buff=0.2).align_to(main_question1, LEFT)
        
        self.play(
            FadeOut(free_space_text),
            FadeOut(question1),
            FadeOut(question2),
            run_time=0.8
        )
        
        self.play(Write(main_question1), run_time=0.8)
        self.play(Write(main_question2), run_time=0.8)
        self.wait(0.8)
        
        alternative_question = Text(
            "Or does the material change the game?",
            font_size=question_font_size,
            color="#FF6B6B",
            font="Arial",
            weight="BOLD"
        ).next_to(main_question1, DOWN, buff=0.2).align_to(main_question1, LEFT)
        
        self.play(
            Transform(main_question2, alternative_question),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        answer_text = Text(
            "To answer that question, we first need to understand",
            font_size=text_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(main_question2, DOWN, buff=0.4).align_to(main_question2, LEFT)
        
        conclusion_text = Text(
            "what actually happens inside a material",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(answer_text, DOWN, buff=0.3).align_to(answer_text, LEFT)
        
        final_text = Text(
            "when it is subjected to an electric field.",
            font_size=question_font_size,
            color=WHITE,
            font="Arial",
            weight="BOLD"
        ).next_to(conclusion_text, DOWN, buff=0.2).align_to(conclusion_text, LEFT)
        
        self.play(
            FadeOut(main_question1),
            run_time=0.6
        )
        
        self.play(Write(answer_text), run_time=0.8)
        self.wait(0.3)
        self.play(Write(conclusion_text), run_time=0.8)
        self.wait(0.3)
        self.play(Write(final_text), run_time=0.8)
        
        self.wait(2.0)
        
        self.play(
            FadeOut(answer_text),
            FadeOut(conclusion_text),
            FadeOut(final_text),
            FadeOut(main_question2),
            run_time=1.0
        )