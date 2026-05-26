# Interpretable CNNs to Predict Galaxy Bias

Fabian Maldonado \
Catalina Riveros-Jara \
Cristian Soriano
---

## Notebooks

The project is splitted in two notebooks, `notebooks/model.ipynb` which has data processing and network implementation code and `notebooks/explanations.ipynb`, which has SHAP explanations for the developed model. Since our dataset is private, we cant directly provide the raw data but we have the resulting trained model saved in a cloud provider to use it for explanations.

| Notebook | Link |
| --- | --- |
| model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CrisCL20/Proyecto-XAI/blob/main/notebooks/model.ipynb) |
| explanation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CrisCL20/Proyecto-XAI/blob/main/notebooks/explanations.ipynb) |

## Local environment

This project uses uv [(install here)](https://docs.astral.sh/uv/getting-started/installation/) for managing python local environment.

First open a terminal and sync dependencies:

```{bash}
uv sync
```

This creates a python environment which can be activated with the next command:

```{bash}
source .venv/bin/activate 
```
