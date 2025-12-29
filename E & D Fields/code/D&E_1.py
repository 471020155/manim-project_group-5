from manim import *

BACKGROUND_COLOR = "#0b132b"
TEXT_COLOR = WHITE
NEGATIVE_COLOR = "#5DADE2"
POSITIVE_COLOR = "#EC7063"
ATOM_OUTLINE_COLOR = WHITE
FIELD_COLOR = RED
INTERNAL_FIELD_COLOR = YELLOW

SIGN_FONT_SIZE = 25
SPHERE_RADIUS = 0.2

class CombinedSceneSimultaneous(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        atom_radius = 0.7
        separation_gap = 0.25

        overall_shift = LEFT * 5.0
        vertical_shift = UP * 0.5
        
        atom_center = ORIGIN + overall_shift + vertical_shift
        
        # Create all atom elements (FIRST - create but don't show yet)
        atom_outline = Circle(
            radius=atom_radius, 
            stroke_width=3, 
            color=ATOM_OUTLINE_COLOR
        ).move_to(atom_center)

        negative_sphere = Circle(
            radius=SPHERE_RADIUS,
            color=NEGATIVE_COLOR,
            fill_color=NEGATIVE_COLOR,
            fill_opacity=1,
            stroke_width=2
        ).move_to(atom_center + LEFT * (separation_gap/2))

        negative_sign = Text("-", font_size=SIGN_FONT_SIZE, color=BACKGROUND_COLOR).move_to(negative_sphere.get_center())

        positive_sphere = Circle(
            radius=SPHERE_RADIUS,
            color=POSITIVE_COLOR,
            fill_color=POSITIVE_COLOR,
            fill_opacity=1,
            stroke_width=2
        ).move_to(atom_center + RIGHT * (separation_gap/2))

        positive_sign = Text("+", font_size=SIGN_FONT_SIZE, color=BACKGROUND_COLOR).move_to(positive_sphere.get_center())

        original_atom = VGroup(
            atom_outline,
            negative_sphere,
            positive_sphere,
            negative_sign,
            positive_sign
        )
        
        # Create arrows for later
        arrows = VGroup()
        x_start = -7.0
        x_end = -3.0
        y_base = atom_center[1] - 1.2
        
        for i in range(4):
            y = y_base + i * 0.7
            arrow = Arrow(
                start=[x_start, y, 0],
                end=[x_end, y, 0],
                color=FIELD_COLOR,
                stroke_width=5,
                buff=0,
                tip_length=0.2
            )
            arrows.add(arrow)

        external_field_label = Text("E_ext", font_size=24, color=FIELD_COLOR)
        external_field_label.next_to(arrows[2], RIGHT, buff=0.5).shift(UP * 0.1)

        # Create text elements
        line1 = Text(
            "E_total = E_ext - E_int",
            font_size=28,
            color=YELLOW,
            font="Times New Roman",
            weight="BOLD"
        ).to_edge(UP, buff=0.5).shift(RIGHT * 0.5)
        
        line2 = Text(
            "Since the internal field is caused by polarization,",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        ).next_to(line1, DOWN, buff=0.3).align_to(line1, LEFT)
        
        line3 = Text(
            "P = -ε₀ E_int",
            font_size=28,
            color=YELLOW,
            font="Times New Roman",
            weight="BOLD"
        ).next_to(line2, DOWN, buff=0.3).align_to(line2, LEFT)
        
        line4 = Text(
            "E_total = E_ext + P/ε₀",
            font_size=28,
            color=YELLOW,
            font="Times New Roman",
            weight="BOLD"
        ).next_to(line3, DOWN, buff=0.4).align_to(line3, LEFT)
        
        line5 = Text(
            "To separate the free charge contribution from",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        ).next_to(line4, DOWN, buff=0.4).align_to(line4, LEFT)
        
        line6 = Text(
            "the material response, we define a new field:",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        ).next_to(line5, DOWN, buff=0.2).align_to(line5, LEFT)
        
        line7 = Text(
            "D = ε₀ E_total + P",
            font_size=28,
            color=YELLOW,
            font="Times New Roman",
            weight="BOLD"
        ).next_to(line6, DOWN, buff=0.3).align_to(line6, LEFT)
        
        line8 = Text(
            "This leads to:",
            font_size=24,
            color=TEXT_COLOR,
            font="Arial"
        ).next_to(line7, DOWN, buff=0.4).align_to(line7, LEFT)
        
        line9 = Text(
            "D = ε₀ E_ext",
            font_size=28,
            color=YELLOW,
            font="Times New Roman",
            weight="BOLD"
        ).next_to(line8, DOWN, buff=0.3).align_to(line8, LEFT)
        
        # Start with showing BOTH atom and first text line
        self.play(
            FadeIn(original_atom, run_time=0.3),
            Write(line1, run_time=0.4)
        )
        self.wait(0.2)
        
        # Show arrows with second line
        self.play(
            *[GrowArrow(a) for a in arrows], 
            Write(external_field_label, run_time=0.5),
            Write(line2, run_time=0.4)
        )
        self.wait(0.15)
        
        # Continue with text animation while atom is visible
        self.play(Write(line3), run_time=0.4)
        self.wait(0.15)
        
        # Quick transformation to ellipse with next line
        ellipse_width = 2.2
        ellipse_height = 1.4
        
        ellipse_outline = Ellipse(
            width=ellipse_width,
            height=ellipse_height,
            color=ATOM_OUTLINE_COLOR,
            stroke_width=3
        ).move_to(atom_center)
        
        margin = 0.3
        max_x_position = ellipse_width/2 - SPHERE_RADIUS - margin
        
        negative_sphere_new = Circle(
            radius=SPHERE_RADIUS,
            color=NEGATIVE_COLOR,
            fill_color=NEGATIVE_COLOR,
            fill_opacity=1,
            stroke_width=2
        ).move_to(ellipse_outline.get_center() + LEFT * (max_x_position * 0.9))
        
        negative_sign_new = Text("-", font_size=SIGN_FONT_SIZE, color=BACKGROUND_COLOR).move_to(negative_sphere_new.get_center())
        
        positive_sphere_new = Circle(
            radius=SPHERE_RADIUS,
            color=POSITIVE_COLOR,
            fill_color=POSITIVE_COLOR,
            fill_opacity=1,
            stroke_width=2
        ).move_to(ellipse_outline.get_center() + RIGHT * (max_x_position * 0.9))
        
        positive_sign_new = Text("+", font_size=SIGN_FONT_SIZE, color=BACKGROUND_COLOR).move_to(positive_sphere_new.get_center())
        
        # Transform atom while showing next line
        self.play(
            ReplacementTransform(atom_outline, ellipse_outline),
            ReplacementTransform(negative_sphere, negative_sphere_new),
            ReplacementTransform(positive_sphere, positive_sphere_new),
            ReplacementTransform(negative_sign, negative_sign_new),
            ReplacementTransform(positive_sign, positive_sign_new),
            Write(line4, run_time=0.4),
            run_time=0.5
        )
        self.wait(0.15)
        
        # Quick ellipse background
        ellipse_background = Ellipse(
            width=ellipse_width - 0.15,
            height=ellipse_height - 0.15,
            color=ATOM_OUTLINE_COLOR,
            fill_color=ATOM_OUTLINE_COLOR,
            fill_opacity=0.06,
            stroke_width=0
        ).move_to(ellipse_outline.get_center())
        
        # Show next line with ellipse background
        self.play(
            FadeIn(ellipse_background, run_time=0.2),
            Write(line5, run_time=0.4)
        )
        self.wait(0.1)
        
        # Quick yellow arrow with next line
        yellow_arrow_start = positive_sphere_new.get_center() + LEFT * SPHERE_RADIUS * 0.9
        yellow_arrow_end = negative_sphere_new.get_center() + RIGHT * SPHERE_RADIUS * 0.9
        
        yellow_arrow = Arrow(
            start=yellow_arrow_start,
            end=yellow_arrow_end,
            color=INTERNAL_FIELD_COLOR,
            stroke_width=4,
            buff=0,
            tip_length=0.15
        )
        
        yellow_arrow_label = Text("E_int", font_size=20, color=INTERNAL_FIELD_COLOR)
        yellow_arrow_label.next_to(yellow_arrow, UP, buff=0.1)
        
        self.play(
            Create(yellow_arrow, run_time=0.3),
            Write(yellow_arrow_label, run_time=0.3),
            Write(line6, run_time=0.4)
        )
        self.wait(0.1)
        
        # Continue with remaining text
        self.play(Write(line7), run_time=0.4)
        self.wait(0.15)
        self.play(Write(line8), run_time=0.25)
        self.wait(0.1)
        self.play(Write(line9), run_time=0.4)
        
        # Keep everything static
        self.wait(4)

# For testing
if __name__ == "__main__":
    from manim import config
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    config.quality = "high_quality"
    scene = CombinedSceneSimultaneous()
    scene.render()