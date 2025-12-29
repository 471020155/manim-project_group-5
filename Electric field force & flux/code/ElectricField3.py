from manim import *

class ElectricFieldScenes(Scene):
    def construct(self):
        self.camera.background_color = "#0b132b"
        
        
        self.show_scene1()
        self.wait(1)
        
       
        self.clear_scene()
        self.show_scene2()
    
    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def show_scene1(self):
        
        medium_charge = Circle(
            radius=0.6,
            color=RED,
            stroke_width=8,
            fill_color=RED,
            fill_opacity=0.4
        )
        medium_charge.move_to(LEFT * 3 + UP * 1.5)
        
        
        plus_sign = VGroup(
            Line(UP * 0.3, DOWN * 0.3, color=WHITE, stroke_width=12),
            Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE, stroke_width=12)
        )
        plus_sign.move_to(medium_charge.get_center())
        
       
        arrow_length = 1.2
        field_arrows = VGroup()
        for i in range(8):
            angle = i * 45 * DEGREES
            start_point = medium_charge.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.6
            end_point = start_point + np.array([np.cos(angle), np.sin(angle), 0]) * arrow_length
            arrow = Arrow(
                start=start_point,
                end=end_point,
                color=RED,
                stroke_width=5,
                buff=0,
                max_tip_length_to_length_ratio=0.3
            )
            field_arrows.add(arrow)
        
        
        field_law = MathTex(
            r"E = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r^2}",
            font_size=48,
            color=WHITE
        )
        field_law.move_to(RIGHT * 2 + UP * 1.5)
        
        self.play(
            Create(medium_charge),
            Create(plus_sign),
            run_time=1
        )
        self.play(Create(field_arrows), run_time=1.5)
        self.play(Write(field_law), run_time=1.5)
        self.wait(1)
        
      
        depends_text = Text(
            "The electric field depends on:",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        depends_text.scale(0.6)
        depends_text.move_to(DOWN * 0.3)
        
        self.play(Write(depends_text), run_time=1)
        
        
        point1 = Text(
            "• Q: The source charge generating the field",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        point1.scale(0.45)
        point1.next_to(depends_text, DOWN, buff=0.3).align_to(depends_text, LEFT)
        
        point2 = Text(
            "• r: Distance from the charge",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        point2.scale(0.45)
        point2.next_to(point1, DOWN, buff=0.2).align_to(point1, LEFT)
        
        point3 = Text(
            "• ε₀: Permittivity of the medium",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        point3.scale(0.45)
        point3.next_to(point2, DOWN, buff=0.2).align_to(point2, LEFT)
        
        self.play(LaggedStart(
            Write(point1),
            Write(point2),
            Write(point3),
            lag_ratio=0.7
        ), run_time=2)
        
        self.wait(3)
    
    def show_scene2(self):
        
        assumption_text = Text(
            "Assuming we are in free space...",
            font="Arial Black",
            color=YELLOW,
            weight=BOLD
        )
        assumption_text.scale(0.7)
        assumption_text.to_edge(UP, buff=0.5)
        
        self.play(Write(assumption_text), run_time=1)
        
        source_charge = Circle(
            radius=0.5,
            color=RED,
            stroke_width=8,
            fill_color=RED,
            fill_opacity=0.4
        )
        source_charge.move_to(LEFT * 4)
        
        
        source_plus = VGroup(
            Line(UP * 0.25, DOWN * 0.25, color=WHITE, stroke_width=10),
            Line(LEFT * 0.25, RIGHT * 0.25, color=WHITE, stroke_width=10)
        )
        source_plus.move_to(source_charge.get_center())
        
        self.play(
            Create(source_charge),
            Create(source_plus),
            run_time=1
        )
        
        
        initial_radius = 1.0
        white_circle = Circle(
            radius=initial_radius,
            color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )
        white_circle.move_to(source_charge.get_center())
        
        E_label = Text("E", font="Arial Black", color=RED, weight=BOLD)
        E_label.scale(2.5)  
        E_label.move_to(white_circle.get_right() + RIGHT * 0.1)
        
        self.play(Create(white_circle), run_time=1)
        self.play(FadeIn(E_label), run_time=0.5)
        self.wait(0.5)
        
        text1 = Text(
            "As we move away from the charge:",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text1.scale(0.5)
        text1.move_to(RIGHT * 3.5 + UP * 2.2)  
        
        self.play(Write(text1), run_time=1)
        
        
        text2 = Text(
            "1. Electric field strength decreases",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text2.scale(0.45)
        text2.next_to(text1, DOWN, buff=0.2).align_to(text1, LEFT)
        
        self.play(Write(text2), run_time=1)
        
        text3 = Text(
            "2. Sphere surface area increases",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        text3.scale(0.45)
        text3.next_to(text2, DOWN, buff=0.15).align_to(text2, LEFT)
        
        self.play(Write(text3), run_time=1)
        
        area_eq = MathTex(
            r"S = 4\pi r^2",
            font_size=36,
            color=YELLOW
        )
        area_eq.next_to(text3, DOWN, buff=0.3).align_to(text3, LEFT)
        
        self.play(Write(area_eq), run_time=1)
        
        radius1 = 1.8
        white_circle1 = Circle(
            radius=radius1,
            color=WHITE,
            stroke_width=2.5,
            fill_opacity=0
        )
        white_circle1.move_to(source_charge.get_center())
        
        E_label1 = Text("E", font="Arial Black", color=RED, weight=BOLD)
        E_label1.scale(2.5) 
        E_label1.move_to(source_charge.get_center() + RIGHT * radius1)
        
        self.play(
            Transform(white_circle, white_circle1),
            Transform(E_label, E_label1),
            run_time=1.5
        )
        self.wait(0.5)
        
        radius2 = 2.6
        white_circle2 = Circle(
            radius=radius2,
            color=WHITE,
            stroke_width=2.0,
            fill_opacity=0
        )
        white_circle2.move_to(source_charge.get_center())
        
        E_label2 = Text("E", font="Arial Black", color=RED, weight=BOLD)
        E_label2.scale(2.0)  
        E_label2.move_to(source_charge.get_center() + RIGHT * radius2)
        
        self.play(
            Transform(white_circle, white_circle2),
            Transform(E_label, E_label2),
            run_time=1.5
        )
        self.wait(0.5)
        
        radius3 = 3.4
        white_circle3 = Circle(
            radius=radius3,
            color=WHITE,
            stroke_width=1.5,
            fill_opacity=0
        )
        white_circle3.move_to(source_charge.get_center())
        
        E_label3 = Text("E", font="Arial Black", color=RED, weight=BOLD)
        E_label3.scale(1.5)  
        E_label3.move_to(source_charge.get_center() + RIGHT * radius3)
        
        self.play(
            Transform(white_circle, white_circle3),
            Transform(E_label, E_label3),
            run_time=1.5
        )
        self.wait(1)
        
        radius4 = 4.2
        white_circle4 = Circle(
            radius=radius4,
            color=WHITE,
            stroke_width=1.0,
            fill_opacity=0
        )
        white_circle4.move_to(source_charge.get_center())
        
        E_label4 = Text("E", font="Arial Black", color=RED, weight=BOLD)
        E_label4.scale(0.8)  
        E_label4.move_to(source_charge.get_center() + RIGHT * radius4)
        
        self.play(
            Transform(white_circle, white_circle4),
            Transform(E_label, E_label4),
            run_time=1.5
        )
        self.wait(1)
        
        
        observation = Text(
            "It is observed that:",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        observation.scale(0.5)
        observation.next_to(area_eq, DOWN, buff=0.5).align_to(area_eq, LEFT)  
        
        product_eq = MathTex(
            r"E \cdot S \approx \frac{Q}{\varepsilon_0}",
            font_size=42,
            color=GREEN
        )
        product_eq.next_to(observation, DOWN, buff=0.3).align_to(observation, LEFT)
        
        conclusion = Text(
            "This shows something constant with constant charge and medium,",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        conclusion.scale(0.35)
        conclusion.next_to(product_eq, DOWN, buff=0.3).align_to(product_eq, LEFT)
        
        called_text = Text(
            "called",
            font="Arial Black",
            color=WHITE,
            weight=BOLD
        )
        called_text.scale(0.45)
        called_text.next_to(conclusion, DOWN, buff=0.2).align_to(conclusion, LEFT)
        
        flux_name = Text(
            "Electric Flux (Φ)",
            font="Times New Roman",
            color=YELLOW,
            weight=BOLD
        )
        flux_name.scale(0.5)
        flux_name.next_to(called_text, RIGHT, buff=0.1)
        
        self.play(Write(observation), run_time=1)
        self.play(Write(product_eq), run_time=1.5)
        self.play(Write(conclusion), run_time=1.5)
        self.play(Write(called_text), run_time=0.5)
        self.play(Write(flux_name), run_time=1)
        
        self.wait(4)

# manim -pql electric_field_scenes.py ElectricFieldScenes