Title: Hybrid Modules to Bridge Biotechnology and Computer Science
Save_as: index.html
Status: published

## Introduction

Biotechnology and computer science are increasingly converging to accelerate innovation in healthcare. To best prepare life science students for this evolving landscape, a series of 24 scaffolded e-learning modules were developed with the overarching goal of introducing students to Data Science and Machine Learning applications in healthcare. The modules span two domains:

- **Data Science in Biotechnology:** managing, analyzing, and visualizing biological data.
- **Artificial Intelligence in Biotechnology:** widely applied AI methods in healthcare.

## Module Design & Development

Modules are scaffolded to activate prior knowledge and reinforce applied skills. Development has been informed by multiple feedback channels:

- **Industry consultation:** sessions were held with external partners to understand the skills and competencies most valued in the current industry landscape.
- **User feedback:** ongoing input was gathered from students and teaching assistants, with revisions incorporated based on user experience.

The modules are organized into three blocks to facilitate sequential integration across three consecutive courses. They are available as Jupyter Notebooks hosted on the [University of Toronto JupyterHub](https://jupyter.utoronto.ca) cloud computing platform, enabling students and instructors to access and engage with the content without requiring any local software installation. Each module set includes supplemental support resources such as user instructions, FAQs, and answer keys, to facilitate independent use and broad adoption.

## Overview of the Modules

### Module Set 1 – 2nd Year Life Science Courses

This sequence introduces Python programming, data science, and machine learning across eight modules. The curriculum is designed to equip life science students with computational tools to manage, analyze, and model biological data, with an emphasis on practical workflows and interpretation.

1. **Introduction to Python**

    This module introduces Python programming in the context of scientific computing using Jupyter Notebook. Students learn core programming concepts, including variables, data types, control flow, and basic data structures. By the end of the module, students can write simple programs to perform calculations and manipulate structured data.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-1_Introduction-to-Python.git&urlpath=tree%2F1-1_Introduction-to-Python.git%2F&branch=master) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-1_Introduction-to-Python) (public access)

2. **Programming Concepts**

    This module builds on foundational Python skills by introducing more advanced constructs such as dictionaries, iteration, and function-based abstraction. Students begin working with structured data formats (e.g., CSV files) and are introduced to the pandas library. The focus is on writing modular, reusable code for data-oriented tasks.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-2_Programming-Concepts.git&urlpath=tree%2F1-2_Programming-Concepts.git%2F&branch=master) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-2_Programming-Concepts) (public access)

3. **Introduction to Data Science**

    This module introduces core data science workflows using pandas. Students learn how to load, clean, and manipulate datasets, compute descriptive statistics, and prepare data for analysis. Logistic regression is introduced via the statsmodels library, with an emphasis on interpreting model outputs in biological contexts.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-3_Introduction_to_Data_Science.git&urlpath=tree%2F1-3_Introduction_to_Data_Science.git%2F&branch=master) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-3_Introduction_to_Data_Science) (public access)

4. **Visualizing Data**

    This module focuses on data visualization as a tool for exploration and communication. Students use pandas and seaborn to generate common plots (e.g., histograms, box plots, correlation heatmaps) and learn how to customize visualizations for clarity and interpretability. The module emphasizes identifying patterns and relationships in biological data.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-4_Visualizing-Data.git&urlpath=tree%2F1-4_Visualizing-Data.git%2F&branch=master) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-4_Visualizing-Data) (public access)

5. **Introduction to Machine Learning**

    This module presents the supervised machine learning pipeline, including data preparation, exploration, model training, and evaluation. Students expand their data preprocessing skills (e.g., handling missing values, encoding variables, feature selection) and learn dataset splitting using the scikit-learn library. The goal is to establish a conceptual understanding of how machine learning models are developed and assessed.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-5_Introduction-to-Machine-Learning&urlpath=tree%2F1-5_Introduction-to-Machine-Learning%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-5_Introduction-to-Machine-Learning) (public access)

