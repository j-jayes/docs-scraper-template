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

  * Classes
  * Methods
  * Constructors


  * Deprecated Classes

Class

Description

[com.google.adk.apps.ResumabilityConfig](com/google/adk/apps/ResumabilityConfig.html "class in com.google.adk.apps")

Partial feature: only event-reconstruction-based pause/resume for ` SequentialAgent` is implemented. Full session resumability (persisted agent state, durable resume, other workflow agents) is not yet available. Forward-compatible: the same config will drive full resumability once it lands.



  * Deprecated Methods

Method

Description

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

[com.google.adk.apps.App.Builder.resumabilityConfig(ResumabilityConfig)](com/google/adk/apps/App.Builder.html#resumabilityConfig\(com.google.adk.apps.ResumabilityConfig\))

See [`ResumabilityConfig`](com/google/adk/apps/ResumabilityConfig.html "class in com.google.adk.apps"): partial feature, full resumability not yet available.

[com.google.adk.events.Event.setFinishReason(Optional<FinishReason>)](com/google/adk/events/Event.html#setFinishReason\(java.util.Optional\))

[com.google.adk.events.EventActions.Builder.endInvocation(boolean)](com/google/adk/events/EventActions.Builder.html#endInvocation\(boolean\))

Use [`EventActions.Builder.endOfAgent(boolean)`](com/google/adk/events/EventActions.Builder.html#endOfAgent\(boolean\)) instead.

[com.google.adk.events.EventActions.endInvocation()](com/google/adk/events/EventActions.html#endInvocation\(\))

Use [`EventActions.endOfAgent()`](com/google/adk/events/EventActions.html#endOfAgent\(\)) instead.

[com.google.adk.events.EventActions.setEndInvocation(boolean)](com/google/adk/events/EventActions.html#setEndInvocation\(boolean\))

Use [`EventActions.setEndOfAgent(boolean)`](com/google/adk/events/EventActions.html#setEndOfAgent\(boolean\)) instead.

[com.google.adk.events.EventActions.setStateDelta(ConcurrentMap<String, Object>)](com/google/adk/events/EventActions.html#setStateDelta\(java.util.concurrent.ConcurrentMap\))

[com.google.adk.memory.SearchMemoryResponse.Builder.setMemories(ImmutableList<MemoryEntry>)](com/google/adk/memory/SearchMemoryResponse.Builder.html#setMemories\(com.google.common.collect.ImmutableList\))

[com.google.adk.memory.SearchMemoryResponse.Builder.setMemories(List<MemoryEntry>)](com/google/adk/memory/SearchMemoryResponse.Builder.html#setMemories\(java.util.List\))

[com.google.adk.models.VertexCredentials.Builder.setCredentials(GoogleCredentials)](com/google/adk/models/VertexCredentials.Builder.html#setCredentials\(com.google.auth.oauth2.GoogleCredentials\))

[com.google.adk.models.VertexCredentials.Builder.setLocation(String)](com/google/adk/models/VertexCredentials.Builder.html#setLocation\(java.lang.String\))

[com.google.adk.models.VertexCredentials.Builder.setProject(String)](com/google/adk/models/VertexCredentials.Builder.html#setProject\(java.lang.String\))

[com.google.adk.sessions.BaseSessionService.createSession(String, String, ConcurrentMap<String, Object>, String)](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))

Use [`BaseSessionService.createSession(String, String, Map, String)`](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.Map,java.lang.String\)) instead.

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




* * *

Copyright (C) 1980\. All rights reserved.
