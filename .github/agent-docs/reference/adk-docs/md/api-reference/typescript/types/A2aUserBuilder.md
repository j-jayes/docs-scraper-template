[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [A2aUserBuilder]()



# Type Alias A2aUserBuilder

A2aUserBuilder: UserBuilder

A request authenticator for the A2A surface.

This is the `UserBuilder` hook from `@a2a-js/sdk`: an async function that receives the incoming Express request, validates its credentials (for example a bearer token or an OIDC ID token) and resolves to the authenticated `User`. Implementations should reject unauthenticated requests by throwing (or by resolving to a user whose `isAuthenticated` is `false`), which prevents the underlying agent and its tools from being invoked by anonymous callers.

  * Defined in [core/src/a2a/agent_to_a2a.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L38)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