6. **Model Training**

    This module focuses on training machine learning models, with an emphasis on logistic regression. Students are introduced to key concepts such as loss functions, gradient descent, and hyperparameter tuning, and dataset splitting into training, validation, and test sets. The module also addresses challenges such as class imbalance in biological datasets and introduces how to use the pickle library for saving and reusing trained models.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-6_Model-Training&urlpath=tree%2F1-6_Model-Training%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-6_Model-Training) (public access)

7. **Model Evaluation**

    This module examines methods for evaluating model performance using appropriate metrics, including accuracy, precision, recall, F1-score, and confusion matrices. Students learn to interpret these metrics in context and to diagnose issues such as underfitting and overfitting. Emphasis is placed on selecting evaluation strategies suited to biological applications.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-7_Model-Evaluation&urlpath=tree%2F1-7_Model-Evaluation%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-7_Model-Evaluation) (public access)

8. **Applying Machine Learning**

    This module consolidates prior learning by guiding students through the application of the machine learning pipeline to structured problems. It introduces additional supervised models, including decision trees and random forests, as well as foundational unsupervised techniques such as principal component analysis (PCA) and k-means clustering. The focus is on reinforcing workflow integration while expanding students' exposure to commonly used methods.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F1-8_Applying-Machine-Learning&urlpath=tree%2F1-8_Applying-Machine-Learning%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/1-8_Applying-Machine-Learning) (public access)

### Module Set 2 – 3rd Year Life Science Courses

This course builds on foundational programming and machine learning concepts to introduce students to advanced data analysis techniques in computational biology. Emphasis is placed on developing interpretability, critical thinking, and the ability to apply computational methods to high-dimensional biological datasets.

1. **Advanced Visualization**

    This module develops students' data visualization skills using the matplotlib library, with an emphasis on producing clear and customizable figures. Students learn to construct multi-panel plots, apply effective labeling and layout strategies, and visualize relationships between variables using scatter plots. The module also introduces hierarchical clustering via the scipy library, including dendrogram construction and interpretation in an evolutionary context.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-1_Advanced-Visualization.git&urlpath=tree%2F2-1_Advanced-Visualization.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-1_Advanced-Visualization) (public access)

2. **Decision Trees**

    This module provides a detailed description of decision tree models using scikit-learn. It focuses on the trade-off between model complexity and generalization, and introduces key hyperparameters (e.g., maximum depth, minimum samples, and entropy thresholds) that control this balance. Students examine how these parameters influence model performance and interpretability.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-2_Decision-Trees.git&urlpath=tree%2F2-2_Decision-Trees.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-2_Decision-Trees) (public access)

3. **Differential Gene Expression**

    This module introduces a complete workflow for bulk RNA-seq analysis, from raw RNA-seq count data to the identification of significantly differentially expressed genes. Students learn data preprocessing, data quality problems, and statistical analysis using the pyDESeq2 library. The module emphasizes visualization (e.g., volcano plots, heatmaps) and biological interpretation of gene expression changes.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-3_Differential-Gene-Expression.git&urlpath=tree%2F2-3_Differential-Gene-Expression.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-3_Differential-Gene-Expression) (public access)

4. **Gene Set Enrichment Analysis**

    Building on DGE, this module shifts analysis from individual genes to biological pathways. Students are introduced to the conceptual framework of GSEA and implement analyses using the gseapy library. Key concepts include ranked gene lists, enrichment scores (ES), normalized enrichment scores (NES), and false discovery rate (FDR). The module also introduces enrichment plots and other visual summaries to support the interpretation of pathway-level results in a biological context.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-4_Gene-Set-Enrichment-Analysis.git&urlpath=tree%2F2-4_Gene-Set-Enrichment-Analysis.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-4_Gene-Set-Enrichment-Analysis) (public access)

