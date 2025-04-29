import reflex as rx

color_primary = "#2563eb"
hover_primary = "#2055c9"
trans_time = "0.3s ease"
letter_bold = "0.7px"

def color_text():
    return rx.color_mode_cond(
        light="#1f2937",
        dark="#f9fafb",
    ),

def color_text_light():
    return rx.color_mode_cond(
        light="#6b7280",
        dark="#9ca3af",
    ),

def background():
    return rx.color_mode_cond(
        light="#ffffff",
        dark="#111827",
    ),

def color_surface():
    return rx.color_mode_cond(
        light="#f3f4f6",
        dark="#1f2937",
    ),

def btn_color_secondary():
    return rx.color_mode_cond(
        light="#d9dadb",
        dark="#273445",
    ),

def btn_color_secondary_hover():
    return rx.color_mode_cond(
        light="#c5c7c9",
        dark="#333f51",
    ),

