import reflex as rx

def color_primary():
    return "#2563eb"

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