5. **Single-Cell RNA Sequencing**

    This module introduces the analysis of single-cell transcriptomic data using AnnData structures. It guides students through the preprocessing, manipulation, analysis, and visualization of scRNA-seq data. Key preprocessing steps include filtering low-quality cells and genes, computing quality control metrics, and normalizing data to ensure comparability across cells. The module also highlights a central challenge of scRNA-seq data: sparsity.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-5_Single-Cell-RNA-Seq.git&urlpath=tree%2F2-5_Single-Cell-RNA-Seq.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-5_Single-Cell-RNA-Seq) (public access)

6. **Dimensionality Reduction**

    This module introduces principal component analysis (PCA) and Uniform Manifold Approximation and Projection (UMAP) as tools for analyzing high-dimensional data. Students learn when and how to apply each method, the importance of data scaling, and approaches for selecting the number of components (e.g., elbow method, variance thresholds).

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-6_Dimensionality-Reduction.git&urlpath=tree%2F2-6_Dimensionality-Reduction.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-6_Dimensionality-Reduction) (public access)

7. **Clustering**

    Building on dimensionality reduction, students examine how PCA and UMAP can be used in combination for improved representation of high-dimensional data. This module introduces clustering techniques, including k-means and Louvain methods. Students explore how combining dimensionality reduction with clustering enables the identification of biologically meaningful cell populations and states in scRNA-seq datasets.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-7_Clustering-II.git&urlpath=tree%2F2-7_Clustering-II.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-7_Clustering-II) (public access)

8. **Introduction to Integrated Development Environments (IDEs)**

    This module extends students' programming workflow beyond Jupyter notebooks. It introduces the command line interface, environment management using Conda, and modern development tools such as VS Code. These tools support the management of more complex projects.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F2-8_Introduction-to-IDEs.git&urlpath=tree%2F2-8_Introduction-to-IDEs.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/2-8_Introduction-to-IDEs) (public access)

### Module Set 3 – 4th Year Life Science Courses

1. **Introduction to IDEs, Git, and GitHub**

    This module expands students' programming workflow beyond Jupyter notebooks. It introduces the command line, environment management with Conda, development tools like VS Code, and version control using Git and GitHub to support more complex projects.

    - [PDF Tutorial]({static}/files/Introduction-to-IDEs-Git-and-GitHub.pdf)

2. **Utilizing Large Language Models**

    This module introduces LLMs and practical prompt engineering techniques, including zero-shot and few-shot debugging, iterative programming, chain-of-thought reasoning, and negative prompting, emphasizing when each approach is most effective.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F3-1-Utilizing-Large-Language-Models.git&urlpath=tree%2F3-1-Utilizing-Large-Language-Models.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/3-1-Utilizing-Large-Language-Models) (public access)

3. **Introduction to Neural Networks**

    This module introduces how to preprocess data, build, and train a fully-connected neural network model using the PyTorch library.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F3-2-Intro-to-Neural-Networks.git&urlpath=tree%2F3-2-Intro-to-Neural-Networks.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/3-2-Intro-to-Neural-Networks) (public access)

4. **Training and Hyperparameter Optimization for Neural Networks**

    This module focuses on the neural network training process, covering backpropagation, validation, loss functions, and hyperparameter tuning. Students also learn to visualize and interpret training performance.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F3-3-Training-and-Hyperparameter-Optimization-for-Neural-Networks.git&urlpath=tree%2F3-3-Training-and-Hyperparameter-Optimization-for-Neural-Networks.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/3-3-Training-and-Hyperparameter-Optimization-for-Neural-Networks) (public access)

5. **RMSD Prediction Challenge**

    In this module, students apply neural networks to predict RMSD (Root-Mean-Square Deviation). They experiment with model architectures and hyperparameters, analyzing how these choices impact performance.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F3-4-RMSD-Prediction-Challenge&urlpath=tree%2F3-4-RMSD-Prediction-Challenge%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/3-4-RMSD-Prediction-Challenge) (public access)

