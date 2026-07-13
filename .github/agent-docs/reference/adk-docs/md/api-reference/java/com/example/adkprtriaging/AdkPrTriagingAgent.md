JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/AdkPrTriagingAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkprtriaging](package-summary.html)
  2. [AdkPrTriagingAgent](AdkPrTriagingAgent.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. ALLOWED_LABELS
     2. LABEL_GUIDELINES
     3. ROOT_AGENT
  5. Method Details
     1. rootAgent()
     2. getPullRequestDetails(int)
     3. addLabelToPr(int, String)
     4. addCommentToPr(int, String)

Hide sidebar  Show sidebar

# Class AdkPrTriagingAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkprtriaging.AdkPrTriagingAgent

* * *

public final class AdkPrTriagingAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

ADK Pull Request (PR) Triaging Agent for `google/adk-java`. 

This is the Java port of the Python `adk_pr_triaging_agent/agent.py`, adapted to the actual label taxonomy of `google/adk-java`. The Python agent applies one of ten adk-python _component_ labels (e.g. `services`, `models`, `mcp`); those labels do not exist in adk-java, so -- exactly as the sibling ADK Issue Triaging Agent does -- this port classifies PRs with adk-java's own labels (see `ALLOWED_LABELS`). 

The agent uses Gemini to: 

  * recommend a single topic/kind label for each open pull request (e.g. `bug`, ` enhancement`, `documentation`), 
  * check the PR against the repository's contribution guidelines and, when it falls short, post a single, polite comment asking the author for the missing context. 


All GitHub access goes through the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github") (backed by the ` org.kohsuke:github-api` client) that this sample reuses with the ADK Issue Triaging Agent and the ADK Docs Release Analyzer. Tool methods are exposed as [`FunctionTool`](../../google/adk/tools/FunctionTool.html "class in com.google.adk.tools")s and use ` snake_case` via [`Annotations.Schema`](../../google/adk/tools/Annotations.Schema.html "annotation interface in com.google.adk.tools") so the function declarations seen by the model match the Python implementation. Each tool returns an `ImmutableMap` envelope -- `{"status": "success", ...}` on success, `{"status": "error", "message": "..."}` on failure -- matching the Python contract.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final com.google.common.collect.ImmutableSet<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`ALLOWED_LABELS`

The set of labels the agent is allowed to apply to a pull request.

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

`addCommentToPr(int prNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") comment)`

Posts the specified comment on a pull request.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`addLabelToPr(int prNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") label)`

Adds the specified label to a pull request, validating it is on the allowlist.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`getPullRequestDetails(int prNumber)`

Fetches the details of the specified pull request via the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github").

`static [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents")`

`rootAgent()`

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### ALLOWED_LABELS

public static final com.google.common.collect.ImmutableSet<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> ALLOWED_LABELS

The set of labels the agent is allowed to apply to a pull request. These are real labels in `google/adk-java`. adk-python uses ten per-component labels that do not exist in adk-java, so this is a flat allowlist of topic/kind labels adapted to adk-java's taxonomy (the same approach the ADK Issue Triaging Agent takes). 

Insertion order is preserved (via `ImmutableSet`) for deterministic enumeration.

    * ### LABEL_GUIDELINES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") LABEL_GUIDELINES

Label rubric used in the agent's system instruction. Describes the real `google/adk-java` labels so the model classifies PRs using labels that exist in the repo.

See Also:
    
      * [Constant Field Values](../../../constant-values.html#com.example.adkprtriaging.AdkPrTriagingAgent.LABEL_GUIDELINES)

    * ### ROOT_AGENT

public static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") ROOT_AGENT

Exposed for `adk web` / dev-UI agent loaders that look up a `public static final BaseAgent ROOT_AGENT` field on the class.

  * ## Method Details

    * ### rootAgent

public static [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") rootAgent()

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents"). Safe to call at class-init time: it only reads [`Settings`](Settings.html "class in com.example.adkprtriaging") accessors that never throw (no `GITHUB_TOKEN` is required to construct the agent), so the `ROOT_AGENT` field and `adk web` agent loaders work without a token configured.

    * ### getPullRequestDetails

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> getPullRequestDetails(int prNumber)

Fetches the details of the specified pull request via the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github"). Returns the `{"status": "success", "pull_request": {...}}` envelope on success.

    * ### addLabelToPr

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> addLabelToPr(int prNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") label)

Adds the specified label to a pull request, validating it is on the allowlist.

    * ### addCommentToPr

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> addCommentToPr(int prNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") comment)

Posts the specified comment on a pull request.




* * *

Copyright (C) 1980\. All rights reserved.
