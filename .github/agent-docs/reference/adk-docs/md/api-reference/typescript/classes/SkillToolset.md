[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SkillToolset]()



# Class SkillToolset

Base class for toolset.

A toolset is a collection of tools that can be used by an agent.

#### Hierarchy ([View Summary](../hierarchy.html#SkillToolset))

  * [BaseToolset](BaseToolset.html)
    * SkillToolset



  * Defined in [core/src/tools/skill/skill_toolset.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L42)



## Constructors

### constructor

  * new SkillToolset(  
skills: Record<string, [Skill](../interfaces/Skill.html)> | [Skill](../interfaces/Skill.html)[],  
options?: {  
additionalTools?: ([BaseTool](BaseTool.html) | [BaseToolset](BaseToolset.html))[];  
allowInlineScripts?: boolean;  
codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html);  
registry?: [SkillRegistry](../interfaces/SkillRegistry.html);  
},  
): [SkillToolset]()

#### Parameters

    * skills: Record<string, [Skill](../interfaces/Skill.html)> | [Skill](../interfaces/Skill.html)[]
    * options: {  
additionalTools?: ([BaseTool](BaseTool.html) | [BaseToolset](BaseToolset.html))[];  
allowInlineScripts?: boolean;  
codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html);  
registry?: [SkillRegistry](../interfaces/SkillRegistry.html);  
} = {}
      * ##### `Optional`additionalTools?: ([BaseTool](BaseTool.html) | [BaseToolset](BaseToolset.html))[]

      * ##### `Optional`allowInlineScripts?: boolean

Whether to expose the `run_skill_inline_script` tool, which executes model-provided script content in the configured code executor. This is disabled by default because arbitrary inline-script execution is a sensitive capability; opt in explicitly by setting this to `true`. Execution additionally remains gated behind a human-in-the-loop confirmation.

      * ##### `Optional`codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html)

      * ##### `Optional`registry?: [SkillRegistry](../interfaces/SkillRegistry.html)

#### Returns [SkillToolset]()

Overrides [BaseToolset](BaseToolset.html).[constructor](BaseToolset.html#constructor)

    * Defined in [core/src/tools/skill/skill_toolset.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L51)




## Properties

### `Readonly`[BASE_TOOLSET_SIGNATURE_SYMBOL]

"[BASE_TOOLSET_SIGNATURE_SYMBOL]": true

Inherited from [BaseToolset](BaseToolset.html).[[BASE_TOOLSET_SIGNATURE_SYMBOL]](BaseToolset.html#base_toolset_signature_symbol)

  * Defined in [core/src/tools/base_toolset.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L44)



### additionalTools

additionalTools: ([BaseTool](BaseTool.html) | [BaseToolset](BaseToolset.html))[]

  * Defined in [core/src/tools/skill/skill_toolset.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L45)



### `Optional`codeExecutor

codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html)

  * Defined in [core/src/tools/skill/skill_toolset.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L46)



### `Optional` `Readonly`prefix

prefix?: string

Inherited from [BaseToolset](BaseToolset.html).[prefix](BaseToolset.html#prefix)

  * Defined in [core/src/tools/base_toolset.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L48)



### `Optional`registry

registry?: [SkillRegistry](../interfaces/SkillRegistry.html)

  * Defined in [core/src/tools/skill/skill_toolset.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L47)



### skills

skills: Record<string, [Skill](../interfaces/Skill.html)>

  * Defined in [core/src/tools/skill/skill_toolset.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L43)



### `Readonly`toolFilter

toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html)

Inherited from [BaseToolset](BaseToolset.html).[toolFilter](BaseToolset.html#toolfilter)

  * Defined in [core/src/tools/base_toolset.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L47)



## Methods

### close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

Overrides [BaseToolset](BaseToolset.html).[close](BaseToolset.html#close)

    * Defined in [core/src/tools/skill/skill_toolset.ts:99](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L99)




### getOrFetchSkill

  * getOrFetchSkill(name: string, invocationId?: string): Promise<[Skill](../interfaces/Skill.html) | undefined>

#### Parameters

    * name: string
    * `Optional`invocationId: string

#### Returns Promise<[Skill](../interfaces/Skill.html) | undefined>

    * Defined in [core/src/tools/skill/skill_toolset.ts:107](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L107)




### getSkill

  * getSkill(name: string): [Skill](../interfaces/Skill.html) | undefined

#### Parameters

    * name: string

#### Returns [Skill](../interfaces/Skill.html) | undefined

    * Defined in [core/src/tools/skill/skill_toolset.ts:103](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L103)




### getTools

  * getTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [core/src/tools/skill/skill_toolset.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L94)




### `Protected`isToolSelected

  * isToolSelected(tool: [BaseTool](BaseTool.html), context: [ReadonlyContext](ReadonlyContext.html)): boolean

Returns whether the tool should be exposed to LLM.

#### Parameters

    * tool: [BaseTool](BaseTool.html)

The tool to check.

    * context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent.

#### Returns boolean

Whether the tool should be exposed to LLM.

Inherited from [BaseToolset](BaseToolset.html).[isToolSelected](BaseToolset.html#istoolselected)

    * Defined in [core/src/tools/base_toolset.ts:79](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L79)




### processLlmRequest

  * processLlmRequest(toolContext: [Context](Context.html), llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<void>

Processes the outgoing LLM request for this toolset. This method will be called before each tool processes the llm request.

Use cases:

    * Instead of let each tool process the llm request, we can let the toolset process the llm request. e.g. ComputerUseToolset can add computer use tool to the llm request.

#### Parameters

    * toolContext: [Context](Context.html)

The context of the tool.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The outgoing LLM request, mutable this method.

#### Returns Promise<void>

Overrides [BaseToolset](BaseToolset.html).[processLlmRequest](BaseToolset.html#processllmrequest)

    * Defined in [core/src/tools/skill/skill_toolset.ts:138](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/skill/skill_toolset.ts#L138)




Constructors

constructor

Properties

[BASE_TOOLSET_SIGNATURE_SYMBOL]additionalToolscodeExecutorprefixregistryskillstoolFilter

Methods

closegetOrFetchSkillgetSkillgetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


