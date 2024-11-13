Day 1

* [Day 1 Livestream with Paige Bailey – 5-Day Gen AI Intensive Course | Kaggle](https://youtu.be/kpRyiJUUFxY?si=vyq2pMUnQlwrGe2S)

* Today you’ll explore the evolution of LLMs, from transformers to techniques like fine-tuning and inference acceleration. You’ll also get trained in the art of prompt engineering for optimal LLM interaction.

* The code lab will walk you through getting started with the Gemini API and cover several prompt techniques and how different parameters impact the prompts.

* Reading Assignments
  * [Foundational Large Language Models & Text Generation](https://www.kaggle.com/whitepaper-foundational-llm-and-text-generation)
    * [Whitepaper Companion Podcast - Foundational LLMs & Text Generation](https://youtu.be/mQDlCZZsOyo?si=FKp3Uhz_c_uLoG7E)
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
    * Large language models can be used for a variety of tasks including summarization,
      translation, question answering, chat, code generation, and many more. You can
      create your own tasks using the Vertex and Makersuite text generation services which
      leverage Google’s latest language models. After the model has been trained and tuned,
      it is important to experiment with engineering prompts. You should use the technique
      most appropriate for the task-at-hand because LLMs can be sensitive to prompts k.
    * Furthermore, it is also possible to enhance task specific performance or creativity and
      diversity by tweaking the parameters corresponding to sampling techniques such as
      Top-K, Top-P, and Max decoding steps to find the optimum mix of correctness, diversity,
      and creativity required for the task at hand.
  * [Prompt Engineering](https://www.kaggle.com/whitepaper-prompt-engineering)
    * [Whitepaper Companion Podcast - Prompt Engineering](https://youtu.be/F_hJ2Ey4BNc?si=wMn_Z0a7KZaUvxZV) 

- - - -

Attention is a machine learning method that determines the relative importance of each component in a sequence relative to the other components in that sequence. In natural language processing, importance is represented by "soft" weights assigned to each word in a sentence. More generally, attention encodes vectors called token embeddings across a fixed-width sequence that can range from tens to millions of tokens in size.

- - - -
An enum, or enumerated type, is a data type that consists of a set of named values, or elements, that are used to represent a choice from a set of mutually exclusive values.
* enum Season { Spring, Summer, Autumn, Winter }
