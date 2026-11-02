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
    * [Build and Verify a Node.js MCP Client with the TypeScript SDK](https://modelcontextprotocol.info/docs/tutorials/building-a-client-node/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/tutorials/building-a-client-node/)
  * [简体中文](https://mcpcn.com/docs/tutorials/building-a-client-node/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. What you need and how to set it up
  * 2\. The client
  * 3\. A server to run it against
  * 4\. Running it and reading the outcomes
  * 5\. Which protocol era did you connect in?
  * 6\. Putting a model in the loop
  * 7\. Failure modes
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Tutorials: From Concept to Production](https://modelcontextprotocol.info/docs/tutorials/)

Build and Verify a Node.js MCP Client with the TypeScript SDK

# Build and Verify a Node.js MCP Client with the TypeScript SDK

A working Node.js MCP client is short; the example here is under seventy lines. The sections below build a small client with the current TypeScript SDK, connect it to a stdio server you control, and handle a successful call, a tool failure, an unknown tool, a timeout, a server that exits mid-call and a missing command. The same client then connects to legacy and modern servers to show why the SDK's default mode fails against a 2026-07-28 server and when to use `auto` instead.

The TypeScript tab of the official client tutorial (linked under Sources) goes on to wire an Anthropic model into a chat loop and needs an API key. The example stops at that boundary: everything below runs without a key, and section 6 says where the model plugs in. For the server side of the same SDK read [Build an MCP server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/); to look at a server without writing a client, use the [Inspector](https://modelcontextprotocol.info/tools/inspector/).

## 1\. What you need and how to set it up

You need Node.js 20 or later (the official tutorial asks for 20, and the client package declares `>=20`) and npm. Five packages, pinned to exact versions because this is the 2.x line of the SDK: the official tutorials of the 2025 revisions install a single package, `@modelcontextprotocol/sdk`, and import from its subpaths, while the 2026-07-28 tutorial installs `@modelcontextprotocol/client` and imports from it:

Package| Version| What it is for  
---|---|---  
`@modelcontextprotocol/client`| `2.4.0`| The client: `Client`, the transports, the error classes  
`@modelcontextprotocol/server`| `2.4.0`| Only for the test server of section 3  
`zod`| `4.6.7`| Declares the input and output schemas of the test server's tools  
`@types/node`| `26.6.5`| Node.js type declarations  
`typescript`| `7.0.2`| Compiles `src/` to `build/`  
  
Put these two files in an empty directory:

**package.json**
    
    
    {
      "name": "mcp-node-client",
      "version": "1.0.0",
      "private": true,
      "type": "module",
      "engines": { "node": ">=20" },
      "scripts": {
        "build": "tsc"
      },
      "dependencies": {
        "@modelcontextprotocol/client": "2.4.0",
        "@modelcontextprotocol/server": "2.4.0",
        "zod": "4.6.7"
      },
      "devDependencies": {
        "@types/node": "26.6.5",
        "typescript": "7.0.2"
      }
    }

**tsconfig.json**
    
    
    {
      "compilerOptions": {
        "target": "ES2022",
        "module": "Node16",
        "moduleResolution": "Node16",
        "types": ["node"],
        "outDir": "./build",
        "rootDir": "./src",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": ["src"]
    }

Then install and compile:
    
    
    npm install
    npm run build

## 2\. The client

`src/client.ts` wraps the SDK's `Client` class. It is the part you would keep when you add a model.

**src/client.ts**
    
    
     import { Client, ProtocolError, SdkError, StreamableHTTPClientTransport } from "@modelcontextprotocol/client";
    import { StdioClientTransport } from "@modelcontextprotocol/client/stdio";
    
    export type Transport = StdioClientTransport | StreamableHTTPClientTransport;
    
    /** How a tool call ended, in the four ways a caller has to tell apart. `sdk-error` is the SDK giving up: a timeout or a closed connection. */
    export type ToolOutcome =
      | { kind: "ok"; text: string; structured?: unknown }
      | { kind: "tool-error"; text: string }
      | { kind: "protocol-error"; code: number; message: string }
      | { kind: "sdk-error"; code: string; message: string };
    
    function textOf(content: ReadonlyArray<{ type: string; text?: string }>): string {
      return content
        .filter((block) => block.type === "text")
        .map((block) => block.text ?? "")
        .join("\n");
    }
    
    export class McpToolClient {
      private readonly client: Client;
    
      /**
       * With `auto` the client probes with `server/discover` and falls back to `initialize`.
       * Without it the SDK sends `initialize` only, which a server of revision 2026-07-28 or later may refuse.
       */
      constructor(name: string, options: { auto?: boolean } = {}) {
        this.client = new Client({ name, version: "1.0.0" }, options.auto ? { versionNegotiation: { mode: "auto" } } : {});
      }
    
      async connect(transport: Transport): Promise<void> {
        await this.client.connect(transport);
      }
    
      get protocolVersion(): string | undefined {
        return this.client.getNegotiatedProtocolVersion();
      }
    
      async toolNames(): Promise<string[]> {
        const { tools } = await this.client.listTools();
        return tools.map((tool) => tool.name);
      }
    
      async callTool(name: string, args: Record<string, unknown>, timeoutMs = 5000): Promise<ToolOutcome> {
        try {
          const result = await this.client.callTool({ name, arguments: args }, { timeout: timeoutMs });
          const text = textOf(result.content);
          if (result.isError) {
            return { kind: "tool-error", text };
          }
          return result.structuredContent === undefined
            ? { kind: "ok", text }
            : { kind: "ok", text, structured: result.structuredContent };
        } catch (error) {
          if (ProtocolError.isInstance(error)) {
            return { kind: "protocol-error", code: error.code, message: error.message };
          }
          if (SdkError.isInstance(error)) {
            return { kind: "sdk-error", code: error.code, message: error.message };
          }
          throw error;
        }
      }
    
      async close(): Promise<void> {
        await this.client.close();
      }
    }

Four things in it matter:

  * **The constructor takes the connect mode.** `versionNegotiation: { mode: "auto" }` makes the client probe with `server/discover` and fall back to `initialize`. The SDK's own default is `'legacy'`: `initialize` only. Section 5 shows what that default costs.
  * **`connect` performs the handshake of the era that was chosen**, and `getNegotiatedProtocolVersion()` tells you which one you got.
  * **`listTools()` called without a cursor walks every page** and returns the whole list, so you do not paginate by hand.
  * **`callTool` ends in one of four ways.** The spec splits errors in two: protocol errors, which are JSON-RPC errors such as an unknown tool, and tool execution errors, which come back as a normal result with `isError: true`. The SDK adds a third kind that has no JSON-RPC form: it gives up itself, on a timeout or a closed connection. A caller has to treat all four differently, so the client returns them as four kinds instead of throwing.



## 3\. A server to run it against

A client needs something to talk to. `src/server.ts` is a stdio server built with the server package of the same SDK. It has four tools, each there to produce one outcome: `add` works and returns structured output, `fail` throws, `slow` answers after a delay, `crash` ends the process.

**src/server.ts**
    
    
     import { McpServer } from "@modelcontextprotocol/server";
    import { serveStdio } from "@modelcontextprotocol/server/stdio";
    import { z } from "zod";
    
    // serveStdio calls this whenever it needs an instance, so every call must return a fresh server.
    function createServer() {
      const server = new McpServer({ name: "fixture", version: "1.0.0" });
    
      server.registerTool(
        "add",
        {
          description: "Add two numbers",
          inputSchema: z.object({ a: z.number(), b: z.number() }),
          outputSchema: z.object({ sum: z.number() }),
        },
        async ({ a, b }) => ({
          content: [{ type: "text", text: String(a + b) }],
          structuredContent: { sum: a + b },
        }),
      );
    
      server.registerTool("fail", { description: "Always throws", inputSchema: z.object({}) }, async () => {
        throw new Error("boom");
      });
    
      server.registerTool(
        "slow",
        { description: "Answers after a delay", inputSchema: z.object({ ms: z.number() }) },
        async ({ ms }) => {
          await new Promise((resolve) => setTimeout(resolve, ms));
          return { content: [{ type: "text", text: "done" }] };
        },
      );
    
      server.registerTool("crash", { description: "Exits the server process", inputSchema: z.object({}) }, async () => {
        process.exit(1);
      });
    
      return server;
    }
    
    serveStdio(createServer, { onerror: (error) => console.error("fixture server error:", error) });
    console.error("fixture server running on stdio");

Two points about the server. `serveStdio` negotiates the protocol revision with each client, so the same server answers clients of 2026-07-28 and clients that still open with the 2025-era `initialize`; a server wired by hand with `server.connect(new StdioServerTransport())` serves only 2025-era clients. And it logs with `console.error`, because the stdio transport reserves standard output for protocol messages: a server "MUST NOT write anything to its `stdout` that is not a valid MCP message".

## 4\. Running it and reading the outcomes

`src/scenarios.ts` connects the client to the server twice, once in each connect mode, and then makes seven calls and one failing connection.

**src/scenarios.ts**
    
    
     import { fileURLToPath } from "node:url";
    import { StdioClientTransport } from "@modelcontextprotocol/client/stdio";
    import { McpToolClient, type ToolOutcome } from "./client.js";
    
    const serverPath = fileURLToPath(new URL("./server.js", import.meta.url));
    
    function stdio(command = process.execPath, args = [serverPath]) {
      return new StdioClientTransport({ command, args, stderr: "ignore" });
    }
    
    function show(outcome: ToolOutcome): string {
      switch (outcome.kind) {
        case "ok":
          return `ok text=${JSON.stringify(outcome.text)}` + (outcome.structured === undefined ? "" : ` structured=${JSON.stringify(outcome.structured)}`);
        case "tool-error":
          return `tool-error text=${JSON.stringify(outcome.text)}`;
        case "protocol-error":
          return `protocol-error code=${outcome.code} message=${JSON.stringify(outcome.message)}`;
        case "sdk-error":
          return `sdk-error code=${outcome.code}`;
      }
    }
    
    async function main(): Promise<void> {
      // 1. The same server, connected the SDK's default way and with version negotiation.
      for (const auto of [false, true]) {
        const probe = new McpToolClient("scenario-probe", { auto });
        await probe.connect(stdio());
        console.log(`connect ${auto ? "auto   " : "default"}: protocol ${probe.protocolVersion}, tools ${(await probe.toolNames()).join(", ")}`);
        await probe.close();
      }
    
      // 2. Tool calls over one negotiated connection.
      const client = new McpToolClient("scenario-client", { auto: true });
      await client.connect(stdio());
      const calls: Array<[string, Record<string, unknown>, number?]> = [
        ["add", { a: 2, b: 3 }],
        ["add", { a: "2", b: 3 }],
        ["nosuch", {}],
        ["fail", {}],
        ["slow", { ms: 3000 }, 300],
        ["slow", { ms: 50 }, 2000],
        ["crash", {}],
      ];
      for (const [name, args, timeoutMs] of calls) {
        const label = `${name}(${JSON.stringify(args)})${timeoutMs === undefined ? "" : ` timeout=${timeoutMs}ms`}`;
        console.log(`${label} -> ${show(await client.callTool(name, args, timeoutMs))}`);
      }
      await client.close();
    
      // 3. A server command that does not exist.
      const missing = new McpToolClient("scenario-missing", { auto: true });
      try {
        await missing.connect(stdio("mcp-server-that-does-not-exist", []));
        console.log("missing command -> connected (unexpected)");
      } catch (error) {
        console.log(`missing command -> connect rejected: ${error instanceof Error ? error.message : String(error)}`);
      }
    }
    
    main().catch((error: unknown) => {
      console.error("scenario run failed:", error);
      process.exit(1);
    });

Run it with `node build/scenarios.js`. This is the output of that run:

**Recorded output: node build/scenarios.js**
    
    
     connect default: protocol 2025-11-25, tools add, fail, slow, crash
    connect auto   : protocol 2026-07-28, tools add, fail, slow, crash
    add({"a":2,"b":3}) -> ok text="5" structured={"sum":5}
    add({"a":"2","b":3}) -> tool-error text="Input validation error: Invalid arguments for tool add: a: Invalid input: expected number, received string"
    nosuch({}) -> protocol-error code=-32602 message="Tool nosuch not found"
    fail({}) -> tool-error text="boom"
    slow({"ms":3000}) timeout=300ms -> sdk-error code=REQUEST_TIMEOUT
    slow({"ms":50}) timeout=2000ms -> ok text="done"
    crash({}) -> sdk-error code=CONNECTION_CLOSED
    missing command -> connect rejected: spawn mcp-server-that-does-not-exist ENOENT

The first two lines are the two connections, which section 5 explains. The table covers the other eight lines:

Call| Result| What it shows  
---|---|---  
`add({"a":2,"b":3})`| `ok text="5" structured={"sum":5}`| A normal result: the text content, plus the structured result that the tool's output schema describes  
`add({"a":"2","b":3})`| `tool-error text="Input validation error: Invalid arguments for tool add: a: Invalid input: expected number, received string"`| A wrong argument type: the server rejected the input inside a result with `isError: true`, so the model can read the message and retry  
`nosuch({})`| `protocol-error code=-32602 message="Tool nosuch not found"`| An unknown tool: a JSON-RPC error with code `-32602`, not a tool result  
`fail({})`| `tool-error text="boom"`| The tool threw: the server turned the exception into a tool execution error that carries its message  
`slow({"ms":3000}) timeout=300ms`| `sdk-error code=REQUEST_TIMEOUT`| The client gave up after 300 ms; the SDK reports its own error code, not a JSON-RPC one  
`slow({"ms":50}) timeout=2000ms`| `ok text="done"`| The next call on the same connection: it still works  
`crash({})`| `sdk-error code=CONNECTION_CLOSED`| The server process exited during the call, and the connection is gone  
`missing command`| `connect rejected: spawn mcp-server-that-does-not-exist ENOENT`| The command does not exist: `connect` itself rejects, before any request is sent  
  
Three things to take from it:

  1. The same server connects as 2025-11-25 by default and as 2026-07-28 with `auto`. The server did not change; the client's connect mode did.
  2. An argument of the wrong type comes back as a tool execution error, an unknown tool as a JSON-RPC error with code `-32602`. That is the spec's split, and it tells you what to do with each: the spec says clients "SHOULD provide tool execution errors to language models to enable self-correction" and "MAY provide protocol errors".
  3. A timeout abandons one request and leaves the connection usable: the call after it returned `done`. A server that exits during a call ends that call with `CONNECTION_CLOSED`.



## 5\. Which protocol era did you connect in?

The first two lines of the output show it: the default mode connected as 2025-11-25, `auto` as 2026-07-28. The default sends `initialize` and nothing else, which is what every client did until 2026-07-28. The spec's compatibility matrix says what happens when such a client meets a server of the new era: a legacy client against a modern server "Fails". To see it on the wire, `src/probe-client.ts` connects over Streamable HTTP to the probe server of the [clients page](https://modelcontextprotocol.info/docs/clients/) in each era, with each connect mode, and `era_runs.py` runs the checker of the [architecture page](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/) over what the probe saw. It imports two scripts that are embedded on those pages, `client_probe_server.py` and `lifecycle_check.py`; save both next to it.

**src/probe-client.ts**
    
    
     import { ProtocolError, SdkError, StreamableHTTPClientTransport } from "@modelcontextprotocol/client";
    import { McpToolClient } from "./client.js";
    
    // Usage: node build/probe-client.js default|auto PORT
    const [mode, port] = process.argv.slice(2);
    if ((mode !== "default" && mode !== "auto") || !/^\d+$/.test(port ?? "")) {
      console.error("usage: probe-client.js default|auto PORT");
      process.exit(2);
    }
    
    const client = new McpToolClient("probe-client", { auto: mode === "auto" });
    try {
      await client.connect(new StreamableHTTPClientTransport(new URL(`http://127.0.0.1:${port}/mcp`)));
      const names = await client.toolNames();
      console.log(`connected: protocol ${client.protocolVersion}, ${names.length} tools`);
      await client.close();
    } catch (error) {
      const reason = ProtocolError.isInstance(error)
        ? `ProtocolError ${error.code}`
        : SdkError.isInstance(error)
          ? error.code
          : error instanceof Error
            ? error.name
            : "unknown";
      console.log(`connect failed: ${reason}`);
    }

**era_runs.py**
    
    
     #!/usr/bin/env python3
    """Connect the TypeScript SDK client (probe-client.js) to the probe server of the clients page, in both eras and in the
    SDK's two connect modes, and run lifecycle_check over what the probe saw.
    
    Usage: era_runs.py BUILD_DIR      BUILD_DIR = the directory that holds the compiled `build/probe-client.js`
    Exit code 0 = each of the four runs ended as the table at the top of EXPECTED says; 2 = node or the build is missing.
    Needs only the standard library, and two scripts from other pages saved next to this file: `client_probe_server.py`
    (the probe server of the clients page) and `lifecycle_check.py` (the checker of the architecture page).
    """
    import shutil
    import subprocess
    import sys
    import threading
    from pathlib import Path
    
    HERE = Path(__file__).resolve().parent
    sys.path.insert(0, str(HERE))
    import client_probe_server  # noqa: E402
    import lifecycle_check  # noqa: E402
    
    PORT = 8246
    # (SDK mode, probe era) -> (the client says, whether lifecycle_check must pass)
    EXPECTED = {
        ("default", "legacy"): ("connected: protocol 2025-11-25, 0 tools", True),
        ("default", "modern"): ("connect failed:", False),
        ("auto", "legacy"): ("connected: protocol 2025-11-25, 0 tools", True),
        ("auto", "modern"): ("connected: protocol 2026-07-28, 0 tools", True),
    }
    
    
    def run(build, mode, era):
        records = []
        server = client_probe_server.serve(era, PORT, records.append)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            done = subprocess.run([shutil.which("node"), str(build / "build" / "probe-client.js"), mode, str(PORT)],
                                  capture_output=True, text=True, timeout=60, cwd=str(build))
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)
        return (done.stdout.strip() or done.stderr.strip()), records
    
    
    def chain(records):
        return " -> ".join(r["method"] for r in records)
    
    
    def main():
        if len(sys.argv) != 2 or not shutil.which("node") or not (Path(sys.argv[1]) / "build" / "probe-client.js").is_file():
            print("usage: era_runs.py BUILD_DIR (node on PATH, `npm run build` done in BUILD_DIR)", file=sys.stderr)
            return 2
        build = Path(sys.argv[1])
        bad = 0
        for (mode, era), (says, must_pass) in EXPECTED.items():
            output, records = run(build, mode, era)
            print("run: sdk-mode=%s probe=%s" % (mode, era))
            print("  client says: %s" % output)
            print("  requests: %s" % chain(records))
            ok = output.startswith(says)
            if must_pass:
                passed, warned, failed = lifecycle_check.summary(lifecycle_check.run_checks(records))
                print("  lifecycle_check: %d pass, %d warn, %d fail" % (passed, warned, failed))
                ok = ok and (warned, failed) == (0, 0)
            else:
                print("  lifecycle_check: not run (the connection failed)")
            print("  check: %s" % ("as expected" if ok else "UNEXPECTED"))
            bad += 0 if ok else 1
        return 1 if bad else 0
    
    
    if __name__ == "__main__":
        sys.exit(main())

**Recorded output: era_runs.py**
    
    
     run: sdk-mode=default probe=legacy
      client says: connected: protocol 2025-11-25, 0 tools
      requests: initialize -> notifications/initialized -> tools/list
      lifecycle_check: 7 pass, 0 warn, 0 fail
      check: as expected
    run: sdk-mode=default probe=modern
      client says: connect failed: ProtocolError -32601
      requests: initialize
      lifecycle_check: not run (the connection failed)
      check: as expected
    run: sdk-mode=auto probe=legacy
      client says: connected: protocol 2025-11-25, 0 tools
      requests: server/discover -> initialize -> notifications/initialized -> tools/list
      lifecycle_check: 7 pass, 0 warn, 0 fail
      check: as expected
    run: sdk-mode=auto probe=modern
      client says: connected: protocol 2026-07-28, 0 tools
      requests: server/discover -> tools/list
      lifecycle_check: 7 pass, 0 warn, 0 fail
      check: as expected

Connect mode| Server era| What the client reported| Requests the server saw| Lifecycle checks  
---|---|---|---|---  
`default`| `legacy`| `connected: protocol 2025-11-25`| `initialize` → `notifications/initialized` → `tools/list`| `7 pass, 0 warn, 0 fail`  
`default`| `modern`| `connect failed: ProtocolError -32601`| `initialize`| not run: the connection failed  
`auto`| `legacy`| `connected: protocol 2025-11-25`| `server/discover` → `initialize` → `notifications/initialized` → `tools/list`| `7 pass, 0 warn, 0 fail`  
`auto`| `modern`| `connected: protocol 2026-07-28`| `server/discover` → `tools/list`| `7 pass, 0 warn, 0 fail`  
  
Read the table in this order:

  1. With the default mode, the client connects to the legacy probe, and its trace passes all seven lifecycle checks.
  2. With the default mode against the modern probe, the client sends one `initialize` and the connection fails with the probe's `-32601`. Nothing is wrong with the server; the client spoke the wrong era.
  3. With `auto`, the client connects in the right era both times. Against the legacy probe the trace starts with `server/discover`, which the probe refuses, and continues with `initialize`; against the modern probe `server/discover` is followed directly by the list request. All three connected traces pass.



Use `auto` unless you know that the server speaks only the older revisions. One cost to know about, which these HTTP runs do not show: on stdio, the SDK documents that the probe runs on a short-lived sibling process "spawned from the same parameters" as your transport, "one extra spawn per connect". In `auto` mode your server command is started twice when you connect, and a server with an expensive start-up pays for it twice. Over HTTP the probe uses the connection itself.

## 6\. Putting a model in the loop

The client stops where the model begins. The model-facing loop is three steps, and the client of section 2 covers each:

Step| Client call| What to do with the result  
---|---|---  
Describe the tools| `listTools()` gives each tool's `name`, `description` and `inputSchema`| Hand them to the model in the format of its own API; keep the names  
Run what the model chose| `callTool(name, args)`| Dispatch on the four kinds, below  
Give the answer back| `ok` and `tool-error` carry text for the model| Pass the text back as the tool result; mark a `tool-error` as an error so that the model can correct its arguments  
  
Of the four kinds, `ok` and `tool-error` go back to the model. A `protocol-error` is a bug in the request or the server, and the spec says only that a client MAY show it to the model; log it and stop that branch. An `sdk-error` is the host's decision: retry the call, reconnect, or give up. The official tutorial's TypeScript tab shows one complete loop with an Anthropic model, linked under Sources. What makes a model pick the right tool and fill its arguments is the tool definition, which [tools](https://modelcontextprotocol.info/docs/concepts/tools/) and [writing effective tools](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/) cover.

## 7\. Failure modes

What you see| Why| What to do  
---|---|---  
`connect failed: ProtocolError -32601` after a single `initialize`| The default mode sent `initialize` to a server that does not answer it| Use `versionNegotiation: { mode: "auto" }` (section 5)  
`spawn … ENOENT` thrown by `connect`| The server command does not exist or is not on the path| Check the command and its working directory; the run above shows `connect` rejecting with this message  
The server's log lines appear in your terminal| The SDK's default for the child's stderr is `"inherit"`| Set `stderr` to `"ignore"` (as `src/scenarios.ts` does) or `"pipe"`; the spec lets a client capture, forward or ignore stderr and says not to treat it as an error  
Stray text on the standard output of a stdio server, for example from `console.log`| The spec reserves standard output for MCP messages: a server MUST NOT write anything else there| Log to stderr, as `src/server.ts` does  
A tool result that looks fine but is an error message| `isError: true` was ignored| Branch on `isError` before using the text; both the validation failure and the thrown exception arrived this way  
`REQUEST_TIMEOUT` from a slow tool| The tool took longer than the `timeout` of the call| Raise the timeout for that call; the connection stays usable, as the next call in the run shows  
`CONNECTION_CLOSED` in the middle of a call| The server process exited| Treat it as a lost connection: report it, then reconnect or stop  
Code copied from a 2025-revision tutorial does not compile| Those tutorials use `@modelcontextprotocol/sdk` and its subpath imports| Use the packages pinned in section 1 and the imports in `src/client.ts`  
The server starts twice on connect| On stdio, `auto` mode probes on a second process (SDK documentation)| Make start-up cheap, or keep the default mode only for servers that are known to be legacy  
  
## Versions and Verification

Everything was run on 2026-10-26 on macOS with Node.js 24.18.0, npm 11.16.0, TypeScript 7.0.2 and `@modelcontextprotocol/client` and `@modelcontextprotocol/server` 2.4.0; the recorded output in the text is that run, unedited. Statements about the SDK are checked against the text of the installed packages, statements about the protocol against one pinned commit of the official repository (`dae694f6`).

### Sources

  * Client tutorial, TypeScript tab: `docs/docs/2026-07-28/develop/build-client.mdx`; server tutorial: `docs/docs/2026-07-28/develop/build-server.mdx`. Both on the site: [Build an MCP client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/) and [Build an MCP server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/).
  * Tool errors: `docs/specification/2026-07-28/server/tools.mdx`; stdio rules and the `server/discover` probe: `basic/transports/stdio.mdx`; compatibility matrix: `basic/versioning.mdx`.
  * The SDK: the type declarations and `package.json` of `@modelcontextprotocol/client` 2.4.0 and `@modelcontextprotocol/server` 2.4.0, from npm.
  * Spec and tutorials at commit `dae694f61a31f7a3ec2af3aff709e11f70f61e48` of [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol).



[Building MCP clients-Python](https://modelcontextprotocol.info/docs/tutorials/building-a-client/ "Building MCP clients-Python")[Writing Effective MCP Tools: Names, Descriptions and Schemas](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/ "Writing Effective MCP Tools: Names, Descriptions and Schemas")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
