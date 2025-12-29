from manim import *
import numpy as np

BACKGROUND_COLOR = "#0b132b"
FIELD_COLOR = RED
DIELECTRIC_COLOR = GRAY
Q_COLOR = RED

class DFieldWithDielectric(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        center = ORIGIN

        # ================= TEXT BLOCK (RIGHT SIDE) =================
        text_1 = Text(
            "That's why, when we calculate the flux in the presence of a material,",
            font_size=20,
            color=WHITE
        )

        text_2 = Text(
            "we don't use the electric field E —",
            font_size=20,
            color=WHITE
        )

        text_3 = Text(
            "we use the displacement field D.",
            font_size=20,
            color=WHITE
        )

        flux_symbol = Text("Φ = ", font_size=26, color=YELLOW)
        integral = Text("∮ D⃗ · dA⃗ = Q_free", font_size=26, color=YELLOW, font="Times New Roman")
        
        eq_group = VGroup(flux_symbol, integral).arrange(RIGHT, buff=0.2)

        text_4 = Text(
            "This means that the flux calculated using D directly represents",
            font_size=20,
            color=WHITE
        )

        text_5 = Text(
            "the amount of free charge enclosed by the surface",
            font_size=20,
            color=WHITE
        )

        text_group = VGroup(
            text_1, text_2, text_3, eq_group, text_4, text_5
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        text_group.to_edge(RIGHT).shift(LEFT * 0.3)

        self.add(text_group)

        # ================= CHARGE =================
        charge_radius = 0.5

        charge = VGroup(
            Dot(center, radius=charge_radius, color=Q_COLOR, fill_opacity=0.25),
            Dot(center, radius=0.35, color=Q_COLOR),
            Text("+Q", font_size=20, color=WHITE).move_to(center)
        )

        # ================= DIELECTRIC =================
        dielectric_inner = charge_radius * 0.6
        dielectric_outer = 2.2

        dielectric = Annulus(
            inner_radius=dielectric_inner,
            outer_radius=dielectric_outer,
            color=DIELECTRIC_COLOR,
            fill_opacity=0.35,
            stroke_width=0
        ).move_to(center)

        # ================= FIELD LINES =================
        num_lines = 28
        field_lines = VGroup()

        for i in range(num_lines):
            angle = i * TAU / num_lines
            direction = np.array([np.cos(angle), np.sin(angle), 0])

            line = Arrow(
                center + direction * charge_radius,
                center + direction * (dielectric_outer + 0.7),
                buff=0,
                color=FIELD_COLOR,
                stroke_width=4,
                tip_length=0.2
            )
            field_lines.add(line)

        # ================= GROUP & TRANSFORM =================
        full_system = VGroup(charge, dielectric, field_lines)
        full_system.scale(0.65)  # Smaller scale
        
        # Move to left edge
        full_system.to_edge(LEFT, buff=0.5)

        # ================= ANIMATION =================
        self.play(FadeIn(charge))
        self.play(FadeIn(dielectric))
        self.play(Create(field_lines), run_time=2)
        self.play(dielectric.animate.set_fill(opacity=0.15), run_time=1.5)

        self.wait(3)