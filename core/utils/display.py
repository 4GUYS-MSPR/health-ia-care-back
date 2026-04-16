from django.utils.html import format_html

def display_video(size: int, field):
    if field:
        return format_html("""
            <video width="{}" controls style="border-radius:4px;">
                <source src="{}" type="video/mp4">
            </video>
        """, size, field.url)
    return "No video"
