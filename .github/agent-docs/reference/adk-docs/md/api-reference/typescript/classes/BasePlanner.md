[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BasePlanner]()



# Class BasePlanner`Abstract`

Abstract base class for all planners.

The planner allows the agent to generate plans for the queries to guide its action.

#### Hierarchy ([View Summary](../hierarchy.html#BasePlanner))

  * BasePlanner
    * [BuiltInPlanner](BuiltInPlanner.html)
    * [PlanReActPlanner](PlanReActPlanner.html)



  * Defined in [core/src/planners/base_planner.ts:39](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/base_planner.ts#L39)



## Constructors

### constructor

  * new BasePlanner(): [BasePlanner]()

#### Returns [BasePlanner]()




## Properties

### `Readonly`[BASE_PLANNER_SIGNATURE_SYMBOL]

"[BASE_PLANNER_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base planner class.

  * Defined in [core/src/planners/base_planner.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/base_planner.ts#L41)



## Methods

### `Abstract`buildPlanningInstruction

  * buildPlanningInstruction(  
readonlyContext: [ReadonlyContext](ReadonlyContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): string | undefined

Builds the system instruction to be appended to the LLM request for planning.

#### Parameters

    * readonlyContext: [ReadonlyContext](ReadonlyContext.html)

The readonly context of the invocation.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The LLM request. Readonly.

#### Returns string | undefined

The planning system instruction, or undefined if no instruction is needed.

    * Defined in [core/src/planners/base_planner.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/base_planner.ts#L52)




### `Abstract`processPlanningResponse

  * processPlanningResponse(  
callbackContext: [Context](Context.html),  
responseParts: Part[],  
): Part[] | undefined

Processes the LLM response for planning.

#### Parameters

    * callbackContext: [Context](Context.html)

The callback context of the invocation.

    * responseParts: Part[]

The LLM response parts. Readonly.

#### Returns Part[] | undefined

The processed response parts, or undefined if no processing is needed.

    * Defined in [core/src/planners/base_planner.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/base_planner.ts#L65)




Constructors

constructor

Properties

[BASE_PLANNER_SIGNATURE_SYMBOL]

Methods

buildPlanningInstructionprocessPlanningResponse

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


