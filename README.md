
# Building Effective  Agents

This repository explores patterns for building effective AI agentic systems based on principles shared by [Anthropic](https://www.anthropic.com/engineering/building-effective-agents). The focus is on using simple, composable patterns rather than overly complex frameworks, starting with foundational components and adding complexity only when necessary and demonstrably beneficial.

Kaggle to play: [Link](https://www.kaggle.com/code/santoshpremiadhikari/build-effecftive-agents)
## Core Concepts

Based on the source material, agentic systems can be understood through these key components and patterns:

1.  **The Augmented LLM**: This is the **basic building block** of agentic systems. It represents an LLM enhanced with capabilities such as **retrieval, tools, and memory**. Our current models can actively use these augmentations, for example, by generating search queries or selecting tools. This is the enhanced component used in individual steps of more complex systems.

2.  **Agentic Systems (Workflows and Agents)**: Workflows and agents are both categorized as **agentic systems**. They are architectures built *using* augmented LLMs to orchestrate multiple LLM calls and tool usage over time to accomplish more complex tasks.

    *   **Workflows**: These are systems where LLMs and tools are orchestrated through **predefined code paths**. The sequence of steps is determined beforehand in the system's code. Workflows are suitable for tasks that can be easily broken down into **fixed subtasks** and are used to gain **consistency for well-defined tasks**.

    *   **Agents**: These are systems where LLMs **dynamically direct their own processes and tool usage**, maintaining control over how they accomplish tasks. Once the task is clear, agents plan and operate **independently**, potentially returning to the human for clarification or judgement. They typically operate in a loop, using tools based on environmental feedback. Agents are recommended for **open-ended problems** where it's difficult or impossible to predict the required number of steps or hardcode a fixed path. They are the better option when **flexibility and model-driven decision-making are needed at scale**. Agents may potentially operate for many turns.

## Workflow Patterns

The sources describe several common workflow patterns, which follow predefined code paths:

*   **Prompt Chaining**: Decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. Useful for tasks that can be easily decomposed into **fixed subtasks** to trade latency for higher accuracy.
*   **Routing**: Classifies an input and directs it to a specialized followup task. Allows for separation of concerns and building more specialized prompts. Works well for complex tasks with distinct categories handled separately.
*   **Parallelization**: LLMs work simultaneously on a task, and their outputs are aggregated programmatically. Manifests as Sectioning (breaking a task into independent subtasks run in parallel) or Voting (running the same task multiple times). Effective when subtasks can be parallelized for speed or when multiple perspectives are needed for higher confidence results.
*   **Orchestrator-Workers**: An orchestrator LLM breaks down tasks, delegates them to worker LLMs, and synthesizes results. Well-suited for complex tasks where you **can't predict the subtasks needed** beforehand (unlike Parallelization).
*   **Evaluator-Optimizer**: One LLM generates a response while another provides evaluation and feedback in a loop. Particularly effective when there are **clear evaluation criteria** and iterative refinement provides measurable value.

## When to Use

The recommendation is to **start with the simplest solution**, often optimizing single augmented LLM calls, and only add the complexity of multi-step agentic systems (workflows or agents) when simpler solutions fall short and the added complexity demonstrably improves outcomes. Agentic systems often trade latency and cost for better task performance.

*   Use **Workflows** for complex tasks that can be cleanly decomposed into predictable, **fixed subtasks** where **consistency** is key.
*   Use **Agents** for **open-ended problems**, when a **fixed path cannot be hardcoded**, the LLM will operate for many turns, and **flexibility and dynamic decision-making** are needed.

## Implementation Principles

When implementing agents, the sources suggest following three core principles:

1.  Maintain simplicity in your agent's design.
2.  Prioritize transparency by explicitly showing the agent’s planning steps.
3.  Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing. This is analogous to investing effort in Human-Computer Interfaces (HCI).

Frameworks can help get started quickly but understand the underlying code and avoid adding unnecessary complexity.

