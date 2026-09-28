[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [findEventByLastFunctionResponseId]()



# Function findEventByLastFunctionResponseId

  * findEventByLastFunctionResponseId(events: [Event](../interfaces/Event.html)[]): [Event](../interfaces/Event.html) | null

It iterates through the events in reverse order, and returns the event containing a function call with a [functionCall.id](http://functionCall.id) matching the [functionResponse.id](http://functionResponse.id) from the last event in the session.

#### Parameters

    * events: [Event](../interfaces/Event.html)[]

#### Returns [Event](../interfaces/Event.html) | null

    * Defined in [core/src/runner/runner.ts:661](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L661)




[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


