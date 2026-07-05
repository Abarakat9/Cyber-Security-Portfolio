# Facial Recognition AI — ITEC 612 Capstone

A complete facial-recognition pipeline in Python — from raw image collection through preprocessing, face detection, embedding generation, and classification — built with a four-person team (ITEC 612: Applications of Artificial Intelligence). All four classifiers reached **100% accuracy** on the held-out test set.

## My role

I authored two of the pipeline stages:
- **Deliverable 1 preprocessing** (`FacialRecognition.py`) — resized images to 224×224, converted to RGB, normalized pixel values, saved as NumPy arrays
- **Deliverable 2 feature extraction** (`FeatureExtraction.py`) — face detection, eye-based alignment, and 128-dimensional embedding generation

I also wrote the accompanying **Probability and AI Confidence** exercise (included here as a standalone Python demo).

## How the system works

1. **Data** — 106 images of 10 celebrities, split 69 train / 17 validation / 20 test.
2. **Preprocessing** — resize to 224×224, RGB conversion, 0–1 normalization.
3. **Detection & alignment** — dlib's HOG frontal-face detector + 68-point landmark predictor crop each face, level the eyes via affine rotation, and resize uniformly.
4. **Embeddings** — the `face_recognition` library (a ResNet-based deep network) produces a 128-dimensional vector per face. 104 of 106 images embedded successfully; two failed (one at detection, one at encoding) and were documented in a failure report.
5. **Classification** — four models trained on the embeddings: **SVM** (linear kernel), **KNN** (k=3, Euclidean), **Logistic Regression** (multinomial), and **Cosine Similarity** (1-NN).

## Results

| Model | Validation | Test |
|---|---|---|
| SVM (linear) | 100% | 100% |
| KNN (k=3) | 100% | 100% |
| Logistic Regression | 100% | 100% |
| Cosine Similarity (1-NN) | 100% | 100% |

Per-class precision/recall/F1 were all 1.00, with perfect-diagonal confusion matrices.

## Thought process & honest analysis

The write-up deliberately treats 100% accuracy as a **limitation, not a victory**: with only 10 well-separated classes and 20 test samples, high-quality embeddings make the classification trivial even for simple models. The report is candid that this is a **proof-of-concept**, not evidence of production readiness — it wouldn't survive a larger, more diverse, or lower-quality dataset.

**Decisions worth calling out:**
- **Embedding-based approach over training a CNN from scratch** — a pre-trained ResNet embedder is far more sample-efficient given only 6–9 images per person; the downstream classifier does little work because the embeddings are already discriminative.
- **Four classifiers instead of one** — comparing SVM/KNN/LogReg/Cosine shows they perform identically here, which is itself the finding: at this scale the model choice doesn't matter, the embedding quality does.
- **A dedicated ethical reflection** — the paper addresses demographic bias (the 10-celebrity set isn't balanced), privacy/consent, potential for mass-surveillance misuse, and the real-world stakes of false positives/negatives in law enforcement.

## Files

- `Facial Recognition System Using AI and Python.pdf` — the full technical report
- `ProbabilisticAI.py` — a runnable conditional-probability / AI-confidence demo
- `Probability and AI Confidence.docx` — the write-up explaining probability in AI decision-making

> Note: the core pipeline scripts (`FacialRecognition.py`, `FeatureExtraction.py`) live in the team's separate project repository; this folder documents my contribution and the results.
