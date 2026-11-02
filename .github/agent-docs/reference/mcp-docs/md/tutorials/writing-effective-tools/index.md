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
    * [Writing Effective MCP Tools: Names, Descriptions and Schemas](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/)
  * [简体中文](https://mcpcn.com/docs/tutorials/writing-effective-tools/)



  * Light 

  * Dark 

  * System 




On this page

  * 1\. What the model reads, and what you control
  * 2\. Decisions that change which tool a model picks
  * 3\. Three drafts of one tool set
  * 4\. What the checker looks at
  * 5\. The selection test and what it can prove
  * 6\. Run results
  * A live listing from the official SDK
  * 7\. Test with your own model
  * 8\. Failure modes and recovery
  * 9\. What changed between revisions
  * 10\. Before you ship
  * Versions and Verification
  * Sources



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

[MCP Tutorials: From Concept to Production](https://modelcontextprotocol.info/docs/tutorials/)

Writing Effective MCP Tools: Names, Descriptions and Schemas

# Writing Effective MCP Tools: Names, Descriptions and Schemas

A model chooses a tool by reading the words you put in `tools/list`. The spec fixes what a tool definition is and a few rules for names, schemas and errors. It does not say how to write one that the model picks correctly. The sections below separate three layers so you can tell them apart: what the spec requires, what the schema's defaults imply, and design heuristics that come from the script below and are not spec text. It ends with a checker you can run on your own listing and a selection test that ranks your tools for your own tasks.

For the protocol side of a tool call (messages, schemas per revision, error channels, SDK behaviour), read [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/). For the rules a remote server must pass, read [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/). The spec text is in [Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/).

## 1\. What the model reads, and what you control

The spec does not fix what a client passes to the model, and its argument for a deterministic order speaks of the case "when tools are included in model context". Assume that anything in the listing may reach the model. The table says what to write in each field and where the rule comes from.

Field| What to write| Basis  
---|---|---  
`name`| Verb plus object, one naming style, unique in the server; 1 to 128 characters from `A-Z a-z 0-9 _ - .`, case-sensitive| Spec, "Tool Names" (SHOULD)  
`title`| A label for people. Clients use it for display; do not rely on the model seeing it| Spec: "Optional human-readable name of the tool for display purposes"  
`description`| What the tool does, when to use it, and when to use a neighbour instead. The schema marks it optional; the checker warns below 8 words| Spec: "Human-readable description of functionality"; the word count is a heuristic  
`inputSchema`| A valid JSON Schema object, never `null`. Describe every parameter or give an `enum`; declare `required` even when it is empty. For a tool without parameters use `{ "type": "object", "additionalProperties": false }`| Spec, "Tool" (MUST for the object; the closed form is recommended)  
`outputSchema`, `structuredContent`| Declare `outputSchema` when the result is structured. Results MUST conform to it; also return the serialized JSON in a text block for older clients| Spec, "Output Schema", "Structured Content"  
`annotations`| Declare `readOnlyHint` and `destructiveHint` truthfully. Omitted hints mean the schema defaults: `readOnlyHint` false, `destructiveHint` true, `idempotentHint` false, `openWorldHint` true. Clients MUST treat annotations as untrusted unless the server is trusted| Official `schema.json`; spec, "Tool"  
`isError` result text| For a failure the model can fix, say what was wrong and what is valid. Clients SHOULD show execution errors to the model| Spec, "Error Handling"  
`tools/list` order and size| Return tools in a deterministic order. The checker prints the size of the listing in bytes| Spec, "Capabilities" (SHOULD for order)  
  
## 2\. Decisions that change which tool a model picks

Each row is a choice you make while writing definitions. The last column names the check of the script in section 4 that covers it, or says that nothing does.

Decision| Choose| Why| Checked by  
---|---|---|---  
One tool with an `action` parameter, or one tool per operation| One tool per operation when the effects differ (read, write, delete)| Annotations describe the tool as a whole; a tool that can both read and delete cannot carry a truthful `readOnlyHint` or `destructiveHint`| `annotations`  
A short generic name or an object-first name| `tickets_search`, not `search`| Names must be unique within a server; clients that merge servers may meet two `search` tools and are told to disambiguate by prefix. A name that already says the object stays meaningful without a prefix| `name-generic`, `name-unique`  
Free text or `enum` for a closed set of values| `enum`| The model sees the allowed values in the definition instead of guessing them| `params-described`  
Which arguments are mandatory| Declare `required`, with an empty list when all are optional| Without it the definition does not say what the call needs| `params-required`  
An object-valued parameter| Give it `properties`| A bare `{"type": "object"}` tells the model nothing about its content| `params-opaque`  
How to tell two neighbours apart| Say in each description when to use it and when to use the other; use the words your users use| The draft in section 6 failed a task because a neighbour's description contained the task's words and the right tool did not| `near-duplicate`, selection test  
State across calls| Return an explicit handle from a creation tool and take it as an argument later; state the retention in the creation tool's description| MCP has no protocol-level session. Spec: an expired or unknown handle should return an execution error that says so| No  
A destructive operation| Set `destructiveHint`; expect the client to ask the user| The spec wants a human able to deny tool calls; hints are not a security control because clients must treat them as untrusted| `annotations`  
A result that can be large| Add filters and a limit, and name the limit in the description (`at most 20 per call`)| The spec gives no size; decide the cap from what your real calls return| No  
A failure the model can fix| Return `isError: true` with the rule and the valid form (a date in the past, a value out of range)| Spec: execution errors "contain actionable feedback that language models can use to self-correct"| No; see [tools, section 5](https://modelcontextprotocol.info/docs/concepts/tools/)  
  
## 3\. Three drafts of one tool set

The same eight intents (show a ticket, search, close, delete, summarize a week, look up a user, comment, create) are written three times. The fixtures are hand-written.

Set| Names| Descriptions| Parameters| Annotations  
---|---|---|---|---  
`confusing-tools.json`| `get_data`, `fetch_data`, `query`, `search`, `find`, `run`, `create`, `update`, `delete`| Two to six words ("Update ticket data.")| Bare strings and objects, no `required`| None  
`draft-tools.json`| `tickets_get`, `tickets_search`, `tickets_create`, `tickets_update_status`, `tickets_add_comment`, `tickets_delete`, `users_find`, `reports_weekly_summary`| A sentence or two that says when to use the tool| Described, `enum` for statuses, `required` declared| Declared  
`clear-tools.json`| Same as the draft| The draft with five descriptions reworded after the failures in section 6| Same| Same  
**confusing-tools.json**
    
    
    {"jsonrpc": "2.0", "id": 1, "result": {"resultType": "complete", "ttlMs": 0, "cacheScope": "public", "tools": [
      {"name": "get_data", "description": "Get ticket data by id.", "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}}},
      {"name": "fetch_data", "description": "Fetch ticket data.", "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}}},
      {"name": "query", "description": "Query ticket data with a filter.", "inputSchema": {"type": "object", "properties": {"filter": {"type": "object"}}}},
      {"name": "search", "description": "Search ticket data.", "inputSchema": {"type": "object", "properties": {"q": {"type": "string"}}}},
      {"name": "find", "description": "Find ticket or user data.", "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}}}},
      {"name": "run", "description": "Run a report job.", "inputSchema": {"type": "object", "properties": {"job": {"type": "string"}}}},
      {"name": "create", "description": "Create a new ticket.", "inputSchema": {"type": "object", "properties": {"data": {"type": "object"}}}},
      {"name": "update", "description": "Update ticket data.", "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}, "data": {"type": "object"}}}},
      {"name": "delete", "description": "Delete ticket data.", "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}}}
    ]}}

**draft-tools.json**
    
    
    {"jsonrpc": "2.0", "id": 1, "result": {"resultType": "complete", "ttlMs": 0, "cacheScope": "public", "tools": [
      {"name": "tickets_get", "description": "Return one support ticket (title, status, assignee, comments) when you already know its numeric id. Use tickets_search when the id is not known.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}}, "required": ["ticket_id"]}, "annotations": {"readOnlyHint": true}},
      {"name": "tickets_search", "description": "List support tickets that match a status, an assignee or free text, newest first, at most 20 per call. Use this to find ticket ids; it does not change anything.", "inputSchema": {"type": "object", "properties": {"status": {"type": "string", "enum": ["open", "resolved", "closed"], "description": "Only tickets in this status."}, "assignee": {"type": "string", "description": "User name or id of the assignee."}, "text": {"type": "string", "description": "Words that must appear in the title or a comment."}}, "required": []}, "annotations": {"readOnlyHint": true}},
      {"name": "tickets_create", "description": "Create a new support ticket and return its id. Use it only for a problem that has no ticket yet; search first to avoid duplicates.", "inputSchema": {"type": "object", "properties": {"title": {"type": "string", "description": "One-line summary of the problem."}, "body": {"type": "string", "description": "Steps to reproduce and expected behaviour."}}, "required": ["title"]}, "annotations": {"readOnlyHint": false, "destructiveHint": false}},
      {"name": "tickets_update_status", "description": "Move one ticket to a new status. Use it to close, resolve or reopen a ticket; it does not add comments.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}, "status": {"type": "string", "enum": ["open", "resolved", "closed"], "description": "The new status."}}, "required": ["ticket_id", "status"]}, "annotations": {"readOnlyHint": false, "destructiveHint": false, "idempotentHint": true}},
      {"name": "tickets_add_comment", "description": "Append a comment to one ticket. Use it for notes and replies; comments cannot be edited afterwards.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}, "comment": {"type": "string", "description": "Comment text, plain text only."}}, "required": ["ticket_id", "comment"]}, "annotations": {"readOnlyHint": false, "destructiveHint": false}},
      {"name": "tickets_delete", "description": "Permanently delete one ticket and its comments. This cannot be undone; use tickets_update_status to close a ticket instead.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}}, "required": ["ticket_id"]}, "annotations": {"readOnlyHint": false, "destructiveHint": true, "idempotentHint": true}},
      {"name": "users_find", "description": "Look up users by name or email and return their ids. Use it to turn a person's name into the assignee value of tickets_search.", "inputSchema": {"type": "object", "properties": {"name": {"type": "string", "description": "Full or partial name, or an email address."}}, "required": ["name"]}, "annotations": {"readOnlyHint": true}},
      {"name": "reports_weekly_summary", "description": "Write the weekly summary of closed tickets for one team as markdown. Reads tickets only.", "inputSchema": {"type": "object", "properties": {"team": {"type": "string", "description": "Team name, for example support."}}, "required": ["team"]}, "annotations": {"readOnlyHint": true}}
    ]}}

**clear-tools.json**
    
    
    {"jsonrpc": "2.0", "id": 1, "result": {"resultType": "complete", "ttlMs": 0, "cacheScope": "public", "tools": [
      {"name": "tickets_get", "description": "Show one support ticket (title, status, assignee, comments) when you already know its numeric id. Use tickets_search when the id is not known.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}}, "required": ["ticket_id"]}, "annotations": {"readOnlyHint": true}},
      {"name": "tickets_search", "description": "Find support tickets by status (open, resolved, closed), by who they are assigned to, or by free text, newest first, at most 20 per call. Use this to find ticket ids; it does not change anything.", "inputSchema": {"type": "object", "properties": {"status": {"type": "string", "enum": ["open", "resolved", "closed"], "description": "Only tickets in this status."}, "assignee": {"type": "string", "description": "User name or id of the assignee."}, "text": {"type": "string", "description": "Words that must appear in the title or a comment."}}, "required": []}, "annotations": {"readOnlyHint": true}},
      {"name": "tickets_create", "description": "Create a new support ticket and return its id. Use it only for a problem that has no ticket yet; run tickets_search first so the problem is not filed twice.", "inputSchema": {"type": "object", "properties": {"title": {"type": "string", "description": "One-line summary of the problem."}, "body": {"type": "string", "description": "Steps to reproduce and expected behaviour."}}, "required": ["title"]}, "annotations": {"readOnlyHint": false, "destructiveHint": false}},
      {"name": "tickets_update_status", "description": "Move one ticket to a new status: close it, mark it resolved, or reopen it. It does not add comments.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}, "status": {"type": "string", "enum": ["open", "resolved", "closed"], "description": "The new status."}}, "required": ["ticket_id", "status"]}, "annotations": {"readOnlyHint": false, "destructiveHint": false, "idempotentHint": true}},
      {"name": "tickets_add_comment", "description": "Append a comment to one ticket. Use it for notes and replies; comments cannot be edited afterwards.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}, "comment": {"type": "string", "description": "Comment text, plain text only."}}, "required": ["ticket_id", "comment"]}, "annotations": {"readOnlyHint": false, "destructiveHint": false}},
      {"name": "tickets_delete", "description": "Permanently remove one ticket and its comments. This cannot be undone; to keep the history, change the status instead.", "inputSchema": {"type": "object", "properties": {"ticket_id": {"type": "integer", "description": "Numeric ticket id, for example 4521."}}, "required": ["ticket_id"]}, "annotations": {"readOnlyHint": false, "destructiveHint": true, "idempotentHint": true}},
      {"name": "users_find", "description": "Look up users by name or email and return their ids. Use it to turn a person's name into the assignee value of tickets_search.", "inputSchema": {"type": "object", "properties": {"name": {"type": "string", "description": "Full or partial name, or an email address."}}, "required": ["name"]}, "annotations": {"readOnlyHint": true}},
      {"name": "reports_weekly_summary", "description": "Write the weekly summary of closed tickets for one team as markdown. Reads tickets only.", "inputSchema": {"type": "object", "properties": {"team": {"type": "string", "description": "Team name, for example support."}}, "required": ["team"]}, "annotations": {"readOnlyHint": true}}
    ]}}

**tasks-confusing.json**
    
    
    [
      {"task": "Show me ticket 4521", "expect": "get_data"},
      {"task": "Find open tickets assigned to Maria", "expect": "search"},
      {"task": "Close ticket 4521 as resolved", "expect": "update"},
      {"task": "Remove the duplicate ticket 4533", "expect": "delete"},
      {"task": "Write the weekly summary of closed tickets for the support team", "expect": "run"},
      {"task": "Look up the user named Maria Chen", "expect": "find"},
      {"task": "Add a comment to ticket 4521 saying the fix is deployed", "expect": "update"},
      {"task": "Create a new ticket for the login bug", "expect": "create"}
    ]

**tasks-clear.json**
    
    
    [
      {"task": "Show me ticket 4521", "expect": "tickets_get"},
      {"task": "Find open tickets assigned to Maria", "expect": "tickets_search"},
      {"task": "Close ticket 4521 as resolved", "expect": "tickets_update_status"},
      {"task": "Remove the duplicate ticket 4533", "expect": "tickets_delete"},
      {"task": "Write the weekly summary of closed tickets for the support team", "expect": "reports_weekly_summary"},
      {"task": "Look up the user named Maria Chen", "expect": "users_find"},
      {"task": "Add a comment to ticket 4521 saying the fix is deployed", "expect": "tickets_add_comment"},
      {"task": "Create a new ticket for the login bug", "expect": "tickets_create"}
    ]

## 4\. What the checker looks at

`tool_design_check.py` reads a saved `tools/list` response (plain JSON or one SSE data line), its `result`, or a bare array of tools. FAIL means a rule of the spec on names or `inputSchema` is broken, or a selection task is answered wrongly; WARN means a heuristic of the script is not met. The exit code is 0 without FAIL, 1 with at least one FAIL, and 2 when the input cannot be read.

Check| Level| What it flags| Basis  
---|---|---|---  
`list-complete`| WARN| `nextCursor` is present, so only the first page was read| Pagination of `tools/list`  
`name-spec`| FAIL| A name outside 1 to 128 characters of `A-Z a-z 0-9 _ - .`| Spec, "Tool Names"  
`name-unique`| FAIL| The same name twice| Spec, "Tool Names"  
`name-case-collision`| WARN| Two names that differ only in case or separators (`TicketsGet`, `tickets_get`)| Heuristic  
`name-style`| WARN| More than one of snake_case, kebab-case, dotted and camelCase| Heuristic  
`name-generic`| WARN| A name made only of generic words such as `get`, `data`, `run`, `search`| Heuristic  
`input-schema`| FAIL| `inputSchema` is not an object| Spec, "Tool"  
`description`| WARN| No description, or fewer than 8 words| Heuristic  
`params-described`| WARN| A parameter with no description, `enum` or `const`| Heuristic  
`params-required`| WARN| Parameters declared but no `required` key| Heuristic  
`params-opaque`| WARN| An object parameter without `properties`| Heuristic  
`no-params-closed`| WARN| A tool without parameters that lacks `additionalProperties: false`| Spec, "Tool" (recommended)  
`annotations`| WARN| The first verb in the name (from the script's read and write lists) decides: a read verb without `readOnlyHint`, or a write verb with neither `readOnlyHint` nor `destructiveHint`| Heuristic on the schema defaults  
`near-duplicate`| WARN| Two descriptions that share half of their words or more| Heuristic  
`select-N`| FAIL or WARN| Task N: the expected tool is not the top-ranked tool, no word of the task appears in any definition, or the runner-up scores within 80 percent of the winner| Section 5  
  
`SHORT = 8`, `DUPLICATE = 0.5` and `AMBIGUOUS = 0.8` are settings of the script. They have no official source; change them when your definitions are written in another style. The verb lists are short and by name only, so `add` in an arithmetic tool is reported as a write verb (section 6 shows it).

**tool_design_check.py**
    
    
     #!/usr/bin/env python3
    """Check how well MCP tool definitions help a model choose and call the right tool, and run a selection test.
    
    Usage: tool_design_check.py SOURCE [--tasks FILE]
    SOURCE: JSON file ("-" = stdin) holding a tools/list response (plain JSON or one SSE data line), its result,
    or a tools array.
    --tasks: JSON array of {"task": "...", "expect": "tool_name"}. Each task is ranked against the tools by weighted
    word overlap, a stand-in for a model that only has the words of your definitions to go on.
    Levels: FAIL = a rule of the spec on names or inputSchema is broken, or a selection task is answered wrongly;
    WARN = a design heuristic of this script is not met (heuristics are not spec text).
    Exit code: 0 no FAIL, 1 at least one FAIL, 2 the input cannot be read.
    """
    import argparse
    import json
    import math
    import re
    import sys
    
    NAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,128}$")
    RUN_RE = re.compile(r"[A-Za-z0-9]+")
    PART_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|[0-9]+")
    STOP = set("a an the of to in on for and or is are be it this that with by from as at when you your use used "
               "using into any all not no if then than can will which what who whom i me my we our".split())
    GENERIC = set("get fetch query run do execute data info information tool process handle search find list update "
                  "delete create read write call action item thing stuff object result record manage".split())
    WRITE_VERBS = set("create update delete remove drop send write set add post put patch cancel close publish deploy "
                      "insert upload reset clear edit rename move run execute".split())
    READ_VERBS = set("get list search find read fetch query lookup show view describe check".split())
    AMBIGUOUS = 0.8       # the runner-up scores at least this share of the winner: the definitions do not separate
    DUPLICATE = 0.5       # Jaccard overlap of two descriptions that is reported as a near-duplicate
    SHORT = 8             # a description with fewer words cannot say both what the tool does and when to use it
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    
    
    def report(name, ok, detail, level="WARN"):
        status = "PASS" if ok else level
        counts[status] += 1
        print("%s %s: %s" % (status, name, detail))
    
    
    def tokens(text):
        """Lower-case word parts of `text`, split at camelCase, digits and separators, plural 's' folded."""
        out = []
        for run in RUN_RE.findall(text or ""):
            for part in PART_RE.findall(run):
                t = part.lower()
                if t not in STOP and len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
                    t = t[:-1]
                out.append(t)
        return out
    
    
    def content(text):
        return {t for t in tokens(text) if t not in STOP}
    
    
    def style(name):
        for mark, label in (("_", "snake_case"), ("-", "kebab-case"), (".", "dotted")):
            if mark in name:
                return label
        return "camelCase" if re.search(r"[a-z][A-Z]", name) else None
    
    
    def load(source):
        """Return the tools array of a tools/list response, its result, or a bare array; and the result envelope."""
        text = sys.stdin.read() if source == "-" else open(source, encoding="utf-8").read()
        try:
            data = json.loads(text)
        except ValueError:
            data = None
            for line in reversed(text.splitlines()):
                if line.startswith("data:"):
                    data = json.loads(line[5:].strip())
                    break
            if data is None:
                raise ValueError("%s holds neither JSON nor an SSE data line" % source)
        if isinstance(data, dict) and "error" in data:
            raise ValueError("the response is a JSON-RPC error: %s" % json.dumps(data["error"])[:160])
        data = data.get("result", data) if isinstance(data, dict) else data
        tools = data.get("tools") if isinstance(data, dict) else data
        if not isinstance(tools, list):
            raise ValueError("no tools array found in %s" % source)
        return tools, data if isinstance(data, dict) else {}
    
    
    def lint(tools, envelope):
        names = [t["name"] for t in tools]
        size = len(json.dumps(tools, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))
        print("INFO %d tools, %d bytes as compact JSON (a client sends this, in some form, to the model)"
              % (len(tools), size))
        report("list-complete", not envelope.get("nextCursor"), "the listing has no further page"
               if not envelope.get("nextCursor") else "nextCursor present: only the first page was read")
        bad = [n for n in names if not NAME_RE.match(n)]
        report("name-spec", not bad, "all names are 1-128 characters from A-Z a-z 0-9 _ - ." if not bad
               else "outside the allowed set: %s" % ", ".join(repr(n) for n in bad), "FAIL")
        dup = sorted({n for n in names if names.count(n) > 1})
        report("name-unique", not dup, "every name is unique" if not dup else "repeated: %s" % ", ".join(dup), "FAIL")
        folded = {}
        for n in names:
            folded.setdefault("".join(tokens(n)), []).append(n)
        clash = [v for v in folded.values() if len(set(v)) > 1]
        report("name-case-collision", not clash, "no two names differ only in case or separators" if not clash
               else "differ only in case or separators: %s" % "; ".join(" / ".join(sorted(set(v))) for v in clash))
        styles = sorted({s for s in map(style, names) if s})
        report("name-style", len(styles) < 2, "one naming style%s" % (" (%s)" % styles[0] if styles else "")
               if len(styles) < 2 else "mixed styles: %s" % ", ".join(styles))
        generic = [n for n in names if tokens(n) and set(tokens(n)) <= GENERIC]
        report("name-generic", not generic, "every name says which object it works on" if not generic
               else "names that never say which object: %s" % ", ".join(generic))
        for t in tools:
            n = t["name"]
            desc = t.get("description")
            schema = t.get("inputSchema")
            ok = isinstance(schema, dict)
            report("input-schema:%s" % n, ok, "inputSchema is a JSON Schema object" if ok
                   else "inputSchema must be an object, got %s" % type(schema).__name__, "FAIL")
            schema = schema if ok else {}
            words = tokens(desc) if isinstance(desc, str) else []
            report("description:%s" % n, len(words) >= SHORT, "%d words" % len(words) if len(words) >= SHORT
                   else ("no description" if not words else "%d words, fewer than %d" % (len(words), SHORT)))
            props = schema.get("properties") if isinstance(schema.get("properties"), dict) else {}
            loose = [k for k, v in props.items() if not isinstance(v, dict)
                     or not (v.get("description") or "enum" in v or "const" in v)]
            report("params-described:%s" % n, not loose, "every parameter has a description, enum or const"
                   if not loose else "no description or enum: %s" % ", ".join(loose))
            if props:
                report("params-required:%s" % n, "required" in schema, "required is declared"
                       if "required" in schema else "no `required` (use an empty list when all are optional)")
            opaque = [k for k, v in props.items() if isinstance(v, dict) and v.get("type") == "object"
                      and not v.get("properties")]
            report("params-opaque:%s" % n, not opaque, "no free-form object parameter" if not opaque
                   else "object parameter without `properties`: %s" % ", ".join(opaque))
            if not props:
                closed = schema.get("additionalProperties") is False
                report("no-params-closed:%s" % n, closed, "closed with additionalProperties: false" if closed
                       else "a tool without parameters should say additionalProperties: false")
            verb = next((w for w in tokens(n) if w in WRITE_VERBS or w in READ_VERBS), None)
            hints = t.get("annotations") if isinstance(t.get("annotations"), dict) else {}
            if verb:
                want = ("readOnlyHint", "destructiveHint") if verb in WRITE_VERBS else ("readOnlyHint",)
                done = any(k in hints for k in want)
                report("annotations:%s" % n, done, "%s is set" % " or ".join(want) if done
                       else "`%s` is not set; the schema default says the tool may modify and be destructive"
                       % "` or `".join(want))
        docs = {t["name"]: content(t.get("description") or "") for t in tools}
        pairs = []
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                union = docs[a] | docs[b]
                if a != b and union and len(docs[a] & docs[b]) / len(union) >= DUPLICATE:
                    pairs.append("%s and %s (%.0f%%)" % (a, b, 100 * len(docs[a] & docs[b]) / len(union)))
        report("near-duplicate", not pairs, "no two descriptions overlap by %.0f%% or more" % (100 * DUPLICATE)
               if not pairs else "descriptions that share most of their words: %s" % "; ".join(pairs))
    
    
    def select(tools, tasks):
        """Rank every tool for every task; a tool wins by weighted word overlap, name words count three times."""
        docs = []
        for t in tools:
            body = content(t.get("title")) | content(t.get("description"))
            props = (t.get("inputSchema") or {}).get("properties")
            for k, v in (props.items() if isinstance(props, dict) else []):
                v = v if isinstance(v, dict) else {}
                body |= content(k) | content(v.get("description"))
                for choice in v.get("enum") or []:
                    body |= content(choice) if isinstance(choice, str) else set()
            docs.append((content(t["name"]), body))
        df = {}
        for name_t, body_t in docs:
            for w in name_t | body_t:
                df[w] = df.get(w, 0) + 1
        good = ambiguous = wrong = 0
        for i, item in enumerate(tasks, 1):
            want = item["expect"]
            scores = []
            for t, (name_t, body_t) in zip(tools, docs):
                s = 0.0
                for w in content(item["task"]):
                    if w in df:
                        weight = math.log(1 + len(tools) / df[w])
                        s += 3 * weight if w in name_t else weight if w in body_t else 0
                scores.append((s, t["name"]))
            scores.sort(key=lambda p: (-p[0], p[1]))
            top = scores[0][0]
            mine = next((s for s, n in scores if n == want), None)
            label = "select-%d" % i
            shown = item["task"] if len(item["task"]) <= 50 else item["task"][:47] + "..."
            if mine is None:
                report(label, False, "expected tool %r is not in the listing" % want, "FAIL")
                wrong += 1
            elif top == 0:
                report(label, False, '"%s": no word of the task appears in any definition' % shown, "FAIL")
                wrong += 1
            elif mine < top:
                report(label, False, '"%s": %s wins (%.1f), %s scores %.1f' % (shown, scores[0][1], top, want, mine),
                       "FAIL")
                wrong += 1
            else:
                runner = next((p for p in scores if p[1] != want), (0.0, "-"))
                if runner[0] >= AMBIGUOUS * top:
                    report(label, False, '"%s": %s (%.1f) is not clearly ahead of %s (%.1f)'
                           % (shown, want, top, runner[1], runner[0]))
                    ambiguous += 1
                else:
                    report(label, True, '"%s": %s (%.1f), next %s %.1f' % (shown, want, top, runner[1], runner[0]))
                    good += 1
        print("INFO selection: %d tasks, %d clear, %d ambiguous, %d wrong or not found"
              % (len(tasks), good, ambiguous, wrong))
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("source")
        ap.add_argument("--tasks", help="JSON file with [{\"task\": ..., \"expect\": tool name}]")
        args = ap.parse_args()
        try:
            tools, envelope = load(args.source)
            bad = [t for t in tools if not isinstance(t, dict) or not isinstance(t.get("name"), str)]
            if bad:
                raise ValueError("%d entries of the tools array have no string `name`" % len(bad))
            tasks = json.load(open(args.tasks, encoding="utf-8")) if args.tasks else []
            if not all(isinstance(i, dict) and isinstance(i.get("task"), str) and isinstance(i.get("expect"), str)
                       for i in tasks):
                raise ValueError("every task needs string fields `task` and `expect`")
        except (OSError, ValueError) as exc:
            print("ERROR %s" % exc)
            return 2
        lint(tools, envelope)
        if tasks:
            select(tools, tasks)
        print("%d pass, %d warn, %d fail" % (counts["PASS"], counts["WARN"], counts["FAIL"]))
        return 1 if counts["FAIL"] else 0
    
    
    if __name__ == "__main__":
        sys.exit(main())

## 5\. The selection test and what it can prove

The selection test is a word-overlap ranker, not a language model. It finds definitions that share too few words with a task, or too many with each other. It cannot say how your model behaves.

For each task the script ranks every tool. Words are lower-cased, split at camelCase, digits and separators, common words are dropped, and a plural `s` is folded. A word that occurs in the name counts three times, a word in the title, description, a parameter name, a parameter description or an `enum` value counts once, and each word is weighted by `ln(1 + N / df)`, where N is the number of tools and df the number of tools that contain the word, so a word shared by many tools counts less. A task is **clear** when the expected tool wins and the runner-up scores below 80 percent of it, **ambiguous** when the margin is smaller (a tie included), and **wrong** when another tool wins or no word of the task appears anywhere.

What a run can show:

  * A **vocabulary gap** : the words your users use appear in no definition. The model has to bridge it with its own knowledge.
  * **Overlap** : two tools look alike to a ranker, so the model has little to choose on.
  * A **word magnet** : a neighbour's description contains the task's words and the right tool's does not.



What it cannot show: that a model chooses correctly. A model reads meaning, not words, and may bridge a gap the ranker cannot. A FAIL says "this definition leaves the choice to the model", not "the model fails".

## 6\. Run results

The commands run from the folder that holds the script and the fixtures.
    
    
    python3 tool_design_check.py confusing-tools.json --tasks tasks-confusing.json
    python3 tool_design_check.py draft-tools.json --tasks tasks-clear.json
    python3 tool_design_check.py clear-tools.json --tasks tasks-clear.json

Set| Result line| Selection| Exit code  
---|---|---|---  
`confusing-tools.json`| `22 pass, 45 warn, 2 fail`| 2 clear, 4 ambiguous, 2 wrong| 1  
`draft-tools.json`| `59 pass, 1 warn, 2 fail`| 5 clear, 1 ambiguous, 2 wrong| 1  
`clear-tools.json`| `62 pass, 0 warn, 0 fail`| 8 clear| 0  
**Recorded output: confusing-tools.json**
    
    
     INFO 9 tools, 1170 bytes as compact JSON (a client sends this, in some form, to the model)
    PASS list-complete: the listing has no further page
    PASS name-spec: all names are 1-128 characters from A-Z a-z 0-9 _ - .
    PASS name-unique: every name is unique
    PASS name-case-collision: no two names differ only in case or separators
    PASS name-style: one naming style (snake_case)
    WARN name-generic: names that never say which object: get_data, fetch_data, query, search, find, run, create, update, delete
    PASS input-schema:get_data: inputSchema is a JSON Schema object
    WARN description:get_data: 5 words, fewer than 8
    WARN params-described:get_data: no description or enum: id
    WARN params-required:get_data: no `required` (use an empty list when all are optional)
    PASS params-opaque:get_data: no free-form object parameter
    WARN annotations:get_data: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:fetch_data: inputSchema is a JSON Schema object
    WARN description:fetch_data: 3 words, fewer than 8
    WARN params-described:fetch_data: no description or enum: id
    WARN params-required:fetch_data: no `required` (use an empty list when all are optional)
    PASS params-opaque:fetch_data: no free-form object parameter
    WARN annotations:fetch_data: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:query: inputSchema is a JSON Schema object
    WARN description:query: 6 words, fewer than 8
    WARN params-described:query: no description or enum: filter
    WARN params-required:query: no `required` (use an empty list when all are optional)
    WARN params-opaque:query: object parameter without `properties`: filter
    WARN annotations:query: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:search: inputSchema is a JSON Schema object
    WARN description:search: 3 words, fewer than 8
    WARN params-described:search: no description or enum: q
    WARN params-required:search: no `required` (use an empty list when all are optional)
    PASS params-opaque:search: no free-form object parameter
    WARN annotations:search: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:find: inputSchema is a JSON Schema object
    WARN description:find: 5 words, fewer than 8
    WARN params-described:find: no description or enum: text
    WARN params-required:find: no `required` (use an empty list when all are optional)
    PASS params-opaque:find: no free-form object parameter
    WARN annotations:find: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:run: inputSchema is a JSON Schema object
    WARN description:run: 4 words, fewer than 8
    WARN params-described:run: no description or enum: job
    WARN params-required:run: no `required` (use an empty list when all are optional)
    PASS params-opaque:run: no free-form object parameter
    WARN annotations:run: `readOnlyHint` or `destructiveHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:create: inputSchema is a JSON Schema object
    WARN description:create: 4 words, fewer than 8
    WARN params-described:create: no description or enum: data
    WARN params-required:create: no `required` (use an empty list when all are optional)
    WARN params-opaque:create: object parameter without `properties`: data
    WARN annotations:create: `readOnlyHint` or `destructiveHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:update: inputSchema is a JSON Schema object
    WARN description:update: 3 words, fewer than 8
    WARN params-described:update: no description or enum: id, data
    WARN params-required:update: no `required` (use an empty list when all are optional)
    WARN params-opaque:update: object parameter without `properties`: data
    WARN annotations:update: `readOnlyHint` or `destructiveHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:delete: inputSchema is a JSON Schema object
    WARN description:delete: 3 words, fewer than 8
    WARN params-described:delete: no description or enum: id
    WARN params-required:delete: no `required` (use an empty list when all are optional)
    PASS params-opaque:delete: no free-form object parameter
    WARN annotations:delete: `readOnlyHint` or `destructiveHint` is not set; the schema default says the tool may modify and be destructive
    WARN near-duplicate: descriptions that share most of their words: fetch_data and search (50%); fetch_data and update (50%); fetch_data and delete (50%); search and update (50%); search and delete (50%); update and delete (50%)
    WARN select-1: "Show me ticket 4521": get_data (0.8) is not clearly ahead of create (0.8)
    FAIL select-2: "Find open tickets assigned to Maria": find wins (7.7), search scores 0.8
    WARN select-3: "Close ticket 4521 as resolved": update (0.8) is not clearly ahead of create (0.8)
    WARN select-4: "Remove the duplicate ticket 4533": delete (0.8) is not clearly ahead of create (0.8)
    FAIL select-5: "Write the weekly summary of closed tickets for ...": create wins (0.8), run scores 0.0
    PASS select-6: "Look up the user named Maria Chen": find (2.3), next create 0.0
    WARN select-7: "Add a comment to ticket 4521 saying the fix is ...": update (0.8) is not clearly ahead of create (0.8)
    PASS select-8: "Create a new ticket for the login bug": create (10.0), next delete 0.8
    INFO selection: 8 tasks, 2 clear, 4 ambiguous, 2 wrong or not found
    22 pass, 45 warn, 2 fail

**Recorded output: draft-tools.json**
    
    
     INFO 8 tools, 3431 bytes as compact JSON (a client sends this, in some form, to the model)
    PASS list-complete: the listing has no further page
    PASS name-spec: all names are 1-128 characters from A-Z a-z 0-9 _ - .
    PASS name-unique: every name is unique
    PASS name-case-collision: no two names differ only in case or separators
    PASS name-style: one naming style (snake_case)
    PASS name-generic: every name says which object it works on
    PASS input-schema:tickets_get: inputSchema is a JSON Schema object
    PASS description:tickets_get: 24 words
    PASS params-described:tickets_get: every parameter has a description, enum or const
    PASS params-required:tickets_get: required is declared
    PASS params-opaque:tickets_get: no free-form object parameter
    PASS annotations:tickets_get: readOnlyHint is set
    PASS input-schema:tickets_search: inputSchema is a JSON Schema object
    PASS description:tickets_search: 30 words
    PASS params-described:tickets_search: every parameter has a description, enum or const
    PASS params-required:tickets_search: required is declared
    PASS params-opaque:tickets_search: no free-form object parameter
    PASS annotations:tickets_search: readOnlyHint is set
    PASS input-schema:tickets_create: inputSchema is a JSON Schema object
    PASS description:tickets_create: 25 words
    PASS params-described:tickets_create: every parameter has a description, enum or const
    PASS params-required:tickets_create: required is declared
    PASS params-opaque:tickets_create: no free-form object parameter
    PASS annotations:tickets_create: readOnlyHint or destructiveHint is set
    PASS input-schema:tickets_update_status: inputSchema is a JSON Schema object
    PASS description:tickets_update_status: 21 words
    PASS params-described:tickets_update_status: every parameter has a description, enum or const
    PASS params-required:tickets_update_status: required is declared
    PASS params-opaque:tickets_update_status: no free-form object parameter
    PASS annotations:tickets_update_status: readOnlyHint or destructiveHint is set
    PASS input-schema:tickets_add_comment: inputSchema is a JSON Schema object
    PASS description:tickets_add_comment: 17 words
    PASS params-described:tickets_add_comment: every parameter has a description, enum or const
    PASS params-required:tickets_add_comment: required is declared
    PASS params-opaque:tickets_add_comment: no free-form object parameter
    PASS annotations:tickets_add_comment: readOnlyHint or destructiveHint is set
    PASS input-schema:tickets_delete: inputSchema is a JSON Schema object
    PASS description:tickets_delete: 20 words
    PASS params-described:tickets_delete: every parameter has a description, enum or const
    PASS params-required:tickets_delete: required is declared
    PASS params-opaque:tickets_delete: no free-form object parameter
    PASS annotations:tickets_delete: readOnlyHint or destructiveHint is set
    PASS input-schema:users_find: inputSchema is a JSON Schema object
    PASS description:users_find: 26 words
    PASS params-described:users_find: every parameter has a description, enum or const
    PASS params-required:users_find: required is declared
    PASS params-opaque:users_find: no free-form object parameter
    PASS annotations:users_find: readOnlyHint is set
    PASS input-schema:reports_weekly_summary: inputSchema is a JSON Schema object
    PASS description:reports_weekly_summary: 15 words
    PASS params-described:reports_weekly_summary: every parameter has a description, enum or const
    PASS params-required:reports_weekly_summary: required is declared
    PASS params-opaque:reports_weekly_summary: no free-form object parameter
    PASS near-duplicate: no two descriptions overlap by 50% or more
    WARN select-1: "Show me ticket 4521": tickets_get (3.2) is not clearly ahead of tickets_add_comment (3.2)
    FAIL select-2: "Find open tickets assigned to Maria": users_find wins (5.5), tickets_search scores 5.3
    PASS select-3: "Close ticket 4521 as resolved": tickets_update_status (6.4), next tickets_delete 4.8
    FAIL select-4: "Remove the duplicate ticket 4533": tickets_create wins (4.3), tickets_delete scores 2.1
    PASS select-5: "Write the weekly summary of closed tickets for ...": reports_weekly_summary (18.9), next tickets_create 4.8
    PASS select-6: "Look up the user named Maria Chen": users_find (9.2), next tickets_search 1.6
    PASS select-7: "Add a comment to ticket 4521 saying the fix is ...": tickets_add_comment (10.9), next tickets_update_status 5.7
    PASS select-8: "Create a new ticket for the login bug": tickets_create (10.3), next tickets_update_status 3.7
    INFO selection: 8 tasks, 5 clear, 1 ambiguous, 2 wrong or not found
    59 pass, 1 warn, 2 fail

**Recorded output: clear-tools.json**
    
    
     INFO 8 tools, 3482 bytes as compact JSON (a client sends this, in some form, to the model)
    PASS list-complete: the listing has no further page
    PASS name-spec: all names are 1-128 characters from A-Z a-z 0-9 _ - .
    PASS name-unique: every name is unique
    PASS name-case-collision: no two names differ only in case or separators
    PASS name-style: one naming style (snake_case)
    PASS name-generic: every name says which object it works on
    PASS input-schema:tickets_get: inputSchema is a JSON Schema object
    PASS description:tickets_get: 24 words
    PASS params-described:tickets_get: every parameter has a description, enum or const
    PASS params-required:tickets_get: required is declared
    PASS params-opaque:tickets_get: no free-form object parameter
    PASS annotations:tickets_get: readOnlyHint is set
    PASS input-schema:tickets_search: inputSchema is a JSON Schema object
    PASS description:tickets_search: 36 words
    PASS params-described:tickets_search: every parameter has a description, enum or const
    PASS params-required:tickets_search: required is declared
    PASS params-opaque:tickets_search: no free-form object parameter
    PASS annotations:tickets_search: readOnlyHint is set
    PASS input-schema:tickets_create: inputSchema is a JSON Schema object
    PASS description:tickets_create: 31 words
    PASS params-described:tickets_create: every parameter has a description, enum or const
    PASS params-required:tickets_create: required is declared
    PASS params-opaque:tickets_create: no free-form object parameter
    PASS annotations:tickets_create: readOnlyHint or destructiveHint is set
    PASS input-schema:tickets_update_status: inputSchema is a JSON Schema object
    PASS description:tickets_update_status: 20 words
    PASS params-described:tickets_update_status: every parameter has a description, enum or const
    PASS params-required:tickets_update_status: required is declared
    PASS params-opaque:tickets_update_status: no free-form object parameter
    PASS annotations:tickets_update_status: readOnlyHint or destructiveHint is set
    PASS input-schema:tickets_add_comment: inputSchema is a JSON Schema object
    PASS description:tickets_add_comment: 17 words
    PASS params-described:tickets_add_comment: every parameter has a description, enum or const
    PASS params-required:tickets_add_comment: required is declared
    PASS params-opaque:tickets_add_comment: no free-form object parameter
    PASS annotations:tickets_add_comment: readOnlyHint or destructiveHint is set
    PASS input-schema:tickets_delete: inputSchema is a JSON Schema object
    PASS description:tickets_delete: 19 words
    PASS params-described:tickets_delete: every parameter has a description, enum or const
    PASS params-required:tickets_delete: required is declared
    PASS params-opaque:tickets_delete: no free-form object parameter
    PASS annotations:tickets_delete: readOnlyHint or destructiveHint is set
    PASS input-schema:users_find: inputSchema is a JSON Schema object
    PASS description:users_find: 26 words
    PASS params-described:users_find: every parameter has a description, enum or const
    PASS params-required:users_find: required is declared
    PASS params-opaque:users_find: no free-form object parameter
    PASS annotations:users_find: readOnlyHint is set
    PASS input-schema:reports_weekly_summary: inputSchema is a JSON Schema object
    PASS description:reports_weekly_summary: 15 words
    PASS params-described:reports_weekly_summary: every parameter has a description, enum or const
    PASS params-required:reports_weekly_summary: required is declared
    PASS params-opaque:reports_weekly_summary: no free-form object parameter
    PASS near-duplicate: no two descriptions overlap by 50% or more
    PASS select-1: "Show me ticket 4521": tickets_get (5.4), next tickets_add_comment 3.2
    PASS select-2: "Find open tickets assigned to Maria": tickets_search (7.5), next users_find 5.5
    PASS select-3: "Close ticket 4521 as resolved": tickets_update_status (7.0), next tickets_search 3.7
    PASS select-4: "Remove the duplicate ticket 4533": tickets_delete (4.3), next tickets_add_comment 2.1
    PASS select-5: "Write the weekly summary of closed tickets for ...": reports_weekly_summary (18.9), next tickets_create 4.8
    PASS select-6: "Look up the user named Maria Chen": users_find (9.2), next tickets_search 1.6
    PASS select-7: "Add a comment to ticket 4521 saying the fix is ...": tickets_add_comment (10.9), next tickets_update_status 5.7
    PASS select-8: "Create a new ticket for the login bug": tickets_create (10.3), next tickets_update_status 3.7
    INFO selection: 8 tasks, 8 clear, 0 ambiguous, 0 wrong or not found
    62 pass, 0 warn, 0 fail

**What the draft taught.** Two tasks failed. "Find open tickets assigned to Maria" went to `users_find`: its name holds `find` and name words count three times, while `tickets_search` described itself with "match a status, an assignee or free text". "Remove the duplicate ticket 4533" went to `tickets_create`, whose description said "avoid duplicates", while `tickets_delete` never used the word "remove". One task was a tie: "Show me ticket 4521" shares no word with any description except `ticket` and the example id `4521`, so every `tickets_*` tool with a `ticket_id` parameter scored the same. The fixes are wording only: `tickets_search` now says "Find … assigned to", `tickets_get` says "Show", `tickets_delete` says "remove", `tickets_create` says the problem should not be "filed twice", and `tickets_update_status` says "close it, mark it resolved". Reword to the users' words, then rerun. The loop optimizes definitions for a word ranker, so finish with section 7.

### A live listing from the official SDK

The listing of the reference server from [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/) (five tools, official Python SDK 2.3.0) was fetched with `curl` and checked. The request carries the per-request `_meta` that revision 2026-07-28 requires.
    
    
    curl -s http://127.0.0.1:8200/mcp -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -H 'MCP-Protocol-Version: 2026-07-28' -H 'Mcp-Method: tools/list' \
      -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientInfo":{"name":"design-check","version":"0"},"io.modelcontextprotocol/clientCapabilities":{}}}}' \
      > sdk-tools.json
    python3 tool_design_check.py sdk-tools.json

The result is `22 pass, 14 warn, 0 fail` with exit code 0: no rule of the spec is broken. The warnings are what the SDK's docstring-based definitions leave out: descriptions of two to six words, undescribed parameters (`location`, `a`, `b`), no annotations, and no `additionalProperties: false` on the three tools without parameters. `add` is reported as a write verb because it starts with `add`; it only sums two numbers, so `readOnlyHint: true` is the right fix. That is the false positive to expect from a name-based heuristic.

**Recorded output: the live SDK listing**
    
    
     INFO 5 tools, 1838 bytes as compact JSON (a client sends this, in some form, to the model)
    PASS list-complete: the listing has no further page
    PASS name-spec: all names are 1-128 characters from A-Z a-z 0-9 _ - .
    PASS name-unique: every name is unique
    PASS name-case-collision: no two names differ only in case or separators
    PASS name-style: one naming style (snake_case)
    PASS name-generic: every name says which object it works on
    PASS input-schema:get_weather: inputSchema is a JSON Schema object
    WARN description:get_weather: 6 words, fewer than 8
    WARN params-described:get_weather: no description or enum: location
    PASS params-required:get_weather: required is declared
    PASS params-opaque:get_weather: no free-form object parameter
    WARN annotations:get_weather: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:list_users: inputSchema is a JSON Schema object
    WARN description:list_users: 6 words, fewer than 8
    PASS params-described:list_users: every parameter has a description, enum or const
    PASS params-opaque:list_users: no free-form object parameter
    WARN no-params-closed:list_users: a tool without parameters should say additionalProperties: false
    WARN annotations:list_users: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:add: inputSchema is a JSON Schema object
    WARN description:add: 3 words, fewer than 8
    WARN params-described:add: no description or enum: a, b
    PASS params-required:add: required is declared
    PASS params-opaque:add: no free-form object parameter
    WARN annotations:add: `readOnlyHint` or `destructiveHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:get_current_time: inputSchema is a JSON Schema object
    WARN description:get_current_time: 3 words, fewer than 8
    PASS params-described:get_current_time: every parameter has a description, enum or const
    PASS params-opaque:get_current_time: no free-form object parameter
    WARN no-params-closed:get_current_time: a tool without parameters should say additionalProperties: false
    WARN annotations:get_current_time: `readOnlyHint` is not set; the schema default says the tool may modify and be destructive
    PASS input-schema:explode: inputSchema is a JSON Schema object
    WARN description:explode: 2 words, fewer than 8
    PASS params-described:explode: every parameter has a description, enum or const
    PASS params-opaque:explode: no free-form object parameter
    WARN no-params-closed:explode: a tool without parameters should say additionalProperties: false
    PASS near-duplicate: no two descriptions overlap by 50% or more
    22 pass, 14 warn, 0 fail

## 7\. Test with your own model

The ranker is a stand-in. The same task file is the input of the test that matters.

  1. Save the `tools/list` result your server returns for the credentials a real user would have.
  2. Write tasks in the words of your users, at least one per tool, plus tasks that no tool should handle. The checker's file has no "no tool" expectation; record that case in your own harness.
  3. Give each task and the listing to your model and record the first tool it calls and its arguments. Do not count a later call.
  4. Compare with the expected tool, read each miss against the failure table in section 8, change the definition, and rerun both this checker and the model run.
  5. Keep the task file under version control and rerun after any change to the listing, because the listing is part of the prompt.



The pass bar is yours. No pass rate is given here, because none comes from a first-party source.

## 8\. Failure modes and recovery

Symptom| Likely cause| How to detect| Recovery  
---|---|---|---  
The model calls tool B for A's job| Overlapping descriptions, or B's text contains the task's words| `near-duplicate`; a selection task that is ambiguous or wrong| Say when to use each and when to use the other; remove borrowed words  
A tool is never chosen| The users' words appear in no definition| A selection FAIL "no word of the task appears"| Use the users' words in the name and description; put example values in parameter descriptions  
Arguments arrive in the wrong format| A parameter without description or `enum`| `params-described`| Describe the format with an example; use `enum` for closed sets  
The model repeats the same invalid call| The error text names no rule| Read your own `isError` results| Return what was wrong and what is valid, as in the spec's example  
A write happens where a read was meant| One tool does both, or no annotations| `annotations`| Split by effect; set `readOnlyHint` and `destructiveHint`; keep the client's confirmation  
Tools differ between connections| The list varies by connection, which the spec forbids; only the authorization may change it| List with two credentials and compare| Keep the listing stable and vary it only by authorization  
Two merged servers both expose `search`| Generic names collide in an aggregator| `name-generic`| Put the object in the name; clients should still prefix with a server identifier  
The model loops on an expired handle| The error does not say the handle expired| Call with an old handle| Return an execution error that says so; state the retention in the creation tool  
The listing is large| Many tools or long schemas| The `INFO` line with the size in bytes| Cut what does not change the choice; keep the order deterministic for caching  
Tools seem missing| The listing is paginated| `list-complete`| Follow `nextCursor` and save every page  
  
## 9\. What changed between revisions

Each row is the first revision whose official files contain the item. The `Tool` fields that matter for selection are the same in 2025-11-25 and 2026-07-28, except that 2025-11-25 also has `execution`; see [tools, section 2](https://modelcontextprotocol.info/docs/concepts/tools/) for the field-by-field table.

Item| First revision| Changelog  
---|---|---  
Tool `annotations`| 2025-03-26| "Added comprehensive **tool annotations** "  
Tool `title`| 2025-06-18| "Add `title` field for human-friendly display names"  
Tool `outputSchema`, `structuredContent`| 2025-06-18| "structured tool output"  
Tool `icons`| 2025-11-25| "expose icons as additional metadata for tools"  
Guidance on tool names| 2025-11-25| "Provide guidance on tool names (SEP-986)"  
Input validation errors as tool execution errors| 2025-11-25| "to enable model self-correction (SEP-1303)"  
Deterministic tool order; no per-connection variation| 2026-07-28| "Servers **SHOULD** return tools from `tools/list` in a deterministic order"  
  
## 10\. Before you ship

  * Every name is unique, in one style, and says which object it works on; the checker reports no FAIL.
  * Every description says what the tool does and when to use it; every parameter has a description or an `enum`; `required` is declared.
  * Annotations are set truthfully; destructive tools are separate tools.
  * The error text of every failure the model can fix names the rule and the valid form.
  * A task file in the users' words runs clean through the checker and through your own model.
  * The listing is deterministic, complete and measured in bytes.



## Versions and Verification

Spec wording and schemas are read from one pinned commit of the official repository (`dae694f6`, revision 2026-07-28 and the four before it). The checker was run with Python 3.14 on macOS; the live listing comes from the official Python SDK 2.3.0 (`mcp==2.3.0`). The three tool sets are fixtures written for this tutorial; they show what the checker detects, not how common such definitions are. The selection test is only a word-overlap ranker and cannot say how your model behaves; section 7 shows how to run the same tasks through it.

### Sources

  * [Tools](https://modelcontextprotocol.info/specification/2026-07-28/server/tools/): tool names, definition fields, annotations, structured content, error handling and handles.
  * Changelogs: [2025-03-26](https://modelcontextprotocol.info/specification/2025-03-26/changelog/), [2025-06-18](https://modelcontextprotocol.info/specification/2025-06-18/changelog/), [2025-11-25](https://modelcontextprotocol.info/specification/2025-11-25/changelog/) and [2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/changelog/).
  * [MCP tools explained](https://modelcontextprotocol.info/docs/concepts/tools/), [MCP server best practices](https://modelcontextprotocol.info/docs/best-practices/) and [MCP Inspector](https://modelcontextprotocol.info/tools/inspector/), for the protocol side and for trying a listing by hand.



[Build and Verify a Node.js MCP Client with the TypeScript SDK](https://modelcontextprotocol.info/docs/tutorials/building-a-client-node/ "Build and Verify a Node.js MCP Client with the TypeScript SDK")[Give a Specialized Agent Ticket Access over MCP: Resources, Controlled Tools and Failure Recovery](https://modelcontextprotocol.info/docs/tutorials/a2a-mcp-tool-access/ "Give a Specialized Agent Ticket Access over MCP: Resources, Controlled Tools and Failure Recovery")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
