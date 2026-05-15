import gradio as gr

from ui.state import STATE

from configs.paths import SDG_IMAGE_DIR, GRI_IMAGE_DIR

# Filter SDG
sdg_icons = {
    i: f"{SDG_IMAGE_DIR}/E_PRINT_{i:02d}.jpg"
    for i in range(1, 18)
}

sdg_images = [sdg_icons[i] for i in range(1, 18)]

def filter_sdg(evt: gr.SelectData):

    df = STATE.get("df")

    sdg_num = evt.index + 1
    pattern = f"SDG_{sdg_num}:"

    filtered = df[df["17 SDG Alignment"].astype(str).str.contains(pattern, na=False)]

    title = f"Showing results for SDG {sdg_num}"

    return filtered, title


# Filter GRI
gri_topics = ["General", "Economic", "Environmental", "Social"]

gri_images = [
    f"{GRI_IMAGE_DIR}/General.PNG",
    f"{GRI_IMAGE_DIR}/Economic.PNG",
    f"{GRI_IMAGE_DIR}/Environmental.PNG",
    f"{GRI_IMAGE_DIR}/Social.PNG"
]

def filter_gri(evt: gr.SelectData):

    df = STATE.get("df")

    selected_idx = evt.index
    topic = gri_topics[selected_idx]   # Social / Economic / ...

    filtered = df[df["GRI Topic Alignment"].astype(str) == topic]

    title = f"Showing results for GRI Topic: {topic}"

    return filtered, title


# TOGGLE FILTERS
def toggle_filters(tasks):

    if tasks is None:
        tasks = []

    if isinstance(tasks, str):
        tasks = [tasks]

    show_sdg = "17 SDG Alignment" in tasks
    show_gri = "GRI Topic Alignment" in tasks

    return (
        gr.update(visible=show_sdg),
        gr.update(visible=show_gri)
    )