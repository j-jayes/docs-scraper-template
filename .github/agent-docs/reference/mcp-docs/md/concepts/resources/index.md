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
    * [MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors](https://modelcontextprotocol.info/docs/concepts/resources/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/concepts/resources/)
  * [简体中文](https://mcpcn.com/docs/concepts/resources/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. Resource, tool or prompt
  * 2\. The path of a resource read
  * 3\. The definitions across five revisions
  * 4\. Listing, reading and subscribing
  * 5\. One message, five schemas
  * 6\. Reading over Streamable HTTP: the Mcp-Name header
  * 7\. Errors: what to return and what to expect
  * 8\. What the official Python SDK 2.3.0 returns
  * 9\. Failure modes and recovery
  * 10\. Lint your own resources endpoint
  * 11\. Before you ship a resource
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[Core Concepts](https://modelcontextprotocol.info/docs/concepts/)

MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors

# MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors

A resource is a piece of data that a server exposes under a URI so that the host application can put it in front of a model: a file, a database schema, a record, a log. Its path runs through capability declaration, list, template, read, subscription, and failure. The sections below follow that path on the 2026-07-28 revision and show what changed in each revision since 2024-11-05.

For the action side, read [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/). For how to design a server that a model uses well, read [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/). For the normative text, read the official [Resources](https://modelcontextprotocol.info/specification/2026-07-28/server/resources/) page.

## 1\. Resource, tool or prompt

The spec gives each primitive a different controller. The controller decides who triggers the primitive, and that decides which one you should build.

You want to| Build| Who triggers it| Why  
---|---|---|---  
Hand the application data to include as context (file contents, a schema, a record)| Resource| The host application: resources are **application-driven** , and the spec does not mandate a user interface| The host can list, search, let the user pick, or include them by heuristics  
Let the model perform an action or fetch something on its own| Tool| The model: tools are **model-controlled**|  The model calls `tools/call` when it decides to  
Offer a reusable message template that the user picks, such as a slash command| Prompt| The user: prompts are **user-controlled**|  The user selects it explicitly  
Point from a tool result to a larger piece of data| Tool returning a `resource_link`| The model calls the tool, the client may then read the URI| A resource link in a tool result is not guaranteed to appear in `resources/list`  
  
If the model has to find data by itself during a conversation, a resource alone is not enough, because the host decides what is included. Expose a tool for that, and keep resources for data the host application chooses to attach.

## 2\. The path of a resource read

Step| Message| What to know| Section  
---|---|---|---  
1| Capability| A server that supports resources **MUST** declare the `resources` capability. `listChanged` and `subscribe` are optional and independent; `{ "resources": {} }` is valid| 4  
2| `resources/list`| Supports pagination and caching. The set **MAY** be empty and **MAY** change over time, but **MUST NOT** vary per connection| 3, 4  
3| `resources/templates/list`| Parameterized resources as RFC 6570 URI templates; supports pagination and caching| 3, 4  
4| `resources/read`| Takes a `uri`. Over Streamable HTTP the URI is also sent in the `Mcp-Name` header| 4, 6  
5| Result| `contents`: text or base64 blob items, each with its own `uri`; or an `input_required` result| 4, 5  
6| Subscription| A client that wants updates opens `subscriptions/listen` with `resourceSubscriptions`; the server sends `notifications/resources/updated`, the client reads again| 4  
7| List change| With `listChanged`, the server sends `notifications/resources/list_changed`; the client lists again| 4  
  
## 3\. The definitions across five revisions

Only `uri` and `name` (resources) and `uriTemplate` and `name` (templates) are required, in every revision. The rest was added later. The table is generated from `definitions` / `$defs` of each revision's `schema.json`; `—` means the revision does not define the field. Columns are labeled by year and month in this table and the next ones: `2024-11` is 2024-11-05, `2025-03` is 2025-03-26, `2025-06` is 2025-06-18, `2025-11` is 2025-11-25 and `2026-07` is 2026-07-28.

Field| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`Resource.uri`| required| required| required| required| required  
`Resource.name`| required| required| required| required| required  
`Resource.title`| —| —| optional| optional| optional  
`Resource.description`| optional| optional| optional| optional| optional  
`Resource.mimeType`| optional| optional| optional| optional| optional  
`Resource.size`| optional| optional| optional| optional| optional  
`Resource.icons`| —| —| —| optional| optional  
`Resource.annotations`| optional| optional| optional| optional| optional  
`Resource._meta`| —| —| optional| optional| optional  
`ResourceTemplate.uriTemplate`| required| required| required| required| required  
`ResourceTemplate.name`| required| required| required| required| required  
`ResourceTemplate.title`| —| —| optional| optional| optional  
`ResourceTemplate.description`| optional| optional| optional| optional| optional  
`ResourceTemplate.mimeType`| optional| optional| optional| optional| optional  
`ResourceTemplate.icons`| —| —| —| optional| optional  
`ResourceTemplate.annotations`| optional| optional| optional| optional| optional  
`ResourceTemplate._meta`| —| —| optional| optional| optional  
`Annotations.audience`| —| optional| optional| optional| optional  
`Annotations.priority`| —| optional| optional| optional| optional  
`Annotations.lastModified`| —| —| optional| optional| optional  
  
  * `title` and `_meta` arrived in 2025-06-18, `icons` in 2025-11-25. `size` (the raw size in bytes, before base64) has existed since the start. `Annotations` arrived in 2025-03-26 with `audience` and `priority`; `lastModified` followed in 2025-06-18.
  * **URIs.** Each resource is identified by a URI (RFC 3986), declared with `format: uri` in the 2026-07-28 schema. The spec names `https://` (only when the client can fetch the resource from the web itself, without the server), `file://` (resources that behave like a filesystem, whether or not a physical one exists) and `git://`. Custom schemes **MUST** follow RFC 3986. The schema accepts any string as a URI unless a validator enforces `format`; the linter in section 10 checks that listed URIs have a scheme.
  * **Annotations.** `audience` is `"user"`, `"assistant"` or both, `priority` runs from 0.0 (optional) to 1.0 (effectively required), `lastModified` is an ISO 8601 timestamp. They are hints for filtering, ordering and display.
  * **Contents.** A read returns text (`text`) or binary (`blob`, base64) items, each with a `uri` and an optional `mimeType`. The schema makes `text` and `blob` two alternatives; it does not forbid an item that has both (section 5).



## 4\. Listing, reading and subscribing

The first table lists the fields of the messages that matter. `resources/read params` is a named definition from 2025-11-25 and an inline object before; `_meta` is left out of that group because the older inline definition does not list it (the matrix in section 5 covers its 2026-07-28 requirement).

Field| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`ListResourcesResult.resources`| required| required| required| required| required  
`ListResourcesResult.nextCursor`| optional| optional| optional| optional| optional  
`ListResourcesResult.ttlMs`| —| —| —| —| required  
`ListResourcesResult.cacheScope`| —| —| —| —| required  
`ListResourcesResult.resultType`| —| —| —| —| required  
`ListResourcesResult._meta`| optional| optional| optional| optional| optional  
`ListResourceTemplatesResult.resourceTemplates`| required| required| required| required| required  
`ListResourceTemplatesResult.nextCursor`| optional| optional| optional| optional| optional  
`ListResourceTemplatesResult.ttlMs`| —| —| —| —| required  
`ListResourceTemplatesResult.cacheScope`| —| —| —| —| required  
`ListResourceTemplatesResult.resultType`| —| —| —| —| required  
`ListResourceTemplatesResult._meta`| optional| optional| optional| optional| optional  
`resources/read params.uri`| required| required| required| required| required  
`resources/read params.inputResponses`| —| —| —| —| optional  
`resources/read params.requestState`| —| —| —| —| optional  
`ReadResourceResult.contents`| required| required| required| required| required  
`ReadResourceResult.ttlMs`| —| —| —| —| required  
`ReadResourceResult.cacheScope`| —| —| —| —| required  
`ReadResourceResult.resultType`| —| —| —| —| required  
`ReadResourceResult._meta`| optional| optional| optional| optional| optional  
  
The second table shows which messages exist in which revision. 2026-07-28 replaced the subscription RPCs with a stream:

Item| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`resources/subscribe` request| ✓| ✓| ✓| ✓| —  
`resources/unsubscribe` request| ✓| ✓| ✓| ✓| —  
`notifications/resources/updated`| ✓| ✓| ✓| ✓| ✓  
`notifications/resources/list_changed`| ✓| ✓| ✓| ✓| ✓  
`subscriptions/listen` request| —| —| —| —| ✓  
`notifications/subscriptions/acknowledged`| —| —| —| —| ✓  
`resourceSubscriptions` filter| —| —| —| —| ✓  
`resource_link` content block| —| —| ✓| ✓| ✓  
  
What this means in practice:

  * **`resultType`, `ttlMs` and `cacheScope` are required** on the three results in 2026-07-28. Servers **MUST** include caching hints on `resultType: "complete"` results of `resources/list`, `resources/templates/list` and `resources/read`, with a `ttlMs` that is `>= 0`; `ttlMs: 0` means immediately stale. `"public"` fits lists and templates that are identical for all users; `"private"` fits `resources/read` results that depend on the authenticated user, or lists filtered per user; a cache **MUST NOT** share private responses across authorization contexts.
  * **The list does not depend on the connection.** A server that declares `resources` **MUST** answer `resources/list` with the set currently available to the requesting client. The set **MAY** change over time and **MAY** vary by the authorization presented on the request, but **MUST NOT** vary per connection or as a side effect of other requests on the connection.
  * **One read, several contents.** A server **MAY** return multiple contents for one `resources/read`, for example the files of a directory resource. It **MAY** also answer with an `InputRequiredResult`; the client retries with `inputResponses` and, if the server sent one, `requestState`.
  * **Templates.** `resources/templates/list` returns RFC 6570 URI templates such as `file:///{path}`. Template arguments may be auto-completed through the [completion API](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/completion/).
  * **Subscriptions.** The client sends `subscriptions/listen` with `notifications.resourceSubscriptions`, a list of URIs. The server acknowledges first, then sends `notifications/resources/updated` for those URIs on the same stream. The notification carries only the `uri` and `io.modelcontextprotocol/subscriptionId`, which equals the JSON-RPC `id` of the listen request; the client reads the resource again to get the new contents. Each notification type is opt-in: the server **MUST NOT** send a type the client did not request. `resources/subscribe` and `resources/unsubscribe` no longer exist. The `subscribe` capability says whether the server supports resource-specific update notifications.
  * **List changes.** A server that declared `listChanged` **SHOULD** send `notifications/resources/list_changed`; a client opts in with `resourcesListChanged: true` in the same `subscriptions/listen` filter. A server **MAY** give `ttlMs` without `listChanged`; then clients rely on the TTL alone.
  * **Ending a stream.** The client closes the stream. A server that ends a subscription on its own **SHOULD** first send a successful `subscriptions/listen` result; a close without it is an unexpected disconnect that the client **MAY** treat as a reason to reconnect. See [Subscriptions](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/subscriptions/).



## 5\. One message, five schemas

Does a message that is valid for one revision survive the others? Each row is validated against all five `schema.json` files. `✓` means valid, `✗` means rejected, `—` means the revision does not define the thing the row is about, so validation says nothing.

Message| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`ListResourcesResult` without `ttlMs`, `cacheScope`, `resultType`| ✓| ✓| ✓| ✓| ✗  
`ReadResourceResult` without `ttlMs`, `cacheScope`, `resultType`| ✓| ✓| ✓| ✓| ✗  
`resources/read` request without `params._meta`| ✓| ✓| ✓| ✓| ✗  
`ReadResourceResult` whose `contents` is an empty array| ✓| ✓| ✓| ✓| ✓  
`ReadResourceResult` whose item has both `text` and `blob`| ✓| ✓| ✓| ✓| ✓  
An `input_required` result returned for `resources/read`| ✗| ✗| ✗| ✗| ✓  
`Resource` with `icons`| —| —| —| ✓| ✓  
`resources/subscribe` request| ✓| ✓| ✓| ✓| —  
  
How the rows were built: rows 1 to 7 start from official examples of the 2026-07-28 revision. Rows 1 to 3 have the named fields deleted, row 4 empties `contents`, row 5 adds a `blob` to a text item, row 6 is the official `input_required` example validated as a `resources/read` response and row 7 adds an `icons` array. Row 8 is a hand-written `resources/subscribe` request. All unmodified examples are valid against the 2026-07-28 schema: 22 resource-related examples in 21 definitions validated, none was invalid.

  * **Rows 1 to 3.** 2026-07-28 requires `resultType`, `ttlMs` with `cacheScope`, and request `_meta`. Code written for 2025-11-25 and earlier fails validation until it adds them.
  * **Rows 4 and 5 are valid everywhere, and still wrong.** An empty `contents` array for a resource that does not exist is rejected only by the prose of the spec, never by the schema; the same goes for an item that has both `text` and `blob`. A schema check will not catch these two. The linter in section 10 does.
  * **Row 6.** An `input_required` result is not a valid read result before 2026-07-28: it has no `contents`.
  * **Row 8.** `resources/subscribe` is a valid request up to 2025-11-25 and does not exist in 2026-07-28.
  * **The limit of this method.** JSON Schema validation checks shape only. A column without `✗` does not mean the behaviors are compatible.



Several changes live only in the prose of the Resources page. The next table checks each revision's page for the sentence that introduced the rule:

Spec text mentions| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
Not found MUST be answered with `-32602`| —| —| —| —| ✓  
Not found answered with `-32002`| ✓| ✓| ✓| ✓| —  
MUST NOT return an empty `contents` array for a missing resource| —| —| —| —| ✓  
`resources/list` MUST NOT vary per connection| —| —| —| —| ✓  
Several contents may answer one `resources/read`| —| —| —| —| ✓  
`resources/read` may answer with `InputRequiredResult`| —| —| —| —| ✓  
`resources/subscribe` starts a subscription| ✓| ✓| ✓| ✓| —  
`subscriptions/listen` delivers updates| —| —| —| —| ✓  
Custom URI schemes follow RFC 3986| —| —| ✓| ✓| ✓  
File paths MUST be sanitized for `file://`| —| —| —| —| ✓  
  
The not-found row is the one that breaks clients: up to 2025-11-25 the spec says `-32002`, and 2026-07-28 says `-32602` (section 7).

## 6\. Reading over Streamable HTTP: the `Mcp-Name` header

Over Streamable HTTP a `resources/read` request **MUST** carry two headers: `Mcp-Method: resources/read` and `Mcp-Name` with the value of `params.uri`. A server that processes the body **MUST** compare the decoded header with the body and reject a mismatch with HTTP `400` and the JSON-RPC error `-32020` (`HeaderMismatchError`). A request without the header is rejected the same way.

A URI is often not plain ASCII, so the header has an escape. If the value cannot be safely represented as a plain ASCII header value (non-ASCII, control characters, leading or trailing whitespace) or if it itself looks like the escape, the client **MUST** send `=?base64?` \+ Base64 of the UTF-8 bytes + `?=`. The server decodes before it compares. The URI `notes://café` goes out like this:
    
    
    POST /mcp HTTP/1.1
    Mcp-Method: resources/read
    Mcp-Name: =?base64?bm90ZXM6Ly9jYWbDqQ==?=
    
    
    {"jsonrpc": "2.0", "id": 1, "method": "resources/read",
     "params": {"uri": "notes://café", "_meta": {"io.modelcontextprotocol/protocolVersion": "2026-07-28", "...": "..."}}}

A plain URI such as `config://app/settings` is sent as it is. The two typical bugs are a client that sends the raw non-ASCII value (the header is invalid) and a server that compares the header with the body without decoding (every non-ASCII URI answers `-32020`). The linter probes both (`header-mismatch`, `header-base64`).

## 7\. Errors: what to return and what to expect

Situation| What arrives| What to do  
---|---|---  
The resource, or the value of a template, does not exist| JSON-RPC error `-32602` (`InvalidParamsError`), `data.uri` holding the URI. The spec's example message is `Resource not found`| Client: refresh the list and stop retrying. Server: **MUST** return this, never an empty `contents`  
A server from 2025-11-25 or earlier says the same| `-32002`| Clients **SHOULD** also accept `-32002`; servers on 2026-07-28 use `-32602`  
`uri` is missing, or the URI is not usable| `-32602`: the SDK answers `Invalid request parameters` for a missing `uri` and `Unknown resource` for an unusable one| Fix the client; retrying the same request cannot succeed. Servers **MUST** validate all resource URIs  
A template value tries to escape its root (`../`, an absolute path)| The SDK answers `-32602` `Unknown resource` before the handler runs. The spec: servers **MUST** sanitize file paths to prevent directory traversal when serving `file://` resources| Test it; treat any success as a vulnerability  
The backend behind the resource failed (database down, quota)| `-32603` (`InternalError`). Spec: servers **SHOULD** return it for internal errors| Retry with backoff; do not put secrets in the message  
Headers disagree with `uri` (`Mcp-Method`, `Mcp-Name`), or are missing| HTTP `400` and `-32020` (`HeaderMismatchError`)| A client or gateway bug; fix the headers, Base64-encode non-ASCII URIs  
The protocol version is unknown, or a needed client capability is missing| HTTP `400` and `-32022` or `-32021` (same shapes as for tools)| See [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/)  
The method does not exist, for example `resources/subscribe` against a 2026-07-28 server| HTTP `404` and `-32601` (`MethodNotFoundError`)| Use `subscriptions/listen`  
The server needs more input before it can read| Not an error: a result with `resultType: "input_required"`| Answer the requests and retry with `inputResponses`, `requestState` and a new JSON-RPC `id`  
  
Resource errors are protocol errors: unlike a tool result, a read result has no `isError` field (section 4).

## 8\. What the official Python SDK 2.3.0 returns

The reference server defines one resource per shape: a text resource with annotations, a binary resource, and three templates. It uses the official SDK (`pip install mcp==2.3.0`). The `touch` tool exists only so that the subscription runs can make a resource "change":

**resources_ref_server.py**
    
    
     """Official Python SDK (mcp==2.3.0) resources server at http://127.0.0.1:8230/mcp, no auth.
    
    Resources: a text resource with annotations, a binary resource, three templates (a closed set of notes, files under
    `sample-docs/` served through `safe_join`, a status that fails on purpose) and the tool `touch`, which announces a
    resource update. The templates keep the SDK's default `ResourceSecurity` policy: traversal, absolute paths and
    NUL bytes in a template value are rejected before the handler runs.
    """
    import base64
    from pathlib import Path
    
    from mcp.server.mcpserver import Context, MCPServer
    from mcp.server.mcpserver.exceptions import ResourceError, ResourceNotFoundError
    from mcp.shared.path_security import safe_join
    from mcp.types import Annotations
    
    ROOT = Path(__file__).resolve().parent / "sample-docs"
    NOTES = {"standup": "Standup at 09:30.", "release": "Release freeze on Friday."}
    # A 1x1 transparent PNG.
    PIXEL = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==")
    
    server = MCPServer("resources-ref")
    
    
    @server.resource("config://app/settings", name="settings", title="Application settings",
                     description="Current settings as JSON", mime_type="application/json",
                     annotations=Annotations(audience=["user"], priority=0.8))
    def settings() -> str:
        return '{"theme": "dark", "retries": 3}'
    
    
    @server.resource("image://logo", name="logo", mime_type="image/png")
    def logo() -> bytes:
        return PIXEL
    
    
    @server.resource("notes://{topic}", name="notes", description="A note by topic")
    def note(topic: str) -> str:
        if topic not in NOTES:
            raise ResourceNotFoundError("no note %r" % topic)
        return NOTES[topic]
    
    
    @server.resource("docs://files/{+path}", name="docs", description="Files under sample-docs")
    def doc(path: str) -> str:
        try:
            return safe_join(ROOT, path).read_text(encoding="utf-8")
        except (FileNotFoundError, IsADirectoryError):
            raise ResourceNotFoundError("no file %r" % path) from None
    
    
    @server.resource("status://{kind}", name="status", description="Service status; busy and crash fail on purpose")
    def status(kind: str) -> str:
        if kind == "ok":
            return "all systems normal"
        if kind == "busy":
            raise ResourceError("upstream quota exhausted, retry later")  # an anticipated failure
        if kind == "crash":
            raise RuntimeError("db password is hunter2")  # a crash: the SDK withholds this text from the client
        raise ResourceNotFoundError("no status %r" % kind)
    
    
    @server.tool()
    async def touch(uri: str, ctx: Context) -> str:
        """Announce that a resource changed, so `subscriptions/listen` streams deliver an update."""
        await ctx.notify_resource_updated(uri)
        return "announced " + uri
    
    
    if __name__ == "__main__":
        server.run("streamable-http", port=8230)

Twenty runs were sent over Streamable HTTP in the 2026-07-28 request format. Every response was validated against its definition in the 2026-07-28 `schema.json`, an error also against the definition of its code, and every stream frame against its notification (all twenty are valid; the definition is named at the end of each recorded line):

Run| Request| What the SDK returned| Against the spec  
---|---|---|---  
`list`| `resources/list`| `ttlMs: 0`, `cacheScope: "private"`, `resultType: "complete"`, 2 resources (templates are listed separately)| Valid. The SDK fills the required hints with the most conservative values  
`templates`| `resources/templates/list`| The same hints, 3 templates| Valid  
`read-text`| the settings resource| One text content, `application/json`| Valid  
`read-blob`| `image://logo`| One blob content, `image/png`, the 70 raw bytes base64-encoded| Valid  
`read-template`| `notes://standup`| One text content from the template| Valid  
`read-file`| `docs://files/README.md`| The file text, through the `{+path}` template| Valid  
`unknown-uri`| a static URI that is not registered| HTTP `400`, `-32602`, `Unknown resource: config://nope`| Matches the not-found rule  
`unknown-topic`| `notes://nope`| HTTP `400`, `-32602`, the handler's message| Matches: the handler raised `ResourceNotFoundError`  
`missing-file`| `docs://files/missing.md`| HTTP `400`, `-32602`| Matches: the handler turned `FileNotFoundError` into `ResourceNotFoundError`  
`traversal`| A `docs://files/` URI whose path starts with `../`| HTTP `400`, `-32602`, `Unknown resource`| Safe: the template did not match, the handler never ran  
`absolute-path`| `docs://files//etc/passwd`| Same| Same  
`bad-uri`| `not a uri`| Same| An unusable URI is answered like a missing resource  
`non-ascii-uri`| `notes://café`, header sent as a Base64 sentinel| `-32602` with `no note 'café'`| The handler received the decoded value: the header was accepted  
`status-busy`| `status://busy`, the handler raises `ResourceError`| HTTP `200`, `-32603`, the handler's message| Valid `InternalError`. The message reaches the client: write text that is safe to show  
`status-crash`| `status://crash`, the handler raises `RuntimeError("db password is hunter2")`| HTTP `200`, `-32603`, `Error creating resource from template status://crash`| Valid. The SDK withholds the original text and logs the traceback on the server  
`header-mismatch`| a read with `Mcp-Name` set to another URI| HTTP `400`, `-32020`| Matches the Streamable HTTP rule  
`missing-uri`| `resources/read` without `uri`| HTTP `400`, `-32602`, `Invalid request parameters`| Matches  
`subscribe-old`| `resources/subscribe`| HTTP `404`, `-32601`| The method is gone in 2026-07-28 (section 4)  
`listen-ack`| `subscriptions/listen` with one URI in `resourceSubscriptions`| One frame: the acknowledgement, tagged with the request `id` as `subscriptionId`| Valid against the schema of the acknowledgement notification  
`listen-update`| The same stream; `touch` announces `config://other`, then the subscribed URI| The acknowledgement, then one update notification for the subscribed URI only| Valid; the unrequested URI is not delivered, as the spec demands  
**Recorded output of the twenty runs**
    
    
     list             HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete resources=2 | ListResourcesResultResponse valid
    templates        HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete templates=3 | ListResourceTemplatesResultResponse valid
    read-text        HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete contents: application/json text '{"theme": "dark", "retries": 3}' | ReadResourceResultResponse valid
    read-blob        HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete contents: image/png blob 70 bytes | ReadResourceResultResponse valid
    read-template    HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete contents: text/plain text 'Standup at 09:30.' | ReadResourceResultResponse valid
    read-file        HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete contents: text/plain text '# Sample docs\n\nServed through the `docs:' | ReadResourceResultResponse valid
    unknown-uri      HTTP 400 error    code -32602 'Unknown resource: config://nope' | JSONRPCErrorResponse+InvalidParamsError valid
    unknown-topic    HTTP 400 error    code -32602 "no note 'nope'" | JSONRPCErrorResponse+InvalidParamsError valid
    missing-file     HTTP 400 error    code -32602 "no file 'missing.md'" | JSONRPCErrorResponse+InvalidParamsError valid
    traversal        HTTP 400 error    code -32602 'Unknown resource: docs://files/../resources_ref_server.py' | JSONRPCErrorResponse+InvalidParamsError valid
    absolute-path    HTTP 400 error    code -32602 'Unknown resource: docs://files//etc/passwd' | JSONRPCErrorResponse+InvalidParamsError valid
    bad-uri          HTTP 400 error    code -32602 'Unknown resource: not a uri' | JSONRPCErrorResponse+InvalidParamsError valid
    non-ascii-uri    HTTP 400 error    code -32602 "no note 'café'" | JSONRPCErrorResponse+InvalidParamsError valid
    status-busy      HTTP 200 error    code -32603 'upstream quota exhausted, retry later' | JSONRPCErrorResponse+InternalError valid
    status-crash     HTTP 200 error    code -32603 'Error creating resource from template status://crash' | JSONRPCErrorResponse+InternalError valid
    header-mismatch  HTTP 400 error    code -32020 "mcp-name header does not match the request body's 'uri' parameter" | JSONRPCErrorResponse+HeaderMismatchError valid
    missing-uri      HTTP 400 error    code -32602 'Invalid request parameters' | JSONRPCErrorResponse+InvalidParamsError valid
    subscribe-old    HTTP 404 error    code -32601 'Method not found' | JSONRPCErrorResponse+MethodNotFoundError valid
    listen-ack       HTTP 200 stream   ack(resourceSubscriptions=1) | SubscriptionsAcknowledgedNotification valid
    listen-update    HTTP 200 stream   ack(resourceSubscriptions=1) -> updated(config://app/settings) | ResourceUpdatedNotification+SubscriptionsAcknowledgedNotification valid

What the runs say about the SDK:

  * **Not found is`ResourceNotFoundError`.** Raising it from a handler gives `-32602`, as the 2026-07-28 spec requires. A handler that raises a plain exception for a missing note takes the crash path of `status-crash`: `-32603` with a generic message, which clients treat as a server fault and may retry.
  * **`ResourceError` and crashes both end as `-32603`.** `ResourceError` is for failures you anticipated: its message reaches the client. Any other exception is a crash: the client sees only the URI, the traceback stays in the server log.
  * **Security is the default for templates.** Template values that contain `..`, are absolute paths or contain NUL bytes are refused before the handler runs. If you read files, still resolve them with `safe_join` as the example does, and never build paths with string concatenation.
  * **Updates are fire-and-forget.** The SDK acknowledges first, tags every frame with the request id and delivers only what was requested. Its documentation states that delivery has no replay: after a dropped stream the client re-listens and reads again.
  * **The cache hints are conservative.** `ttlMs: 0` and `"private"` are always valid, and they disable caching. Set real values when the data allows it.



## 9\. Failure modes and recovery

Symptom| Cause| How to detect| Recovery  
---|---|---|---  
A client treats a missing resource as a server fault, or retries forever| The server answers `-32603` (an unexpected exception) instead of `-32602`| Read a URI that cannot exist; run the linter (`not-found-code`)| Raise the SDK's `ResourceNotFoundError`, or return `-32602` yourself  
A client cannot tell "empty" from "missing"| The server answers `contents: []` for a missing resource. The spec: **MUST NOT** , an empty array is ambiguous| `not-found-code`, `template-not-found`| Return the `-32602` error  
A client does not recognize a legacy server's not-found| The code changed from `-32002` to `-32602` in 2026-07-28; servers up to 2025-11-25 still send `-32002`| Read a missing URI against both generations| Accept both codes in clients; servers on 2026-07-28 return `-32602`  
Files outside the root are readable through a template| The handler joins paths without checking| `traversal-rejected`| Resolve with `safe_join` or an equivalent, keep the SDK's default `ResourceSecurity`, and check access permissions before reading  
Every non-ASCII URI answers `-32020`| The server compares `Mcp-Name` with the body without decoding the Base64 sentinel, or the client sent raw non-ASCII| `header-base64`| Decode before comparing; the client encodes  
Requests through a gateway fail with `-32020` or `400`| The gateway dropped or rewrote `Mcp-Method` or `Mcp-Name`| `header-mismatch`; compare the headers at both ends| Forward the standard headers unchanged  
A client keeps showing stale content| It did not subscribe: `subscribe` is not declared, or `subscriptions/listen` has no `resourceSubscriptions`, or the stream dropped and nothing re-listened| Check the capability; watch the stream for the acknowledgement| Declare `subscribe`, listen with the URIs, re-listen after a disconnect and read the resource again, because the notification carries only the URI  
An old client's `resources/subscribe` fails| The method does not exist in 2026-07-28| HTTP `404`, `-32601`| Switch to `subscriptions/listen`  
Two clients get different lists| The list depends on connection state. It **MUST NOT** ; only the authorization may change it| Call `resources/list` on two connections with the same credentials and diff| Compute the list from the request's authorization only  
One user's content is served to another from a cache| A read result that depends on the user was marked `cacheScope: "public"`, or the cache ignores authorization| Compare `cacheScope` and the content for two tokens| Use `"private"` for user-dependent results  
A client cannot render a binary resource| `blob` is not valid base64, or `mimeType` is missing| `read-blob-base64`, `read-mime`| Encode the raw bytes with standard base64 and state the MIME type  
A secret appears in a client error message| A handler put a backend message into a `ResourceError`| Trigger each failure and read the message| Raise `ResourceError` only with text that is safe to show; let the SDK withhold the rest and log the cause  
A template answers any value| The handler returns something for every input, so "missing" cannot be told| `template-not-found` (WARN)| Validate the value against what exists and raise `ResourceNotFoundError`  
  
## 10\. Lint your own resources endpoint

`lint_resources.py` talks to a Streamable HTTP endpoint. It lists resources and templates, reads up to five listed resources and sends a few probe reads that no healthy server may satisfy: a missing URI, a missing template value, path traversal, a mismatching `Mcp-Name` and a non-ASCII URI. The probes are plain reads and change nothing; do not point them at an endpoint where reading has side effects. It needs only the Python standard library.

**lint_resources.py**
    
    
     #!/usr/bin/env python3
    """Lint the resources of an MCP server against spec 2026-07-28 over Streamable HTTP.
    
    Usage: lint_resources.py URL [--token T] [--max-reads N]
    URL: the Streamable HTTP endpoint. The linter lists resources and templates, reads up to N listed resources
    (default 5) and sends a few probe reads that no healthy server may satisfy: a missing URI, a missing template
    value, path traversal, a mismatching `Mcp-Name` header and a non-ASCII URI. The probes are plain reads and change
    nothing; do not point them at an endpoint where reading has side effects.
    Levels: FAIL = a MUST of the spec is violated, WARN = a SHOULD or a recommendation is not followed.
    Exit code: 0 no FAIL, 1 at least one FAIL, 2 the endpoint cannot be read.
    """
    import argparse
    import base64
    import binascii
    import http.client
    import json
    import re
    import sys
    from urllib.parse import urlsplit
    
    VERSION = "2026-07-28"
    SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
    VARIABLE_RE = re.compile(r"\{[+#./;?&]?[^}]+\}")
    MISSING_URI = "lint-probe://missing/resource"
    MISSING_VALUE = "x-lint-missing"
    TRAVERSAL_VALUES = ["../x-lint-traversal", "%2e%2e/x-lint-traversal", "/etc/passwd"]
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    
    
    def report(name, ok, detail, level="FAIL"):
        status = "PASS" if ok else level
        counts[status] += 1
        print("%s %s: %s" % (status, name, detail))
    
    
    def mcp_name(value):
        """Mcp-Name header value: plain ASCII as is, anything else in the Base64 sentinel format."""
        plain = value.isascii() and value.isprintable() and value == value.strip() \
            and not (value.startswith("=?base64?") and value.endswith("?="))
        return value if plain else "=?base64?%s?=" % base64.b64encode(value.encode()).decode()
    
    
    def request(url, method, params=None, token=None, name=None):
        """Build one 2026-07-28 request: (parsed URL, body, headers).
    
        `Mcp-Name` is `params.name` or `params.uri`; pass `name` to send another value."""
        meta = {"io.modelcontextprotocol/protocolVersion": VERSION,
                "io.modelcontextprotocol/clientInfo": {"name": "lint-resources", "version": "0"},
                "io.modelcontextprotocol/clientCapabilities": {}}
        headers = {"Accept": "application/json, text/event-stream", "Content-Type": "application/json",
                   "MCP-Protocol-Version": VERSION, "Mcp-Method": method}
        source = name if name is not None else (params or {}).get("name", (params or {}).get("uri"))
        if isinstance(source, str):
            headers["Mcp-Name"] = mcp_name(source)
        if token:
            headers["Authorization"] = "Bearer " + token
        body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": {**(params or {}), "_meta": meta}})
        return urlsplit(url), body, headers
    
    
    def rpc(url, method, params=None, token=None, name=None):
        """POST one request and return (HTTP status, JSON-RPC message or None)."""
        parts, body, headers = request(url, method, params, token, name)
        cls = http.client.HTTPSConnection if parts.scheme == "https" else http.client.HTTPConnection
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
    
    
    def list_all(url, method, key, token):
        """Return (items, first result) of a paginated list method."""
        items, cursor, first = [], None, None
        for _ in range(50):
            status, msg = rpc(url, method, {"cursor": cursor} if cursor else None, token)
            result = (msg or {}).get("result")
            if status != 200 or not isinstance(result, dict) or not isinstance(result.get(key), list):
                raise ValueError("%s failed: HTTP %s, %s" % (method, status, json.dumps(msg)[:200]))
            items += result[key]
            first = first or result
            cursor = result.get("nextCursor")
            if not cursor:
                return items, first
        raise ValueError("%s still paginating after 50 pages" % method)
    
    
    def envelope_problems(result):
        """Results of 2026-07-28 MUST carry resultType and the caching hints, with ttlMs >= 0."""
        ttl, scope = result.get("ttlMs"), result.get("cacheScope")
        problems = []
        if not isinstance(result.get("resultType"), str):
            problems.append("resultType is missing")
        if not isinstance(ttl, int) or isinstance(ttl, bool) or ttl < 0:
            problems.append("ttlMs is %r, want an integer >= 0" % ttl)
        if scope not in ("public", "private"):
            problems.append("cacheScope is %r, want 'public' or 'private'" % scope)
        return problems
    
    
    def envelope_check(result):
        """(ok, detail) of the envelope of a list result."""
        problems = envelope_problems(result)
        return not problems, "; ".join(problems) if problems else "resultType=%s ttlMs=%d cacheScope=%s" % (
            result["resultType"], result["ttlMs"], result["cacheScope"])
    
    
    def lint_capability(url, token):
        status, msg = rpc(url, "server/discover", None, token)
        result = (msg or {}).get("result")
        caps = result.get("capabilities") if isinstance(result, dict) else None
        declared = isinstance(caps, dict) and isinstance(caps.get("resources"), dict)
        report("capability-declared", declared, "the `resources` capability is %s (server/discover, HTTP %s)"
               % ("declared" if declared else "missing", status))
        if declared:
            print("INFO resources capability: listChanged=%s subscribe=%s" % (
                caps["resources"].get("listChanged", False), caps["resources"].get("subscribe", False)))
    
    
    def lint_listed(resources, templates):
        named = [r for r in resources if isinstance(r, dict) and isinstance(r.get("uri"), str)
                 and SCHEME_RE.match(r["uri"]) and isinstance(r.get("name"), str)]
        report("resource-fields", len(named) == len(resources),
               "%d of %d resources have a name and an absolute URI with a scheme" % (len(named), len(resources)))
        uris = [r["uri"] for r in named]
        dup = sorted({u for u in uris if uris.count(u) > 1})
        report("uri-unique", not dup, "duplicates: %s" % dup if dup else "no duplicate URIs", "WARN")
        plain = [r["uri"] for r in named if not isinstance(r.get("mimeType"), str)]
        report("resource-mime", not plain, "no mimeType: %s" % plain if plain
               else "every listed resource states a mimeType", "WARN")
        good = [t for t in templates if isinstance(t, dict) and isinstance(t.get("name"), str)
                and isinstance(t.get("uriTemplate"), str) and VARIABLE_RE.search(t["uriTemplate"])]
        report("template-fields", len(good) == len(templates),
               "%d of %d templates have a name and a uriTemplate with a {variable}" % (len(good), len(templates)))
    
    
    def decode_blob(blob):
        try:
            base64.b64decode(blob, validate=True)
            return True
        except (binascii.Error, ValueError, TypeError):
            return False
    
    
    def lint_reads(url, uris, token):
        """Read each URI and check envelope, contents, blob encoding and mimeType."""
        envelope, content, blob, mime, answered = [], [], [], [], 0
        for uri in uris:
            status, msg = rpc(url, "resources/read", {"uri": uri}, token)
            result = (msg or {}).get("result") if isinstance(msg, dict) else None
            if not isinstance(result, dict):
                content.append("%s: HTTP %s without a result" % (uri, status))
                continue
            answered += 1
            if envelope_problems(result):
                envelope.append(uri)
            items = result.get("contents")
            if not isinstance(items, list) or not items:
                content.append("%s: contents is empty or not an array" % uri)
                continue
            for item in items:
                kinds = [k for k in ("text", "blob") if isinstance(item, dict) and isinstance(item.get(k), str)]
                if not isinstance(item, dict) or not isinstance(item.get("uri"), str) or len(kinds) != 1:
                    content.append("%s: an item needs a uri and exactly one of text or blob" % uri)
                    continue
                if "blob" in item and not decode_blob(item["blob"]):
                    blob.append(uri)
                if not isinstance(item.get("mimeType"), str):
                    mime.append(uri)
        report("read-envelope", not envelope, "resultType, ttlMs or cacheScope is wrong for %s" % envelope if envelope
               else "%d reads carry resultType, ttlMs and cacheScope" % answered)
        report("read-contents", not content, "; ".join(content) if content
               else "%d reads return non-empty contents, each item with a uri and exactly one of text or blob" % answered)
        report("read-blob-base64", not blob, "blob is not valid base64: %s" % blob if blob
               else "every blob is valid base64")
        report("read-mime", not mime, "no mimeType on contents of %s" % mime if mime
               else "every content item states a mimeType", "WARN")
    
    
    def probe_not_found(url, uri, token, answered="FAIL"):
        """Read something that cannot exist. Return (PASS|WARN|FAIL, detail): -32602 is required, the legacy -32002
        only a WARN, an empty contents array is a FAIL, contents for a made-up URI get the level `answered`."""
        status, msg = rpc(url, "resources/read", {"uri": uri}, token)
        if not isinstance(msg, dict):
            return "FAIL", "HTTP %s without a JSON-RPC message for %s" % (status, uri)
        error = msg.get("error")
        if isinstance(error, dict):
            code = error.get("code")
            return ("PASS" if code == -32602 else "WARN" if code == -32002 else "FAIL",
                    "%s answered with code %s (HTTP %s)" % (uri, code, status))
        if (msg.get("result") or {}).get("contents") == []:
            return "FAIL", "%s answered with an empty contents array, which hides the missing resource" % uri
        return answered, "%s was answered with contents, so the server cannot tell what is missing" % uri
    
    
    def worst(outcomes):
        """The most severe (level, detail) of several outcomes; the details of that level are joined."""
        level = max((o[0] for o in outcomes), key=("PASS", "WARN", "FAIL").index)
        return level, "; ".join(o[1] for o in outcomes if o[0] == level)
    
    
    def fill(template, value):
        return VARIABLE_RE.sub(value, template)
    
    
    def lint_probes(url, templates, token):
        level, detail = probe_not_found(url, MISSING_URI, token)
        report("not-found-code", level == "PASS", detail, level)
        templates = [t["uriTemplate"] for t in templates if isinstance(t, dict) and isinstance(t.get("uriTemplate"), str)]
        templates = templates[:5]
        if templates:
            level, detail = worst([probe_not_found(url, fill(t, MISSING_VALUE), token, "WARN") for t in templates])
            report("template-not-found", level == "PASS", detail if level != "PASS"
                   else "%d template probes answered with -32602" % len(templates), level)
        leaked = []
        for template in templates:
            for value in TRAVERSAL_VALUES:
                uri = fill(template, value)
                status, msg = rpc(url, "resources/read", {"uri": uri}, token)
                if isinstance(msg, dict) and (msg.get("result") or {}).get("contents"):
                    leaked.append(uri)
        if templates:
            report("traversal-rejected", not leaked, "read succeeded for %s" % leaked if leaked
                   else "%d traversal probes were rejected" % (len(templates) * len(TRAVERSAL_VALUES)))
        else:
            print("INFO no templates, the template and traversal probes are skipped")
        status, msg = rpc(url, "resources/read", {"uri": MISSING_URI}, token, name="lint-probe://other")
        code = ((msg or {}).get("error") or {}).get("code") if isinstance(msg, dict) else None
        report("header-mismatch", status == 400 and code == -32020,
               "a mismatching Mcp-Name was answered with HTTP %s, code %s (want 400, -32020)" % (status, code))
        status, msg = rpc(url, "resources/read", {"uri": "lint-probe://caf\u00e9"}, token)
        code = ((msg or {}).get("error") or {}).get("code") if isinstance(msg, dict) else None
        report("header-base64", code != -32020, "a non-ASCII URI sent as a Base64 sentinel was answered with code %s"
               % code)
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("url")
        ap.add_argument("--token", help="bearer token for the endpoint")
        ap.add_argument("--max-reads", type=int, default=5, help="how many listed resources to read")
        args = ap.parse_args()
        if not args.url.startswith(("http://", "https://")):
            ap.error("URL must start with http:// or https://")
        try:
            resources, listing = list_all(args.url, "resources/list", "resources", args.token)
            templates, template_listing = list_all(args.url, "resources/templates/list", "resourceTemplates", args.token)
            print("INFO %d resources, %d templates" % (len(resources), len(templates)))
            lint_capability(args.url, args.token)
            report("list-envelope", *envelope_check(listing))
            report("templates-envelope", *envelope_check(template_listing))
            lint_listed(resources, templates)
            uris = [r["uri"] for r in resources if isinstance(r, dict) and isinstance(r.get("uri"), str)]
            if uris:
                lint_reads(args.url, uris[:args.max_reads], args.token)
            else:
                print("INFO no listed resources, the read checks are skipped")
            lint_probes(args.url, templates, args.token)
        except (OSError, ValueError, http.client.HTTPException) as exc:
            print("ERROR %s" % exc)
            return 2
        print("%d pass, %d warn, %d fail" % (counts["PASS"], counts["WARN"], counts["FAIL"]))
        return 1 if counts["FAIL"] else 0
    
    
    if __name__ == "__main__":
        sys.exit(main())
    
    
    python3 lint_resources.py http://127.0.0.1:8230/mcp
    python3 lint_resources.py https://example.com/mcp --token "$TOKEN" --max-reads 10

`FAIL` means a MUST is violated; `WARN` means a SHOULD or a recommendation is not followed. Exit code 0 means no FAIL, 1 at least one FAIL, 2 means the endpoint could not be read.

Check| Level| Rule  
---|---|---  
`capability-declared`| FAIL| `server/discover` declares the `resources` capability  
`list-envelope`| FAIL| The `resources/list` result carries `resultType`, an integer `ttlMs` `>= 0` and a `cacheScope` of `public` or `private`  
`templates-envelope`| FAIL| The same for `resources/templates/list`  
`resource-fields`| FAIL| Every listed resource has a string `name` and a `uri` with a scheme  
`uri-unique`| WARN| Listed URIs are unique  
`resource-mime`| WARN| Listed resources state a `mimeType`  
`template-fields`| FAIL| Every template has a `name` and a `uriTemplate` with a `{variable}`  
`read-envelope`| FAIL| Each read result carries `resultType`, `ttlMs` and `cacheScope`  
`read-contents`| FAIL| `contents` is a non-empty array; each item has a `uri` and exactly one of `text` or `blob`  
`read-blob-base64`| FAIL| Every `blob` is valid base64  
`read-mime`| WARN| Every content item states a `mimeType`  
`not-found-code`| FAIL| A made-up URI is answered with `-32602`; `-32002` is only a WARN, an empty `contents` or any content is a FAIL  
`template-not-found`| FAIL| A made-up template value is answered with `-32602`; `-32002` or content for the made-up value is a WARN, an empty `contents` is a FAIL  
`traversal-rejected`| FAIL| `../`, `%2e%2e/` and an absolute path in template values never return contents (skipped when the server lists no templates)  
`header-mismatch`| FAIL| A read whose `Mcp-Name` differs from `uri` is answered with HTTP `400` and `-32020`  
`header-base64`| FAIL| A non-ASCII URI sent as a Base64 sentinel is not rejected with `-32020`  
  
Recorded output against the SDK server of section 8:
    
    
    INFO 2 resources, 3 templates
    PASS capability-declared: the `resources` capability is declared (server/discover, HTTP 200)
    INFO resources capability: listChanged=True subscribe=True
    PASS list-envelope: resultType=complete ttlMs=0 cacheScope=private
    PASS templates-envelope: resultType=complete ttlMs=0 cacheScope=private
    PASS resource-fields: 2 of 2 resources have a name and an absolute URI with a scheme
    PASS uri-unique: no duplicate URIs
    PASS resource-mime: every listed resource states a mimeType
    PASS template-fields: 3 of 3 templates have a name and a uriTemplate with a {variable}
    PASS read-envelope: 2 reads carry resultType, ttlMs and cacheScope
    PASS read-contents: 2 reads return non-empty contents, each item with a uri and exactly one of text or blob
    PASS read-blob-base64: every blob is valid base64
    PASS read-mime: every content item states a mimeType
    PASS not-found-code: lint-probe://missing/resource answered with code -32602 (HTTP 400)
    PASS template-not-found: 3 template probes answered with -32602
    PASS traversal-rejected: 9 traversal probes were rejected
    PASS header-mismatch: a mismatching Mcp-Name was answered with HTTP 400, code -32020 (want 400, -32020)
    PASS header-base64: a non-ASCII URI sent as a Base64 sentinel was answered with code -32602
    16 pass, 0 warn, 0 fail

The linter was also run against a stub endpoint that breaks exactly one rule at a time. Each defect is named by a check in the table: an empty `contents` for a missing resource, the legacy `-32002`, results in the 2025-11-25 shape, an item with both `text` and `blob`, a broken blob, a missing name or scheme, a template that accepts `../`, a server that ignores or cannot decode `Mcp-Name`, and a server that does not declare the capability.

## 11\. Before you ship a resource

  * `resources/list` is the same for every connection (it may depend on authorization only), carries `ttlMs` and `cacheScope`, and filtered lists are `"private"`.
  * Every URI has a scheme; custom schemes follow RFC 3986; `https://` is used only when the client can fetch it directly.
  * A missing resource or template value is `-32602`, never an empty `contents`; clients also accept the legacy `-32002`.
  * Text is `text`, binary is base64 `blob`, each item has a `uri` and a `mimeType`.
  * Template values are validated; paths are resolved against a root; traversal and absolute paths are refused.
  * Errors that reach the client carry no secrets; crashes are logged on the server.
  * The server reads `Mcp-Name`, decodes the Base64 sentinel and rejects a mismatch with `-32020`.
  * If the data changes, declare `subscribe` and `listChanged`, and tell clients to read again after `notifications/resources/updated`; set a real `ttlMs`.
  * The linter passes on your endpoint; re-run it after changing the SDK, the gateway or the revision you serve.



## Versions and Verification

The tables are generated from the official `schema.json` files, the official examples are validated against them, and the runtime behavior comes from running the official Python SDK 2.3.0 (`mcp==2.3.0`). Spec wording and schemas are read from one pinned commit of the official repository (`dae694f6`, 2026-07-28 revision and the four before it). The tables were generated and checked with `jsonschema` 4.26.0, using the draft-07 validator for the revisions whose schema declares draft-07 and the 2020-12 validator for the others. The SDK runs used `mcp==2.3.0` on Python 3.14 (macOS). A change in the official text or in the SDK needs a re-run.

### Sources

  * The official 2026-07-28 pages: [Resources](https://modelcontextprotocol.info/specification/2026-07-28/server/resources/), [Subscriptions](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/subscriptions/), [Caching](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/caching/), [Pagination](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/pagination/), [Streamable HTTP, standard request headers](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/) and the [schema reference](https://modelcontextprotocol.info/specification/2026-07-28/schema/)
  * The `schema.json` of each revision and the official examples in the [official repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
  * This site's [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/), [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/) and [MCP Inspector](https://modelcontextprotocol.info/tools/inspector/)



[MCP Prompts Explained: Arguments, Messages, Completion and Errors](https://modelcontextprotocol.info/docs/concepts/prompts/ "MCP Prompts Explained: Arguments, Messages, Completion and Errors")[MCP Tools Explained: Definitions, Results, Errors and Version Differences](https://modelcontextprotocol.info/docs/concepts/tools/ "MCP Tools Explained: Definitions, Results, Errors and Version Differences")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
