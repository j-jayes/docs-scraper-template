JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](index.html)
  * [Tree](overview-tree.html)
  * Deprecated
  * [Index](index-all.html)
  * [Search](search.html)






# Deprecated API

## Contents

  * Methods
  * Constructors


  * Deprecated Methods

Method

Description

[com.google.adk.agents.RunConfig.Builder.setAutoCreateSession(boolean)](com/google/adk/agents/RunConfig.Builder.html#setAutoCreateSession\(boolean\))

[com.google.adk.agents.RunConfig.Builder.setInputAudioTranscription(AudioTranscriptionConfig)](com/google/adk/agents/RunConfig.Builder.html#setInputAudioTranscription\(com.google.genai.types.AudioTranscriptionConfig\))

[com.google.adk.agents.RunConfig.Builder.setMaxLlmCalls(int)](com/google/adk/agents/RunConfig.Builder.html#setMaxLlmCalls\(int\))

[com.google.adk.agents.RunConfig.Builder.setOutputAudioTranscription(AudioTranscriptionConfig)](com/google/adk/agents/RunConfig.Builder.html#setOutputAudioTranscription\(com.google.genai.types.AudioTranscriptionConfig\))

[com.google.adk.agents.RunConfig.Builder.setResponseModalities(Iterable<Modality>)](com/google/adk/agents/RunConfig.Builder.html#setResponseModalities\(java.lang.Iterable\))

[com.google.adk.agents.RunConfig.Builder.setSaveInputBlobsAsArtifacts(boolean)](com/google/adk/agents/RunConfig.Builder.html#setSaveInputBlobsAsArtifacts\(boolean\))

[com.google.adk.agents.RunConfig.Builder.setSpeechConfig(SpeechConfig)](com/google/adk/agents/RunConfig.Builder.html#setSpeechConfig\(com.google.genai.types.SpeechConfig\))

[com.google.adk.agents.RunConfig.Builder.setStreamingMode(RunConfig.StreamingMode)](com/google/adk/agents/RunConfig.Builder.html#setStreamingMode\(com.google.adk.agents.RunConfig.StreamingMode\))

[com.google.adk.agents.RunConfig.Builder.setToolExecutionMode(RunConfig.ToolExecutionMode)](com/google/adk/agents/RunConfig.Builder.html#setToolExecutionMode\(com.google.adk.agents.RunConfig.ToolExecutionMode\))

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

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setAutoSchemaUpgrade(boolean)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setAutoSchemaUpgrade\(boolean\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setBatchFlushInterval(Duration)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setBatchFlushInterval\(java.time.Duration\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setBatchSize(int)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setBatchSize\(int\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setClusteringFields(List<String>)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setClusteringFields\(java.util.List\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setConnectionId(String)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setConnectionId\(java.lang.String\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setContentFormatter(BiFunction<Object, String, Object>)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setContentFormatter\(java.util.function.BiFunction\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setCredentials(Credentials)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setCredentials\(com.google.auth.Credentials\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setCustomTags(Map<String, Object>)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setCustomTags\(java.util.Map\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setDatasetId(String)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setDatasetId\(java.lang.String\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setEnabled(boolean)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setEnabled\(boolean\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setEventAllowlist(List<String>)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setEventAllowlist\(java.util.List\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setEventDenylist(List<String>)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setEventDenylist\(java.util.List\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setLogMultiModalContent(boolean)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setLogMultiModalContent\(boolean\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setLogSessionMetadata(boolean)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setLogSessionMetadata\(boolean\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setMaxContentLength(int)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setMaxContentLength\(int\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setProjectId(String)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setProjectId\(java.lang.String\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setQueueMaxSize(int)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setQueueMaxSize\(int\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setRetryConfig(BigQueryLoggerConfig.RetryConfig)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setRetryConfig\(com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setShutdownTimeout(Duration)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setShutdownTimeout\(java.time.Duration\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.Builder.setTableName(String)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.Builder.html#setTableName\(java.lang.String\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig.Builder.setInitialDelay(Duration)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.RetryConfig.Builder.html#setInitialDelay\(java.time.Duration\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig.Builder.setMaxDelay(Duration)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.RetryConfig.Builder.html#setMaxDelay\(java.time.Duration\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig.Builder.setMaxRetries(int)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.RetryConfig.Builder.html#setMaxRetries\(int\))

[com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig.Builder.setMultiplier(double)](com/google/adk/plugins/agentanalytics/BigQueryLoggerConfig.RetryConfig.Builder.html#setMultiplier\(double\))

[com.google.adk.sessions.BaseSessionService.createSession(String, String, ConcurrentMap<String, Object>, String)](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))

Use [`BaseSessionService.createSession(String, String, Map, String)`](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.Map,java.lang.String\)) instead.

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




* * *

Copyright (C) 1980\. All rights reserved.
