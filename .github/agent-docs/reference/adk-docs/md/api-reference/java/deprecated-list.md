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

[com.google.adk.agents.InvocationContext(BaseSessionService, BaseArtifactService, BaseMemoryService, Plugin, Optional<LiveRequestQueue>, Optional<String>, String, BaseAgent, Session, Optional<Content>, RunConfig, boolean)](com/google/adk/agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,com.google.adk.plugins.Plugin,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.agents.InvocationContext(BaseSessionService, BaseArtifactService, BaseMemoryService, Optional<LiveRequestQueue>, Optional<String>, String, BaseAgent, Session, Optional<Content>, RunConfig, boolean)](com/google/adk/agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.agents.InvocationContext.agent(BaseAgent)](com/google/adk/agents/InvocationContext.html#agent\(com.google.adk.agents.BaseAgent\))

Use [`InvocationContext.toBuilder()`](com/google/adk/agents/InvocationContext.html#toBuilder\(\)) and [`InvocationContext.Builder.agent(BaseAgent)`](com/google/adk/agents/InvocationContext.Builder.html#agent\(com.google.adk.agents.BaseAgent\)) instead.

[com.google.adk.agents.InvocationContext.branch(String)](com/google/adk/agents/InvocationContext.html#branch\(java.lang.String\))

Use [`InvocationContext.toBuilder()`](com/google/adk/agents/InvocationContext.html#toBuilder\(\)) and [`InvocationContext.Builder.branch(String)`](com/google/adk/agents/InvocationContext.Builder.html#branch\(java.lang.String\)) instead.

[com.google.adk.agents.InvocationContext.Builder.branch(Optional<String>)](com/google/adk/agents/InvocationContext.Builder.html#branch\(java.util.Optional\))

Use [`InvocationContext.Builder.branch(String)`](com/google/adk/agents/InvocationContext.Builder.html#branch\(java.lang.String\)) instead.

[com.google.adk.agents.InvocationContext.Builder.liveRequestQueue(Optional<LiveRequestQueue>)](com/google/adk/agents/InvocationContext.Builder.html#liveRequestQueue\(java.util.Optional\))

Use [`InvocationContext.Builder.liveRequestQueue(LiveRequestQueue)`](com/google/adk/agents/InvocationContext.Builder.html#liveRequestQueue\(com.google.adk.agents.LiveRequestQueue\)) instead.

[com.google.adk.agents.InvocationContext.copyOf(InvocationContext)](com/google/adk/agents/InvocationContext.html#copyOf\(com.google.adk.agents.InvocationContext\))

Use `other.toBuilder().build()` instead.

[com.google.adk.agents.InvocationContext.create(BaseSessionService, BaseArtifactService, BaseAgent, Session, LiveRequestQueue, RunConfig)](com/google/adk/agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.agents.InvocationContext.create(BaseSessionService, BaseArtifactService, String, BaseAgent, Session, Content, RunConfig)](com/google/adk/agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

Use runAsync with sessionId.

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig, Map<String, Object>)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))

Use runAsync with sessionId.



  * Deprecated Methods

Method

Description

[com.google.adk.agents.InvocationContext.agent(BaseAgent)](com/google/adk/agents/InvocationContext.html#agent\(com.google.adk.agents.BaseAgent\))

Use [`InvocationContext.toBuilder()`](com/google/adk/agents/InvocationContext.html#toBuilder\(\)) and [`InvocationContext.Builder.agent(BaseAgent)`](com/google/adk/agents/InvocationContext.Builder.html#agent\(com.google.adk.agents.BaseAgent\)) instead.

[com.google.adk.agents.InvocationContext.branch(String)](com/google/adk/agents/InvocationContext.html#branch\(java.lang.String\))

Use [`InvocationContext.toBuilder()`](com/google/adk/agents/InvocationContext.html#toBuilder\(\)) and [`InvocationContext.Builder.branch(String)`](com/google/adk/agents/InvocationContext.Builder.html#branch\(java.lang.String\)) instead.

[com.google.adk.agents.InvocationContext.Builder.branch(Optional<String>)](com/google/adk/agents/InvocationContext.Builder.html#branch\(java.util.Optional\))

Use [`InvocationContext.Builder.branch(String)`](com/google/adk/agents/InvocationContext.Builder.html#branch\(java.lang.String\)) instead.

[com.google.adk.agents.InvocationContext.Builder.liveRequestQueue(Optional<LiveRequestQueue>)](com/google/adk/agents/InvocationContext.Builder.html#liveRequestQueue\(java.util.Optional\))

Use [`InvocationContext.Builder.liveRequestQueue(LiveRequestQueue)`](com/google/adk/agents/InvocationContext.Builder.html#liveRequestQueue\(com.google.adk.agents.LiveRequestQueue\)) instead.

[com.google.adk.agents.InvocationContext.copyOf(InvocationContext)](com/google/adk/agents/InvocationContext.html#copyOf\(com.google.adk.agents.InvocationContext\))

Use `other.toBuilder().build()` instead.

[com.google.adk.agents.InvocationContext.create(BaseSessionService, BaseArtifactService, BaseAgent, Session, LiveRequestQueue, RunConfig)](com/google/adk/agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.agents.InvocationContext.create(BaseSessionService, BaseArtifactService, String, BaseAgent, Session, Content, RunConfig)](com/google/adk/agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))

Use runAsync with sessionId.

[com.google.adk.runner.Runner.runAsync(Session, Content, RunConfig, Map<String, Object>)](com/google/adk/runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))

Use runAsync with sessionId.



  * Deprecated Constructors

Constructor

Description

[com.google.adk.agents.InvocationContext(BaseSessionService, BaseArtifactService, BaseMemoryService, Plugin, Optional<LiveRequestQueue>, Optional<String>, String, BaseAgent, Session, Optional<Content>, RunConfig, boolean)](com/google/adk/agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,com.google.adk.plugins.Plugin,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.agents.InvocationContext(BaseSessionService, BaseArtifactService, BaseMemoryService, Optional<LiveRequestQueue>, Optional<String>, String, BaseAgent, Session, Optional<Content>, RunConfig, boolean)](com/google/adk/agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))

Use [`InvocationContext.builder()`](com/google/adk/agents/InvocationContext.html#builder\(\)) instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List<BasePlugin>)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List<BasePlugin>, ResumabilityConfig)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.flows.llmflows.ResumabilityConfig\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.

[com.google.adk.runner.Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List<BasePlugin>, ResumabilityConfig, EventsCompactionConfig)](com/google/adk/runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.flows.llmflows.ResumabilityConfig,com.google.adk.summarizer.EventsCompactionConfig\))

Use [`Runner.Builder`](com/google/adk/runner/Runner.Builder.html "class in com.google.adk.runner") instead.




* * *

Copyright (C) 1980\. All rights reserved.
