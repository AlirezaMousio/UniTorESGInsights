import gradio as gr

from ui.filters import (
    sdg_images,
    gri_images,
    filter_sdg,
    filter_gri,
    toggle_filters
)

from ui.gradio_functions import (
    load_pdf,
    change_page,
    load_pdf_wrapper,
    change_page,
    highlight,
    upload_csv1,
    upload_csv2,
    run_sa_wrapper,
    set_task, 
    run_task,
    run_selected_tasks
)

def build_interface():
    with gr.Blocks() as demo:

        gr.Markdown("# An Interactive Human–AI Hierarchical Multi-Level System for Sustainability Report Paragraph-Level ESG Analysis")

        gr.Image(
            value="assets/logo.png",
            label="UniTor ESG Insights System",
            interactive=False,
            #width=600
        )
        gr.Image(
            value="assets/architecture.png",
            label="Architecture Overview",
            interactive=False,
            #width=600
        )

        gr.Image(
            value="assets/workflow.png",
            label="Human-in-the-Loop Interactive Workflow Overview",
            interactive=False,
            #width=600
        )

        # =========================
        # STAGE 1: PDF → CSV
        # =========================
        gr.Markdown("## Step 1: Upload PDF and Extract Data")

        file = gr.File(label="Upload PDF")
        load_btn = gr.Button("Load PDF", variant="primary")

        extracted_download = gr.File(label="Download Extracted CSV")

        upload_csv_1 = gr.File(label="(Optional) Upload Custom CSV")

        with gr.Row():
            prev = gr.Button("⬅", variant="primary")
            next = gr.Button("➡", variant="primary")

        with gr.Row():
            img = gr.Image()
            table = gr.Dataframe(interactive=True)

        text = gr.Markdown()

        # =========================
        # STAGE 2: SA
        # =========================
        gr.Markdown("## Step 2: Sustainability Frameworks (GRI & SDG) Alignment (SFA) for Relevant/Irrelevant Classification Task")

        sa_btn = gr.Button("Run SFA", variant="primary")

        sa_download = gr.File(label="Download SFA Results")

        chart1 = gr.Plot(label="Distribution")

        upload_csv_2 = gr.File(label="(Optional) Upload Modified SFA CSV")

        # =========================
        # CONNECTIONS
        # =========================
        # --- STEP 1 ---
        load_btn.click(load_pdf_wrapper, file, [img, table, extracted_download])

        next.click(lambda: change_page(1), outputs=[img, table])
        prev.click(lambda: change_page(-1), outputs=[img, table])

        table.select(highlight, outputs=text)

        # Optional CSV override (Stage 1)
        upload_csv_1.upload(upload_csv1, upload_csv_1, table)

        # --- STEP 2 ---
        sa_btn.click(
            run_sa_wrapper,
            outputs=[sa_download, table, chart1]
        )

        # Optional CSV override (Stage 2)
        upload_csv_2.upload(upload_csv2, upload_csv_2, table)

        # =========================
        # STAGE 3: SDG / GRI
        # =========================
        gr.Markdown("## Step 3: SDG/GRI Classification (Topic Alignment)")

        task_selector_1 = gr.Dropdown(
            choices=[
                "17 SDG Alignment",
                "GRI Topic Alignment"
            ],
            multiselect=True,
            label="Select Tasks"
        )

        run_tasks_btn_1 = gr.Button("Run", variant="primary")

        chart_tasks_1 = gr.Plot()
        download_1 = gr.File(label="Download Results")


        # ---------- SDG FILTER ----------
        sdg_container = gr.Column(visible=False)

        with sdg_container:
            gr.Markdown("### SDG Filter")

            sdg_gallery = gr.Gallery(
                value=sdg_images,
                columns=6,
                allow_preview=False
            )

        sdg_result_table = gr.Dataframe(interactive=True)

        sdg_gallery.select(
            fn=filter_sdg,
            outputs=[sdg_result_table, text]
        )


        # ---------- GRI FILTER ----------
        gri_container = gr.Column(visible=False)

        with gri_container:
            gr.Markdown("### GRI Topic Filter")

            gri_gallery = gr.Gallery(
                value=gri_images,
                columns=4,
                allow_preview=False
            )

        gri_result_table = gr.Dataframe(interactive=True)

        gri_gallery.select(
            fn=filter_gri,
            outputs=[gri_result_table, text]
        )


        # ---------- TOGGLE FILTERS ----------
        task_selector_1.change(
            fn=toggle_filters,
            inputs=task_selector_1,
            outputs=[sdg_container, gri_container]
        )


        # ---------- RUN STEP 3 ----------
        run_tasks_btn_1.click(
            run_selected_tasks,
            inputs=task_selector_1,
            outputs=[download_1, table, chart_tasks_1]
        )

        # =========================
        # STAGE 4: DISCLOSURE QUALITY
        # =========================
        gr.Markdown("## Step 4: Disclosure Quality Analysis")

        task_selector_2 = gr.Dropdown(
            choices=[
                "Informative & Non-Informative/Vague Sustainability Text Identification",
                "Qualitative & Quantitative Sustainability Text Identification",
                "High Potential Greenwashing Detection"
            ],
            multiselect=True,
            label="Select Tasks"
        )

        run_tasks_btn_2 = gr.Button("Run", variant="primary")

        chart_tasks_2 = gr.Plot()
        download_2 = gr.File(label="Download Results")

        run_tasks_btn_2.click(
            run_selected_tasks,
            inputs=task_selector_2,
            outputs=[download_2, table, chart_tasks_2]
        )

        # =========================
        # STAGE 5: CLIMATE ANALYSIS
        # =========================
        gr.Markdown("## Step 5: More Specific Climate Analysis")

        task_selector_3 = gr.Dropdown(
            choices=[
                "Climate Alignment",
                "GRI Climate Alignment",
                "GRI Climate Action (SDG13) Alignment",
                "Climate Action (SDG13) Alignment"
            ],
            multiselect=True,
            label="Select Tasks"
        )

        run_tasks_btn_3 = gr.Button("Run", variant="primary")

        chart_tasks_3 = gr.Plot()
        download_3 = gr.File(label="Download Results")

        run_tasks_btn_3.click(
            run_selected_tasks,
            inputs=task_selector_3,
            outputs=[download_3, table, chart_tasks_3]
        )


        return demo