[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ResumeInputs]()



# Type Alias ResumeInputs`Experimental`

ResumeInputs: Record<string, unknown>

Inputs handed to a tool call that is being resumed after it paused for them, keyed by the id of the interrupt that asked for each one. JSON-serializable.

Deliberately separate from `ToolConfirmation`. Both travel the same route — built by a resume processor, threaded through `handleFunctionCallList` onto the tool context — but they say different things. A `ToolConfirmation` says a human looked at an action and approved it, and the confirmation gate runs a tool on the strength of that. `ResumeInputs` says only that the user answered a question the tool asked; it carries no authority and cannot satisfy a gate, which is why it has no `confirmed` field to set.

Named here rather than left as a bare mapping so the distinction above has somewhere to live, but the shape mirrors `Context.resume_inputs` in `google/adk-python` (`agents/context.py`): the same flat mapping keyed by interrupt id, defaulting to empty rather than absent.

(Experimental, subject to change)

  * Defined in [core/src/tools/resume_inputs.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/resume_inputs.ts#L26)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


