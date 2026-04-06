JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../SessionKey.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.sessions](../package-summary.html)
  2. [SessionKey](../SessionKey.html)



# Uses of Class  
com.google.adk.sessions.SessionKey

Packages that use [SessionKey](../SessionKey.html "class in com.google.adk.sessions")

Package

Description

com.google.adk.artifacts

 

com.google.adk.runner

 

com.google.adk.sessions

 

  * ## Uses of [SessionKey](../SessionKey.html "class in com.google.adk.sessions") in [com.google.adk.artifacts](../../artifacts/package-summary.html)

Methods in [com.google.adk.artifacts](../../artifacts/package-summary.html) with parameters of type [SessionKey](../SessionKey.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Completable`

BaseArtifactService.`[deleteArtifact](../../artifacts/BaseArtifactService.html#deleteArtifact\(com.google.adk.sessions.SessionKey,java.lang.String\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

 

`default io.reactivex.rxjava3.core.Single<[ListArtifactsResponse](../../artifacts/ListArtifactsResponse.html "class in com.google.adk.artifacts")>`

BaseArtifactService.`[listArtifactKeys](../../artifacts/BaseArtifactService.html#listArtifactKeys\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

 

`default io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>>`

BaseArtifactService.`[listVersions](../../artifacts/BaseArtifactService.html#listVersions\(com.google.adk.sessions.SessionKey,java.lang.String\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

 

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

BaseArtifactService.`[loadArtifact](../../artifacts/BaseArtifactService.html#loadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename)`

Loads the latest version of an artifact from the service.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Part>`

BaseArtifactService.`[loadArtifact](../../artifacts/BaseArtifactService.html#loadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,int\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, int version)`

 

`default io.reactivex.rxjava3.core.Single<com.google.genai.types.Part>`

BaseArtifactService.`[saveAndReloadArtifact](../../artifacts/BaseArtifactService.html#saveAndReloadArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,com.google.genai.types.Part\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact and returns it with fileData if available.

`default io.reactivex.rxjava3.core.Single<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")>`

BaseArtifactService.`[saveArtifact](../../artifacts/BaseArtifactService.html#saveArtifact\(com.google.adk.sessions.SessionKey,java.lang.String,com.google.genai.types.Part\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") filename, com.google.genai.types.Part artifact)`

Saves an artifact.

  * ## Uses of [SessionKey](../SessionKey.html "class in com.google.adk.sessions") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [SessionKey](../SessionKey.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.SessionKey,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

  * ## Uses of [SessionKey](../SessionKey.html "class in com.google.adk.sessions") in [com.google.adk.sessions](../package-summary.html)

Methods in [com.google.adk.sessions](../package-summary.html) that return [SessionKey](../SessionKey.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`static [SessionKey](../SessionKey.html "class in com.google.adk.sessions")`

SessionKey.`[fromJson](../SessionKey.html#fromJson\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)`

 

`[SessionKey](../SessionKey.html "class in com.google.adk.sessions")`

Session.`[sessionKey](../Session.html#sessionKey\(\))()`

Returns the session key.

Methods in [com.google.adk.sessions](../package-summary.html) with parameters of type [SessionKey](../SessionKey.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`static [Session.Builder](../Session.Builder.html "class in com.google.adk.sessions")`

Session.`[builder](../Session.html#builder\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Creates a new [`Session.Builder`](../Session.Builder.html "class in com.google.adk.sessions") with the given session key.

`default io.reactivex.rxjava3.core.Single<[Session](../Session.html "class in com.google.adk.sessions")>`

BaseSessionService.`[createSession](../BaseSessionService.html#createSession\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Creates a new session with the specified application name and user ID, using a default state (null) and allowing the service to generate a unique session ID.

`default io.reactivex.rxjava3.core.Single<[Session](../Session.html "class in com.google.adk.sessions")>`

BaseSessionService.`[createSession](../BaseSessionService.html#createSession\(com.google.adk.sessions.SessionKey,java.util.Map\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

Creates a new session with the specified parameters.

`default io.reactivex.rxjava3.core.Completable`

BaseSessionService.`[deleteSession](../BaseSessionService.html#deleteSession\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Deletes a specific session.

`default io.reactivex.rxjava3.core.Maybe<[Session](../Session.html "class in com.google.adk.sessions")>`

BaseSessionService.`[getSession](../BaseSessionService.html#getSession\(com.google.adk.sessions.SessionKey,com.google.adk.sessions.GetSessionConfig\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey, @Nullable [GetSessionConfig](../GetSessionConfig.html "class in com.google.adk.sessions") config)`

Retrieves a specific session, optionally filtering the events included.

`default io.reactivex.rxjava3.core.Single<[ListEventsResponse](../ListEventsResponse.html "class in com.google.adk.sessions")>`

BaseSessionService.`[listEvents](../BaseSessionService.html#listEvents\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Lists the events within a specific session.

`default io.reactivex.rxjava3.core.Single<[ListSessionsResponse](../ListSessionsResponse.html "class in com.google.adk.sessions")>`

BaseSessionService.`[listSessions](../BaseSessionService.html#listSessions\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Lists sessions associated with a specific application and user.

`[Session.Builder](../Session.Builder.html "class in com.google.adk.sessions")`

Session.Builder.`[sessionKey](../Session.Builder.html#sessionKey\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Sets the session key.

Constructors in [com.google.adk.sessions](../package-summary.html) with parameters of type [SessionKey](../SessionKey.html "class in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[Builder](../Session.Builder.html#%3Cinit%3E\(com.google.adk.sessions.SessionKey\))([SessionKey](../SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Creates a new [`Session.Builder`](../Session.Builder.html "class in com.google.adk.sessions") with the given session key.




* * *

Copyright (C) 1980\. All rights reserved.
