from ui.interface import build_interface

demo = build_interface()

demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    ssr_mode=False
)