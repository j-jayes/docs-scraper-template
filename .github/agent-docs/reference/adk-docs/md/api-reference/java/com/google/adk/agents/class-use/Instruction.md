JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Instruction.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [Instruction](../Instruction.html)



# Uses of Interface  
com.google.adk.agents.Instruction

Packages that use [Instruction](../Instruction.html "interface in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

  * ## Uses of [Instruction](../Instruction.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Classes in [com.google.adk.agents](../package-summary.html) that implement [Instruction](../Instruction.html "interface in com.google.adk.agents")

Modifier and Type

Class

Description

`static final record `

`[Instruction.Provider](../Instruction.Provider.html "class in com.google.adk.agents")`

Returns an instruction dynamically constructed from the given context.

`static final record `

`[Instruction.Static](../Instruction.Static.html "class in com.google.adk.agents")`

Plain instruction directly provided to the agent.

Methods in [com.google.adk.agents](../package-summary.html) that return [Instruction](../Instruction.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[Instruction](../Instruction.html "interface in com.google.adk.agents")`

LlmAgent.`[globalInstruction](../LlmAgent.html#globalInstruction\(\))()`

 

`[Instruction](../Instruction.html "interface in com.google.adk.agents")`

LlmAgent.`[instruction](../LlmAgent.html#instruction\(\))()`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Instruction](../Instruction.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[globalInstruction](../LlmAgent.Builder.html#globalInstruction\(com.google.adk.agents.Instruction\))([Instruction](../Instruction.html "interface in com.google.adk.agents") globalInstruction)`

 

`[LlmAgent.Builder](../LlmAgent.Builder.html "class in com.google.adk.agents")`

LlmAgent.Builder.`[instruction](../LlmAgent.Builder.html#instruction\(com.google.adk.agents.Instruction\))([Instruction](../Instruction.html "interface in com.google.adk.agents") instruction)`

 




* * *

Copyright (C) 2025\. All rights reserved.
