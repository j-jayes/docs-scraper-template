[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [PlanReActPlanner]()



# Class PlanReActPlanner

Plan-Re-Act planner that constrains the LLM response to generate a plan before any action/observation.

Note: this planner does not require the model to support built-in thinking features or setting the thinking config.

#### Hierarchy ([View Summary](../hierarchy.html#PlanReActPlanner))

  * [BasePlanner](BasePlanner.html)
    * PlanReActPlanner



  * Defined in [core/src/planners/plan_re_act_planner.ts:35](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/plan_re_act_planner.ts#L35)



## Constructors

### constructor

  * new PlanReActPlanner(): [PlanReActPlanner]()

#### Returns [PlanReActPlanner]()

Inherited from [BasePlanner](BasePlanner.html).[constructor](BasePlanner.html#constructor)




## Properties

### `Readonly`[BASE_PLANNER_SIGNATURE_SYMBOL]

"[BASE_PLANNER_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base planner class.

Inherited from [BasePlanner](BasePlanner.html).[[BASE_PLANNER_SIGNATURE_SYMBOL]](BasePlanner.html#base_planner_signature_symbol)

  * Defined in [core/src/planners/base_planner.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/base_planner.ts#L41)



## Methods

### buildPlanningInstruction

  * buildPlanningInstruction(  
_readonlyContext: [ReadonlyContext](ReadonlyContext.html),  
_llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): string

Builds the system instruction to be appended to the LLM request for planning.

#### Parameters

    * _readonlyContext: [ReadonlyContext](ReadonlyContext.html)
    * _llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

#### Returns string

The planning system instruction, or undefined if no instruction is needed.

Overrides [BasePlanner](BasePlanner.html).[buildPlanningInstruction](BasePlanner.html#buildplanninginstruction)

    * Defined in [core/src/planners/plan_re_act_planner.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/plan_re_act_planner.ts#L36)




### processPlanningResponse

  * processPlanningResponse(  
_callbackContext: [Context](Context.html),  
responseParts: Part[],  
): Part[] | undefined

Processes the LLM response for planning.

#### Parameters

    * _callbackContext: [Context](Context.html)
    * responseParts: Part[]

The LLM response parts. Readonly.

#### Returns Part[] | undefined

The processed response parts, or undefined if no processing is needed.

Overrides [BasePlanner](BasePlanner.html).[processPlanningResponse](BasePlanner.html#processplanningresponse)

    * Defined in [core/src/planners/plan_re_act_planner.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/planners/plan_re_act_planner.ts#L43)




Constructors

constructor

Properties

[BASE_PLANNER_SIGNATURE_SYMBOL]

Methods

buildPlanningInstructionprocessPlanningResponse

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


