# Assessment Portfolio Template: Part 1 - Training the Image Identifier for Puzzle Pieces

**Instructions for Students:**  
This template forms the first part of your assessment portfolio for the clustered AI course covering units ICTAII501 (Automate work tasks using machine learning) and ICTAII502 (Train and evaluate machine learning models). Use this to document your work on training an image identifier for the puzzle pieces using tools from the NVIDIA Hello AI course on Jetson Nano, the thumbs classifier example, Roboflow for annotations, and related techniques.  

Fill in each section with your own details, evidence, and reflections. Include screenshots, code snippets, or links to your Roboflow project as evidence. This checkpoint focuses on the initial ML training step, which aligns with designing and implementing an AI component for the broader PuzzArm project.  

At the end, map your work to the relevant elements and performance criteria (PC) from the units. Use the provided table and explain how your activities demonstrate competency. Submit this as a Word/PDF document or GitHub Markdown file.  

**Student Name:** [Your Name]  
**Student ID:** [Your ID]  
**Date Completed:** [Date]  
**Project Context:** Briefly describe the overall PuzzArm project and how this image identifier fits in (e.g., "The image identifier detects and classifies puzzle pieces 0-9 for autonomous robotic solving.").  

---

## Section 1: Task Description and Planning
**Objective:** Document the business or task need for the image identifier and how you planned the ML solution. This aligns with designing AI solutions (ICTAII501) and evaluating data requirements (ICTAII502).  

- **Identified Need:** Explain the problem (e.g., "Automate detection of puzzle pieces to enable robotic pick-and-place, improving efficiency in educational robotics demos."). How does this automate a work task? [Your response, 100-200 words]  
- **Tools and Approach Selected:** Describe why you chose Hello AI on Jetson Nano, thumbs classifier (as a starting example), and Roboflow (e.g., "Jetson Nano for edge AI; thumbs classifier for binary inspiration; Roboflow for dataset management and annotations."). [Your response, including rationale]  
- **Data Requirements:** Outline data sources (e.g., photos of puzzle pieces), size (e.g., 50-100 images per class), and transformations planned (e.g., augmentations for rotations). [Your response]  

---

## Section 2: Implementation Process
**Objective:** Detail the step-by-step process of training the model. This demonstrates implementation skills (ICTAII502 Elements 2-4).  

- **Data Preparation:**  
  - How did you collect and annotate images? (e.g., "Used Roboflow to upload photos, annotate bounding boxes for 0-9 pieces with fruit patterns."). [Your response, include Roboflow project link or screenshot]  
  - Describe any feature engineering (e.g., "Applied rotations and flips for orientation handling."). [Your response]  

- **Model Training:**  
  - Steps in Hello AI/Jetson Nano: (e.g., "Modified thumbs classifier code to multi-class for 10 digits; trained on Jetson with PyTorch."). Include key code snippets.  
    ```python
    # Example code snippet (replace with yours)
    import torch
    # Your training code here...
    ```
  - Training Parameters: (e.g., "Epochs: 50; Batch size: 32; Learning rate: 0.001."). [Your response]  
  - Validation and Test Sets: How did you split data (e.g., 70/20/10)? Describe issues fixed (e.g., "Refined parameters after overfitting detected."). [Your response]  

- **Challenges Encountered:** (e.g., "Lighting variations reduced accuracy; resolved with augmentations."). [Your response]  

---

## Section 3: Evaluation and Results
**Objective:** Evaluate the model's performance. This covers ICTAII502 Element 5 (Finalise ML evaluations).  

- **Metrics and Outputs:** Record accuracy (e.g., "95% on validation set; confusion matrix shows high precision for digits 0-9."). Include graphs/screenshots (e.g., from TensorBoard or matplotlib). [Your response]  
- **Comparison to Targets:** How do results match expectations? (e.g., "Achieved >90% predictive accuracy as per brief."). [Your response]  
- **Adjustments Made:** (e.g., "Tuned hyperparameters to improve recall on rotated pieces."). [Your response]  

---

## Section 4: Evidence
**Objective:** Provide supporting materials.  

- **Screenshots/Artifacts:**  
  - Roboflow dataset overview: [Paste or link]  
  - Training logs/output: [Paste or link]  
  - Model inference example (e.g., photo of detected piece): [Paste or link]  
- **Code Repository Link:** (e.g., GitHub repo with Jupyter notebooks). [Your link]  

---

## Section 5: Reflection
**Objective:** Reflect on learning and improvements. This supports foundation skills like problem-solving.  

- **What Worked Well:** (e.g., "Roboflow simplified annotations, speeding up data prep."). [100-150 words]  
- **Areas for Improvement:** (e.g., "Could add more diverse lighting in dataset for robustness."). [Your response]  
- **Skills Gained:** How has this step built your AI competencies? (e.g., "Learned ML training pipelines and edge deployment on Jetson."). [Your response]  

---
