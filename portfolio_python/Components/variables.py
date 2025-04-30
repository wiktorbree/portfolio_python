import reflex as rx

color_primary = "#EB5E28"
hover_primary = "#cd4f1f"
trans_time = "0.3s ease"
letter_bold = "0.7px"

def color_text():
    return rx.color_mode_cond(
        light="#403D39",
        dark="#CCC5B9",
    ),

def color_text_light():
    return rx.color_mode_cond(
        light="#5b5752",
        dark="#b0aaa0",
    ),

def background():
    return rx.color_mode_cond(
        light="#FFFCF2",
        dark="#252422",
    ),

def color_surface():
    return rx.color_mode_cond(
        light="#efe7da",
        dark="#403D39",
    ),

def btn_color_secondary():
    return rx.color_mode_cond(
        light="#d8d1c4",
        dark="#58534c",
    ),
