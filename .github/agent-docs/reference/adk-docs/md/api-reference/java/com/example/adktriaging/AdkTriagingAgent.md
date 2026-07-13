JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/AdkTriagingAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adktriaging](package-summary.html)
  2. [AdkTriagingAgent](AdkTriagingAgent.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. COMPONENT_LABELS
     2. LABEL_GUIDELINES
     3. ROOT_AGENT
  5. Method Details
     1. gtechRotation()
     2. rootAgent()
     3. listUntriagedIssues(int)
     4. addLabelToIssue(int, String)
     5. assignGtechOwnerToIssue(int)

Hide sidebar  Show sidebar

# Class AdkTriagingAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adktriaging.AdkTriagingAgent

* * *

public final class AdkTriagingAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

ADK Issue Triaging Agent for `google/adk-java`. 

This is the Java port of the Python `adk_triaging_agent/agent.py`, adapted to the actual label taxonomy of `google/adk-java` (which, unlike adk-python, does not use per-component labels). The agent uses Gemini to: 

  * recommend a topic/kind label for each open issue (e.g. `bug`, `enhancement`, `documentation`, `question`), 
  * round-robin assign owners from a configurable triager rotation. 


All GitHub access goes through the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github") (backed by the ` org.kohsuke:github-api` client) that this sample reuses with the ADK Docs Release Analyzer. Tool methods are exposed as [`FunctionTool`](../../google/adk/tools/FunctionTool.html "class in com.google.adk.tools")s and use `snake_case` via [`Annotations.Schema`](../../google/adk/tools/Annotations.Schema.html "annotation interface in com.google.adk.tools") so the function declarations seen by the model match the Python implementation. Each tool returns an `ImmutableMap` envelope -- `{"status": "success", ...}` on success, ` {"status": "error", "message": "..."}` on failure -- matching the Python contract. 

NOTE: `COMPONENT_LABELS` contains labels that actually exist in `google/adk-java` as of this writing. `gtechRotation()` cannot be derived from any public source (adk-java has no `CODEOWNERS` file), so it defaults to an obvious placeholder and must be supplied at runtime via the `GTECH_ASSIGNEES` environment variable (a comma-separated list of GitHub handles). Real triager handles never need to live in source.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final com.google.common.collect.ImmutableSet<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`COMPONENT_LABELS`

The set of labels the agent is allowed to apply.

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`LABEL_GUIDELINES`

Label rubric used in the agent's system instruction.

`static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents")`

`ROOT_AGENT`

Exposed for `adk web` / dev-UI agent loaders that look up a `public static final BaseAgent ROOT_AGENT` field on the class.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`addLabelToIssue(int issueNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") label)`

Adds the specified label to a GitHub issue, validating it is on the allowlist.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`assignGtechOwnerToIssue(int issueNumber)`

Round-robin assigns a gTech triager to the issue using `issue_number % N`.

`static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`gtechRotation()`

Round-robin rotation of triagers.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`listUntriagedIssues(int issueCount)`

Lists open issues that still need triaging.

`static [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents")`

`rootAgent()`

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### COMPONENT_LABELS

public static final com.google.common.collect.ImmutableSet<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> COMPONENT_LABELS

The set of labels the agent is allowed to apply. These are real labels in ` google/adk-java`. Unlike adk-python, adk-java has no per-component labels, so this is a flat allowlist of topic/kind labels rather than a label->owner map. 

Insertion order is preserved (via `ImmutableSet`) for deterministic enumeration.

    * ### LABEL_GUIDELINES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") LABEL_GUIDELINES

Label rubric used in the agent's system instruction. Describes the real `google/adk-java` labels so the model classifies issues using labels that exist in the repo.

See Also:
    
      * [Constant Field Values](../../../constant-values.html#com.example.adktriaging.AdkTriagingAgent.LABEL_GUIDELINES)

    * ### ROOT_AGENT

public static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") ROOT_AGENT

Exposed for `adk web` / dev-UI agent loaders that look up a `public static final BaseAgent ROOT_AGENT` field on the class.

  * ## Method Details

    * ### gtechRotation

public static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> gtechRotation()

Round-robin rotation of triagers. Issues are assigned via `issue_number % N`. Sourced from the `GTECH_ASSIGNEES` environment variable (comma-separated GitHub handles); falls back to `PLACEHOLDER_ROTATION` when unset. 

Read lazily (per call) rather than at class load, matching the lazy-accessor pattern in [`Settings`](Settings.html "class in com.example.adktriaging"): this keeps the class loadable in tests/agent loaders and lets the environment be overridden before the rotation is first consulted.

    * ### rootAgent

public static [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") rootAgent()

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents"). Safe to call at class-init time: it only reads [`Settings`](Settings.html "class in com.example.adktriaging") accessors that never throw (no `GITHUB_TOKEN` is required to construct the agent), so the `ROOT_AGENT` field and `adk web` agent loaders work without a token configured.

    * ### listUntriagedIssues

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> listUntriagedIssues(int issueCount)

Lists open issues that still need triaging. An issue is considered untriaged if it is missing a recognized label OR it has no assignee. Each returned entry is a compact map (number, title, body, url, labels, plus the triage flags) rather than the full GitHub issue payload, to keep the model's context small.

    * ### addLabelToIssue

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> addLabelToIssue(int issueNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") label)

Adds the specified label to a GitHub issue, validating it is on the allowlist.

    * ### assignGtechOwnerToIssue

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> assignGtechOwnerToIssue(int issueNumber)

Round-robin assigns a gTech triager to the issue using `issue_number % N`. This matches the Python implementation and keeps the assignment stable for a given issue number.




* * *

Copyright (C) 1980\. All rights reserved.
