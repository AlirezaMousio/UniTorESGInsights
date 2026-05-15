# UniTor ESG Insight System
![Logo](assets/Logo.png)
## An Interactive Human–AI Hierarchical Multi-Level System for Sustainability Report Paragraph-Level ESG Analysis 
An interactive human-in-the-loop system for hierarchical, multi-level analysis of sustainability report paragraphs, integrating AI-assisted workflows for PDF parsing, GRI–SDG framework relevance filtering, SDG/GRI topic alignment, disclosure quality assessment, and climate-related analysis.

Companion repository for the paper submitted at [CIKM 2026](https://cikm2026.diag.uniroma1.it/), Rome, ITALY. 

## Table of Contents
- [Architecture](#architecture)
- [Tasks](#tasks)
- [Workflow](#workflow)
- [Hugging Face links for Running the Application](#hugging-face-links-for-running-the-application)
- [Demo Examples](#demo-examples)
- [Repository Structure](#repository-structure)
- [Citation](#citation)
- [License](#license)

## Architecture
UniTor ESG Insight System is based on:
1. Automatic GRI-SDG Annotation that follows
2. Hierarchical Multi-Level Human Validation for Multi-Level Datasets Construction that enables
3. Topic Alignment, Quility Analysis, Cliamte Analysis Downstream Tasks Classification Useful for
4. Four Target Audiences Groups: Investors & Financial Analysts, Auditors, Assurance Providers, Policy-Makers & Regulators, and Corporate Managers & CSO

![Architecture of UniTor ESG Insight System ](assets/UniTorESGArch.pdf)

## Tasks
  Performance table
  All trained models are hosted on Hugging Face and dynamically loaded into the Gradio application.

## Workflow

## Hugging Face links for Running the Application

## Demo examples


## Repository Structure
UniTor ESG Insight System/
│
├── app.py
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
│
├── configs/
│   ├── model_config.py
│   ├── labels.py
│   └── paths.py
│
├── models/
│   ├── classifier.py
│   ├── sdg_classifier.py
│   ├── model_loader.py
│   └── predictor.py
│
├── processing/
│   ├── pdf_processor.py
│   └── image_processor.py
│
├── ui/
│   ├── gradio_functions.py
│   ├── filters.py
│   ├── charts.py
│   ├── state.py
│   ├── theme.py
│   └── interface.py
│
├── assets/
│   ├── architecture.png
│   ├── workflow.png
│   │
│   ├── sdg_icons/
│   ├── gri_icons/
│   │
│   ├── example_reports/
│   │   ├── sample_report_1.pdf
│   │   └── sample_report_2.pdf
│   │
│   └── example_outputs/
│       ├── extracted.csv
│       ├── results.csv
│       ├── chart_sdg.png
│       └── chart_gri.png
│
└── huggingface/
    ├── model_links.json
    └── space_info.json

## Citation
## License

