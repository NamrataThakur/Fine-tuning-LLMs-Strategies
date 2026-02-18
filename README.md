# Fine-tuning-LLMs-Strategies
We cover four strategies to fine-tune an existing pretrained model.
- Supervised Instruction Fine-Tuning on LLAMA3.2-1bn model
- Retrieval Augmented Fine-Tuning on LLAMA3.2-1bn model
- Federated Learning based Fine-Tuning
- GRPO based Fine-Tuning to introduce/improve reasoning capabilities

We also cover model evaluation to quantify the improvements on base model, brought in by the fine-tuning experiments. We also cover synthetic dataset generator to create the fine-tuning datasets from an external document for the first two strategies. We also use open-sourced datasets for remaining strategies.

Tech Stack: Python, Langchain, RAGAS, Flower, Huggingface, Ollama, FAISS