JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](index.html)
  * [Tree](overview-tree.html)
  * Deprecated
  * [Index](index-all.html)
  * [Search](search.html)






# Deprecated API

## Contents

  * Terminally Deprecated
  * Methods
  * Constructors


  * Terminally Deprecated Elements

Element

Description

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

Use runAsync with sessionId.

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig, Map<String, Object>)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))

Use runAsync with sessionId.

[com.google.adk.runner.Runner.runWithSessionId(String, Content, RunConfig)](com/google/adk/runner/Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))



  * Deprecated Methods

Method

Description

[com.google.adk.events.Event.setFinishReason(Optional<FinishReason>)](com/google/adk/events/Event.html#setFinishReason\(java.util.Optional\))

[com.google.adk.events.EventActions.Builder.endInvocation(boolean)](com/google/adk/events/EventActions.Builder.html#endInvocation\(boolean\))

Use [`EventActions.Builder.endOfAgent(boolean)`](com/google/adk/events/EventActions.Builder.html#endOfAgent\(boolean\)) instead.

[com.google.adk.events.EventActions.endInvocation()](com/google/adk/events/EventActions.html#endInvocation\(\))

Use [`EventActions.endOfAgent()`](com/google/adk/events/EventActions.html#endOfAgent\(\)) instead.

[com.google.adk.events.EventActions.setEndInvocation(boolean)](com/google/adk/events/EventActions.html#setEndInvocation\(boolean\))

Use [`EventActions.setEndOfAgent(boolean)`](com/google/adk/events/EventActions.html#setEndOfAgent\(boolean\)) instead.

[com.google.adk.events.EventActions.setStateDelta(ConcurrentMap<String, Object>)](com/google/adk/events/EventActions.html#setStateDelta\(java.util.concurrent.ConcurrentMap\))

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

Use runAsync with sessionId.

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig, Map<String, Object>)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))

Use runAsync with sessionId.

[com.google.adk.runner.Runner.runWithSessionId(String, Content, RunConfig)](com/google/adk/runner/Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

[com.google.adk.sessions.BaseSessionService.createSession(String, String, ConcurrentMap<String, Object>, String)](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))

Use [`BaseSessionService.createSession(String, String, Map, String)`](com/google/adk/sessions/BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.Map,java.lang.String\)) instead.

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
