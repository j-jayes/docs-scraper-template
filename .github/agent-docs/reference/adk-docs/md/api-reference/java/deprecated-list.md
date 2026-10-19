JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](index.html)
  * [Tree](overview-tree.html)
  * Deprecated
  * [Index](index-all.html)
  * [Search](search.html)
  * 


Select Theme

LightDarkSystem Setting




# Deprecated API

## Contents

  * Methods
  * Constructors
  * Enum Constants


  * Deprecated Methods

Method

Description

[com.google.adk.agents.ContextCacheConfig.maxInvocations()](com/google/adk/agents/ContextCacheConfig.html#maxInvocations\(\))

Use [`ContextCacheConfig.cacheIntervals()`](com/google/adk/agents/ContextCacheConfig.html#cacheIntervals\(\)), the name ADK Python and ADK Kotlin use.

[com.google.adk.agents.InvocationContext.isLegacyResumability()](com/google/adk/agents/InvocationContext.html#isLegacyResumability\(\))

Reports the deprecated plain-text continuation shim and goes away with it; use [`InvocationContext.isResumable()`](com/google/adk/agents/InvocationContext.html#isResumable\(\)).

[com.google.adk.agents.RunConfig.Builder.groupFunctionResponsesInHistory(boolean)](com/google/adk/agents/RunConfig.Builder.html#groupFunctionResponsesInHistory\(boolean\))

Expected only for specific model endpoints.

[com.google.adk.agents.RunConfig.Builder.groupFunctionResponsesInHistoryOverride(boolean)](com/google/adk/agents/RunConfig.Builder.html#groupFunctionResponsesInHistoryOverride\(boolean\))

Expected only for specific model endpoints.

[com.google.adk.agents.RunConfig.Builder.groupFunctionResponsesInHistoryOverride(Optional<Boolean>)](com/google/adk/agents/RunConfig.Builder.html#groupFunctionResponsesInHistoryOverride\(java.util.Optional\))

Expected only for specific model endpoints.

[com.google.adk.agents.RunConfig.Builder.setAutoCreateSession(boolean)](com/google/adk/agents/RunConfig.Builder.html#setAutoCreateSession\(boolean\))

[com.google.adk.agents.RunConfig.Builder.setInputAudioTranscription(AudioTranscriptionConfig)](com/google/adk/agents/RunConfig.Builder.html#setInputAudioTranscription\(com.google.genai.types.AudioTranscriptionConfig\))

[com.google.adk.agents.RunConfig.Builder.setMaxLlmCalls(int)](com/google/adk/agents/RunConfig.Builder.html#setMaxLlmCalls\(int\))

[com.google.adk.agents.RunConfig.Builder.setOutputAudioTranscription(AudioTranscriptionConfig)](com/google/adk/agents/RunConfig.Builder.html#setOutputAudioTranscription\(com.google.genai.types.AudioTranscriptionConfig\))

[com.google.adk.agents.RunConfig.Builder.setResponseModalities(Iterable<Modality>)](com/google/adk/agents/RunConfig.Builder.html#setResponseModalities\(java.lang.Iterable\))

[com.google.adk.agents.RunConfig.Builder.setSaveInputBlobsAsArtifacts(boolean)](com/google/adk/agents/RunConfig.Builder.html#setSaveInputBlobsAsArtifacts\(boolean\))

[com.google.adk.agents.RunConfig.Builder.setSpeechConfig(SpeechConfig)](com/google/adk/agents/RunConfig.Builder.html#setSpeechConfig\(com.google.genai.types.SpeechConfig\))

[com.google.adk.agents.RunConfig.Builder.setStreamingMode(RunConfig.StreamingMode)](com/google/adk/agents/RunConfig.Builder.html#setStreamingMode\(com.google.adk.agents.RunConfig.StreamingMode\))

[com.google.adk.agents.RunConfig.Builder.setToolExecutionMode(RunConfig.ToolExecutionMode)](com/google/adk/agents/RunConfig.Builder.html#setToolExecutionMode\(com.google.adk.agents.RunConfig.ToolExecutionMode\))

[com.google.adk.agents.RunConfig.groupFunctionResponsesInHistory()](com/google/adk/agents/RunConfig.html#groupFunctionResponsesInHistory\(\))

Expected only for specific model endpoints.

[com.google.adk.agents.RunConfig.groupFunctionResponsesInHistoryOverride()](com/google/adk/agents/RunConfig.html#groupFunctionResponsesInHistoryOverride\(\))

Expected only for specific model endpoints.

[com.google.adk.apps.ResumabilityConfig.Builder.plainTextContinuationAutoResume(boolean)](com/google/adk/apps/ResumabilityConfig.Builder.html#plainTextContinuationAutoResume\(boolean\))

Back-compat shim only; migrate to `Runner.runAsync(...)` with an invocation id (or send a function response to the paused call). See [`ResumabilityConfig.isPlainTextContinuationAutoResume()`](com/google/adk/apps/ResumabilityConfig.html#isPlainTextContinuationAutoResume\(\)).

[com.google.adk.apps.ResumabilityConfig.isPlainTextContinuationAutoResume()](com/google/adk/apps/ResumabilityConfig.html#isPlainTextContinuationAutoResume\(\))

Back-compat shim for callers that deliver a resume as a plain-text turn; migrate to `Runner.runAsync(userId, sessionId, invocationId, message, runConfig, stateDelta)` or answer the paused call with a function response, and set [`ResumabilityConfig.isResumable()`](com/google/adk/apps/ResumabilityConfig.html#isResumable\(\)) instead; this flag will be removed.

[com.google.adk.events.Event.setFinishReason(Optional<FinishReason>)](com/google/adk/events/Event.html#setFinishReason\(java.util.Optional\))

Use [`Event.setFinishReason(FinishReason)`](com/google/adk/events/Event.html#setFinishReason\(com.google.genai.types.FinishReason\)) with `finishReason.orElse(null)` instead.

[com.google.adk.events.EventActions.Builder.endInvocation(boolean)](com/google/adk/events/EventActions.Builder.html#endInvocation\(boolean\))

Use [`EventActions.Builder.endOfAgent(boolean)`](com/google/adk/events/EventActions.Builder.html#endOfAgent\(boolean\)) instead.

[com.google.adk.events.EventActions.endInvocation()](com/google/adk/events/EventActions.html#endInvocation\(\))

Use [`EventActions.endOfAgent()`](com/google/adk/events/EventActions.html#endOfAgent\(\)) instead.

[com.google.adk.events.EventActions.setEndInvocation(boolean)](com/google/adk/events/EventActions.html#setEndInvocation\(boolean\))

Use [`EventActions.setEndOfAgent(boolean)`](com/google/adk/events/EventActions.html#setEndOfAgent\(boolean\)) instead.

[com.google.adk.events.EventActions.setStateDelta(ConcurrentMap<String, Object>)](com/google/adk/events/EventActions.html#setStateDelta\(java.util.concurrent.ConcurrentMap\))

Update the map returned by [`EventActions.stateDelta()`](com/google/adk/events/EventActions.html#stateDelta\(\)) instead, and use [`EventActions.removeStateByKey(String)`](com/google/adk/events/EventActions.html#removeStateByKey\(java.lang.String\)) to remove a key.

[com.google.adk.memory.SearchMemoryResponse.Builder.setMemories(ImmutableList<MemoryEntry>)](com/google/adk/memory/SearchMemoryResponse.Builder.html#setMemories\(com.google.common.collect.ImmutableList\))

[com.google.adk.memory.SearchMemoryResponse.Builder.setMemories(List<MemoryEntry>)](com/google/adk/memory/SearchMemoryResponse.Builder.html#setMemories\(java.util.List\))

[com.google.adk.models.VertexCredentials.Builder.setCredentials(GoogleCredentials)](com/google/adk/models/VertexCredentials.Builder.html#setCredentials\(com.google.auth.oauth2.GoogleCredentials\))

[com.google.adk.models.VertexCredentials.Builder.setLocation(String)](com/google/adk/models/VertexCredentials.Builder.html#setLocation\(java.lang.String\))

[com.google.adk.models.VertexCredentials.Builder.setProject(String)](com/google/adk/models/VertexCredentials.Builder.html#setProject\(java.lang.String\))

[com.google.adk.sessions.BaseSessionService.createSession(String, String, ConcurrentMap<String, Object>, String)](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))

Use [`BaseSessionService.createSession(String, String, Map, String)`](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.Map,java.lang.String\)) instead.

[com.google.adk.sessions.Session.Builder.eventsView(List<Event>)](com/google/adk/sessions/Session.Builder.html#eventsView\(java.util.List\))

Not a real deprecation - a warn-off for application code from a seam meant for ADK's own framework and interop adapters; use [`Session.Builder.events(List)`](com/google/adk/sessions/Session.Builder.html#events\(java.util.List\)) instead.

[com.google.adk.sessions.Session.events()](com/google/adk/sessions/Session.html#events\(\))

Prefer [`Session.immutableEvents()`](com/google/adk/sessions/Session.html#immutableEvents\(\)) when reading or iterating over events (to avoid [`ConcurrentModificationException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ConcurrentModificationException.html "class in java.util")), and [`Session.addEvent(Event)`](com/google/adk/sessions/Session.html#addEvent\(com.google.adk.events.Event\)) or [`Session.addEvents(Collection)`](com/google/adk/sessions/Session.html#addEvents\(java.util.Collection\)) when appending events.

[com.google.adk.telemetry.Instrumentation.recordAgentInvocation(InvocationContext, BaseAgent)](com/google/adk/telemetry/Instrumentation.html#recordAgentInvocation\(com.google.adk.agents.InvocationContext,com.google.adk.agents.BaseAgent\))

Use the version with explicit parent context instead. This method will be removed once all callers are updated.

[com.google.adk.telemetry.Tracing.traceAgent(String, String, String, InvocationContext)](com/google/adk/telemetry/Tracing.html#traceAgent\(java.lang.String,java.lang.String,java.lang.String,com.google.adk.agents.InvocationContext\))

[com.google.adk.tools.ExampleTool.Builder.setDescription(String)](com/google/adk/tools/ExampleTool.Builder.html#setDescription\(java.lang.String\))

[com.google.adk.tools.ExampleTool.Builder.setExampleProvider(BaseExampleProvider)](com/google/adk/tools/ExampleTool.Builder.html#setExampleProvider\(com.google.adk.examples.BaseExampleProvider\))

[com.google.adk.tools.ExampleTool.Builder.setName(String)](com/google/adk/tools/ExampleTool.Builder.html#setName\(java.lang.String\))

[com.google.adk.tools.ToolPredicate.test(BaseTool, Optional<ReadonlyContext>)](com/google/adk/tools/ToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))

Use [`ToolPredicate.test(BaseTool, ReadonlyContext)`](com/google/adk/tools/ToolPredicate.html#test\(com.google.adk.tools.BaseTool,com.google.adk.agents.ReadonlyContext\)) instead.



  * Deprecated Constructors

Constructor

Description

[com.google.adk.codeexecutors.ContainerCodeExecutor(String, String, String)](com/google/adk/codeexecutors/ContainerCodeExecutor.html#%3Cinit%3E\(java.lang.String,java.lang.String,java.lang.String\))

Use one of the static factory methods instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List<? extends Plugin>)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List<? extends Plugin>, EventsCompactionConfig, ContextCacheConfig)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List<? extends Plugin>, EventsCompactionConfig, ContextCacheConfig, ResumabilityConfig)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig,com.google.adk.apps.ResumabilityConfig\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.



  * Deprecated Enum Constants

Enum Constant

Description

[com.google.adk.sessions.InMemorySessionService.DuplicateSessionIdBehavior.OVERWRITE](com/google/adk/sessions/InMemorySessionService.DuplicateSessionIdBehavior.html#OVERWRITE)

Construct the service with [`InMemorySessionService.DuplicateSessionIdBehavior.REJECT`](com/google/adk/sessions/InMemorySessionService.DuplicateSessionIdBehavior.html#REJECT) instead, which becomes the default in a future release.




* * *

Copyright (C) 1980\. All rights reserved.
