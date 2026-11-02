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
    * [MCP Server Best Practices: Transport, Security and Tool Design](https://modelcontextprotocol.info/docs/best-practices/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/best-practices/)
  * [简体中文](https://mcpcn.com/docs/best-practices/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. Pick the deployment shape first
  * 2\. Make the server stateless on purpose
  * 3\. The rules a remote server must pass
  * 4\. Define tools so the model can recover
  * 5\. Failure modes and recovery
  * 6\. Run the HTTP probe
  * 7\. Before you ship
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

MCP Server Best Practices: Transport, Security and Tool Design

# MCP Server Best Practices: Transport, Security and Tool Design

Before an MCP server faces real users or real data, settle the deployment shape, transport, and auth model; meet the MUST rules for Streamable HTTP and OAuth; and make sure tool definitions let a model correct itself. Each practice points to the official text that requires it, with failure modes and recovery steps; a script in the text tests the HTTP rules of a live endpoint.

**Scope.** Server side only, 2026-07-28 revision. Client behavior is covered by the official [client best practices](https://modelcontextprotocol.info/docs/2026-07-28/develop/clients/client-best-practices/); hardening a local stdio server on a developer machine is covered by [Local MCP Server Security](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/).

## 1\. Pick the deployment shape first

Most security decisions follow from where the server runs and who can reach it. Decide this before writing handlers.

Your situation| Use| Authentication| Official basis  
---|---|---|---  
A tool for one user, started by the host on the same machine| `stdio`| Read credentials from the environment. Do not implement the HTTP authorization flow| Authorization is OPTIONAL; implementations on stdio SHOULD NOT follow the HTTP authorization spec ([Basic protocol: Auth](https://modelcontextprotocol.info/specification/2026-07-28/basic/))  
A local HTTP server that other processes on the machine could reach| Streamable HTTP| Bind to `127.0.0.1`, validate `Origin`, and require a token or use IPC with restricted access| Streamable HTTP, "Security & Endpoint"; Security Best Practices, "Local MCP Server Compromise"  
A shared server for many users| Streamable HTTP| OAuth 2.1 resource server: Protected Resource Metadata, token validation, audience binding| [Authorization](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/)  
A server that calls another API on the user's behalf| Streamable HTTP| A token issued for your server. Use separate credentials downstream and never forward the client's token| Authorization, "Token Handling": servers MUST NOT accept or transit tokens issued for other resources  
  
## 2\. Make the server stateless on purpose

Revision 2026-07-28 has no protocol sessions. Every request carries its own `_meta` (protocol version, client info, capabilities), and servers MUST NOT rely on earlier requests on the same connection ([Basic protocol: Statelessness](https://modelcontextprotocol.info/specification/2026-07-28/basic/)). A client may interleave unrelated work on one connection, so a connection or process is not a conversation.

State that spans requests, such as a cart, a draft or a long job, lives behind an explicit handle that the model carries as an ordinary tool argument ([Tools: Stateful Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/), non-normative).

You need to remember| Do| Avoid  
---|---|---  
A cart, a transaction, a long-running job| Return an opaque handle from a creation tool and accept it as an argument on later calls| Keying state on the connection, the process, or an `Mcp-Session-Id` header  
Who may use a handle| Store state under `<user_id>:<handle>` where the user comes from the verified token, and reject other principals| Treating possession of a handle as authentication  
Handle format| Cryptographically random, opaque, expiring| Counters, timestamps, or identifiers that encode internal structure  
Expiry| State the retention rule in the creation tool's description, and answer an expired handle with a tool execution error that says so| Silent failure or a generic protocol error  
Scaling out| Keep shared state in a store behind the handle so any instance can serve any request| Requiring the same connection or process for related requests (SHOULD NOT)  
  
A server that supports only this revision should ignore an incoming `Mcp-Session-Id` and neither mint nor echo one ([Streamable HTTP: Earlier Streamable HTTP Revisions](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/)).

## 3\. The rules a remote server must pass

Each row is a practice, the level of the official text behind it, where to read it, and which probe check in section 6 exercises it. "Guidance" marks text that describes behavior without an RFC 2119 keyword.

#| Practice| Level| Official source| Probe check  
---|---|---|---|---  
1| Implement `server/discover` and list the versions you support in `supportedVersions`| MUST| Discovery| `discover`  
2| Validate `Origin` on all incoming connections. If it is present and invalid, answer `403 Forbidden`| MUST| Streamable HTTP, "Security & Endpoint"| `origin`  
3| Reject a request whose `Mcp-Method`, `Mcp-Name` or `MCP-Protocol-Version` header is missing, malformed or different from the body: `400` with JSON-RPC error `-32020` (`HeaderMismatch`)| MUST| Streamable HTTP, "Server Validation"| `method-header-missing`, `method-header-mismatch`  
4| For an unsupported protocol version answer `400` with `UnsupportedProtocolVersionError` (`-32022`) and list the supported versions| MUST| Streamable HTTP, "Protocol Version Header"| `unsupported-version`, `unsupported-version-lists-supported`  
5| For an unknown RPC method answer `404` with `-32601`| MUST| Streamable HTTP, "Protocol Version Header"| `unknown-method`  
6| Reject a request without `MCP-Protocol-Version`, unless you deliberately serve clients older than 2025-06-18| MUST, for servers that do not support such clients| Streamable HTTP, "Protocol Version Header"| `version-header-missing` (WARN)  
7| Answer GET and DELETE on the endpoint with `405`; ignore `Mcp-Session-Id` and do not mint session IDs| SHOULD| Streamable HTTP, "Earlier Streamable HTTP Revisions"| `get-not-allowed`, `no-session-id` (WARN)  
8| Validate all tool inputs, enforce access control, rate limit invocations, sanitize outputs| MUST| Tools, "Security Considerations"| not probed  
9| Report input validation failures as results with `isError: true`; report an unknown tool as a protocol error (`-32602`)| Guidance| Tools, "Error Handling"| `tool-input-error`, `unknown-tool` (WARN)  
10| Serve Protected Resource Metadata with at least one entry in `authorization_servers`, and advertise it through the `resource_metadata` parameter of `WWW-Authenticate` or a well-known URI| MUST| Authorization Server Discovery| `auth-resource-metadata`  
11| Validate access tokens, accept only tokens issued for this server as audience, answer invalid or expired tokens with `401`| MUST| Authorization, "Token Handling"| `auth-required`, `auth-invalid-token`, `auth-audience`  
12| Never accept or pass through tokens issued for another resource| MUST NOT| Authorization, "Token Handling"; Security Best Practices, "Token Passthrough"| `auth-audience` (acceptance only)  
13| For insufficient scope answer `403` with `WWW-Authenticate` carrying `error="insufficient_scope"`, `scope` and `resource_metadata`, and put every scope the operation needs into one challenge| SHOULD| Authorization, "Scope Challenge Handling"| not probed  
14| Use least-privilege scopes: a small initial set, no wildcard scopes, no full catalog in `scopes_supported`| Guidance| Security Best Practices, "Scope Minimization"| not probed  
15| Make state handles unpredictable and bind them server-side to the authenticated user| SHOULD| Security Best Practices, "State Handle Hijacking"| not probed  
  
Rows 8, 13, 14 and 15 need your application logic or a token with limited scope, so no generic probe can cover them. Write those tests yourself. The scenarios are in section 5.

## 4\. Define tools so the model can recover

Rule| Level| Official source  
---|---|---  
Name: 1 to 128 characters from `A-Z a-z 0-9 _ - .`, case-sensitive, unique within the server| SHOULD| Tools, "Tool Names"  
`inputSchema` is a valid JSON Schema object, never `null`. For a tool without parameters use `{ "type": "object", "additionalProperties": false }`| MUST (valid object); recommended form| Tools, "Tool"  
If you declare `outputSchema`, every structured result conforms to it. Also return the serialized JSON in a text block for older clients| MUST; SHOULD| Tools, "Output Schema" and "Structured Content"  
`tools/list` returns the tools available to the requesting client and does not vary per connection or as a side effect of other requests. It MAY vary with the authorization on the request. Keep the order deterministic| MUST NOT vary per connection; SHOULD for order| Tools, "Capabilities"  
Return validation and business-rule failures as `isError: true` results with a message that says what was wrong and what is valid, such as the format or range. Clients SHOULD show execution errors to the model, while protocol errors are less likely to be recovered| Guidance| Tools, "Error Handling"  
Do not mark secrets or personal data with `x-mcp-header`; header values are visible to network intermediaries| SHOULD NOT| Tools, "x-mcp-header"  
Do not depend on annotations as a security control. Clients MUST treat them as untrusted unless the server is trusted| MUST (client)| Tools, "Tool"  
  
Guidance that does not belong in a single tool description, such as how tools relate to each other, goes into the server `instructions`. [Server Instructions in Practice](https://modelcontextprotocol.info/blog/server-instructions/) covers where that field is delivered in each revision and how to test it.

## 5\. Failure modes and recovery

Symptom| Likely cause| How to confirm| Fix  
---|---|---|---  
Every request through a gateway fails with `400` and `-32020`| A proxy drops or rewrites `Mcp-Method`, `Mcp-Name` or `MCP-Protocol-Version`. The spec counts a missing or mismatched header as a validation failure| Run the probe against the origin and through the gateway, then compare `method-header-*`| Forward the three headers unchanged and keep body and headers in sync  
A client retries after `-32022` and never succeeds| It ignores `data.supported`, or your list holds versions it does not speak| Read `data.supported` and `data.requested` in the error body| Return an accurate list. The client retries with a version both sides support ([Versioning](https://modelcontextprotocol.info/specification/2026-07-28/basic/versioning/))  
A legacy client fails on its first request| A modern-only server and a client that starts with `initialize`. SDK 2.3.0 answered a request without `MCP-Protocol-Version` with `400` and `-32600`| `version-header-missing`| Accept that, or implement the earlier-revision behavior described in the corresponding spec revision  
A browser app gets `403`| The `Origin` allow-list lacks the app's origin| Repeat the request with the app's `Origin`| Add exact origins. The probe only sends a hostile origin, so add a test for each allowed one  
Every call returns `401` after enabling auth| The token was minted for another audience, or the server compares against a resource identifier that differs from what the client requested| Run the probe with `--token`; `discover` must pass first| Bind tokens to the server's canonical URI and configure the same URI in the server  
A token issued for another service is accepted| Nothing checks the audience. In SDK 2.3.0, `AuthSettings.validate_token_resource` is unset by default: the SDK warns, does not check, and says it will default to `True` in 3.0| `auth-audience` fails with `got 200` (reproduced in section 6)| Set `validate_token_resource=True`, or check the audience inside your `TokenVerifier`  
The client keeps sending the user through consent| The server challenges one scope at a time| Count the `403` challenges for one operation| Put all scopes the operation needs into one challenge; clients should cap retries  
One user reaches another user's cart| A guessable handle, or a handle not bound to the caller| Replay a handle with a second user's token| Random opaque handles, keyed by `<user_id>:<handle>` with the user taken from the verified token  
The model repeats the same bad call| The failure came back as a protocol error or as vague text| Compare a JSON-RPC error with an `isError` result and read the message| Return `isError: true` naming the field and the valid values  
The tool list differs between two connections| The listing depends on connection state or on unordered storage| Call `tools/list` on two connections and diff| Compute it from the request's authorization alone and sort it  
  
Test scenarios to add to your own CI for the rows the probe cannot cover: a token with too few scopes gets `403` and the challenge lists every needed scope; a second user's token cannot use the first user's handle; an expired handle returns an `isError` result; two connections get the same `tools/list` for the same token; a tool call over the rate limit is refused.

## 6\. Run the HTTP probe

`probe_http.py` uses only the Python standard library. It sends the requests behind the probed rows of section 3 and prints one line per check. `FAIL` means a MUST is not met, `WARN` means a SHOULD or the tools page's error guidance is not followed. Exit code 0 means no FAIL, 1 at least one FAIL, 2 means the endpoint was unreachable.
    
    
    python3 probe_http.py http://127.0.0.1:8000/mcp --tool echo --bad-args '{"text":123}'
    python3 probe_http.py http://127.0.0.1:8001/mcp --tool echo --bad-args '{"text":123}' \
      --token good-token --expect-auth --bad-audience-token other-audience-token

**probe_http.py**
    
    
     #!/usr/bin/env python3
    """Probe a Streamable HTTP MCP endpoint against the HTTP rules of spec 2026-07-28 (stdlib only).
    
    Usage: probe_http.py URL [--tool NAME --bad-args JSON] [--token T [--expect-auth] [--bad-audience-token T]]
    Levels: FAIL = a MUST in the spec is not met, WARN = a SHOULD or the tools page's error guidance is not followed
    (version-header-missing is WARN because a server may serve pre-2025-06-18 clients and treat the request as 2025-03-26).
    Exit code: 0 no FAIL, 1 at least one FAIL, 2 endpoint unreachable.
    """
    import argparse
    import http.client
    import json
    import sys
    from urllib.parse import urlsplit
    
    VERSION = "2026-07-28"
    EVIL_ORIGIN = "https://evil.example"
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    
    
    def meta(version):
        return {
            "io.modelcontextprotocol/protocolVersion": version,
            "io.modelcontextprotocol/clientInfo": {"name": "probe", "version": "0"},
            "io.modelcontextprotocol/clientCapabilities": {},
        }
    
    
    def parse(raw):
        """Return the JSON-RPC response from a JSON body or an SSE stream, else None."""
        try:
            return json.loads(raw)
        except ValueError:
            pass
        found = None
        for line in raw.splitlines():
            if line.startswith("data:"):
                try:
                    msg = json.loads(line[5:].strip())
                except ValueError:
                    continue
                if isinstance(msg, dict) and ("result" in msg or "error" in msg):
                    found = msg
        return found
    
    
    def request(url, verb="POST", method=None, params=None, headers=None, version=VERSION):
        """Send one request; a header whose value is None is removed. Returns (status, headers, body)."""
        parts = urlsplit(url)
        cls = http.client.HTTPSConnection if parts.scheme == "https" else http.client.HTTPConnection
        conn = cls(parts.netloc, timeout=10)
        hdrs = {"Accept": "application/json, text/event-stream", "MCP-Protocol-Version": version}
        payload = None
        if verb == "POST":
            hdrs.update({"Content-Type": "application/json", "Mcp-Method": method})
            if params and "name" in params:
                hdrs["Mcp-Name"] = params["name"]
            payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method,
                                  "params": {**(params or {}), "_meta": meta(version)}})
        hdrs.update(headers or {})
        conn.request(verb, parts.path or "/", payload, {k: v for k, v in hdrs.items() if v is not None})
        resp = conn.getresponse()
        raw = resp.read().decode("utf-8", "replace")
        conn.close()
        return resp.status, resp, parse(raw)
    
    
    def code(body):
        err = body.get("error") if isinstance(body, dict) else None
        return err.get("code") if isinstance(err, dict) else None
    
    
    def show(status, rpc_code):
        return "%s/%s" % (status, rpc_code) if rpc_code is not None else str(status)
    
    
    def report(name, ok, detail, level="FAIL"):
        status = "PASS" if ok else level
        counts[status] += 1
        print("%s %s: %s" % (status, name, detail))
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("url")
        ap.add_argument("--tool", help="name of an existing tool, enables the tool-error check")
        ap.add_argument("--bad-args", default="{}", help="JSON arguments that violate the tool's input schema")
        ap.add_argument("--token", help="bearer token that the server accepts")
        ap.add_argument("--expect-auth", action="store_true", help="the endpoint is protected: run the auth checks")
        ap.add_argument("--bad-audience-token", help="a valid token issued for a different resource")
        args = ap.parse_args()
        if args.expect_auth and not args.token:
            ap.error("--expect-auth needs --token (the other checks must get past authentication)")
        auth = {"Authorization": "Bearer " + args.token} if args.token else {}
        url = args.url
    
        try:
            status, _, body = request(url, method="server/discover", headers=auth)
        except (OSError, http.client.HTTPException) as exc:
            print("ERROR endpoint unreachable: %s" % exc)
            return 2
        result = body.get("result") if isinstance(body, dict) else None
        ok = status == 200 and isinstance(result, dict) and VERSION in result.get("supportedVersions", [])
        report("discover", ok, "HTTP %s, supportedVersions %s" % (status, (result or {}).get("supportedVersions")))
        tools = "tools" in (result or {}).get("capabilities", {})
    
        def expect(name, want_status, want_code, **kw):
            st, _, b = request(url, **{"headers": auth, **kw})
            report(name, st == want_status and (want_code is None or code(b) == want_code),
                   "want %s, got %s" % (show(want_status, want_code), show(st, code(b))))
            return b
    
        expect("origin", 403, None, method="server/discover", headers={**auth, "Origin": EVIL_ORIGIN})
        expect("method-header-missing", 400, -32020, method="server/discover", headers={**auth, "Mcp-Method": None})
        expect("method-header-mismatch", 400, -32020, method="server/discover", headers={**auth, "Mcp-Method": "tools/list"})
        b = expect("unsupported-version", 400, -32022, method="server/discover", version="2099-01-01",
                   headers={**auth})
        supported = ((b or {}).get("error") or {}).get("data", {}).get("supported") if isinstance(b, dict) else None
        report("unsupported-version-lists-supported", bool(supported) and VERSION in supported, "data.supported = %s" % supported)
        expect("unknown-method", 404, -32601, method="nope/nothing")
    
        st, _, b = request(url, method="server/discover", headers={**auth, "MCP-Protocol-Version": None})
        report("version-header-missing", st == 400, "want 400, got %s" % show(st, code(b)), "WARN")
        st, _, _ = request(url, verb="GET", headers=auth)
        report("get-not-allowed", st == 405, "want 405, got %s" % st, "WARN")
        st, resp, _ = request(url, method="server/discover", headers={**auth, "Mcp-Session-Id": "probe-session"})
        report("no-session-id", resp.getheader("Mcp-Session-Id") is None, "Mcp-Session-Id in response: %s" % resp.getheader("Mcp-Session-Id"), "WARN")
    
        if args.tool:
            st, _, b = request(url, method="tools/call", params={"name": args.tool, "arguments": json.loads(args.bad_args)}, headers=auth)
            is_error = isinstance(b, dict) and (b.get("result") or {}).get("isError") is True
            report("tool-input-error", st == 200 and is_error, "want 200 with result.isError=true, got %s" % show(st, "isError" if is_error else code(b)), "WARN")
            st, _, b = request(url, method="tools/call", params={"name": "no_such_tool", "arguments": {}}, headers=auth)
            report("unknown-tool", code(b) == -32602, "want JSON-RPC error -32602, got %s" % show(st, code(b) or "result"), "WARN")
        elif tools:
            print("SKIP tool checks: pass --tool NAME --bad-args JSON")
    
        if args.expect_auth:
            st, resp, b = request(url, method="server/discover")
            challenge = resp.getheader("WWW-Authenticate") or ""
            report("auth-required", st == 401, "no token: want 401, got %s" % st)
            report("auth-invalid-token", request(url, method="server/discover", headers={"Authorization": "Bearer invalid"})[0] == 401,
                   "garbage token must get 401")
            if args.bad_audience_token:
                st = request(url, method="server/discover", headers={"Authorization": "Bearer " + args.bad_audience_token})[0]
                report("auth-audience", st == 401, "token for another resource: want 401, got %s" % st)
            meta_url = challenge.split('resource_metadata="')[1].split('"')[0] if 'resource_metadata="' in challenge else None
            origin = "%s://%s" % (urlsplit(url).scheme, urlsplit(url).netloc)
            well_known = "/.well-known/oauth-protected-resource"
            found = None
            for candidate in [meta_url, origin + well_known + urlsplit(url).path, origin + well_known]:
                if not candidate:
                    continue
                st, _, doc = request(candidate, verb="GET", headers={})
                if st == 200 and isinstance(doc, dict):
                    found = doc
                    break
            report("auth-resource-metadata", bool(found and found.get("authorization_servers")),
                   "challenge resource_metadata=%s; document authorization_servers=%s" % (meta_url, (found or {}).get("authorization_servers")))
    
        print("%d pass, %d warn, %d fail" % (counts["PASS"], counts["WARN"], counts["FAIL"]))
        return 1 if counts["FAIL"] else 0
    
    
    if __name__ == "__main__":
        try:
            sys.exit(main())
        except (OSError, http.client.HTTPException) as exc:
            print("ERROR connection failed: %s" % exc)
            sys.exit(2)

The two reference servers use the official Python SDK (`pip install mcp==2.3.0`):

**ref_server.py**
    
    
     """Official Python SDK (mcp==2.3.0) server on Streamable HTTP, http://127.0.0.1:8000/mcp, no auth."""
    from mcp.server.mcpserver import MCPServer
    
    server = MCPServer("ref")
    
    
    @server.tool()
    def echo(text: str) -> str:
        """Echo text."""
        return text
    
    
    if __name__ == "__main__":
        server.run("streamable-http")

**auth_ref_server.py**
    
    
     """Same server behind bearer-token auth, http://127.0.0.1:8001/mcp.
    
    Tokens: good-token is issued for this server; other-audience-token is valid but issued for another resource.
    """
    from mcp.server.auth.provider import AccessToken
    from mcp.server.auth.settings import AuthSettings
    from mcp.server.mcpserver import MCPServer
    
    RESOURCE = "http://127.0.0.1:8001/mcp"
    
    
    class Verifier:
        async def verify_token(self, token: str) -> AccessToken | None:
            if token == "good-token":
                return AccessToken(token=token, client_id="probe", scopes=[], resource=RESOURCE)
            if token == "other-audience-token":
                return AccessToken(token=token, client_id="probe", scopes=[], resource="https://other.example/mcp")
            return None
    
    
    server = MCPServer(
        "ref-auth",
        token_verifier=Verifier(),
        auth=AuthSettings(
            issuer_url="https://auth.example.com",
            resource_server_url=RESOURCE,
            validate_token_resource=True,
        ),
    )
    
    
    @server.tool()
    def echo(text: str) -> str:
        """Echo text."""
        return text
    
    
    if __name__ == "__main__":
        server.run("streamable-http", port=8001)

What the probe reported on this setup (Python 3.14, macOS, `mcp==2.3.0`):

Target| Result  
---|---  
SDK server without auth (`ref_server.py`)| 11 pass, 1 warn, 0 fail  
SDK server with bearer auth (`auth_ref_server.py`)| 15 pass, 1 warn, 0 fail  
The same auth server with `validate_token_resource` removed (the SDK default)| 1 fail: `auth-audience`, got 200  
A stub written from the spec text, without and with auth| 12 pass, 0 warn, 0 fail; 16 pass, 0 warn, 0 fail  
The stub with one rule broken at a time, 11 variants| 8 variants fail the named check, 3 variants only warn, none passes silently  
  
Full output for the auth server:
    
    
    PASS discover: HTTP 200, supportedVersions ['2026-07-28']
    PASS origin: want 403, got 403
    PASS method-header-missing: want 400/-32020, got 400/-32020
    PASS method-header-mismatch: want 400/-32020, got 400/-32020
    PASS unsupported-version: want 400/-32022, got 400/-32022
    PASS unsupported-version-lists-supported: data.supported = ['2026-07-28']
    PASS unknown-method: want 404/-32601, got 404/-32601
    PASS version-header-missing: want 400, got 400/-32600
    PASS get-not-allowed: want 405, got 405
    PASS no-session-id: Mcp-Session-Id in response: None
    PASS tool-input-error: want 200 with result.isError=true, got 200/isError
    WARN unknown-tool: want JSON-RPC error -32602, got 200/result
    PASS auth-required: no token: want 401, got 401
    PASS auth-invalid-token: garbage token must get 401
    PASS auth-audience: token for another resource: want 401, got 401
    PASS auth-resource-metadata: challenge resource_metadata=http://127.0.0.1:8001/.well-known/oauth-protected-resource/mcp; document authorization_servers=['https://auth.example.com']
    15 pass, 1 warn, 0 fail

How to read it:

  * **The one warning is a finding, not a bug in the probe.** The tools page lists "Unknown tool" under protocol errors with `-32602`. SDK 2.3.0 returns a normal result with `isError: true` instead. The text is guidance rather than a MUST, and the model can recover from either, but pick one behavior on purpose and test it.
  * **The default-audience run shows why negative tests matter.** The server answered `200` for a token issued for `https://other.example/mcp`. Nothing crashed and the happy path worked, so only a negative test finds it.
  * **Passing proves the listed behaviors on one setup.** The probe does not test: that an allow-listed origin passes, TLS, rate limits, scope challenges, streamed (SSE) responses, cancellation, `x-mcp-header` mirroring, multi round-trip requests, output sanitization, or load. A stub and the SDK passing the same checks are two independent readings of the spec, but they do not rule out a shared misreading, so keep the matrix in section 3 as the review list.



## 7\. Before you ship

  * You chose the deployment shape in section 1 and wrote down why.
  * Nothing depends on connection or process identity; every handle is opaque, expiring and bound to its owner.
  * Origin validation, header validation and version errors pass the probe, and your gateway forwards the three mirrored headers.
  * For a protected server: invalid, expired and wrong-audience tokens get `401`; the metadata document names an authorization server; no token is forwarded downstream.
  * Tool names, schemas and result shapes follow section 4, and validation failures are `isError` results the model can act on.
  * Rows 8, 13, 14 and 15 have tests in your own suite.
  * You re-run the probe when you change the SDK, the gateway or the authorization server.



## Versions and Verification

Spec facts come from the 2026-07-28 pages published on this site. The experiments in section 6 ran locally against the official Python SDK 2.3.0 and are labeled as such.

### Sources

  * [Streamable HTTP transport](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/streamable-http/), [Authorization](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/), [Authorization Server Discovery](https://modelcontextprotocol.info/specification/2026-07-28/basic/authorization/authorization-server-discovery/), [Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/), [Versioning](https://modelcontextprotocol.info/specification/2026-07-28/basic/versioning/) and [Basic protocol](https://modelcontextprotocol.info/specification/2026-07-28/basic/) in the 2026-07-28 specification
  * [Security Best Practices](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/), [Local MCP Server Security](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/) and [Authorization tutorial](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/)
  * [Server Instructions in Practice](https://modelcontextprotocol.info/blog/server-instructions/) on this site



[MCP FAQ: Versions, Authorization and Troubleshooting](https://modelcontextprotocol.info/docs/faqs/ "MCP FAQ: Versions, Authorization and Troubleshooting")[Build an MCP Server](https://modelcontextprotocol.info/docs/development/build-server/ "Build an MCP Server")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