6. **Introduction to Vision Transformers**

    This module introduces ViTs, the current state-of-the-art method for computer vision tasks, and focuses on image classification for histology data. Students explore how images are processed as patches and how attention mechanisms capture relationships between them. They build a ViT model and run inference, focusing on understanding its structure and interpreting its predictions.

    - [GitHub repository](https://github.com/CS-Biotech/3-5-Introduction-to-Vision-Transformers) (public access)

7. **Fine-Tuning Vision Transformers**

    This module focuses on training and fine-tuning a ViT on histology data. Students implement a full training pipeline, including data splitting, augmentation, and loss optimization. They evaluate model performance using metrics and visualizations to understand how well the model learns to distinguish between benign and malignant tissue.

    - [GitHub repository](https://github.com/CS-Biotech/3-6-Fine-Tuning-Vision-Transformers) (public access)

8. **Capstone Project**

    This module first introduces foundation models for protein analysis and shows how to convert amino acid sequences into embeddings using tokenization and pretrained models. Students apply multi-class classification to predict protein characteristics and evaluate their models using appropriate metrics. As a capstone, students choose one of three tasks—protein function, localization, or domain classification—and complete a full machine learning pipeline, from working with raw biological data and pretrained embeddings to building, evaluating, and interpreting their own neural network models.

    - [Open in University of Toronto JupyterHub](https://jupyter.utoronto.ca/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FCS-Biotech%2F3-7-Capstone-Project-Protein-Classification.git&urlpath=tree%2F3-7-Capstone-Project-Protein-Classification.git%2F&branch=main) (requires UTORid login)
    - [GitHub repository](https://github.com/CS-Biotech/3-7-Capstone-Project-Protein-Classification) (public access)

## People

### Principal Investigators

- **Prof. Naomi Levy-Strumpf**, Assistant Professor, Teaching Stream, Department of Cell & Systems Biology and Human Biology, Faculty of Arts & Science
- **Prof. David Liu**, Associate Professor, Teaching Stream, Computer Science, Faculty of Arts & Science
- **Prof. Alice Gao**, Assistant Professor, Teaching Stream, Computer Science, Faculty of Arts & Science

### Project Team

**Module Developers:** Gerd Bizi, Edward Chen, Micaela Consens, Sophie Kim, Maxim Kirby, Emily Nguyen, Yifei Sun, Nakul Upadhya, Elias Williams, Olivia (Xi) Yan

**Research Assistants:** Mahreen Khan, Jennifer Pfeil, Reuben Philip, Cory Richman, Callum Stirton

**Module Editors:** Mustafa Nisar, Estelle Wang

**Project Coordinators:** Dan Chen, Eryka Kateline Shi-Shun

### Consultants

- **Prof. Gary Bader**, Professor, Computational Biology, Department of Molecular Genetics, University of Toronto; Ontario Research Chair in Biomarkers of Disease
- **Dr. Irene Harmesen**, MD, PhD — CTO & Co-founder, Cove Neuroscience Inc.
- **Lauren Phillips**, Chief Product Officer, BioBox Analytics Inc.
- **Aidan MacAdam**, Chief Executive Officer, GastroTrackAI Inc.
- **Ali Mehdi**, Chief Executive Officer, Pytri AI

### Contact

For questions about the modules, or if you are an instructor looking for module solutions and teaching materials, please contact Naomi Levy-Strumpf at [naomi.levy.strumpft@utoronto.ca](mailto:naomi.levy.strumpft@utoronto.ca).

## License

The module materials are licensed under a [Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0). You are free to share and adapt the materials for non-commercial purposes, provided you give appropriate credit and distribute any derivative works under the same license.

## Acknowledgements

This project was supported by the Learning & Education Advancement Fund from the Office of the Vice-Provost, Innovations in Undergraduate Education, University of Toronto.
