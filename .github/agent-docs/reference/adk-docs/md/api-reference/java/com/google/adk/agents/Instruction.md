JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instruction.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [Instruction](Instruction.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary



# Interface Instruction

All Known Implementing Classes:
    `[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents")`, `[Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")`

* * *

public sealed interface Instruction permits [Instruction.Static](Instruction.Static.html "class in com.google.adk.agents"), [Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents")

Represents an instruction that can be provided to an agent to guide its behavior. 

In the instructions, you should describe concisely what the agent will do, when it should defer to other agents/tools, and how it should respond to the user. 

Templating is supported using placeholders like `{variable_name}` or ` {artifact.artifact_name}`. These are replaced with values from the agent's session state or loaded artifacts, respectively. For example, an instruction like `"Translate the following text to {language}: {user_query}"` would substitute `{language}` and `{user_query}` with their corresponding values from the session state. 

Instructions can also be dynamically constructed using [`Instruction.Provider`](Instruction.Provider.html "class in com.google.adk.agents"). This allows for more complex logic where the instruction text is generated based on the current [`ReadonlyContext`](ReadonlyContext.html "class in com.google.adk.agents"). Additionally, an instruction could be built to include specific information based on based on some external factors fetched during the Provider call like the current time, the result of some API call, etc.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

`static final record `

`[Instruction.Provider](Instruction.Provider.html "class in com.google.adk.agents")`

Returns an instruction dynamically constructed from the given context.

`static final record `

`[Instruction.Static](Instruction.Static.html "class in com.google.adk.agents")`

Plain instruction directly provided to the agent.




* * *

Copyright (C) 2025\. All rights reserved.
