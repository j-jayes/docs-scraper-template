[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BuiltInPlanner]()



# Class BuiltInPlanner

The built-in planner that uses model's built-in thinking features.

#### Hierarchy ([View Summary](../hierarchy.html#BuiltInPlanner))

  * [BasePlanner](BasePlanner.html)
    * BuiltInPlanner



  * Defined in [core/src/planners/built_in_planner.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L41)



## Constructors

### constructor

  * new BuiltInPlanner(options: { thinkingConfig: ThinkingConfig }): [BuiltInPlanner]()

Initializes the built-in planner.

#### Parameters

    * options: { thinkingConfig: ThinkingConfig }
      * ##### thinkingConfig: ThinkingConfig

Config for model built-in thinking features. An error will be returned if this field is set for models that don't support thinking.

#### Returns [BuiltInPlanner]()

Overrides [BasePlanner](BasePlanner.html).[constructor](BasePlanner.html#constructor)

    * Defined in [core/src/planners/built_in_planner.ts:58](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L58)




## Properties

### `Readonly`[BASE_PLANNER_SIGNATURE_SYMBOL]

"[BASE_PLANNER_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base planner class.

Inherited from [BasePlanner](BasePlanner.html).[[BASE_PLANNER_SIGNATURE_SYMBOL]](BasePlanner.html#base_planner_signature_symbol)

  * Defined in [core/src/planners/base_planner.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/base_planner.ts#L41)



### `Readonly`[BUILT_IN_PLANNER_SIGNATURE_SYMBOL]

"[BUILT_IN_PLANNER_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK built-in planner class.

  * Defined in [core/src/planners/built_in_planner.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L43)



### thinkingConfig

thinkingConfig: ThinkingConfig

Config for model built-in thinking features. An error will be returned if this field is set for models that don't support thinking.

  * Defined in [core/src/planners/built_in_planner.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L49)



## Methods

### applyThinkingConfig

  * applyThinkingConfig(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Applies the thinking config to the LLM request.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The LLM request to apply the thinking config to.

#### Returns void

    * Defined in [core/src/planners/built_in_planner.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L68)




### buildPlanningInstruction

  * buildPlanningInstruction(  
_readonlyContext: [ReadonlyContext](ReadonlyContext.html),  
_llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): string | undefined

Builds the system instruction to be appended to the LLM request for planning.

#### Parameters

    * _readonlyContext: [ReadonlyContext](ReadonlyContext.html)
    * _llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

#### Returns string | undefined

The planning system instruction, or undefined if no instruction is needed.

Overrides [BasePlanner](BasePlanner.html).[buildPlanningInstruction](BasePlanner.html#buildplanninginstruction)

    * Defined in [core/src/planners/built_in_planner.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L75)




### processPlanningResponse

  * processPlanningResponse(  
_callbackContext: [Context](Context.html),  
_responseParts: Part[],  
): Part[] | undefined

Processes the LLM response for planning.

#### Parameters

    * _callbackContext: [Context](Context.html)
    * _responseParts: Part[]

#### Returns Part[] | undefined

The processed response parts, or undefined if no processing is needed.

Overrides [BasePlanner](BasePlanner.html).[processPlanningResponse](BasePlanner.html#processplanningresponse)

    * Defined in [core/src/planners/built_in_planner.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/built_in_planner.ts#L82)




Constructors

constructor

Properties

[BASE_PLANNER_SIGNATURE_SYMBOL][BUILT_IN_PLANNER_SIGNATURE_SYMBOL]thinkingConfig

Methods

applyThinkingConfigbuildPlanningInstructionprocessPlanningResponse

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


