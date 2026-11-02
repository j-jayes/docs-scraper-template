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
    * [MCP Prompts Explained: Arguments, Messages, Completion and Errors](https://modelcontextprotocol.info/docs/concepts/prompts/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/concepts/prompts/)
  * [简体中文](https://mcpcn.com/docs/concepts/prompts/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. Prompt, tool or resource
  * 2\. The path of a prompt
  * 3\. The definitions across five revisions
  * 4\. Listing, getting and being notified
  * 5\. One message, five schemas
  * 6\. Getting a prompt over Streamable HTTP: the Mcp-Name header
  * 7\. Errors: what to return and what to expect
  * 8\. What the official Python SDK 2.3.0 returns
  * 9\. Failure modes and recovery
  * 10\. Lint your own prompts endpoint
  * 11\. Before you ship a prompt
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[Core Concepts](https://modelcontextprotocol.info/docs/concepts/)

MCP Prompts Explained: Arguments, Messages, Completion and Errors

# MCP Prompts Explained: Arguments, Messages, Completion and Errors

A prompt is a reusable message template that a server offers and that the user picks, for example from a slash-command menu. Its path runs through capability declaration, list, arguments, get, completion, change notification, and failure. The sections below follow that path on the 2026-07-28 revision and show what changed in each revision since 2024-11-05.

For data the host application attaches, read [MCP resources explained](https://modelcontextprotocol.info/docs/concepts/resources/). For actions the model takes, read [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/). For how to design a server that a model uses well, read [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/). For the normative text, read the official [Prompts](https://modelcontextprotocol.info/specification/2026-07-28/server/prompts/) page.

## 1\. Prompt, tool or resource

The spec gives each primitive a different controller. The controller decides who triggers the primitive, and that decides which one you should build. For prompts, the spec is explicit: "user-controlled" refers to who decides when the prompt is used, not who writes its content. The content is defined by the server.

You want to| Build| Who triggers it| Why  
---|---|---|---  
Offer a reusable starting message that the user picks explicitly (a slash command, a menu entry)| Prompt| The user: prompts are **user-controlled**|  The user selects it, the server fills in the messages  
Bundle instructions with a file or a record in one user-selected message| Prompt whose message holds an embedded `resource` or a `resource_link`| The user picks the prompt; the server decides what it embeds| One choice by the user brings the instructions and the data together  
Hand the application data to include as context| Resource| The host application: resources are **application-driven**|  The host can list, search, or include them by heuristics  
Let the model perform an action or fetch something on its own| Tool| The model: tools are **model-controlled**|  The model calls `tools/call` when it decides to  
Have the model decide on its own to use a template| Tool| The model| A model cannot select a prompt: the user does. Expose the capability as a tool  
  
Arguments of a prompt are always strings (section 3). If the input is structured, either encode it in the string or make the capability a tool, whose `inputSchema` can describe it.

## 2\. The path of a prompt

Step| Message| What to know| Section  
---|---|---|---  
1| Capability| A server that supports prompts **MUST** declare the `prompts` capability. `listChanged` says whether it will announce changes| 4  
2| `prompts/list`| Supports pagination and caching. The set **MAY** be empty and **MAY** change over time, but **MUST NOT** vary per connection| 3, 4  
3| `completion/complete`| Optional. Needs the `completions` capability. The reference is `{"type": "ref/prompt", "name": ...}`; at most 100 values per answer| 4  
4| `prompts/get`| Arguments are strings; the result is an array of messages. It may also answer with `InputRequiredResult`| 4, 5  
5| Use| The client puts the messages into the conversation. This is the host's job, not a protocol message| 4  
6| `subscriptions/listen`| With `promptsListChanged: true`, the server **SHOULD** send `notifications/prompts/list_changed` when the set changes. The notification carries no list: list again| 4  
  
## 3\. The definitions across five revisions

`—` means the revision does not define the field. The columns are the five revisions (year and month; the full dates are 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25 and 2026-07-28).

Field| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`Prompt.name`| required| required| required| required| required  
`Prompt.title`| —| —| optional| optional| optional  
`Prompt.description`| optional| optional| optional| optional| optional  
`Prompt.arguments`| optional| optional| optional| optional| optional  
`Prompt.icons`| —| —| —| optional| optional  
`Prompt._meta`| —| —| optional| optional| optional  
`PromptArgument.name`| required| required| required| required| required  
`PromptArgument.title`| —| —| optional| optional| optional  
`PromptArgument.description`| optional| optional| optional| optional| optional  
`PromptArgument.required`| optional| optional| optional| optional| optional  
`PromptMessage.role`| required| required| required| required| required  
`PromptMessage.content`| required| required| required| required| required  
Field| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`ListPromptsResult.prompts`| required| required| required| required| required  
`ListPromptsResult.nextCursor`| optional| optional| optional| optional| optional  
`ListPromptsResult.ttlMs`| —| —| —| —| required  
`ListPromptsResult.cacheScope`| —| —| —| —| required  
`ListPromptsResult.resultType`| —| —| —| —| required  
`ListPromptsResult._meta`| optional| optional| optional| optional| optional  
`prompts/get params.name`| required| required| required| required| required  
`prompts/get params.arguments`| optional| optional| optional| optional| optional  
`prompts/get params.inputResponses`| —| —| —| —| optional  
`prompts/get params.requestState`| —| —| —| —| optional  
`GetPromptResult.description`| optional| optional| optional| optional| optional  
`GetPromptResult.messages`| required| required| required| required| required  
`GetPromptResult.resultType`| —| —| —| —| required  
`GetPromptResult._meta`| optional| optional| optional| optional| optional  
`PromptReference.type`| required| required| required| required| required  
`PromptReference.name`| required| required| required| required| required  
`PromptReference.title`| —| —| optional| optional| optional  
  
Which content blocks a prompt message may hold, resolved from `PromptMessage.content`:

Content block| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`text`| ✓| ✓| ✓| ✓| ✓  
`image`| ✓| ✓| ✓| ✓| ✓  
`audio`| —| ✓| ✓| ✓| ✓  
`resource_link`| —| —| ✓| ✓| ✓  
`resource`| ✓| ✓| ✓| ✓| ✓  
  
What the tables say:

  * **Only`name` is required** on a prompt and on an argument. `title` arrived with 2025-06, `icons` with 2025-11. An argument with no `required` is optional.
  * **2026-07 changed the list result.** `ListPromptsResult` now requires `ttlMs`, `cacheScope` and `resultType`. `GetPromptResult` requires only `resultType`: the caching rules list `prompts/list` but not `prompts/get`, so a rendered prompt carries no caching hints.
  * **`prompts/get` gained `inputResponses` and `requestState`** in 2026-07, for the multi round-trip flow (section 4).
  * **Content blocks grew.** `audio` is accepted since 2025-03 and `resource_link` since 2025-06. The 2026-07 prompts page is the first to describe resource links in prose (the rules table in section 5), so a server that sends them is correct against the schema of 2025-06 and later, but a client written to the older page may not expect them.
  * **Roles are`user` and `assistant`** in every revision. There is no `system` role (section 5).



## 4\. Listing, getting and being notified

  * **Capability.** A server that supports prompts **MUST** declare it in its discovery result, for example `{ "capabilities": { "prompts": { "listChanged": true } } }`. `listChanged` is optional.
  * **The list.** `prompts/list` returns the prompts available to the requesting client. The set **MAY** be empty, **MAY** change over time and **MAY** depend on the authorization on the request, but **MUST NOT** vary per connection or as a side effect of other requests. It is paginated: follow `nextCursor`. The result carries `ttlMs` (an integer `>= 0`; `0` means immediately stale) and `cacheScope`. Use `"public"` only for a list that is identical for all users; caches **MUST NOT** be shared across authorization contexts.
  * **Arguments.** Each listed prompt may have `arguments`: a list of `name`, optional `title`, `description` and `required`. In `prompts/get` the client sends `arguments` as an object of string values. The spec says servers **SHOULD** validate prompt arguments before processing, and implementations **MUST** carefully validate all prompt inputs and outputs (last row of the rules table in section 5).
  * **Messages.** The result holds `messages`, each with a `role` and one `content` block. Text is `text`. Images and audio carry base64 `data` and a `mimeType` (both **MUST**). A `resource_link` points to a resource without embedding it. An embedded `resource` holds a `uri` and either `text` or `blob`. Use a link when the client can read the URI itself, an embedded resource when the prompt must bring the data.
  * **More input.** A server **MAY** answer `prompts/get` with an `InputRequiredResult`. The client retries with `inputResponses` and, if the server sent one, `requestState`. See the official [multi round-trip requests](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/) page.
  * **Completion.** A server that declares the `completions` capability can complete prompt arguments: the client sends `completion/complete` with `ref: {"type": "ref/prompt", "name": ...}` and the `argument` name and the value typed so far. At most 100 values come back, and `context.arguments` carries the arguments already chosen. See [Completion](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/completion/).
  * **Change notification.** A server that declared `listChanged` **SHOULD** send `notifications/prompts/list_changed` to clients that opened `subscriptions/listen` with `promptsListChanged: true`. The client lists again.



## 5\. One message, five schemas

Does a message that is valid for one revision survive the others? Each row is validated against all five `schema.json` files. `✓` means valid, `✗` means rejected, `—` means the revision does not define the thing the row is about, so validation says nothing.

Message| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`ListPromptsResult` without `ttlMs`, `cacheScope`, `resultType`| ✓| ✓| ✓| ✓| ✗  
`GetPromptResult` without `resultType`| ✓| ✓| ✓| ✓| ✗  
`GetPromptResult` without `ttlMs` and `cacheScope`| ✓| ✓| ✓| ✓| ✓  
A message with an `audio` content block| ✗| ✓| ✓| ✓| ✓  
A message with a `resource_link` content block| ✗| ✗| ✓| ✓| ✓  
A message with the role `system`| ✗| ✗| ✗| ✗| ✗  
`GetPromptResult` with an empty `messages` array| ✓| ✓| ✓| ✓| ✓  
`prompts/get` request without `params._meta`| ✓| ✓| ✓| ✓| ✗  
`prompts/get` request whose argument value is a number| ✗| ✗| ✗| ✗| ✗  
An `input_required` result returned for `prompts/get`| ✗| ✗| ✗| ✗| ✓  
`Prompt` with `icons`| —| —| —| ✓| ✓  
  
Which messages and rules exist in which revision:

Item| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
`notifications/prompts/list_changed`| ✓| ✓| ✓| ✓| ✓  
`completion/complete` with a `PromptReference`| ✓| ✓| ✓| ✓| ✓  
`subscriptions/listen` request| —| —| —| —| ✓  
`promptsListChanged` filter| —| —| —| —| ✓  
`inputResponses` in `prompts/get`| —| —| —| —| ✓  
Spec text says| `2024-11`| `2025-03`| `2025-06`| `2025-11`| `2026-07`  
---|---|---|---|---|---  
Servers declare the `prompts` capability| ✓| ✓| ✓| ✓| ✓  
Invalid prompt name: `-32602`| ✓| ✓| ✓| ✓| ✓  
Missing required arguments: `-32602`| ✓| ✓| ✓| ✓| ✓  
`prompts/list` MUST NOT vary per connection| —| —| —| —| ✓  
The list MAY vary by the authorization presented| —| —| —| —| ✓  
`prompts/get` may answer with `InputRequiredResult`| —| —| —| —| ✓  
List changes arrive on `subscriptions/listen` (`promptsListChanged`)| —| —| —| —| ✓  
Audio data MUST be base64-encoded| —| ✓| ✓| ✓| ✓  
Prompt messages MAY include links to resources| —| —| —| —| ✓  
Implementations MUST validate all prompt inputs and outputs| ✓| ✓| ✓| ✓| ✓  
  
Reading the matrix:

  * **A 2025-11-25 style result is rejected by 2026-07-28** : the list without `resultType`, `ttlMs` and `cacheScope` and the get result without `resultType` (rows 1 and 2). A get result without caching hints is valid (row 3).
  * **`system` is never valid.** If you port a system prompt, send it as a `user` message. A numeric argument is never valid either; the client stringifies.
  * **An empty`messages` array passes every schema.** Nothing in the spec forbids it, so a client should treat it as "nothing to insert", not as an error.
  * **`prompts/get` without `params._meta` is rejected by 2026-07-28 only.** Every request now carries the protocol version and client information.
  * **The spec text lags the schema** for resource links: the schema allows them from 2025-06, the prompts page describes them from 2026-07 (rules table).



The official examples of the latest revision were validated against their definitions: 14 prompt-related examples in 12 definitions, none invalid.

## 6\. Getting a prompt over Streamable HTTP: the `Mcp-Name` header

Over Streamable HTTP a `prompts/get` request **MUST** carry two headers: `Mcp-Method: prompts/get` and `Mcp-Name` with the value of `params.name`. A server that processes the body **MUST** compare the decoded header with the body and reject a mismatch with HTTP `400` and the JSON-RPC error `-32020` (`HeaderMismatchError`). A request without the header is rejected the same way.

If the name cannot be safely represented as a plain ASCII header value (non-ASCII, control characters, leading or trailing whitespace) or if it itself looks like the escape, the client **MUST** send `=?base64?` \+ Base64 of the UTF-8 bytes + `?=`. The server decodes before it compares. A prompt named `résumé` goes out like this:
    
    
    POST /mcp HTTP/1.1
    Mcp-Method: prompts/get
    Mcp-Name: =?base64?csOpc3Vtw6k=?=

A plain name such as `code_review` is sent as it is. The typical bugs are a client that sends the raw non-ASCII value and a server that compares the header with the body without decoding. The linter probes both (`header-mismatch`, `header-base64`).

## 7\. Errors: what to return and what to expect

For prompts the spec says servers **SHOULD** return standard JSON-RPC errors: `-32602` (Invalid params) for an invalid prompt name and for missing required arguments, `-32603` for internal errors. It is a SHOULD, not a MUST, which is why the linter reports a different code as a WARN and a rendered result as a FAIL.

Situation| What arrives| What to do  
---|---|---  
The prompt name does not exist| Spec: `-32602`. The SDK 2.3.0 answers `-32603` `Internal server error`, HTTP `200` (section 8)| Client: refresh the list and stop retrying; treat `-32603` for a name that is not in the list as not found. Server: return `-32602` if your stack allows it  
A required argument is missing| Spec: `-32602`. The SDK 2.3.0 answers `-32603`, HTTP `200`| Same. Never render the prompt with the argument filled with an empty value or `None`  
An argument value is not a string| `-32602` with `Invalid request parameters`, HTTP `400` (SDK)| Fix the client: stringify the value  
Your own validation fails (an argument value that is not acceptable)| Raise the SDK's `MCPError` with code `INVALID_PARAMS`: `-32602` with your message, HTTP `400`| Write a message that is safe to show: it reaches the client  
The template function crashes| `-32603` `Internal server error`, HTTP `200`; the SDK withholds the exception text| Read the server log; retry with backoff is reasonable  
`name` is missing from the request| `-32602` `Invalid request parameters`, HTTP `400`| Fix the client  
Headers disagree with `name`, or are missing| HTTP `400` and `-32020` (`HeaderMismatchError`)| A client or gateway bug; fix the headers, Base64-encode non-ASCII names  
The server needs more input before it can render| Not an error: a result with `resultType: "input_required"`| Answer the requests and retry with `inputResponses` and `requestState`  
  
Prompt errors are protocol errors: unlike a tool result, a prompt result has no `isError` field.

## 8\. What the official Python SDK 2.3.0 returns

The reference server defines one prompt per message shape: plain text with an optional argument, a three-message conversation, an embedded resource from a closed set of files, a resource link, an image, and one that crashes on purpose. It uses the official SDK (`pip install mcp==2.3.0`). The `add_prompt` tool exists only so that the stream runs can make the list change:

**prompts_ref_server.py**
    
    
     """Official Python SDK (mcp==2.3.0) prompts server at http://127.0.0.1:8231/mcp, no auth.
    
    Prompts: a plain-text template with an optional argument, a multi-message conversation, a prompt that embeds a
    file from `sample-docs/` (a closed set, anything else is an invalid-params error), a prompt that links to a
    resource, a prompt that returns an image, and one that fails on purpose. The `focus` argument of `code_review`
    has a completion handler. The tool `add_prompt` registers one more prompt at run time and announces the change
    to `subscriptions/listen` streams.
    """
    from pathlib import Path
    
    from mcp.server.mcpserver import Context, MCPServer
    from mcp.server.mcpserver.prompts.base import AssistantMessage, Message, UserMessage
    from mcp.server.mcpserver.utilities.types import Image
    from mcp.shared.exceptions import MCPError
    from mcp.types import (Completion, EmbeddedResource, INVALID_PARAMS, ResourceLink, TextResourceContents)
    
    ROOT = Path(__file__).resolve().parent / "sample-docs"
    FILES = ["CHANGELOG.md", "checklist.md"]
    FOCUS = ["correctness", "performance", "security", "style"]
    # A 1x1 transparent PNG.
    PIXEL = bytes.fromhex("89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4890000000d49444154789c636460f80f"
                          "0001870180eb47ba920000000049454e44ae426082")
    
    server = MCPServer("prompts-ref")
    
    
    @server.prompt(title="Code review", description="Ask for a review of a piece of code")
    def code_review(code: str, focus: str = "correctness") -> str:
        return "Please review this code, focusing on %s:\n\n%s" % (focus, code)
    
    
    @server.prompt(title="Debug an error", description="Start a debugging conversation about an error message")
    def debug_error(error: str) -> list[Message]:
        return [UserMessage("I am seeing this error:"), UserMessage(error),
                AssistantMessage("What is the smallest input that reproduces it?")]
    
    
    @server.prompt(title="Review a file", description="Embed one of the sample files and ask for a review")
    def review_file(name: str) -> list[Message]:
        if name not in FILES:
            raise MCPError(code=INVALID_PARAMS, message="unknown file %r, want one of %s" % (name, FILES))
        text = (ROOT / name).read_text(encoding="utf-8")
        embedded = EmbeddedResource(type="resource", resource=TextResourceContents(
            uri="file:///sample-docs/" + name, mime_type="text/markdown", text=text))
        return [UserMessage("Review this file for mistakes:"), UserMessage(embedded)]
    
    
    @server.prompt(title="Release notes", description="Point the model at the release notes resource")
    def release_notes() -> list[Message]:
        link = ResourceLink(type="resource_link", name="release", uri="notes://release", mime_type="text/plain")
        return [UserMessage("Summarize the release notes behind this link:"), UserMessage(link)]
    
    
    @server.prompt(title="Explain the logo", description="Attach the logo as an image")
    def explain_logo() -> list[Message]:
        return [UserMessage("What does this logo show?"), UserMessage(Image(data=PIXEL, format="png"))]
    
    
    @server.prompt(title="Broken", description="Fails on purpose; a crash must not leak its text to the client")
    def broken(secret: str = "x") -> str:
        raise RuntimeError("db password is hunter2")
    
    
    @server.completion()
    async def complete(ref, argument, context):
        if getattr(ref, "type", None) == "ref/prompt" and ref.name == "code_review" and argument.name == "focus":
            return Completion(values=[v for v in FOCUS if v.startswith(argument.value)], total=None, has_more=None)
        return None
    
    
    @server.tool()
    async def add_prompt(name: str, ctx: Context) -> str:
        """Register one more prompt named NAME and announce it to `subscriptions/listen` streams."""
        server.add_prompt(server._prompt_manager.get_prompt("code_review").model_copy(update={"name": name}))
        await ctx.notify_prompts_changed()
        return "added " + name
    
    
    if __name__ == "__main__":
        server.run("streamable-http", port=8231)

Twenty runs were sent over Streamable HTTP in the 2026-07-28 request format. Every response was validated against its definition in the 2026-07-28 `schema.json`, an error also against the definition of its code, and every stream frame against its notification (all twenty are valid; the definition is named at the end of each recorded line):

Run| Request| What the SDK returned| Against the spec  
---|---|---|---  
`list`| `prompts/list`| `ttlMs: 0`, `cacheScope: "private"`, `resultType: "complete"`, 6 prompts| Valid. The SDK fills the required hints with the most conservative values  
`get-text`| `code_review` with the required `code`| One `user` text message with the argument filled in| Valid  
`get-optional`| `code_review` with `code` and `focus`| One `user` text message that uses `focus`| Valid  
`get-conversation`| `debug_error`| Three text messages: `user`, `user`, `assistant`| Valid: a prompt can hold several messages and both roles  
`get-embedded`| `review_file` with `checklist.md`| A text message and an embedded `resource` with `uri`, `mimeType` and `text`| Valid  
`get-link`| `release_notes`| A text message and a `resource_link`| Valid  
`get-image`| `explain_logo`| A text message and an `image` block, `image/png`| Valid  
`unknown-prompt`| a name that is not registered| HTTP `200`, `-32603`, `Internal server error`| A valid `InternalError`, but the spec says `-32602` (SHOULD): the linter warns  
`missing-argument`| `code_review` without `code`| HTTP `200`, `-32603`, `Internal server error`| The same  
`extra-argument`| `code_review` with an unknown argument `bogus`| HTTP `200`, `-32603`| A valid error. The spec says nothing about extra arguments; the SDK rejects them  
`number-argument`| `code` sent as the number 5| HTTP `400`, `-32602`, `Invalid request parameters`| Matches: argument values are strings in every revision  
`bad-file`| `review_file` with `../x`| HTTP `400`, `-32602`, `unknown file '../x'` and the allowed names| Matches: the handler raised `MCPError` with `INVALID_PARAMS`; its message reaches the client  
`crash`| `broken`, whose handler raises `RuntimeError("db password is hunter2")`| HTTP `200`, `-32603`, `Internal server error`| Valid. The exception text is not sent to the client  
`header-mismatch`| `Mcp-Name` set to another name| HTTP `400`, `-32020`, `mcp-name header does not match`| Matches the Streamable HTTP rule  
`missing-name`| `prompts/get` without `name`| HTTP `400`, `-32602`, `Invalid request parameters`| Matches  
`complete-focus`| `completion/complete` for `code_review.focus`, value `p`| `values: ["performance"]`| Valid  
`complete-unknown`| a completion for a prompt that does not exist| `values: []`, no error| Valid: the SDK treats an unknown reference as nothing to complete  
`listen-ack`| `subscriptions/listen` with `promptsListChanged: true`| One frame: the acknowledgement, tagged with the request `id` as `subscriptionId`| Valid against the schema of the acknowledgement notification  
`listen-changed`| The same stream; `add_prompt` registers a prompt| The acknowledgement, then one list-changed notification| Valid  
`list-after`| `prompts/list` again| 7 prompts| Valid: the notification carries no list, the client has to list again  
**Recorded output of the twenty runs**
    
    
     list             HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete prompts=6 | ListPromptsResultResponse valid
    get-text         HTTP 200 result   resultType=complete messages: user text 'Please review this code, focus' | GetPromptResultResponse valid
    get-optional     HTTP 200 result   resultType=complete messages: user text 'Please review this code, focus' | GetPromptResultResponse valid
    get-conversation HTTP 200 result   resultType=complete messages: user text 'I am seeing this error:'; user text 'boom'; assistant text 'What is the smallest input tha' | GetPromptResultResponse valid
    get-embedded     HTTP 200 result   resultType=complete messages: user text 'Review this file for mistakes:'; user resource file:///sample-docs/checklist.md | GetPromptResultResponse valid
    get-link         HTTP 200 result   resultType=complete messages: user text 'Summarize the release notes be'; user resource_link notes://release | GetPromptResultResponse valid
    get-image        HTTP 200 result   resultType=complete messages: user text 'What does this logo show?'; user image image/png | GetPromptResultResponse valid
    unknown-prompt   HTTP 200 error    code -32603 'Internal server error' | JSONRPCErrorResponse+InternalError valid
    missing-argument HTTP 200 error    code -32603 'Internal server error' | JSONRPCErrorResponse+InternalError valid
    extra-argument   HTTP 200 error    code -32603 'Internal server error' | JSONRPCErrorResponse+InternalError valid
    number-argument  HTTP 400 error    code -32602 'Invalid request parameters' | JSONRPCErrorResponse+InvalidParamsError valid
    bad-file         HTTP 400 error    code -32602 "unknown file '../x', want one of ['CHANGELOG.md', 'checklist.md']" | JSONRPCErrorResponse+InvalidParamsError valid
    crash            HTTP 200 error    code -32603 'Internal server error' | JSONRPCErrorResponse+InternalError valid
    header-mismatch  HTTP 400 error    code -32020 "mcp-name header does not match the request body's 'name' parameter" | JSONRPCErrorResponse+HeaderMismatchError valid
    missing-name     HTTP 400 error    code -32602 'Invalid request parameters' | JSONRPCErrorResponse+InvalidParamsError valid
    complete-focus   HTTP 200 result   resultType=complete values=['performance'] | CompleteResultResponse valid
    complete-unknown HTTP 200 result   resultType=complete values=[] | CompleteResultResponse valid
    listen-ack       HTTP 200 stream   ack(promptsListChanged=True) | SubscriptionsAcknowledgedNotification valid
    listen-changed   HTTP 200 stream   ack(promptsListChanged=True) -> list_changed | PromptListChangedNotification+SubscriptionsAcknowledgedNotification valid
    list-after       HTTP 200 result   ttlMs=0 cacheScope=private resultType=complete prompts=7 | ListPromptsResultResponse valid

What the runs say about the SDK:

  * **Unknown prompt and missing argument are`-32603`, not `-32602`.** The SDK checks the name and the required arguments before your function runs and raises an ordinary exception, which the server turns into a generic internal error with HTTP `200`. The spec says `-32602` (SHOULD). A client of this SDK has to tell "not found" from "server fault" by looking at the list.
  * **Your own`MCPError` keeps its code.** Raising `MCPError(code=INVALID_PARAMS, ...)` from the function gives `-32602`, HTTP `400` and your message. Use it for validation of argument values, and keep the text safe to show.
  * **Crashes are generic.** The client never sees the text of an exception raised inside a template function; the cause stays in the server log.
  * **Arguments come from the function signature.** A parameter without a default is listed as `required: true`, one with a default as `required: false`. Values must be strings; anything else is `-32602` before your code runs.
  * **Rich messages work.** A returned list of messages keeps its roles; the SDK's `Image` helper becomes an `image` block; an `EmbeddedResource` or a `ResourceLink` passes through unchanged.
  * **Change announcements are small.** The SDK acknowledges the stream first and then sends `notifications/prompts/list_changed`. The notification carries no list, so the client lists again (`list-after`).



## 9\. Failure modes and recovery

Symptom| Cause| How to detect| Recovery  
---|---|---|---  
A client retries a missing prompt forever, or shows a server fault| The server answers `-32603` for an unknown name (what the SDK does) instead of `-32602`| `unknown-prompt` (WARN)| Client: treat `-32603` for a name that is not in the list as not found. Server: return `-32602` where the stack allows  
A prompt is rendered with an empty or `None` argument| The server does not check required arguments| `missing-argument` (FAIL when a result comes back)| Validate before rendering and answer `-32602`  
A client drops or rejects a message| The role is `system` (or anything but `user` and `assistant`)| `get-messages`| Send system text as a `user` message  
An image or audio block does not display| `data` is not valid base64 or `mimeType` is missing| `get-content`| Encode with standard base64 and state the MIME type  
An embedded resource cannot be used| Both `text` and `blob`, or neither, or an invalid blob| `get-content`| Exactly one of `text` or `blob`, plus the `uri`  
A 2026-07-28 client rejects the list| The result lacks `resultType`, `ttlMs` or `cacheScope` (the 2025-11-25 shape)| `list-envelope`| Add the three fields; `ttlMs: 0` and `"private"` are always valid  
A rendered prompt is rejected| The result lacks `resultType`| `get-envelope`| Add `resultType: "complete"`  
Two clients see different prompt lists| The list depends on connection state. It **MUST NOT** ; only the authorization may change it| `list-stable` (WARN, a heuristic), or list on two connections and diff| Compute the list from the request's authorization only; mark such lists `"private"`  
One user's prompts are served to another from a cache| A list that depends on the user was marked `cacheScope: "public"`, or the cache ignores authorization| Compare `cacheScope` and the list for two tokens| Use `"private"` for user-dependent lists  
The client menu shows stale prompts| `listChanged` is not declared, or nothing listens with `promptsListChanged: true`, or the stream dropped| Check the capability; watch the stream for the acknowledgement| Declare `listChanged`, listen, and list again after a notification or a reconnect  
Every non-ASCII prompt name answers `-32020`| The server compares `Mcp-Name` with the body without decoding the Base64 sentinel, or the client sent the raw value| `header-base64`| Decode before comparing; the client encodes  
Requests through a gateway fail with `-32020` or `400`| The gateway dropped or rewrote `Mcp-Method` or `Mcp-Name`| `header-mismatch`; compare the headers at both ends| Forward the standard headers unchanged  
A completion hangs a UI or is cut| The server returns more than 100 values| `completion-values`| Return at most 100 and set `hasMore`  
A secret appears in a client error message| A handler put a backend message into an `MCPError`| Trigger each failure and read the message| Raise `MCPError` only with text that is safe to show; let crashes stay generic  
  
## 10\. Lint your own prompts endpoint

`lint_prompts.py` talks to a Streamable HTTP endpoint. It lists the prompts, renders up to five of them and sends a few probes that no healthy server may satisfy: an unknown prompt name, a missing required argument, a mismatching `Mcp-Name` and a non-ASCII prompt name. Required arguments are filled with the text `lint-sample`; pass `--arg PROMPT.ARGUMENT=VALUE` to give a real value, and a rejected sample is reported as INFO, not as a defect. Rendering a prompt and asking for a completion change nothing in a healthy server; do not point the linter at an endpoint where they have side effects. It needs only Python 3 and the standard library:

**lint_prompts.py**
    
    
     #!/usr/bin/env python3
    """Lint the prompts of an MCP server against spec 2026-07-28 over Streamable HTTP.
    
    Usage: lint_prompts.py URL [--token T] [--max-gets N] [--arg PROMPT.ARGUMENT=VALUE ...]
    URL: the Streamable HTTP endpoint. The linter lists the prompts, renders up to N of them (default 5) and sends a
    few probes that no healthy server may satisfy: an unknown prompt name, a missing required argument, a mismatching
    `Mcp-Name` header and a non-ASCII prompt name. Required arguments of a listed prompt are filled with the text
    `lint-sample` unless `--arg` gives a real value; a rejected sample value is reported as INFO, not as a defect.
    Rendering a prompt and a completion request change nothing in a healthy server; do not point the linter at an
    endpoint where they have side effects.
    Levels: FAIL = a MUST of the spec is violated, WARN = a SHOULD or a recommendation is not followed.
    Exit code: 0 no FAIL, 1 at least one FAIL, 2 the endpoint cannot be read.
    """
    import argparse
    import base64
    import binascii
    import http.client
    import json
    import sys
    from urllib.parse import urlsplit
    
    VERSION = "2026-07-28"
    SAMPLE = "lint-sample"
    MISSING_PROMPT = "lint-probe-missing-prompt"
    ROLES = ("user", "assistant")
    NAMED_METHODS = ("prompts/get", "tools/call")  # methods whose Mcp-Name header carries params.name
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
        """Build one 2026-07-28 request: (parsed URL, body, headers). `Mcp-Name` is `params.name`; pass `name` to
        send another value."""
        meta = {"io.modelcontextprotocol/protocolVersion": VERSION,
                "io.modelcontextprotocol/clientInfo": {"name": "lint-prompts", "version": "0"},
                "io.modelcontextprotocol/clientCapabilities": {}}
        headers = {"Accept": "application/json, text/event-stream", "Content-Type": "application/json",
                   "MCP-Protocol-Version": VERSION, "Mcp-Method": method}
        source = name if name is not None else (params or {}).get("name")
        if isinstance(source, str) and method in NAMED_METHODS:
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
    
    
    def list_all(url, token):
        """Return (prompts, first result) of the paginated `prompts/list`."""
        items, cursor, first = [], None, None
        for _ in range(50):
            status, msg = rpc(url, "prompts/list", {"cursor": cursor} if cursor else None, token)
            result = (msg or {}).get("result")
            if status != 200 or not isinstance(result, dict) or not isinstance(result.get("prompts"), list):
                raise ValueError("prompts/list failed: HTTP %s, %s" % (status, json.dumps(msg)[:200]))
            items += result["prompts"]
            first = first or result
            cursor = result.get("nextCursor")
            if not cursor:
                return items, first
        raise ValueError("prompts/list still paginating after 50 pages")
    
    
    def envelope_problems(result, caching):
        """Every 2026-07-28 result MUST carry resultType; list results also carry ttlMs >= 0 and cacheScope."""
        problems = []
        if not isinstance(result.get("resultType"), str):
            problems.append("resultType is missing")
        if caching:
            ttl, scope = result.get("ttlMs"), result.get("cacheScope")
            if not isinstance(ttl, int) or isinstance(ttl, bool) or ttl < 0:
                problems.append("ttlMs is %r, want an integer >= 0" % ttl)
            if scope not in ("public", "private"):
                problems.append("cacheScope is %r, want 'public' or 'private'" % scope)
        return problems
    
    
    def decode_blob(blob):
        try:
            base64.b64decode(blob, validate=True)
            return True
        except (binascii.Error, ValueError, TypeError):
            return False
    
    
    def content_problem(block):
        """None when a message content block has the shape of its `type`, else the problem as text."""
        if not isinstance(block, dict):
            return "content is not an object"
        kind = block.get("type")
        if kind == "text":
            return None if isinstance(block.get("text"), str) else "text block without a text string"
        if kind in ("image", "audio"):
            ok = isinstance(block.get("mimeType"), str) and isinstance(block.get("data"), str) \
                and decode_blob(block["data"])
            return None if ok else "%s block needs a mimeType and base64 data" % kind
        if kind == "resource_link":
            ok = isinstance(block.get("uri"), str) and isinstance(block.get("name"), str)
            return None if ok else "resource_link block needs a uri and a name"
        if kind == "resource":
            res = block.get("resource")
            kinds = [k for k in ("text", "blob") if isinstance(res, dict) and isinstance(res.get(k), str)]
            if not isinstance(res, dict) or not isinstance(res.get("uri"), str) or len(kinds) != 1:
                return "embedded resource needs a uri and exactly one of text or blob"
            return None if "blob" not in res or decode_blob(res["blob"]) else "embedded blob is not valid base64"
        return "unknown content type %r" % kind
    
    
    def lint_capability(url, token):
        """Check the `prompts` capability and return the capabilities object ({} when unreadable)."""
        status, msg = rpc(url, "server/discover", None, token)
        result = (msg or {}).get("result")
        caps = result.get("capabilities") if isinstance(result, dict) else None
        caps = caps if isinstance(caps, dict) else {}
        declared = isinstance(caps.get("prompts"), dict)
        report("capability-declared", declared, "the `prompts` capability is %s (server/discover, HTTP %s)"
               % ("declared" if declared else "missing", status))
        if declared:
            print("INFO prompts capability: listChanged=%s; completions %s" % (
                caps["prompts"].get("listChanged", False), "declared" if "completions" in caps else "not declared"))
        return caps
    
    
    def lint_listed(prompts):
        named = [p for p in prompts if isinstance(p, dict) and isinstance(p.get("name"), str) and p["name"]]
        report("prompt-fields", len(named) == len(prompts), "%d of %d prompts have a name" % (len(named), len(prompts)))
        names = [p["name"] for p in named]
        dup = sorted({n for n in names if names.count(n) > 1})
        report("name-unique", not dup, "duplicates: %s" % dup if dup else "no duplicate prompt names")
        bad, usable = [], []
        for p in named:
            args = p.get("arguments", [])
            ok = isinstance(args, list) and all(isinstance(a, dict) and isinstance(a.get("name"), str)
                                                and isinstance(a.get("required", False), bool) for a in args)
            (usable if ok else bad).append(p if ok else p["name"])
        report("argument-fields", not bad, "malformed arguments in %s" % bad if bad
               else "every argument has a name and a boolean `required` when present")
        twice = [p["name"] for p in named if isinstance(p.get("arguments"), list)
                 and len({a.get("name") for a in p["arguments"] if isinstance(a, dict)}) < len(p["arguments"])]
        report("argument-unique", not twice, "repeated argument names in %s" % twice if twice
               else "no prompt repeats an argument name", "WARN")
        bare = [p["name"] for p in named if not isinstance(p.get("description"), str) or not p["description"]]
        report("prompt-description", not bare, "no description: %s" % bare if bare
               else "every listed prompt has a description", "WARN")
        return usable
    
    
    def sample_arguments(prompt, overrides):
        """(arguments, sampled): arguments for `prompts/get`, and whether a required one is a made-up sample."""
        args, sampled = {}, False
        for arg in prompt.get("arguments", []):
            if arg.get("required"):
                key = "%s.%s" % (prompt["name"], arg["name"])
                sampled = sampled or key not in overrides
                args[arg["name"]] = overrides.get(key, SAMPLE)
        return args, sampled
    
    
    def lint_gets(url, prompts, overrides, token, limit):
        """Render each prompt and check the envelope, the messages and every content block."""
        envelope, messages, content, failed, skipped, rendered = [], [], [], [], [], 0
        for prompt in prompts[:limit]:
            args, sampled = sample_arguments(prompt, overrides)
            status, msg = rpc(url, "prompts/get", {"name": prompt["name"], "arguments": args} if args
                              else {"name": prompt["name"]}, token)
            result = msg.get("result") if isinstance(msg, dict) else None
            if not isinstance(result, dict):
                code = ((msg or {}).get("error") or {}).get("code") if isinstance(msg, dict) else None
                (skipped if sampled else failed).append("%s (HTTP %s, code %s)" % (prompt["name"], status, code))
                continue
            rendered += 1
            if envelope_problems(result, False):
                envelope.append(prompt["name"])
            items = result.get("messages")
            if not isinstance(items, list):
                messages.append("%s: messages is not an array" % prompt["name"])
                continue
            for item in items:
                if not isinstance(item, dict) or item.get("role") not in ROLES:
                    messages.append("%s: role %r, want one of %s" % (prompt["name"], (item or {}).get("role")
                                                                     if isinstance(item, dict) else item, list(ROLES)))
                    continue
                problem = content_problem(item.get("content"))
                if problem:
                    content.append("%s: %s" % (prompt["name"], problem))
        report("get-envelope", not envelope, "resultType is missing for %s" % envelope if envelope
               else "%d rendered prompts carry resultType" % rendered)
        report("get-messages", not messages, "; ".join(messages) if messages
               else "messages is an array and every message has the role user or assistant")
        report("get-content", not content, "; ".join(content) if content
               else "every content block has the shape of its type (text, image, audio, resource_link, resource)")
        report("get-succeeds", not failed, "prompts/get failed for %s" % "; ".join(failed) if failed
               else "every prompt that needs no sample value rendered", "WARN")
        if skipped:
            print("INFO sample values were rejected for %s; pass --arg PROMPT.ARGUMENT=VALUE to judge them"
                  % "; ".join(skipped))
    
    
    def probe_error(url, params, token, what):
        """Send a request no healthy server may satisfy. Return (PASS|WARN|FAIL, detail): -32602 passes, another
        error code is a WARN (the spec says SHOULD), a rendered result is a FAIL."""
        status, msg = rpc(url, "prompts/get", params, token)
        if not isinstance(msg, dict):
            return "FAIL", "HTTP %s without a JSON-RPC message for %s" % (status, what)
        error = msg.get("error")
        if isinstance(error, dict):
            code = error.get("code")
            return ("PASS" if code == -32602 else "WARN", "%s answered with code %s (HTTP %s)" % (what, code, status))
        return "FAIL", "%s was answered with a result, so the server rendered something that cannot exist" % what
    
    
    def lint_probes(url, prompts, token):
        level, detail = probe_error(url, {"name": MISSING_PROMPT}, token, "an unknown prompt")
        report("unknown-prompt", level == "PASS", detail, level)
        needy = next((p for p in prompts if any(a.get("required") for a in p.get("arguments", []))), None)
        if needy:
            level, detail = probe_error(url, {"name": needy["name"]}, token, "%s without its required arguments"
                                        % needy["name"])
            report("missing-argument", level == "PASS", detail, level)
        else:
            print("INFO no listed prompt has a required argument, the missing-argument probe is skipped")
        status, msg = rpc(url, "prompts/get", {"name": MISSING_PROMPT}, token, name="lint-probe-other")
        code = ((msg or {}).get("error") or {}).get("code") if isinstance(msg, dict) else None
        report("header-mismatch", status == 400 and code == -32020,
               "a mismatching Mcp-Name was answered with HTTP %s, code %s (want 400, -32020)" % (status, code))
        status, msg = rpc(url, "prompts/get", {"name": "lint-probe-caf\u00e9"}, token)
        code = ((msg or {}).get("error") or {}).get("code") if isinstance(msg, dict) else None
        report("header-base64", code != -32020, "a non-ASCII prompt name sent as a Base64 sentinel was answered with "
               "code %s" % code)
    
    
    def lint_completion(url, prompts, caps, token):
        """Ask for completions of the first argument of the first prompt that has one."""
        target = next(((p, a) for p in prompts for a in p.get("arguments", []) if isinstance(a, dict)), None)
        if "completions" not in caps or not target:
            print("INFO completions are not declared or no prompt has an argument, the completion probe is skipped")
            return
        prompt, arg = target
        status, msg = rpc(url, "completion/complete", {"ref": {"type": "ref/prompt", "name": prompt["name"]},
                                                       "argument": {"name": arg["name"], "value": ""}}, token)
        values = (((msg or {}).get("result") or {}).get("completion") or {}).get("values") if isinstance(msg, dict) \
            else None
        ok = isinstance(values, list) and len(values) <= 100 and all(isinstance(v, str) for v in values)
        report("completion-values", ok, "%s.%s answered with %d string values (HTTP %s)" % (
            prompt["name"], arg["name"], len(values), status) if ok else
            "completion for %s.%s is not an array of at most 100 strings (HTTP %s)" % (prompt["name"], arg["name"],
                                                                                        status))
    
    
    def parse_overrides(items, ap):
        overrides = {}
        for item in items:
            key, sep, value = item.partition("=")
            if not sep or "." not in key:
                ap.error("--arg wants PROMPT.ARGUMENT=VALUE, got %r" % item)
            overrides[key] = value
        return overrides
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("url")
        ap.add_argument("--token", help="bearer token for the endpoint")
        ap.add_argument("--max-gets", type=int, default=5, help="how many listed prompts to render")
        ap.add_argument("--arg", action="append", default=[], metavar="PROMPT.ARGUMENT=VALUE",
                        help="a real value for a required argument (repeatable)")
        args = ap.parse_args()
        if not args.url.startswith(("http://", "https://")):
            ap.error("URL must start with http:// or https://")
        overrides = parse_overrides(args.arg, ap)
        try:
            prompts, listing = list_all(args.url, args.token)
            print("INFO %d prompts" % len(prompts))
            caps = lint_capability(args.url, args.token)
            problems = envelope_problems(listing, True)
            report("list-envelope", not problems, "; ".join(problems) if problems else
                   "resultType=%s ttlMs=%d cacheScope=%s" % (listing["resultType"], listing["ttlMs"],
                                                             listing["cacheScope"]))
            named = lint_listed(prompts)
            if named:
                lint_gets(args.url, named, overrides, args.token, args.max_gets)
            else:
                print("INFO no listed prompts, the render checks are skipped")
            lint_probes(args.url, named, args.token)
            lint_completion(args.url, named, caps, args.token)
            again, _ = list_all(args.url, args.token)
            before = sorted(str(p.get("name")) for p in prompts if isinstance(p, dict))
            after = sorted(str(p.get("name")) for p in again if isinstance(p, dict))
            report("list-stable", before == after, "the set of prompts differs between two lists taken one after "
                   "the other (legitimate only if it changed in between)" if before != after
                   else "two consecutive lists return the same prompts", "WARN")
        except (OSError, ValueError, http.client.HTTPException) as exc:
            print("ERROR %s" % exc)
            return 2
        print("%d pass, %d warn, %d fail" % (counts["PASS"], counts["WARN"], counts["FAIL"]))
        return 1 if counts["FAIL"] else 0
    
    
    if __name__ == "__main__":
        sys.exit(main())
    
    
    python3 lint_prompts.py http://127.0.0.1:8231/mcp --arg review_file.name=checklist.md
    python3 lint_prompts.py https://example.com/mcp --token "$TOKEN" --max-gets 10

`FAIL` means a MUST is violated; `WARN` means a SHOULD or a recommendation is not followed. Exit code 0 means no FAIL, 1 at least one FAIL, 2 means the endpoint could not be read, which includes a list that is still paginating after 50 pages.

Check| Level| Rule  
---|---|---  
`capability-declared`| FAIL| `server/discover` declares the `prompts` capability  
`list-envelope`| FAIL| The `prompts/list` result carries `resultType`, an integer `ttlMs` `>= 0` and a `cacheScope` of `public` or `private`  
`prompt-fields`| FAIL| Every listed prompt has a non-empty string `name`  
`name-unique`| FAIL| Prompt names are unique  
`argument-fields`| FAIL| Every argument has a string `name`, and a boolean `required` when present  
`argument-unique`| WARN| A prompt does not repeat an argument name  
`prompt-description`| WARN| Every listed prompt has a description  
`get-envelope`| FAIL| Each rendered result carries `resultType`  
`get-messages`| FAIL| `messages` is an array and every message has the role `user` or `assistant`  
`get-content`| FAIL| Each content block has the shape of its type: `text` has a string, `image` and `audio` have a `mimeType` and base64 `data`, `resource_link` has a `uri` and a `name`, `resource` has a `uri` and exactly one of `text` or `blob` (valid base64)  
`get-succeeds`| WARN| A prompt that needs no sample value renders without an error  
`unknown-prompt`| FAIL| An unknown name is answered with `-32602`; another error code is a WARN, a rendered result is a FAIL  
`missing-argument`| FAIL| A prompt without its required arguments is answered with `-32602`; another error code is a WARN, a rendered result is a FAIL (skipped when no prompt has a required argument)  
`header-mismatch`| FAIL| A `prompts/get` whose `Mcp-Name` differs from `name` is answered with HTTP `400` and `-32020`  
`header-base64`| FAIL| A non-ASCII prompt name sent as a Base64 sentinel is not rejected with `-32020`  
`completion-values`| FAIL| When `completions` is declared, a completion for the first argument of the first prompt is an array of at most 100 strings (skipped otherwise)  
`list-stable`| WARN| Two consecutive lists return the same prompts. A server may legitimately change its list between them  
  
Recorded output against the SDK server of section 8:
    
    
    INFO 6 prompts
    PASS capability-declared: the `prompts` capability is declared (server/discover, HTTP 200)
    INFO prompts capability: listChanged=True; completions declared
    PASS list-envelope: resultType=complete ttlMs=0 cacheScope=private
    PASS prompt-fields: 6 of 6 prompts have a name
    PASS name-unique: no duplicate prompt names
    PASS argument-fields: every argument has a name and a boolean `required` when present
    PASS argument-unique: no prompt repeats an argument name
    PASS prompt-description: every listed prompt has a description
    PASS get-envelope: 5 rendered prompts carry resultType
    PASS get-messages: messages is an array and every message has the role user or assistant
    PASS get-content: every content block has the shape of its type (text, image, audio, resource_link, resource)
    PASS get-succeeds: every prompt that needs no sample value rendered
    WARN unknown-prompt: an unknown prompt answered with code -32603 (HTTP 200)
    WARN missing-argument: code_review without its required arguments answered with code -32603 (HTTP 200)
    PASS header-mismatch: a mismatching Mcp-Name was answered with HTTP 400, code -32020 (want 400, -32020)
    PASS header-base64: a non-ASCII prompt name sent as a Base64 sentinel was answered with code -32603
    PASS completion-values: code_review.code answered with 0 string values (HTTP 200)
    PASS list-stable: two consecutive lists return the same prompts
    15 pass, 2 warn, 0 fail

The linter was also run against a stub endpoint that breaks exactly one rule at a time. Each defect is named by a check in the table: no `prompts` capability, results in the 2025-11-25 shape, a prompt without a name or with duplicate names, an argument without a name or a repeated argument, prompts without descriptions, the role `system`, a text block without text and an image block without data, a blob that is not base64, an unknown prompt or a missing argument that is rendered instead of rejected, `-32603` instead of `-32602`, a prompt that cannot be rendered with sample values, a header that is never compared or not decoded, a list that grows between two calls, a list whose `nextCursor` never ends (exit code 2), a completion with 101 values, a body that is not JSON, and an empty list (which the spec allows and the linter reports without a defect). A defect-free stub passes with no warning.

## 11\. Before you ship a prompt

  * The `prompts` capability is declared; `listChanged` only if you really announce changes.
  * `prompts/list` is the same for every connection (it may depend on authorization only), carries `ttlMs` and `cacheScope`, and user-dependent lists are `"private"`.
  * Every prompt has a unique `name`, a `title` and a `description`; every argument has a `name`, and `required` where it matters.
  * Arguments are strings; required ones are checked before rendering, and a missing one is `-32602`, never an empty value.
  * Messages use the roles `user` and `assistant` only; images and audio are base64 with a `mimeType`; an embedded resource has a `uri` and exactly one of `text` or `blob`.
  * Errors that reach the client carry no secrets; crashes are logged on the server.
  * The server reads `Mcp-Name`, decodes the Base64 sentinel and rejects a mismatch with `-32020`.
  * Completion, if offered, returns at most 100 values.
  * The linter passes on your endpoint; re-run it after changing the SDK, the gateway or the revision you serve.



## Versions and Verification

The tables are generated from the official `schema.json` files, the official examples are validated against them, and the runtime behavior comes from running the official Python SDK 2.3.0 (`mcp==2.3.0`). Spec wording and schemas are read from one pinned commit of the official repository (`dae694f6`, 2026-07-28 revision and the four before it). The tables were generated and checked with `jsonschema` 4.26.0, using the draft-07 validator for the revisions whose schema declares draft-07 and the 2020-12 validator for the others. The SDK runs used `mcp==2.3.0` on Python 3.14 (macOS). A change in the official text or in the SDK needs a re-run.

### Sources

  * The official 2026-07-28 pages: [Prompts](https://modelcontextprotocol.info/specification/2026-07-28/server/prompts/), [Completion](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/completion/), [Caching](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/caching/), [Pagination](https://modelcontextprotocol.info/specification/2026-07-28/server/utilities/pagination/), [Subscriptions](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/subscriptions/), [Multi round-trip requests](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/mrtr/), [Streamable HTTP, standard request headers](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/)
  * The `schema.json` of each revision and the official examples in the [official repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
  * This site's [MCP resources explained](https://modelcontextprotocol.info/docs/concepts/resources/), [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/), [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/) and [MCP Inspector](https://modelcontextprotocol.info/tools/inspector/)



[MCP Architecture: Hosts, Clients, Servers and the Connect Phase](https://modelcontextprotocol.info/docs/concepts/architecture/ "MCP Architecture: Hosts, Clients, Servers and the Connect Phase")[MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors](https://modelcontextprotocol.info/docs/concepts/resources/ "MCP Resources Explained: URIs, Templates, Reads, Subscriptions and Errors")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
