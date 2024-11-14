Day 3 - “Generative AI Agents”

* [Day 3 Livestream with Paige Bailey – 5-Day Gen AI Intensive Course | Kaggle](https://www.youtube.com/live/HQUtMWoTAD4?si=wpuex_e8mKkBtatA)

* Learn to build sophisticated AI agents by understanding their core components and the iterative development process.

* The code labs cover how to connect LLMs to existing systems and to the real world. Learn about function calling by giving SQL tools to a      chatbot, and learn how to build a LangGraph agent that takes orders in a café.

- - - -

Code labs
* Talk to a database with function calling
* Build an agentic ordering system in LangGraph

- - - -

Reading
* [Agents](https://www.kaggle.com/whitepaper-agents)
  * [Whitepaper Companion Podcast - Agents | 5-Day Gen AI Intensive Course with Google](https://youtu.be/H4gZd4BCrDQ?si=L-11Mj9PdYYQKoao)
  * In its most fundamental form, a Generative AI agent can be defined as an application that
    attempts to achieve a goal by observing the world and acting upon it using the tools that it
    has at its disposal.
  * In the scope of an agent, a model refers to the language model (LM) that will be utilized as
    the centralized decision maker for agent processes.
  * The model used by an agent can be one or multiple LM’s of any size (small / large) that are capable of following instruction based
    reasoning and logic frameworks, like ReAct, Chain-of-Thought, or Tree-of-Thoughts.
  * Tools can take a variety of forms and have varying depths of complexity, but typically align with common web API methods like GET, POST,
    PATCH, and DELETE. For example, a tool could update customer information in a database or fetch weather data to influence a travel
    recommendation that the agent is providing to the user. Functions, Extensions, Data Stores and Plugins are additional examples.
  * The orchestration layer describes a cyclical process that governs how the agent takes in
    information, performs some internal reasoning, and uses that reasoning to inform its next
    action or decision.
