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

    * [MCP Docs](https://modelcontextprotocol.info/docs/)
    * [MCP Clients: What Each One Supports and How to Confirm What a Client Declares](https://modelcontextprotocol.info/docs/clients/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/clients/)
  * [简体中文](https://mcpcn.com/docs/clients/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. What “supports MCP” can mean
  * 2\. What each vendor’s page says
  * 3\. The vendors’ wording
  * 4\. What a client declares, revision by revision
  * 5\. A probe server that records the declaration
  * 6\. Run results
  * The official Python SDK
  * Claude Code 2.1.292
  * 7\. Reading the log
  * 8\. Failure modes
  * 9\. Add or re-check a row
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

MCP Clients: What Each One Supports and How to Confirm What a Client Declares

# MCP Clients: What Each One Supports and How to Confirm What a Client Declares

Vendor documentation and capability measurements here are dated **2026-10-26** , not a continuously certified compatibility list. Rerun the embedded probe after upgrading a client. Distinguish specification capabilities, vendor wording and observed declarations; a declaration alone does not validate UI or tool execution.

Before a server relies on a client, confirm three things: which tools, resources and prompts the client puts in front of its users; whether it answers server-initiated roots, sampling and elicitation requests; and which protocol revision it speaks. The tables list only capabilities stated by each vendor; an empty cell means the page is silent. To confirm what the client in front of you actually declares, run the probe server in section 5.

For the lifecycle and the messages that these declarations take part in, read [the learning path](https://modelcontextprotocol.info/docs/learning-path/) and [MCP architecture](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/). For what a server offers, read [tools](https://modelcontextprotocol.info/docs/concepts/tools/), [resources](https://modelcontextprotocol.info/docs/concepts/resources/) and [prompts](https://modelcontextprotocol.info/docs/concepts/prompts/).

## 1\. What "supports MCP" can mean

Three different things hide behind the phrase. Only the second and third are visible in the protocol.

Layer| What the client does| Where it is declared| How a server finds out  
---|---|---|---  
Primitives| Calls `tools/list`, `resources/list` and `prompts/list` and shows or uses the results| Nowhere: tools, resources and prompts are server capabilities, and a client has no capability named after them| By the calls that arrive, or from the vendor's documentation  
Client capabilities| Answers requests that the server starts: `roots/list`, sampling, elicitation (and `tasks` or `extensions` in some revisions)| `ClientCapabilities`: in `initialize` up to 2025-11-25, in the `_meta` of every request in 2026-07-28| By reading the declaration (section 4)  
Revision| Speaks one or more protocol revisions| The `MCP-Protocol-Version` header, and `initialize` or `server/discover`| From the first requests of a connection (section 6)  
  
The rule that makes the declaration worth reading: in 2025-11-25 both sides "Only use capabilities that were successfully negotiated", and in 2026-07-28 a server "MUST NOT rely on capabilities the client has not declared". If it needs one, it returns a `MissingRequiredClientCapabilityError` (`-32021`) with HTTP status 400. Because tools, resources and prompts carry no declaration, the matrix in section 2 rests on what vendors write, and section 5 shows how to measure the rest.

## 2\. What each vendor's page says

A ✓ means that the vendor's own documentation states the feature; the number in brackets is the row of the wording table in section 3. An empty cell means the page does not say. It does not mean the client lacks the feature. Clients that were previously listed without a source are not carried over.

Client| Tools| Resources| Prompts| Roots| Sampling| Elicitation| Revision named  
---|---|---|---|---|---|---|---  
Claude Code| ✓ (1)| ✓ (2)| ✓ (3)| ✓ (4)| | ✓ (5)| 2026-07-28 (6)  
Cursor| ✓ (7)| ✓ (8)| ✓ (9)| ✓ (10)| | ✓ (11)|   
VS Code| ✓ (12)| ✓ (13)| ✓ (14)| ✓ (15)| ✓ (16)| ✓ (17)|   
Zed| ✓ (18)| | ✓ (18)| | | |   
Gemini CLI| ✓ (19)| ✓ (20)| ✓ (21)| | | |   
  
  * All five clients state tools. Zed alone leaves resources empty: its page names "Tools and Prompts" only (18).
  * Sampling is stated by VS Code only (16). Section 6 shows that Claude Code 2.1.292 does not declare it either, which agrees with its empty cell.
  * Roots and elicitation are stated together by Claude Code, Cursor and VS Code, and by nobody else in this table.
  * Only Claude Code names a protocol revision, 2026-07-28 (6). For the others the page is silent, so read what they send (section 6).



The pages that were read:

Client| Page read| Retrieved  
---|---|---  
Claude Code| [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)| 2026-10-26  
Cursor| [cursor.com/docs/mcp](https://cursor.com/docs/mcp)| 2026-10-26  
VS Code| [code.visualstudio.com/api/extension-guides/ai/mcp](https://code.visualstudio.com/api/extension-guides/ai/mcp)| 2026-10-26  
Zed| [zed.dev/docs/ai/mcp](https://zed.dev/docs/ai/mcp)| 2026-10-26  
Gemini CLI| [geminicli.com/docs/tools/mcp-server/](https://geminicli.com/docs/tools/mcp-server/)| 2026-10-26  
  
## 3\. The vendors' wording

Every quote below was fetched from its page and found there on 2026-10-26. Row `c1` is not a matrix cell: it is a limit on one, used in section 8.

#| Client| Covers| What the vendor's page says  
---|---|---|---  
1| Claude Code| Tools| "MCP servers give Claude Code access to your tools, databases, and APIs."  
2| Claude Code| Resources| "MCP servers can expose resources that you can reference using @ mentions"  
3| Claude Code| Prompts| "MCP servers can expose prompts that become available as commands in Claude Code."  
4| Claude Code| Roots| "Claude Code answers roots/list with the session's launch directory"  
5| Claude Code| Elicitation| "MCP servers can request structured input from you mid-task using elicitation."  
6| Claude Code| Revision| "which adds MCP protocol revision 2026-07-28"  
7| Cursor| Tools| "Tools Supported Functions for the AI model to execute"  
8| Cursor| Resources| "Resources Supported Structured data sources that can be read and referenced"  
9| Cursor| Prompts| "Prompts Supported Templated messages and workflows for users"  
10| Cursor| Roots| "Roots Supported Server-initiated inquiries into URI or filesystem boundaries"  
11| Cursor| Elicitation| "Elicitation Supported Server-initiated requests for additional information from users"  
12| VS Code| Tools| "Tools: extend agent mode with extra tools"  
13| VS Code| Resources| "Resources: provide data and content that users can add as chat context or interact with directly in VS Code"  
14| VS Code| Prompts| "Prompts: add reusable prompts as slash commands in chat"  
15| VS Code| Roots| "Roots: provide information about the user's workspace root folder(s)"  
16| VS Code| Sampling| "Sampling: make language model requests using the user's configured models and subscription"  
17| VS Code| Elicitation| "Elicitation: request input from the user"  
18| Zed| Tools, Prompts| "Zed currently supports MCP's Tools and Prompts features."  
19| Gemini CLI| Tools| "An MCP server is an application that exposes tools and resources to the Gemini CLI"  
20| Gemini CLI| Resources| "Gemini CLI discovers these automatically and gives you the possibility to reference them in the chat."  
21| Gemini CLI| Prompts| "MCP servers can expose predefined prompts that can be executed as slash commands within Gemini CLI."  
c1| Claude Code| Limit| "elicitation/create is served only in interactive terminal sessions, and roots/list everywhere"  
  
## 4\. What a client declares, revision by revision

`ClientCapabilities` is the one place where a client says what it will answer. The table is computed from `schema/<revision>/schema.json` at the pinned commit; ✓ lists the sub-fields that the revision's schema defines, and — means the capability does not exist in that revision.

Capability| 2024-11-05| 2025-03-26| 2025-06-18| 2025-11-25| 2026-07-28  
---|---|---|---|---|---  
`roots`| ✓ (`listChanged`)| ✓ (`listChanged`)| ✓ (`listChanged`)| ✓ (`listChanged`)| ✓  
`sampling`| ✓| ✓| ✓| ✓ (`context`, `tools`)| ✓ (`context`, `tools`)  
`elicitation`| —| —| ✓| ✓ (`form`, `url`)| ✓ (`form`, `url`)  
`tasks`| —| —| —| ✓ (`cancel`, `list`, `requests`)| —  
`extensions`| —| —| —| —| ✓  
`experimental`| ✓| ✓| ✓| ✓| ✓  
  
  * **Where it travels.** Up to 2025-11-25 the client declares once, in `initialize`. In 2026-07-28 it puts the declaration in `_meta.io.modelcontextprotocol/clientCapabilities` on every request, and a client that supports roots "MUST declare the `roots` capability" there on each request. There is no `initialize` in that revision; see [the learning path](https://modelcontextprotocol.info/docs/learning-path/).
  * **Elicitation modes.** For backward compatibility an empty `elicitation` object means form mode only. A server MUST NOT send an elicitation request in a mode the client has not declared (2025-11-25).
  * **Sampling sub-capabilities (2025-11-25).** A server MUST NOT send tool-enabled sampling requests unless the client declared `sampling.tools`, and SHOULD NOT use `includeContext` values `thisServer` or `allServers` unless it declared `sampling.context`.
  * **Roots in 2026-07-28.** The request is delivered inside an `InputRequiredResult`, in `inputRequests`. The schema now defines `roots` as an object without fields.
  * **`tasks`** is a client capability in 2025-11-25 only. In 2026-07-28 it is no longer part of the core protocol.
  * **Deprecation (2026-07-28).** Roots and sampling are deprecated by SEP-2577. They remain in the specification, but new implementations SHOULD NOT adopt them; elicitation is not deprecated. Design a new server so that it also works with a client that declares neither roots nor sampling.



## 5\. A probe server that records the declaration

The probe is a standard-library HTTP server. It answers just enough protocol for a client to connect, offers empty tool, resource and prompt lists so that a client has a reason to ask for them, and prints one JSON line per request: the method, the protocol revision, the client's name and version, and the capabilities it declares. It issues no session id, so run one client at a time.
    
    
    python3 client_probe_server.py --era modern --port 8240   # server/discover answered, initialize refused
    python3 client_probe_server.py --era legacy --port 8240   # initialize answered, server/discover refused

Point the client at `http://127.0.0.1:8240/mcp` by adding it as a remote HTTP server in the client's own MCP settings. For Claude Code that is `claude mcp add --transport http probe http://127.0.0.1:8240/mcp`. A client that speaks both eras probes `server/discover` first and falls back to `initialize`, so the legacy probe shows the legacy declaration of any such client; a legacy-only client is refused by the modern probe, which tells you its era. A hosted client cannot reach `127.0.0.1`; use a tunnel for it, and stop the probe when you are done.

**client_probe_server.py**
    
    
     #!/usr/bin/env python3
    """Probe MCP server: record what a connecting client says about itself and which list methods it calls.
    
    Usage: client_probe_server.py [--era modern|legacy] [--port 8240]
    Point a client at http://127.0.0.1:8240/mcp. Every POST prints one JSON line:
      method, protocol (the MCP-Protocol-Version header, or the version the client offers in `initialize`),
      version (the protocolVersion in the `_meta` of a modern request), client (name and version),
      capabilities (what the client declares: roots, sampling, elicitation, ...).
    `--era modern` answers `server/discover` (revision 2026-07-28; a client names itself in the `_meta` of every
    request) and refuses `initialize`. `--era legacy` refuses `server/discover` and answers `initialize` (a client names
    itself once, in the handshake). The server offers empty tool, resource and prompt lists, so a client that wants
    any of the three has a reason to ask. Standard library only.
    """
    import argparse
    import json
    import sys
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    
    PREFIX = "io.modelcontextprotocol/"
    MODERN = "2026-07-28"
    LEGACY = ["2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05"]
    CAPABILITIES = {"tools": {}, "resources": {}, "prompts": {}}
    LISTS = {"tools/list": "tools", "resources/list": "resources", "prompts/list": "prompts"}
    
    
    def make_handler(era, log):
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):  # keep stdout for the records
                pass
    
            def reply(self, status, body=None):
                data = json.dumps(body).encode() if body is not None else b""
                self.send_response(status)
                if body is not None:
                    self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
    
            def do_GET(self):  # no server-initiated stream: the spec allows 405
                self.reply(405)
    
            do_DELETE = do_GET
    
            def do_POST(self):
                try:
                    msg = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
                    method, params = msg["method"], msg.get("params") or {}
                except (ValueError, KeyError, TypeError):
                    return self.reply(400, {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "bad request"}})
                meta = params.get("_meta") or {}
                entry = {"method": method, "protocol": self.headers.get("MCP-Protocol-Version") or params.get("protocolVersion"),
                         "version": meta.get(PREFIX + "protocolVersion"),
                         "client": meta.get(PREFIX + "clientInfo") or params.get("clientInfo"),
                         "capabilities": meta.get(PREFIX + "clientCapabilities", params.get("capabilities"))}
                log({k: v for k, v in entry.items() if v is not None})
                if "id" not in msg:  # a notification gets no body
                    return self.reply(202)
                result, error = None, None
                if method == "server/discover" and era == "modern":
                    result = {"resultType": "complete", "supportedVersions": [MODERN], "capabilities": CAPABILITIES,
                              "ttlMs": 0, "cacheScope": "private"}
                elif method == "initialize" and era == "legacy":
                    offered = params.get("protocolVersion")
                    result = {"protocolVersion": offered if offered in LEGACY else LEGACY[0], "capabilities": CAPABILITIES,
                              "serverInfo": {"name": "client-probe", "version": "1"}}
                elif method in LISTS:
                    result = {LISTS[method]: []}
                    if era == "modern":
                        result.update(resultType="complete", ttlMs=0, cacheScope="private")
                else:
                    error = {"code": -32601, "message": "Method not found: %s" % method}
                body = {"jsonrpc": "2.0", "id": msg["id"]}
                body.update({"error": error} if error else {"result": result})
                self.reply(200, body)
    
        return Handler
    
    
    def summarize(record):
        """One readable line per record: method, protocol, client, and the capability names it declares."""
        parts = ["%-26s" % record["method"], "protocol=%s" % record.get("protocol")]
        client = record.get("client")
        if client:
            parts.append("client=%s/%s" % (client.get("name"), client.get("version")))
        if "capabilities" in record:
            parts.append("declares=%s" % (sorted(record["capabilities"]) or "nothing"))
        return "  " + " ".join(parts).rstrip()
    
    
    def serve(era, port, log):
        return ThreadingHTTPServer(("127.0.0.1", port), make_handler(era, log))
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("--era", choices=["modern", "legacy"], default="modern")
        ap.add_argument("--port", type=int, default=8240)
        args = ap.parse_args()
        server = serve(args.era, args.port, lambda e: print(json.dumps(e, sort_keys=True), flush=True))
        print("probe (%s era) on http://127.0.0.1:%d/mcp" % (args.era, args.port), file=sys.stderr, flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    
    
    if __name__ == "__main__":
        main()

## 6\. Run results

### The official Python SDK

`probe_runs.py` starts the probe inside the script and connects `mcp.client.Client` of the official SDK to it four times: modern and legacy probe, each without callbacks and with callbacks for sampling, roots and elicitation. The three list calls are issued by the script; a real client issues its own.

Probe server| Client callbacks| Requests, in order| Declared  
---|---|---|---  
`modern`| none| `server/discover` → `tools/list`, `resources/list`, `prompts/list`| nothing  
`modern`| `sampling`, `roots`, `elicitation`| `server/discover` → `tools/list`, `resources/list`, `prompts/list`| `elicitation`, `roots`, `sampling`  
`legacy`| none| `server/discover` → `initialize` → `notifications/initialized` → `tools/list`, `resources/list`, `prompts/list`| nothing  
`legacy`| `sampling`, `roots`, `elicitation`| `server/discover` → `initialize` → `notifications/initialized` → `tools/list`, `resources/list`, `prompts/list`| `elicitation`, `roots`, `sampling`  
  
  * The SDK declares what its callbacks allow and nothing else. "The SDK supports sampling" therefore means that the application passed a sampling callback.
  * Against the legacy probe the SDK sends `server/discover`, gets a refusal, and then sends `initialize` with 2025-11-25. Its mode `auto` does this on purpose. A refused `server/discover` is normal in the legacy era and no sign of failure.
  * Its default `clientInfo` is `mcp/0.1.0`. A product built on the SDK may therefore not be identifiable by name alone.

**probe_runs.py**
    
    
     #!/usr/bin/env python3
    """Connect the official Python SDK client (mcp==2.3.0) to the probe server in four configurations and print what
    the probe recorded. The list calls are issued by this script; a real client issues its own, and that is what you read.
    
    Usage: probe_runs.py      Exit code 0 = every run recorded what its configuration implies, 1 = it did not.
    """
    import asyncio
    import sys
    import threading
    
    from mcp import types
    from mcp.client import Client
    
    import client_probe_server as probe
    
    PORT = 8241
    
    
    async def no_sampling(context, params):
        return types.ErrorData(code=-32601, message="not used in this run")
    
    
    async def no_roots(context):
        return types.ErrorData(code=-32601, message="not used in this run")
    
    
    async def no_elicitation(context, params):
        return types.ErrorData(code=-32601, message="not used in this run")
    
    
    def run(era, callbacks):
        records = []
        server = probe.serve(era, PORT, records.append)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        kwargs = {"sampling_callback": no_sampling, "list_roots_callback": no_roots,
                  "elicitation_callback": no_elicitation} if callbacks else {}
    
        async def drive():
            async with Client("http://127.0.0.1:%d/mcp" % PORT, **kwargs) as client:
                await client.list_tools()
                await client.list_resources()
                await client.list_prompts()
    
        try:
            asyncio.run(drive())
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
        return records
    
    
    def main():
        failed = 0
        for era in ("modern", "legacy"):
            for callbacks in (False, True):
                records = run(era, callbacks)
                print("run: era=%s callbacks=%s" % (era, "sampling,roots,elicitation" if callbacks else "none"))
                for record in records:
                    print(probe.summarize(record))
                methods = [r["method"] for r in records]
                declared = [r for r in records if "capabilities" in r]
                wanted = ["elicitation", "roots", "sampling"] if callbacks else []
                ok = (methods[:1] == ["server/discover"]  # the SDK always probes first
                      and ("initialize" in methods) == (era == "legacy")  # only a legacy server gets the handshake
                      and [m for m in methods if m.endswith("/list")] == ["tools/list", "resources/list", "prompts/list"]
                      and bool(declared) and all(sorted(r["capabilities"]) == wanted for r in declared))
                print("  check: %s" % ("as configured" if ok else "NOT as configured"))
                failed += 0 if ok else 1
        return 1 if failed else 0
    
    
    if __name__ == "__main__":
        sys.exit(main())

**Recorded output: probe_runs.py**
    
    
     run: era=modern callbacks=none
      server/discover            protocol=2026-07-28 client=mcp/0.1.0 declares=nothing
      tools/list                 protocol=2026-07-28 client=mcp/0.1.0 declares=nothing
      resources/list             protocol=2026-07-28 client=mcp/0.1.0 declares=nothing
      prompts/list               protocol=2026-07-28 client=mcp/0.1.0 declares=nothing
      check: as configured
    run: era=modern callbacks=sampling,roots,elicitation
      server/discover            protocol=2026-07-28 client=mcp/0.1.0 declares=['elicitation', 'roots', 'sampling']
      tools/list                 protocol=2026-07-28 client=mcp/0.1.0 declares=['elicitation', 'roots', 'sampling']
      resources/list             protocol=2026-07-28 client=mcp/0.1.0 declares=['elicitation', 'roots', 'sampling']
      prompts/list               protocol=2026-07-28 client=mcp/0.1.0 declares=['elicitation', 'roots', 'sampling']
      check: as configured
    run: era=legacy callbacks=none
      server/discover            protocol=2026-07-28 client=mcp/0.1.0 declares=nothing
      initialize                 protocol=2025-11-25 client=mcp/0.1.0 declares=nothing
      notifications/initialized  protocol=2025-11-25
      tools/list                 protocol=2025-11-25
      resources/list             protocol=2025-11-25
      prompts/list               protocol=2025-11-25
      check: as configured
    run: era=legacy callbacks=sampling,roots,elicitation
      server/discover            protocol=2026-07-28 client=mcp/0.1.0 declares=['elicitation', 'roots', 'sampling']
      initialize                 protocol=2025-11-25 client=mcp/0.1.0 declares=['elicitation', 'roots', 'sampling']
      notifications/initialized  protocol=2025-11-25
      tools/list                 protocol=2025-11-25
      resources/list             protocol=2025-11-25
      prompts/list               protocol=2025-11-25
      check: as configured

### Claude Code 2.1.292

`claude_code_probe.py` adds the probe to the real `claude` CLI, runs `claude mcp list` (its health check) and prints what arrived. `HOME`, `XDG_CONFIG_HOME` and `CLAUDE_CONFIG_DIR` point at a throw-away directory, so your own configuration is neither read nor changed. Measured on macOS on 2026-10-26.

Probe server| `claude mcp list`| Requests, in order| Declared in full  
---|---|---|---  
`legacy`| Connected| `server/discover` → `initialize` → `notifications/initialized` → `tools/list`| `{"elicitation": {"form": {}, "url": {}}, "roots": {"listChanged": true}}`  
`modern`| Connected| `server/discover` → `tools/list`| `{"elicitation": {"form": {}, "url": {}}, "roots": {"listChanged": true}}`  
  
  * Claude Code probes `server/discover` with revision 2026-07-28 first, and against the legacy probe falls back to `initialize` with 2025-11-25. It speaks both eras, and the vendor page names 2026-07-28 (6).
  * It declares `elicitation` (with `form` and `url`) and `roots` (with `listChanged`), and no `sampling`. That equals cells 4 and 5 and the empty sampling cell of section 2: the vendor page and the wire agree.
  * In the modern run it still sends `roots.listChanged`, although the 2026-07-28 schema defines `roots` without fields. The schema does not forbid extra fields; a server should ignore this one.
  * `claude mcp list` requested `tools/list` only. It is a health check, not a session, so the missing `resources/list` and `prompts/list` prove nothing (section 7).

**claude_code_probe.py**
    
    
     #!/usr/bin/env python3
    """Connect the real Claude Code CLI to the probe server and print what it declares.
    
    `claude mcp list` health-checks every configured server, so adding the probe and running it once records the
    client's own handshake. HOME, XDG_CONFIG_HOME and CLAUDE_CONFIG_DIR point at a throw-away directory, so your own
    Claude Code configuration and servers are neither read nor changed. Needs the `claude` CLI on PATH; exit code 3
    when it is missing.
    Usage: claude_code_probe.py [--save FILE]   (--save writes the full records of both runs as JSON)
    """
    import argparse
    import json
    import os
    import shutil
    import subprocess
    import sys
    import tempfile
    import threading
    from pathlib import Path
    
    import client_probe_server as probe
    
    PORT = 8243
    URL = "http://127.0.0.1:%d/mcp" % PORT
    
    
    def run_era(era, env, cwd):
        records = []
        server = probe.serve(era, PORT, records.append)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            subprocess.run(["claude", "mcp", "add", "--transport", "http", "-s", "local", "probe", URL],
                           cwd=cwd, env=env, check=True, capture_output=True, text=True, timeout=120)
            listed = subprocess.run(["claude", "mcp", "list"], cwd=cwd, env=env, capture_output=True, text=True, timeout=120)
            status = [line for line in listed.stdout.splitlines() if line.startswith("probe:")]
            subprocess.run(["claude", "mcp", "remove", "probe", "-s", "local"], cwd=cwd, env=env, capture_output=True, text=True, timeout=120)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
        return records, status[0].split(" - ")[-1] if status else "no status line"
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("--save")
        args = ap.parse_args()
        if not shutil.which("claude"):
            print("claude CLI not found on PATH", file=sys.stderr)
            return 3
        version = subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=60).stdout.strip()
        print("claude --version: %s" % version)
        saved = {"version": version}
        with tempfile.TemporaryDirectory() as home, tempfile.TemporaryDirectory() as cwd:
            env = dict(os.environ, HOME=home, XDG_CONFIG_HOME=os.path.join(home, ".config"),
                       CLAUDE_CONFIG_DIR=os.path.join(home, ".claude"))
            for era in ("legacy", "modern"):
                records, status = run_era(era, env, cwd)
                saved[era] = records
                print("run: probe era=%s, claude mcp list says: %s" % (era, status))
                for record in records:
                    print(probe.summarize(record))
                first = next((r for r in records if "capabilities" in r), None)
                if first:
                    print("  declared in full: %s" % json.dumps(first["capabilities"], sort_keys=True))
        if args.save:
            Path(args.save).write_text(json.dumps(saved, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        return 0
    
    
    if __name__ == "__main__":
        sys.exit(main())

**Recorded output: claude_code_probe.py**
    
    
     claude --version: 2.1.292 (Claude Code)
    run: probe era=legacy, claude mcp list says: ✔ Connected
      server/discover            protocol=2026-07-28 client=claude-code/2.1.292 declares=['elicitation', 'roots']
      initialize                 protocol=2025-11-25 client=claude-code/2.1.292 declares=['elicitation', 'roots']
      notifications/initialized  protocol=2025-11-25
      tools/list                 protocol=2025-11-25
      declared in full: {"elicitation": {"form": {}, "url": {}}, "roots": {"listChanged": true}}
    run: probe era=modern, claude mcp list says: ✔ Connected
      server/discover            protocol=2026-07-28 client=claude-code/2.1.292 declares=['elicitation', 'roots']
      tools/list                 protocol=2026-07-28 client=claude-code/2.1.292 declares=['elicitation', 'roots']
      declared in full: {"elicitation": {"form": {}, "url": {}}, "roots": {"listChanged": true}}

## 7\. Reading the log

You see in the log| It means| What to do  
---|---|---  
`server/discover` with `protocol=2026-07-28`, then list calls, no `initialize`| A modern-era client talking to a modern server. Each request carries the declaration in its `_meta`| Read the declaration from every request; keep no per-connection state for it  
`server/discover` refused, then `initialize` with an older `protocol`| A legacy client, or a modern one falling back (the SDK and Claude Code both do). The declaration is made once, in `initialize`| Store it per connection at `initialize`. Do not log the refused `server/discover` as an error  
`declares` has no `sampling`| The client will not answer sampling requests| Make sampling optional: offer a path that does not call the client's model. If a request cannot be served without it, answer with `-32021` in 2026-07-28  
`elicitation` has `form` and `url`| Both modes are allowed. An empty `{}` means form only (2025-11-25)| Pick the mode from the declaration and never send one that is missing  
`roots` is declared, but you see no `roots/list` call| The declaration says the client will answer. It does not ask by itself| Ask when you need it: with a request in the legacy era, inside `inputRequests` in 2026-07-28  
Only `tools/list` was requested| Not proof that resources or prompts are unsupported: this may be a health check, or the host asks when the user does| Compare with the vendor's page (section 3) and a real session  
Requests after `initialize` carry no client name or capabilities| In the legacy era the declaration is made once per connection| Correlate by connection, not by request  
  
## 8\. Failure modes

Failure| Why it happens| Fix  
---|---|---  
The server sends sampling or elicitation without checking the declaration| The client never declared it. Both specs forbid relying on undeclared capabilities| Check `capabilities` before each such request and branch; in 2026-07-28 an unmet need is a `-32021` error  
An empty cell is read as "not supported"| The matrix records what a page says, and a page can be silent about something the product does| Treat empty as unknown and measure it with the probe  
A copied matrix goes stale| Vendors change their pages and their products| Date every cell, keep the quote, and fetch the page again before you rely on it  
A declared capability does not work in some mode| The vendor limits it: Claude Code serves elicitation "only in interactive terminal sessions" (c1)| Read the limits on the vendor's page; test the mode your users run  
One revision is assumed per client| Clients speak several: both clients in section 6 probe the modern revision first and fall back| Support both eras, or follow the compatibility matrix on the [learning path](https://modelcontextprotocol.info/docs/learning-path/)  
Sub-capabilities are ignored| `sampling.tools`, `sampling.context` and `elicitation.url` exist only in later revisions| Test the sub-field, not only the capability  
  
## 9\. Add or re-check a row

  1. Find the vendor's own page for the feature. If it states the feature, copy the sentence exactly and note the URL and the date; if it does not, leave the cell empty.
  2. Run the probe against the client (section 5). Compare `declares` with what the page says about roots, sampling and elicitation. When they disagree, one of the two is wrong; trust the wire for what the client sends, and the vendor for what the product does with it.
  3. Write down the client's version next to the measurement.
  4. Repeat steps 1 and 2 when the client upgrades, and when the page changes.



## Versions and Verification

Vendor wording was fetched on 2026-10-26 from the pages listed in section 2. Spec wording and schemas come from one pinned commit of the official repository (`dae694f6`; revision 2026-07-28 and the four before it). The probe runs used Python 3.14 and `mcp==2.3.0` on macOS, and the Claude Code CLI 2.1.292. Vendors change their pages and their products; every number here is dated, and section 9 says how to re-check one. An earlier version of this page answered the first question with a long list of ✅ and ❌ and named no source for any cell; this version keeps only what a vendor's own page states and quotes it for every cell.

### Sources

  * Vendor pages, as listed in section 2: [Claude Code](https://code.claude.com/docs/en/mcp), [Cursor](https://cursor.com/docs/mcp), [VS Code](https://code.visualstudio.com/api/extension-guides/ai/mcp), [Zed](https://zed.dev/docs/ai/mcp) and [Gemini CLI](https://geminicli.com/docs/tools/mcp-server/).
  * Spec: [lifecycle, 2025-11-25](https://modelcontextprotocol.info/specification/2025-11-25/basic/lifecycle/), [elicitation, 2025-11-25](https://modelcontextprotocol.info/specification/2025-11-25/client/elicitation/), [sampling, 2025-11-25](https://modelcontextprotocol.info/specification/2025-11-25/client/sampling/), [base protocol, 2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/basic/), [architecture, 2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/architecture/), [roots, 2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/client/roots/) and the [2026-07-28 schema](https://modelcontextprotocol.info/specification/2026-07-28/schema/).
  * [The learning path](https://modelcontextprotocol.info/docs/learning-path/), [MCP architecture](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/), [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/), [MCP resources explained](https://modelcontextprotocol.info/docs/concepts/resources/) and [MCP prompts explained](https://modelcontextprotocol.info/docs/concepts/prompts/).



[Understanding Model Context Protocol (MCP)](https://modelcontextprotocol.info/docs/introduction/ "Understanding Model Context Protocol \(MCP\)")[MCP FAQ: Versions, Authorization and Troubleshooting](https://modelcontextprotocol.info/docs/faqs/ "MCP FAQ: Versions, Authorization and Troubleshooting")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
