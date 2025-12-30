JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)



Contents

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Related Packages
  3. Classes and Interfaces



# Package com.google.adk.sessions

* * *

package com.google.adk.sessions

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesException Classes

Class

Description

[ApiResponse](ApiResponse.html "class in com.google.adk.sessions")

The API response contains a response to a call to the GenAI APIs.

[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")

Defines the contract for managing [`Session`](Session.html "class in com.google.adk.sessions")s and their associated [`Event`](../events/Event.html "class in com.google.adk.events")s.

[GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions")

Configuration for getting a session.

[GetSessionConfig.Builder](GetSessionConfig.Builder.html "class in com.google.adk.sessions")

Builder for [`GetSessionConfig`](GetSessionConfig.html "class in com.google.adk.sessions").

[HttpApiClient](HttpApiClient.html "class in com.google.adk.sessions")

Base client for the HTTP APIs.

[HttpApiResponse](HttpApiResponse.html "class in com.google.adk.sessions")

Wraps a real HTTP response to expose the methods needed by the GenAI SDK.

[InMemorySessionService](InMemorySessionService.html "class in com.google.adk.sessions")

An in-memory implementation of [`BaseSessionService`](BaseSessionService.html "interface in com.google.adk.sessions") assuming [`Session`](Session.html "class in com.google.adk.sessions") objects are mutable regarding their state map, events list, and last update time.

[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")

Response for listing events.

[ListEventsResponse.Builder](ListEventsResponse.Builder.html "class in com.google.adk.sessions")

Builder for [`ListEventsResponse`](ListEventsResponse.html "class in com.google.adk.sessions").

[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")

Response for listing sessions.

[ListSessionsResponse.Builder](ListSessionsResponse.Builder.html "class in com.google.adk.sessions")

Builder for [`ListSessionsResponse`](ListSessionsResponse.html "class in com.google.adk.sessions").

[Session](Session.html "class in com.google.adk.sessions")

A [`Session`](Session.html "class in com.google.adk.sessions") object that encapsulates the [`State`](State.html "class in com.google.adk.sessions") and [`Event`](../events/Event.html "class in com.google.adk.events")s of a session.

[Session.Builder](Session.Builder.html "class in com.google.adk.sessions")

Builder for [`Session`](Session.html "class in com.google.adk.sessions").

[SessionException](SessionException.html "class in com.google.adk.sessions")

Represents a general error that occurred during session management operations.

[SessionNotFoundException](SessionNotFoundException.html "class in com.google.adk.sessions")

Indicates that a requested session could not be found.

[SessionUtils](SessionUtils.html "class in com.google.adk.sessions")

Utility functions for session service.

[State](State.html "class in com.google.adk.sessions")

A [`State`](State.html "class in com.google.adk.sessions") object that also keeps track of the changes to the state.

[VertexAiSessionService](VertexAiSessionService.html "class in com.google.adk.sessions")

TODO: Use the genai HttpApiClient and ApiResponse methods once they are public.




* * *

Copyright (C) 2025\. All rights reserved.
