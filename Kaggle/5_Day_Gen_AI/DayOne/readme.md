Day 1

* Today you’ll explore the evolution of LLMs, from transformers to techniques like fine-tuning and inference acceleration. You’ll also get trained in the art of prompt engineering for optimal LLM interaction.

* The code lab will walk you through getting started with the Gemini API and cover several prompt techniques and how different parameters impact the prompts.

* Reading Assignments
  * [Foundational Large Language Models & Text Generation](https://www.kaggle.com/whitepaper-foundational-llm-and-text-generation)
  * The transformer architecture is the basis for all modern-day LLMs. Across the various
    architectures mentioned in this whitepaper we see that it’s important not only to add more
    parameters to the model, but the composition of the dataset is equally important.
  * The order and strategies used for fine-tuning is important and may include multiple steps
    such as Instruction Tuning, Safety Tuning, etc. Supervised Fine Tuning (SFT) is important
    in capturing the essence of a task. RLHF, and potentially RLAIF, can be used to shift the
    distribution from the pretraining distribution to a more desired one through the power of
    the reward function, that can reward desirable behaviors and penalize undesirable ones.
  * Making inference from neural models efficient is an important problem and an active
    field of research. Many methods exist to reduce serving costs and latency with minimal
    impact to model performance, and some exact acceleration methods guarantee identical
    model outputs.
