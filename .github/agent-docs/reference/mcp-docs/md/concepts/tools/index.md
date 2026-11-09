[ Model Context Protocol （MCP） ](https://modelcontextprotocol.info/)[Home ](https://modelcontextprotocol.info/)[Get Started ](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)[Develop ](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)[Connect and Run ](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)[Protocol and Versions ](https://modelcontextprotocol.info/specification/)[Reference ](https://modelcontextprotocol.info/tools/)[Blog ](https://modelcontextprotocol.info/blog/)[About](https://modelcontextprotocol.info/about/)

`CTRL K`




`CTRL K`




  * [Get Started](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)

    * [What is MCP?](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)
    * [Architecture and roles](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/)
    * [Servers and primitives](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/)
    * [Hosts and clients](https://modelcontextprotocol.info/docs/2026-07-28/learn/client-concepts/)

  * [Develop](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

    * [Build a server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)
    * [Build a client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/)
    * [Choose an SDK](https://modelcontextprotocol.info/docs/2026-07-28/sdk/)
    * [Build with agent skills](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-with-agent-skills/)
    * [Node.js client: calls and failures without a model](https://modelcontextprotocol.info/docs/tutorials/building-a-client-node/)
    * [Design and check effective tools](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/)

  * [Connect and Run](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)

    * [Connect a local server](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)
    * [Connect a remote server](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/)
    * [Authorization with OAuth 2.1](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/)
    * [Local server security defaults](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/)
    * [Security checklist before launch](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/)
    * [Host applications at scale](https://modelcontextprotocol.info/docs/2026-07-28/develop/clients/client-best-practices/)
    * [Troubleshoot connections and calls](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/)
    * [Inspector: test a server interactively](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
    * [Inspector CLI: scripted checks and CI](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/)
    * [Inspector recipes: transports, Docker, config import](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/)
    * [Inspector lab: reproducible calls and failure diagnosis](https://modelcontextprotocol.info/tools/inspector/)

  * [Protocol and Versions](https://modelcontextprotocol.info/specification/)

    * [Version negotiation rules](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)
    * [Revision and method matrix](https://modelcontextprotocol.info/specification/)
    * [Key changes in 2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/changelog/)
    * [Deprecated features](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/)
    * [Legacy and modern protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/)
    * [Client extension support matrix](https://modelcontextprotocol.info/extensions/client-matrix/)

  * [Reference](https://modelcontextprotocol.info/tools/)

    * [Tools and Registry overview](https://modelcontextprotocol.info/tools/)
    * [Production checklist](https://modelcontextprotocol.info/docs/best-practices/)
    * [Client capability matrix](https://modelcontextprotocol.info/docs/clients/)
    * [Tools: definitions and version differences](https://modelcontextprotocol.info/docs/concepts/tools/)
    * [Resources: definitions and version differences](https://modelcontextprotocol.info/docs/concepts/resources/)
    * [Prompts: definitions and trade-offs](https://modelcontextprotocol.info/docs/concepts/prompts/)
    * [Sampling: deprecated server requests for client model calls](https://modelcontextprotocol.info/docs/concepts/sampling/)
    * [Current transports: stdio and Streamable HTTP](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/)
    * [Publish a server to the Registry](https://modelcontextprotocol.info/tools/registry/publishing/)
    * [Official SEP status index](https://modelcontextprotocol.info/seps/)
    * [SEP impact and method lifecycle guide](https://modelcontextprotocol.info/docs/reference/sep-impact-guide/)
    * [FAQ: revisions, authorization and failure handling](https://modelcontextprotocol.info/docs/faqs/)

  * In this section

    * [Core Concepts](https://modelcontextprotocol.info/docs/concepts/)
    * [MCP Tools Explained: Definitions, Results, Errors and Version Differences](https://modelcontextprotocol.info/docs/concepts/tools/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/concepts/tools/)
  * [简体中文](https://mcpcn.com/docs/concepts/tools/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. The path of a tool call
  * 2\. The tool definition across five revisions
  * 3\. Listing and calling: fields and value shapes
  * 4\. One message, five schemas
  * 5\. Errors: three channels
  * 6\. What the official Python SDK 2.3.0 returns
  * 7\. Failure modes and recovery
  * 8\. Lint your own tool definitions
  * 9\. Before you ship a tool
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[Core Concepts](https://modelcontextprotocol.info/docs/concepts/)

MCP Tools Explained: Definitions, Results, Errors and Version Differences

# MCP Tools Explained: Definitions, Results, Errors and Version Differences

A tool is a named operation that a server exposes and a model can call. A call passes through five steps: definition, list, call, result, and failure. The sections below follow that path on the 2026-07-28 revision, show what changed in each revision since 2024-11-05, and say which channel an error should use.

For how to design tools that a model can use well, read [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/). To list and call tools on a running server and distinguish connection failures from tool failures, follow the [MCP Inspector testing guide](https://modelcontextprotocol.info/tools/inspector/). For the normative text, read the official [Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/) page.

## 1\. The path of a tool call

Step| Message| What to know| Section  
---|---|---|---  
1| Capability| A server that supports tools **MUST** declare the `tools` capability. `listChanged` says whether it will notify clients when the list changes| 7  
2| `tools/list`| Supports pagination (`cursor`, `nextCursor`) and caching; the result carries `ttlMs` and `cacheScope`| 3, 7  
3| `tools/call`| `name` and `arguments`. Over Streamable HTTP the tool name is also sent in the `Mcp-Name` header| 3, 5  
4| Result| A `CallToolResult` (`content`, optional `structuredContent`, `isError`), or an `input_required` result that asks for more input before the call can complete| 3, 5  
5| List change| With `listChanged`, the server sends `notifications/tools/list_changed` to clients that opened `subscriptions/listen` with `toolsListChanged: true`; the client lists again| 7  
  
## 2\. The tool definition across five revisions

Only `name` and `inputSchema` are required, in every revision. The rest was added later. The table is generated from `definitions` / `$defs` of each revision's `schema.json`; `—` means the revision does not define the field. Columns are labeled by year and month in this table and the next ones: `2024-11` is 2024-11-05, `2025-03` is 2025-03-26, `2025-06` is 2025-06-18, `2025-11` is 2025-11-25 and `2026-07` is 2026-07-28.

Field| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`Tool.name`| required| required| required| required| required  
`Tool.title`| —| —| optional| optional| optional  
`Tool.description`| optional| optional| optional| optional| optional  
`Tool.inputSchema`| required| required| required| required| required  
`Tool.outputSchema`| —| —| optional| optional| optional  
`Tool.annotations`| —| optional| optional| optional| optional  
`Tool.icons`| —| —| —| optional| optional  
`Tool.execution`| —| —| —| optional| —  
`Tool._meta`| —| —| optional| optional| optional  
`ToolAnnotations.title`| —| optional| optional| optional| optional  
`ToolAnnotations.readOnlyHint`| —| optional| optional| optional| optional  
`ToolAnnotations.destructiveHint`| —| optional| optional| optional| optional  
`ToolAnnotations.idempotentHint`| —| optional| optional| optional| optional  
`ToolAnnotations.openWorldHint`| —| optional| optional| optional| optional  
  
  * `annotations` and its hints arrived in 2025-03-26. `title`, `outputSchema` and `_meta` arrived in 2025-06-18. `icons` arrived in 2025-11-25.
  * `Tool.execution` exists only in the 2025-11-25 schema. It is not in the 2026-07-28 schema, and neither is the `task` parameter of `tools/call` (section 3).
  * Annotations are hints. The spec says clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers.



**What the schema does not express** (all from the official Tools page):

  * **Names.** Names **SHOULD** be 1 to 128 characters, case-sensitive, and use only letters, digits, `_`, `-` and `.`. Names **SHOULD** be unique within a server. A client or proxy that aggregates several servers **SHOULD** disambiguate collisions, for example by prefixing a server identifier, and **SHOULD NOT** rely on the server `name` from `serverInfo` for that.
  * **`inputSchema`.** It **MUST** be a valid JSON Schema object (not `null`) and defaults to 2020-12 without `$schema`. For a tool with no parameters, `{ "type": "object", "additionalProperties": false }` is recommended because it accepts only the empty object; `{ "type": "object" }` accepts any object.
  * **`x-mcp-header`.** An annotation inside a property schema that mirrors the argument into an `Mcp-Param-{name}` HTTP header on Streamable HTTP. It has hard constraints; a tool that violates them is dropped by the client (section 7).



## 3\. Listing and calling: fields and value shapes

The first table lists the fields of the three messages that matter. `tools/call params` is a named definition from 2025-11-25 and an inline object before; `_meta` is left out of that group because the older inline definition does not list it (the matrix in section 4 covers its 2026-07-28 requirement).

Field| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`ListToolsResult.tools`| required| required| required| required| required  
`ListToolsResult.nextCursor`| optional| optional| optional| optional| optional  
`ListToolsResult.ttlMs`| —| —| —| —| required  
`ListToolsResult.cacheScope`| —| —| —| —| required  
`ListToolsResult.resultType`| —| —| —| —| required  
`ListToolsResult._meta`| optional| optional| optional| optional| optional  
`tools/call params.name`| required| required| required| required| required  
`tools/call params.arguments`| optional| optional| optional| optional| optional  
`tools/call params.inputResponses`| —| —| —| —| optional  
`tools/call params.requestState`| —| —| —| —| optional  
`tools/call params.task`| —| —| —| optional| —  
`CallToolResult.content`| required| required| required| required| required  
`CallToolResult.structuredContent`| —| —| optional| optional| optional  
`CallToolResult.isError`| optional| optional| optional| optional| optional  
`CallToolResult.resultType`| —| —| —| —| required  
`CallToolResult._meta`| optional| optional| optional| optional| optional  
  
The second table lists value shapes that are not field names:

Aspect| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
JSON Schema dialect of `schema.json`| draft-07| draft-07| draft-07| 2020-12| 2020-12  
`content` block `type` values| `text`, `image`, `resource`| `text`, `image`, `audio`, `resource`| `text`, `image`, `audio`, `resource_link`, `resource`| `text`, `image`, `audio`, `resource_link`, `resource`| `text`, `image`, `audio`, `resource_link`, `resource`  
`structuredContent`| —| —| `object`| `object`| any JSON value  
`outputSchema` root| —| —| root `type` must be `object`| root `type` must be `object`| any JSON Schema  
  
What this means in practice:

  * **`resultType` is required** on both results in 2026-07-28. A server that answers `tools/call` or `tools/list` the 2025-11-25 way, without it, no longer validates (section 4).
  * **`tools/list` must carry cache hints.** Servers **MUST** include caching hints on `resultType: "complete"` results of `tools/list`, and **MUST** provide a `ttlMs` that is `>= 0`. `ttlMs: 0` means immediately stale.
  * **`structuredContent` can be any JSON value** (object, array, string, number, boolean or null) that conforms to the tool's `outputSchema` if there is one. Before 2026-07-28 it had to be an object, and so did the root of `outputSchema`.
  * **The output contract.** If an `outputSchema` is provided, servers **MUST** provide structured results that conform to it and clients **SHOULD** validate them. For backward compatibility, a tool that returns structured content **SHOULD** also return the serialized JSON in a `TextContent` block.
  * **Content blocks** are `text`, `image`, `audio`, `resource_link` and `resource` (embedded). Resource links returned by a tool are not guaranteed to appear in `resources/list`.
  * **Input required.** A server **MAY** answer `tools/call` with an `InputRequiredResult` (`resultType: "input_required"`). The client retries with `inputResponses` and, if the server sent one, `requestState`, and the JSON-RPC `id` **MUST** differ between the first request and the retry. Retries carrying `inputResponses` or `requestState` **MUST NOT** be cached.



## 4\. One message, five schemas

Does a message that is valid for one revision survive the others? Each row is validated against all five `schema.json` files. `✓` means valid, `✗` means rejected, `—` means the revision does not define the property the row is about, so validation says nothing.

Message| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`Tool` whose `outputSchema` has `type: array`| —| —| ✗| ✗| ✓  
`CallToolResult` whose `structuredContent` is an array| —| —| ✗| ✗| ✓  
`CallToolResult` without `resultType`| ✓| ✓| ✓| ✓| ✗  
`ListToolsResult` without `ttlMs`, `cacheScope`, `resultType`| ✓| ✓| ✓| ✓| ✗  
`tools/call` request without `params._meta`| ✓| ✓| ✓| ✓| ✗  
An `input_required` result returned for `tools/call`| ✗| ✗| ✗| ✗| ✓  
  
How the rows were built: rows 1, 2 and 6 are official examples of the 2026-07-28 revision as they are; rows 3, 4 and 5 are official examples with the named fields deleted. All unmodified examples are valid against the 2026-07-28 schema: 22 tool-related examples in 12 definitions were validated, none was invalid.

  * **Rows 1 and 2.** An array-valued `outputSchema` or `structuredContent` is valid only in 2026-07-28. Against 2025-06-18 and 2025-11-25 they are rejected, because both require an object. Check which revision a client is on before returning such shapes.
  * **Rows 3 to 5.** 2026-07-28 requires `resultType`, `ttlMs` with `cacheScope`, and request `_meta`. Code written for 2025-11-25 and earlier fails validation until it adds them.
  * **Row 6.** An `input_required` result is not a valid `tools/call` result before 2026-07-28: it has no `content`.
  * **The limit of this method.** JSON Schema validation checks shape only. A column without `✗` does not mean the behaviors are compatible.



Some changes live only in the prose of the Tools page. The next table checks each revision's page for the sentence that introduced the rule:

Spec text mentions| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
Tool name guidance (1–128 characters, restricted set)| —| —| —| ✓| ✓  
Input validation errors reported as tool execution errors| —| —| —| ✓| ✓  
`tools/list` SHOULD be deterministic| —| —| —| —| ✓  
`tools/list` MUST NOT vary per connection| —| —| —| —| ✓  
`x-mcp-header` mirrors arguments into HTTP headers| —| —| —| —| ✓  
Stateful tools via explicit handles| —| —| —| —| ✓  
List changes delivered through `subscriptions/listen`| —| —| —| —| ✓  
  
## 5\. Errors: three channels

A failed call can surface in different places. Choosing the wrong one blinds the model to an error it could fix, or makes a client give up on one it should retry. The spec splits them like this: **protocol errors** are for problems with the request structure that models are less likely to fix (unknown tool, malformed requests that fail the `CallToolRequest` schema, server errors); **tool execution errors** are for actionable feedback the model can use to self-correct (API failures, input validation errors such as a date in the wrong format or a value out of range, business logic errors). Clients **MAY** show protocol errors to the model and **SHOULD** show execution errors to it.

Situation| Channel and what arrives| What to do  
---|---|---  
The request does not satisfy `CallToolRequest` (no `name`, `arguments` not an object)| JSON-RPC error `-32602` (`InvalidParamsError`)| Fix the client; retrying the same request cannot succeed  
Unknown tool| JSON-RPC error `-32602` with a message such as `Unknown tool: …` in the spec's example (the official SDK returns an `isError` result instead, section 6)| Refresh `tools/list`; handle both shapes  
An argument is the wrong type, out of range or in the wrong format| Tool execution error: `result.isError: true` and text that names the field and the valid values| Give the text to the model and retry with corrected arguments  
The API behind the tool failed, or a business rule refused| Tool execution error: `result.isError: true` with an explanation| Let the model decide: retry, change the plan or report to the user  
The server itself failed| JSON-RPC error `-32603` (`InternalError`)| Retry with backoff; do not feed the raw error back as an instruction  
Headers disagree with the body (`Mcp-Method`, `Mcp-Name`, `Mcp-Param-*`), or are missing| HTTP `400` and JSON-RPC error `-32020` (`HeaderMismatchError`)| A client or gateway bug; fix the headers  
The protocol version is unknown or not supported| HTTP `400` and `-32022` (`UnsupportedProtocolVersionError`); `data.requested` and `data.supported`| Pick a version from `supported` and retry  
The call needs a client capability that was not declared| HTTP `400` and `-32021` (`MissingRequiredClientCapabilityError`); `data.requiredCapabilities`| Declare the capability or stop using that tool  
The RPC method does not exist| HTTP `404` and `-32601` (`MethodNotFoundError`)| The server does not implement that method  
The server needs more input before it can finish| Not an error: a result with `resultType: "input_required"`, `inputRequests` and possibly `requestState`| Answer the requests and retry with `inputResponses`, `requestState` and a new JSON-RPC `id`  
  
The error codes and the three HTTP `400` rules in the table are checked against the 2026-07-28 `schema.json` and the Streamable HTTP page of the pinned commit.

## 6\. What the official Python SDK 2.3.0 returns

The reference server defines one tool per result shape. It uses the official SDK (`pip install mcp==2.3.0`):

**tools_ref_server.py**
    
    
     """Official Python SDK (mcp==2.3.0) server with one tool per result shape, http://127.0.0.1:8200/mcp, no auth."""
    from typing import Annotated
    
    from mcp.server.mcpserver import MCPServer
    from pydantic import BaseModel, Field
    
    server = MCPServer("tools-ref")
    
    
    class Weather(BaseModel):
        temperature: float
        conditions: str
    
    
    class User(BaseModel):
        id: str
        name: str
    
    
    @server.tool()
    def get_weather(location: Annotated[str, Field(min_length=2)]) -> Weather:
        """Return fixed weather for a location."""
        return Weather(temperature=22.5, conditions="Partly cloudy")
    
    
    @server.tool()
    def list_users() -> list[User]:
        """Return two users as an array."""
        return [User(id="1", name="Alice"), User(id="2", name="Bob")]
    
    
    @server.tool()
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b
    
    
    @server.tool()
    def get_current_time() -> str:
        """Take no arguments."""
        return "2026-10-26T00:00:00Z"
    
    
    @server.tool()
    def explode() -> str:
        """Always raise."""
        raise RuntimeError("boom")
    
    
    if __name__ == "__main__":
        server.run("streamable-http", port=8200)

Twelve requests were sent over Streamable HTTP in the 2026-07-28 request format and every response was validated against its definition in the 2026-07-28 `schema.json` (all twelve are valid; the definition is named at the end of each recorded line):

Run| Request| What the SDK returned| Against the spec  
---|---|---|---  
`list`| `tools/list`| `ttlMs: 0`, `cacheScope: "private"`, `resultType: "complete"`, 5 tools, each with an `outputSchema`| Valid. The SDK fills the required hints with the most conservative values  
`weather-ok`| `get_weather` with a valid location| One text block holding the JSON, and `structuredContent` as an object| Matches the output contract and the text-copy recommendation  
`sum-ok`| `add` with `1`, `2`| `structuredContent: {"result": 3}`; the text block is `3`| Valid, but the return value is wrapped in an object and the text block is not the serialization of `structuredContent`  
`users-ok`| `list_users` (returns an array)| `structuredContent: {"result": [...]}` and two text blocks, one per element| Same wrapping; the SDK does not use the 2026-07-28 allowance for array-valued `structuredContent`  
`time-no-args`| `get_current_time` (no parameters)| `inputSchema` has `type: "object"` and no `additionalProperties: false`| Valid; not the recommended closed form  
`bad-type`| `add` with `"x"` for `a`| `isError: true`, a pydantic message with a link to `errors.pydantic.dev`| Matches the spec: input validation is an execution error. The message is verbose and carries a third-party link  
`bad-constraint`| `get_weather` with a one-character location (`minLength` 2)| `isError: true`, same message style| Same  
`missing-argument`| `get_weather` without `location`| `isError: true`, same message style| Same  
`handler-raises`| `explode`, which raises| `isError: true`, text `Error executing tool explode`| Valid. Nothing leaks, but the model cannot self-correct from it; log the cause on the server  
`unknown-tool`| a name that does not exist| `isError: true`, text `Unknown tool: nope`| The spec lists an unknown tool under protocol errors (its example is `-32602`); the SDK returns an execution error. Clients should handle both  
`missing-name`| `tools/call` without `name`| HTTP `400`, JSON-RPC error `-32602`| Matches the spec and validates as `InvalidParamsError`  
`arguments-array`| `arguments` is an array| HTTP `400`, JSON-RPC error `-32602`| Same  
**Recorded output of the twelve runs**
    
    
     list             HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete tools=5 | ListToolsResultResponse valid
    weather-ok       HTTP 200 result   1 text blocks, structuredContent {"temperature":22.5,"conditions":"Partly cloudy"} | CallToolResultResponse valid
    sum-ok           HTTP 200 result   1 text blocks, structuredContent {"result":3} | CallToolResultResponse valid
    users-ok         HTTP 200 result   2 text blocks, structuredContent {"result":[{"id":"1","name":"Alice"},{"id":"2","name":"Bob"}]} | CallToolResultResponse valid
    time-no-args     HTTP 200 result   1 text blocks, structuredContent {"result":"2026-10-26T00:00:00Z"} | CallToolResultResponse valid
    bad-type         HTTP 200 isError  text 'Error executing tool add: 1 validation error for addArguments\n' link=errors.pydantic.dev | CallToolResultResponse valid
    bad-constraint   HTTP 200 isError  text 'Error executing tool get_weather: 1 validation error for get_w' link=errors.pydantic.dev | CallToolResultResponse valid
    missing-argument HTTP 200 isError  text 'Error executing tool get_weather: 1 validation error for get_w' link=errors.pydantic.dev | CallToolResultResponse valid
    handler-raises   HTTP 200 isError  text 'Error executing tool explode' | CallToolResultResponse valid
    unknown-tool     HTTP 200 isError  text 'Unknown tool: nope' | CallToolResultResponse valid
    missing-name     HTTP 400 error    code -32602 'Invalid request parameters' | JSONRPCErrorResponse valid
    arguments-array  HTTP 400 error    code -32602 'Invalid request parameters' | JSONRPCErrorResponse valid

## 7\. Failure modes and recovery

Symptom| Cause| How to detect| Recovery  
---|---|---|---  
A tool is on the server but missing from the client's list| An `x-mcp-header` that breaks the constraints. A Streamable HTTP client **MUST** exclude the tool from `tools/list` and **SHOULD** log a warning with the reason| Run the linter (section 8); read the client's warnings| Fix the annotation: non-empty HTTP token, unique ignoring case, only on `integer`, `string` or `boolean` properties, reachable through `properties` keys only  
The model calls the wrong server's tool| Two aggregated servers expose the same tool name| List names across servers| Prefix a server identifier in the aggregator; do not use the server `name`  
Two clients get different lists, or one client's list changes mid-session| The list depends on connection state. A server **MUST NOT** vary the list per connection or as a side effect of other requests| Call `tools/list` on two connections with the same credentials and diff| Compute the list from the request's authorization only. It **MAY** vary by authorization  
A cached list is shown to the wrong user| A list filtered by scope was marked `cacheScope: "public"`| Compare the list for two tokens with different scopes| Use `"private"` for filtered lists; `"public"` only when the list is identical for all users  
A client keeps showing an outdated list| The server changed its tools, but `notifications/tools/list_changed` reaches only clients that opened `subscriptions/listen` with `toolsListChanged: true`. A server **MAY** give `ttlMs` without `listChanged`, and then clients rely on the TTL alone| Check that the stream is open; compare `ttlMs` with how often the list changes| Declare `listChanged` and send the notification; keep `ttlMs` short, or `0`, for lists that change often  
Prompt caching keeps missing after a restart| The list order is not stable. Servers **SHOULD** return tools in a deterministic order| Diff two `tools/list` responses| Sort by name before returning  
A client built for an older revision breaks on a tool result| An array-valued `structuredContent` or `outputSchema` was sent to a client that expects an object (matrix rows 1 and 2)| Validate your results against the older `schema.json`| Wrap the value in an object, or return the new shape only to clients on 2026-07-28  
Clients reject `structuredContent`| It does not conform to the declared `outputSchema`; servers **MUST** conform| Run the linter with `--call`| Validate the result in the server before returning it  
A call fails with "unknown handle"| A stateful tool's handle expired. A call with an expired or unknown handle should return an execution error that says so| Call twice across the retention period| State the retention in the creation tool's description; return an `isError` result that tells the model to create a new handle  
The model never sees an error| The client treated `isError` as success, or logged it only| Send a bad argument and watch the model's input| Clients **SHOULD** pass execution errors to the model; return text it can act on  
Sensitive values show up in proxy logs| A password or token is mirrored with `x-mcp-header`; header values are visible to intermediaries| Search `inputSchema` for `x-mcp-header`| Do not annotate sensitive parameters (**SHOULD NOT**)  
  
## 8\. Lint your own tool definitions

`lint_tools.py` fetches `tools/list` from a Streamable HTTP endpoint (or reads a JSON file) and checks the rules above. With `--call` it also calls one tool and checks the result against the tool's `outputSchema`. It needs `jsonschema` for the schema checks and reports a warning if the package is missing.

**lint_tools.py**
    
    
     #!/usr/bin/env python3
    """Lint the tool definitions of an MCP server against spec 2026-07-28, and optionally call one tool.
    
    Usage: lint_tools.py SOURCE [--call NAME [--args JSON]] [--token T]
    SOURCE: URL of a Streamable HTTP endpoint, or a JSON file ("-" = stdin) holding a tools/list response,
    its result, or a tools array. The list result itself is checked too (resultType, ttlMs, cacheScope) unless the
    file holds a bare tools array. Schema checks need `pip install jsonschema` (skipped with a WARN without it).
    Levels: FAIL = a MUST of the spec is violated, WARN = a SHOULD or a recommendation is not followed.
    Exit code: 0 no FAIL, 1 at least one FAIL, 2 the source cannot be read.
    """
    import argparse
    import http.client
    import json
    import re
    import sys
    from urllib.parse import urlsplit
    
    try:
        import jsonschema
    except ImportError:
        jsonschema = None
    
    VERSION = "2026-07-28"
    NAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,128}$")
    TCHAR_RE = re.compile(r"^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$")
    HEADER_TYPES = {"integer", "string", "boolean"}
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    
    
    def report(name, ok, detail, level="FAIL"):
        status = "PASS" if ok else level
        counts[status] += 1
        print("%s %s: %s" % (status, name, detail))
    
    
    def rpc(url, method, params=None, token=None):
        """POST one 2026-07-28 request and return (HTTP status, JSON-RPC message or None)."""
        parts = urlsplit(url)
        cls = http.client.HTTPSConnection if parts.scheme == "https" else http.client.HTTPConnection
        meta = {"io.modelcontextprotocol/protocolVersion": VERSION,
                "io.modelcontextprotocol/clientInfo": {"name": "lint-tools", "version": "0"},
                "io.modelcontextprotocol/clientCapabilities": {}}
        headers = {"Accept": "application/json, text/event-stream", "Content-Type": "application/json",
                   "MCP-Protocol-Version": VERSION, "Mcp-Method": method}
        if params and "name" in params:
            headers["Mcp-Name"] = params["name"]
        if token:
            headers["Authorization"] = "Bearer " + token
        body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": {**(params or {}), "_meta": meta}})
        conn = cls(parts.netloc, timeout=15)
        conn.request("POST", parts.path or "/", body, headers)
        resp = conn.getresponse()
        raw = resp.read().decode("utf-8", "replace")
        conn.close()
        try:
            return resp.status, json.loads(raw)
        except ValueError:
            for line in reversed(raw.splitlines()):  # SSE: the last data line holding a response
                if line.startswith("data:"):
                    try:
                        return resp.status, json.loads(line[5:].strip())
                    except ValueError:
                        continue
        return resp.status, None
    
    
    def load_tools(source, token):
        """Return (tools, envelope): envelope is the first tools/list result, None for a bare tools array."""
        if source.startswith(("http://", "https://")):
            tools, cursor, envelope = [], None, None
            for _ in range(50):
                status, msg = rpc(source, "tools/list", {"cursor": cursor} if cursor else None, token)
                result = (msg or {}).get("result")
                if status != 200 or not isinstance(result, dict) or not isinstance(result.get("tools"), list):
                    raise ValueError("tools/list failed: HTTP %s, %s" % (status, json.dumps(msg)[:200]))
                tools += result["tools"]
                envelope = envelope or result
                cursor = result.get("nextCursor")
                if not cursor:
                    return tools, envelope
            raise ValueError("tools/list still paginating after 50 pages")
        data = json.load(sys.stdin if source == "-" else open(source, encoding="utf-8"))
        data = data.get("result", data) if isinstance(data, dict) else data
        tools = data.get("tools") if isinstance(data, dict) else data
        if not isinstance(tools, list):
            raise ValueError("no tools array found in %s" % source)
        return tools, data if isinstance(data, dict) else None
    
    
    def dialect(schema):
        uri = schema.get("$schema", "") if isinstance(schema, dict) else ""
        return jsonschema.Draft7Validator if "draft-07" in uri else jsonschema.Draft202012Validator
    
    
    def schema_problem(schema):
        try:
            dialect(schema).check_schema(schema)
        except jsonschema.SchemaError as exc:
            return exc.message[:100]
        return None
    
    
    def header_annotations(schema):
        """Yield (name, value, chain, reachable) for every x-mcp-header in a schema; reachable means a pure `properties` chain."""
        def walk(node, chain, reachable):
            if not isinstance(node, dict):
                return
            if "x-mcp-header" in node:
                yield node, chain, reachable
            for key, value in node.items():
                if key == "properties" and isinstance(value, dict):
                    for prop, sub in value.items():
                        yield from walk(sub, chain + [prop], reachable)
                elif key not in ("x-mcp-header", "enum", "const", "default", "examples"):
                    for sub in (value if isinstance(value, list) else
                                list(value.values()) if key in ("$defs", "definitions", "patternProperties") else [value]):
                        yield from walk(sub, chain + [key], False)
        yield from walk(schema, [], True)
    
    
    def header_problems(schema):
        problems, seen = [], {}
        for node, chain, reachable in header_annotations(schema):
            value, where = node["x-mcp-header"], "/".join(chain) or "(root)"
            if not reachable:
                problems.append("%s: not statically reachable" % where)
            if not isinstance(value, str) or not TCHAR_RE.match(value):
                problems.append("%s: %r is not a non-empty HTTP token" % (where, value))
                continue
            if value.lower() in seen:
                problems.append("%s: duplicates %s (case-insensitive)" % (where, seen[value.lower()]))
            seen[value.lower()] = where
            kind = node.get("type")
            kinds = set(kind) if isinstance(kind, list) else {kind}
            if not kinds <= HEADER_TYPES:
                problems.append("%s: type %s is not integer, string or boolean" % (where, kind))
        return problems
    
    
    def lint_envelope(result):
        """tools/list results of 2026-07-28 MUST carry resultType, and caching hints with ttlMs >= 0."""
        if result is None:
            return
        ttl, scope = result.get("ttlMs"), result.get("cacheScope")
        problems = []
        if not isinstance(result.get("resultType"), str):
            problems.append("resultType is missing")
        if not isinstance(ttl, int) or isinstance(ttl, bool) or ttl < 0:
            problems.append("ttlMs is %r, want an integer >= 0" % ttl)
        if scope not in ("public", "private"):
            problems.append("cacheScope is %r, want 'public' or 'private'" % scope)
        report("list-envelope", not problems, "; ".join(problems) if problems
               else "resultType=%s ttlMs=%d cacheScope=%s" % (result["resultType"], ttl, scope))
    
    
    def lint(tools, envelope=None):
        lint_envelope(envelope)
        named = [t for t in tools if isinstance(t, dict) and isinstance(t.get("name"), str)]
        report("name-present", len(named) == len(tools), "%d of %d tools have a string name" % (len(named), len(tools)))
        bad = [t["name"] for t in named if not NAME_RE.match(t["name"])]
        report("name-charset", not bad, "bad names: %s" % bad if bad else "%d names match [A-Za-z0-9_.-]{1,128}" % len(named),
               "WARN")
        names = [t["name"] for t in named]
        dup = sorted({n for n in names if names.count(n) > 1})
        report("name-unique", not dup, "duplicates: %s" % dup if dup else "no duplicates", "WARN")
        root = [t["name"] for t in named if not (isinstance(t.get("inputSchema"), dict)
                                                 and t["inputSchema"].get("type") == "object")]
        report("input-root-object", not root, "inputSchema is not an object schema with type=object: %s" % root
               if root else "every inputSchema is an object schema with type=object")
        open_schema = [t["name"] for t in named if isinstance(t.get("inputSchema"), dict)
                       and t["inputSchema"].get("type") == "object" and not t["inputSchema"].get("properties")
                       and t["inputSchema"].get("additionalProperties") is not False]
        report("no-params-closed", not open_schema,
               "no-parameter tools accept any object, add additionalProperties:false: %s" % open_schema
               if open_schema else "no-parameter tools are closed", "WARN")
        hdr = ["%s %s" % (t["name"], p) for t in named if isinstance(t.get("inputSchema"), dict)
               for p in header_problems(t["inputSchema"])]
        report("x-mcp-header", not hdr, "; ".join(hdr) if hdr else "annotations satisfy the constraints (or none used)")
        if jsonschema is None:
            report("schema-valid", False, "skipped, jsonschema is not installed", "WARN")
            return
        problems = ["%s.%s: %s" % (t["name"], k, p) for t in named for k in ("inputSchema", "outputSchema")
                    if isinstance(t.get(k), dict) and (p := schema_problem(t[k]))]
        report("schema-valid", not problems, "; ".join(problems) if problems else "inputSchema / outputSchema are valid JSON Schema")
    
    
    def call(url, tools, name, args, token):
        status, msg = rpc(url, "tools/call", {"name": name, "arguments": args}, token)
        if not isinstance(msg, dict):
            report("call", False, "HTTP %s without a JSON-RPC message" % status)
            return
        if "error" in msg:
            print("INFO call %s: protocol error, HTTP %s, code %s: %s" % (name, status, msg["error"].get("code"),
                                                                           msg["error"].get("message")))
            return
        result = msg.get("result") or {}
        if result.get("resultType") == "input_required":
            print("INFO call %s: input_required, retry with inputResponses (nothing more to check)" % name)
            return
        report("call-result-type", isinstance(result.get("resultType"), str), "resultType=%s" % result.get("resultType")
               if isinstance(result.get("resultType"), str) else "resultType is missing")
        if result.get("isError"):
            text = " ".join(c.get("text", "") for c in result.get("content", []) if c.get("type") == "text")
            print("INFO call %s: execution error (isError), HTTP %s: %s" % (name, status, text[:100].replace("\n", " ")))
            return
        print("INFO call %s: result, HTTP %s, %d content blocks, structuredContent %s" % (
            name, status, len(result.get("content", [])), "present" if "structuredContent" in result else "absent"))
        tool = next((t for t in tools if isinstance(t, dict) and t.get("name") == name), {})
        structured = result.get("structuredContent")
        if tool.get("outputSchema"):
            report("structured-present", "structuredContent" in result, "the tool declares an outputSchema")
            if jsonschema and "structuredContent" in result:
                errs = list(dialect(tool["outputSchema"])(tool["outputSchema"]).iter_errors(structured))
                report("structured-conforms", not errs, errs[0].message[:100] if errs else "structuredContent matches outputSchema")
        if "structuredContent" in result:
            copies = []
            for c in result.get("content", []):
                try:
                    copies.append(c.get("type") == "text" and json.loads(c["text"]) == structured)
                except (ValueError, KeyError):
                    copies.append(False)
            report("structured-text-copy", any(copies), "a text block holds the serialized structuredContent", "WARN")
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("source")
        ap.add_argument("--call", help="name of a tool to call after the lint")
        ap.add_argument("--args", default="{}", help="JSON arguments for --call")
        ap.add_argument("--token", help="bearer token for the endpoint")
        args = ap.parse_args()
        if args.call and not args.source.startswith(("http://", "https://")):
            ap.error("--call needs a URL as SOURCE")
        try:
            tools, envelope = load_tools(args.source, args.token)
            arguments = json.loads(args.args)
        except (OSError, ValueError, http.client.HTTPException) as exc:
            print("ERROR %s" % exc)
            return 2
        print("INFO %d tools" % len(tools))
        lint(tools, envelope)
        if args.call:
            try:
                call(args.source, tools, args.call, arguments, args.token)
            except (OSError, http.client.HTTPException) as exc:
                print("ERROR %s" % exc)
                return 2
        print("%d pass, %d warn, %d fail" % (counts["PASS"], counts["WARN"], counts["FAIL"]))
        return 1 if counts["FAIL"] else 0
    
    
    if __name__ == "__main__":
        sys.exit(main())
    
    
    pip install jsonschema
    python3 lint_tools.py http://127.0.0.1:8200/mcp --call add --args '{"a":1,"b":2}'
    python3 lint_tools.py tools.json            # a saved tools/list response, its result, or a tools array

`FAIL` means a MUST is violated; `WARN` means a SHOULD or a recommendation is not followed. Exit code 0 means no FAIL, 1 at least one FAIL, 2 means the source could not be read. Run it against a URL or a saved response, so that the list result is checked together with the definitions; a bare tools array has no result to check.

Check| Level| Rule  
---|---|---  
`list-envelope`| FAIL| The `tools/list` result carries `resultType`, an integer `ttlMs` `>= 0` and a `cacheScope` of `public` or `private` (skipped for a bare tools array)  
`name-present`| FAIL| Every tool has a string `name`  
`name-charset`| WARN| 1 to 128 characters from letters, digits, `_`, `-`, `.`  
`name-unique`| WARN| Names are unique within a server  
`input-root-object`| FAIL| `inputSchema` is a JSON Schema object with `type: "object"` at the root  
`no-params-closed`| WARN| A tool with no parameters uses `additionalProperties: false`  
`x-mcp-header`| FAIL| Non-empty HTTP token, unique ignoring case, primitive type, reachable through `properties` only  
`schema-valid`| FAIL| `inputSchema` and `outputSchema` are valid JSON Schema in their dialect (needs `jsonschema`)  
`call-result-type`| FAIL| With `--call`: the result carries `resultType`; an `input_required` result is reported and not checked further  
`structured-present`| FAIL| With `--call`: a tool that declares an `outputSchema` returns `structuredContent`  
`structured-conforms`| FAIL| With `--call`: `structuredContent` matches the `outputSchema`  
`structured-text-copy`| WARN| With `--call`: a text block holds the serialized `structuredContent`  
  
Recorded output against the SDK server of section 6:
    
    
    INFO 5 tools
    PASS list-envelope: resultType=complete ttlMs=0 cacheScope=private
    PASS name-present: 5 of 5 tools have a string name
    PASS name-charset: 5 names match [A-Za-z0-9_.-]{1,128}
    PASS name-unique: no duplicates
    PASS input-root-object: every inputSchema is an object schema with type=object
    WARN no-params-closed: no-parameter tools accept any object, add additionalProperties:false: ['list_users', 'get_current_time', 'explode']
    PASS x-mcp-header: annotations satisfy the constraints (or none used)
    PASS schema-valid: inputSchema / outputSchema are valid JSON Schema
    PASS call-result-type: resultType=complete
    INFO call add: result, HTTP 200, 1 content blocks, structuredContent present
    PASS structured-present: the tool declares an outputSchema
    PASS structured-conforms: structuredContent matches outputSchema
    WARN structured-text-copy: a text block holds the serialized structuredContent
    10 pass, 2 warn, 0 fail

With `jsonschema` installed, the linter prints `8 pass, 0 warn, 0 fail` against a set of valid definitions (a list result with its caching hints, nested `x-mcp-header`, an array `outputSchema`, an explicit draft-07 `$schema`, a root `oneOf`). Against a set that contains each defect once (a list result without caching hints, a bad and a duplicate name, a string root, invalid schemas, and six `x-mcp-header` violations) it prints `2 pass, 2 warn, 4 fail` and names every defect.

## 9\. Before you ship a tool

  * The name matches `[A-Za-z0-9_.-]{1,128}` and is unique on the server; an aggregator prefixes names.
  * `inputSchema` has `type: "object"` at the root; a tool without parameters uses `additionalProperties: false`.
  * Validation failures, API failures and business rules return `isError: true` with text that names the field and the valid values. Only a malformed request is a protocol error.
  * If you declare an `outputSchema`, every result conforms to it and a text block carries the serialization.
  * `tools/list` is the same for every connection, ordered, and carries `ttlMs` and `cacheScope`; filtered lists are `"private"`.
  * Non-object structured output is only sent to clients on 2026-07-28, or is wrapped.
  * Sensitive parameters are not mirrored with `x-mcp-header`; the linter passes on your tool list.
  * Re-run the linter after changing the SDK, the gateway or the revision you serve.



## Versions and Verification

The tables are generated from the official `schema.json` files, the official examples are validated against them, and the runtime behavior comes from running the official Python SDK 2.3.0 (`mcp==2.3.0`). Spec wording and schemas are read from one pinned commit of the official repository (`dae694f6`, 2026-07-28 revision and the four before it). The tables were generated and checked with `jsonschema` 4.26.0, using the draft-07 validator for the revisions whose schema declares draft-07 and the 2020-12 validator for the others. The SDK runs used `mcp==2.3.0` on Python 3.14 (macOS). A change in the official text or in the SDK needs a re-run.

### Sources

  * The official 2026-07-28 pages: [Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/), [Caching](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/caching/), [Pagination](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/pagination/), [Streamable HTTP, custom headers from tool parameters](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/) and the [schema reference](https://modelcontextprotocol.info/specification/2026-07-28/schema/)
  * The `schema.json` of each revision and the official examples in the [official repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
  * This site's [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/)



[MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors](https://modelcontextprotocol.info/docs/concepts/resources/ "MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors")[Roots](https://modelcontextprotocol.info/docs/concepts/roots/ "Roots")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
