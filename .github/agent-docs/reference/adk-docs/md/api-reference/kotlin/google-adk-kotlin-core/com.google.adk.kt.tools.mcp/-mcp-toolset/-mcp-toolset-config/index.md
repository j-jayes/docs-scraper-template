toggle menu

[ google-adk-kotlin ](../../../../index.html)

0.1.0 

jvm

switch theme

search in API

[google-adk-kotlin-core](../../../index.html)/[com.google.adk.kt.tools.mcp](../../index.html)/[McpToolset](../index.html)/McpToolsetConfig

# McpToolsetConfig

jvm

data class [McpToolsetConfig](index.html)(val stdioConnectionParams: [McpConnectionParameters.Stdio](../../-mcp-connection-parameters/-stdio/index.html)? = null, val sseConnectionParams: [McpConnectionParameters.Sse](../../-mcp-connection-parameters/-sse/index.html)? = null, val streamableHttpConnectionParams: [McpConnectionParameters.StreamableHttp](../../-mcp-connection-parameters/-streamable-http/index.html)? = null, val toolFilter: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val useMcpResources: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val maxMcpResourceLength: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html) = DEFAULT_MAX_RESOURCE_LENGTH)

Configuration for an [McpToolset](../index.html), used to construct one via [toToolset](to-toolset.html).

Exactly one of [stdioConnectionParams](stdio-connection-params.html), [sseConnectionParams](sse-connection-params.html), or [streamableHttpConnectionParams](streamable-http-connection-params.html) must be set; [toToolset](to-toolset.html) throws if zero or more than one are provided.

Members

## Constructors

[McpToolsetConfig](-mcp-toolset-config.html)

Link copied to clipboard

jvm

constructor(stdioConnectionParams: [McpConnectionParameters.Stdio](../../-mcp-connection-parameters/-stdio/index.html)? = null, sseConnectionParams: [McpConnectionParameters.Sse](../../-mcp-connection-parameters/-sse/index.html)? = null, streamableHttpConnectionParams: [McpConnectionParameters.StreamableHttp](../../-mcp-connection-parameters/-streamable-http/index.html)? = null, toolFilter: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, useMcpResources: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, maxMcpResourceLength: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html) = DEFAULT_MAX_RESOURCE_LENGTH)

## Properties

[maxMcpResourceLength](max-mcp-resource-length.html)

Link copied to clipboard

jvm

val [maxMcpResourceLength](max-mcp-resource-length.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)

Maximum length, in characters, of a single resource payload returned by `load_mcp_resource`. Longer payloads are truncated.

[sseConnectionParams](sse-connection-params.html)

Link copied to clipboard

jvm

val [sseConnectionParams](sse-connection-params.html): [McpConnectionParameters.Sse](../../-mcp-connection-parameters/-sse/index.html)? = null

Connection parameters for an MCP server reached over SSE.

[stdioConnectionParams](stdio-connection-params.html)

Link copied to clipboard

jvm

val [stdioConnectionParams](stdio-connection-params.html): [McpConnectionParameters.Stdio](../../-mcp-connection-parameters/-stdio/index.html)? = null

Connection parameters for a local MCP server reached over stdio (e.g. one launched via `npx` or `python3`).

[streamableHttpConnectionParams](streamable-http-connection-params.html)

Link copied to clipboard

jvm

val [streamableHttpConnectionParams](streamable-http-connection-params.html): [McpConnectionParameters.StreamableHttp](../../-mcp-connection-parameters/-streamable-http/index.html)? = null

Connection parameters for an MCP server reached over the Streamable HTTP transport.

[toolFilter](tool-filter.html)

Link copied to clipboard

jvm

val [toolFilter](tool-filter.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null

Optional allowlist of tool names; when set, only tools whose name appears in the list will be exposed to the agent. When `null`, all tools advertised by the server are exposed.

[useMcpResources](use-mcp-resources.html)

Link copied to clipboard

jvm

val [useMcpResources](use-mcp-resources.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

When `true`, resource-related tools (`list_mcp_resources`, `list_mcp_resource_templates`, `load_mcp_resource`) are added to the toolset, granting the agent access to MCP resources exposed by the server. Defaults to `false`.

## Functions

[toToolset](to-toolset.html)

Link copied to clipboard

jvm

fun [toToolset](to-toolset.html)(headerProvider: ([ReadonlyContext](../../../com.google.adk.kt.agents/-readonly-context/index.html)) -> [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, progressConsumers: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<(McpSchema.ProgressNotification) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html)> = emptyList()): [McpToolset](../index.html)

Creates an [McpToolset](../index.html) from this configuration.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
