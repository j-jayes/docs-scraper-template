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

    * [MCP Tutorials: From Concept to Production](https://modelcontextprotocol.info/docs/tutorials/)
    * [Give a Specialized Agent Ticket Access over MCP: Resources, Controlled Tools and Failure Recovery](https://modelcontextprotocol.info/docs/tutorials/a2a-mcp-tool-access/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/tutorials/a2a-mcp-tool-access/)
  * [简体中文](https://mcpcn.com/docs/tutorials/a2a-mcp-tool-access/)



  * Light 

  * Dark 

  * System 




On this page

  * What you will have at the end
  * Decide what becomes a resource and what becomes a tool
  * Server: one resource, one controlled tool
  * Client: connect, list, call — and what you should see
  * When the server runs remotely: scopes and the token audience
  * Failures: classify, then recover
  * Verify your own deployment
  * Scope of this page and the A2A half



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Tutorials: From Concept to Production](https://modelcontextprotocol.info/docs/tutorials/)

Give a Specialized Agent Ticket Access over MCP: Resources, Controlled Tools and Failure Recovery

# Give a Specialized Agent Ticket Access over MCP: Resources, Controlled Tools and Failure Recovery

A coordination agent hands a ticket-analysis job to a specialized agent. This page builds the MCP half of that handoff: a ticket server that exposes data as a **resource** and actions as **narrowly scoped tools** , and the client calls the specialized agent runs. The A2A half — how the coordination agent discovers the specialist, tracks the task, and receives the result — is a separate concern covered by the A2A guides on [a2acn.com](https://a2acn.com/); this page links to it only where the boundary matters.

The server and client code below was checked against protocol revision 2026-07-28 and run end to end over stdio with Python SDK `mcp==2.3.0` on 2026-10-28. The remote HTTP authorization guidance follows the cited specification; this run did not exercise controlled 401/403 or token-audience cases.

## What you will have at the end

Capability| How it is exposed| Who may call it  
---|---|---  
Read one ticket (subject, severity, customer report)| Resource `tickets://{ticket_id}`| Any caller that can reach the server  
Append an internal note| Tool `add_internal_note`| Callers whose token carries `tickets:notes` (remote) or the local process owner (stdio)  
Reassign or close a ticket| **Not exposed.** High-risk actions stay in the ticketing UI.| —  
  
The last row is the point of this tutorial: a specialized agent gets exactly the access its job needs, and nothing wider.

## Decide what becomes a resource and what becomes a tool

Before writing code, classify each capability. The reader question differs:

Reader question| Primitive| Why  
---|---|---  
"What does ticket 481 say?"| Resource| Reading structured data; the client fetches it on demand, and subscriptions can push updates when it changes  
"Add this finding to the ticket"| Tool| A side effect the model must not trigger accidentally; it needs a schema, a description, and a permission decision  
"What should I do next?"| Neither — the agent's own reasoning| Not the server's job  
  
Use this table as a gate: if you cannot name the reader question and the permission, the capability does not belong on the MCP server.

## Server: one resource, one controlled tool

Install the server the same way the official tutorials do:
    
    
    uv add "mcp==2.3.0"

`ticket_server.py` — the resource returns anticipated failures as `ResourceError`, and the tool validates its input before any effect:
    
    
    import json
    
    from mcp.server import MCPServer
    from mcp.server.mcpserver.exceptions import ResourceError
    
    server = MCPServer("ticket-bridge")
    
    # Stands in for your ticketing system's API. The server never edits
    # TICKETS except through add_internal_note.
    TICKETS = {
        "481": {"subject": "Checkout fails on Safari", "severity": 2,
                "report": "Customer reports the pay button does nothing on Safari 17.",
                "notes": []},
    }
    
    
    @server.resource("tickets://{ticket_id}", name="ticket",
                     description="One support ticket: subject, severity, report, notes")
    def ticket(ticket_id: str) -> str:
        record = TICKETS.get(ticket_id)
        if record is None:
            # An anticipated failure: the client sees this message as-is.
            raise ResourceError(f"no ticket {ticket_id}")
        return json.dumps(record, ensure_ascii=False)
    
    
    @server.tool()
    def add_internal_note(ticket_id: str, note: str) -> str:
        """Append an internal note to a ticket. Staff-visible only.
    
        Args:
            ticket_id: Ticket identifier, e.g. "481".
            note: One or two sentences the next reader can act on.
        """
        record = TICKETS.get(ticket_id)
        if record is None:
            raise ResourceError(f"no ticket {ticket_id}")
        if len(note) > 500:
            raise ResourceError("note too long; keep it under 500 characters")
        record["notes"].append(note)
        return f"note added to {ticket_id}; {len(record['notes'])} total"
    
    
    if __name__ == "__main__":
        server.run("stdio")

Two deliberate choices:

  * `add_internal_note` never reassigns or closes a ticket. Scope is the cheapest security control there is: a capability that is not on the server cannot be abused.
  * The tool checks its input (ticket exists, note length) **before** mutating state, so a rejected call leaves the ticket untouched and can be retried with corrected input.



## Client: connect, list, call — and what you should see

The specialized agent embeds an MCP client. The connection lifecycle is one `async with` block: entering it launches the server subprocess and agrees a protocol version; leaving it shuts the server down.
    
    
    import asyncio
    import os
    
    from mcp import Client, StdioServerParameters
    from mcp.client.stdio import stdio_client
    from mcp_types import TextContent
    
    
    async def main() -> None:
        params = StdioServerParameters(
            command="python",
            args=["ticket_server.py"],
            # A read-only staff token from the environment, never hard-coded.
            env={"TICKET_API_TOKEN": os.environ["TICKET_API_TOKEN"]},
        )
        async with Client(stdio_client(params)) as client:
            tools = await client.list_tools()
            print([t.name for t in tools.tools])  # ['add_internal_note']
    
            result = await client.call_tool(
                "add_internal_note",
                {"ticket_id": "481", "note": "Reproduced on Safari 17; console shows a TypeError."},
            )
            texts = [b.text for b in result.content if isinstance(b, TextContent)]
            print(result.is_error, texts)  # False ['note added to 481; 1 total']
    
    
    asyncio.run(main())

Expected observations, in order: the tool list contains exactly one tool; the successful call returns `is_error=False` with one text block; and the ticket's `notes` now holds your sentence (read the resource to confirm). If `list_tools` shows a tool you did not expect, stop and re-check the server — the client is about to have more authority than you designed.

## When the server runs remotely: scopes and the token audience

Over stdio on one machine, the boundary above is the process owner. Over Streamable HTTP, the same server is a resource server under OAuth 2.1, and the boundary becomes the token:

  * On the first unauthorized request the server answers `401` with a `WWW-Authenticate` header pointing at its Protected Resource Metadata, and the client runs the standard discovery and PKCE flow (see [Authorization with OAuth 2.1](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/)).
  * Give the note tool its own scope and check it, so a token meant for reading cannot write:

Token scope| `tickets://{id}` resource| `add_internal_note`  
---|---|---  
`tickets:read`| yes| no  
`tickets:read tickets:notes`| yes| yes  
  
  * Validate the **audience** , not just the signature. A token minted for a different API that happens to validate here is the token-passthrough problem; the authorization tutorial shows how the audience is embedded in the token and checked server-side.



Local stdio deployment keeps the simpler rule from the official security pages: read credentials from the environment, bind local HTTP servers to `127.0.0.1`, and do not run the browser-based OAuth flow for a single-user local tool.

## Failures: classify, then recover

The three failure families behave differently, and mixing them up is the most common bug in agent loops:

What you see| Family| Meaning| Recovery  
---|---|---|---  
`is_error=True` in a normal `CallToolResult`| Tool failure| Your tool ran and rejected the request (`ResourceError` and friends); the session stays up| Read the message, correct the input, call again — this is the intended path  
JSON-RPC error, e.g. `-32601` method not found| Protocol error| The call never reached your tool: wrong name, or server and client disagree on revision| Fix the name or the negotiated version; retrying the same call unchanged cannot succeed  
Connection-level error (session dropped)| Transport failure| The server process or the stream died| Reconnect with a fresh `async with`; treat the last call's effect as **unknown** — check the ticket before retrying, or make the tool idempotent  
`401` after working before| Authorization| Token expired, or was issued for the wrong audience| Refresh per the RFC 9728 metadata; a wrong-audience token is a configuration error, not something to retry  
Empty message on a crashing tool| SDK containment| An uncaught exception inside a tool; the SDK withholds internal details (stack, secrets) from the client| Fix the server; the withheld text never reaches the model  
  
The last row is worth internalizing: raise `ResourceError` for failures the model can act on, and let anything else crash — the SDK's containment decides what the client learns. The [resources concept page](https://modelcontextprotocol.info/docs/concepts/resources/) demonstrates both behaviors on purpose.

## Verify your own deployment

The checks below run the server and client above end to end; each asserts one observation from this page:

  1. `list_tools` returns exactly `add_internal_note`.
  2. Calling it with a valid ticket returns `is_error=False` and the note count.
  3. Calling it with an unknown ticket returns `is_error=True` with the `no ticket` message, and the session accepts a subsequent valid call.
  4. A note over 500 characters is rejected and the ticket is unchanged.



The scenario scripts and the page assertions live in the site's check suite under `a2a-handoff-check/`; run them against your own server by swapping in your command and parameters.

The recorded run on 2026-10-28 passed all four stdio scenarios with `mcp==2.3.0`. It does not validate the remote HTTP authorization behavior described above; use a controlled resource server and both accepted and rejected tokens for that boundary.

## Scope of this page and the A2A half

This page owns the MCP side only: resources, controlled tools, scopes, audience, and the failure families above. The A2A half of the handoff — advertising the specialized agent, sending it the task, tracking task state, and exchanging messages and artifacts — uses a different protocol and has its own failure modes; see the A2A guides on [a2acn.com](https://a2acn.com/).

Sources, checked 2026-10-27 against the pinned upstream revision `dae694f6`:

  * [Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/) and [Resources](https://modelcontextprotocol.info/specification/2026-07-28/server/resources/) in the 2026-07-28 specification
  * [Build a server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/), [Build a client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/) — SDK patterns used above
  * [Authorization with OAuth 2.1](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/), [Local server security defaults](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/) — scopes, audience, stdio rules
  * [Resources concept and error containment](https://modelcontextprotocol.info/docs/concepts/resources/)



[Writing Effective MCP Tools: Names, Descriptions and Schemas](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/ "Writing Effective MCP Tools: Names, Descriptions and Schemas")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
