JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/SpamDetectionAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkspam](package-summary.html)
  2. [SpamDetectionAgent](SpamDetectionAgent.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. ROOT_AGENT
  5. Method Details
     1. rootAgent()
     2. flagIssueAsSpam(int, String)

Hide sidebar  Show sidebar

# Class SpamDetectionAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkspam.SpamDetectionAgent

* * *

public final class SpamDetectionAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

ADK Issue Monitoring (Spam Detection) Agent for `google/adk-java`. 

This is the Java port of the Python `adk_issue_monitoring_agent/agent.py`. The agent uses Gemini to audit issue threads (the original description plus non-maintainer comments) for SEO spam, unsolicited promotion, and other objectionable content. When spam is detected it applies a `spam` label and posts a single alert comment for human maintainers -- nothing is ever deleted, the agent only flags. 

Following the Python design, the model is given exactly one tool, `flagIssueAsSpam(int, String)`. Cost-saving pre-filtering (skipping maintainer/bot authors, stripping code blocks, truncating, and idempotency) happens in [`SpamDetectionAgentRun`](SpamDetectionAgentRun.html "class in com.example.adkspam") before the model is ever invoked, so safe threads cost zero tokens. 

All GitHub access goes through the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github") (backed by the ` org.kohsuke:github-api` client) that this sample reuses with the ADK Triaging Agent and the ADK Docs Release Analyzer. The tool is exposed as a [`FunctionTool`](../../google/adk/tools/FunctionTool.html "class in com.google.adk.tools") and uses `snake_case` via [`Annotations.Schema`](../../google/adk/tools/Annotations.Schema.html "annotation interface in com.google.adk.tools") so the function declaration seen by the model matches the Python implementation. It returns an `ImmutableMap` envelope -- `{"status": "success", ...}` on success, `{"status": "error", "message": "..."}` on failure -- matching the Python contract.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents")`

`ROOT_AGENT`

Exposed for `adk web` / dev-UI agent loaders that look up a `public static final BaseAgent ROOT_AGENT` field on the class.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`flagIssueAsSpam(int itemNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") detectionReason)`

Flags an issue as spam by applying the configured spam label and posting one alert comment for maintainers.

`static [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents")`

`rootAgent()`

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### ROOT_AGENT

public static final [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") ROOT_AGENT

Exposed for `adk web` / dev-UI agent loaders that look up a `public static final BaseAgent ROOT_AGENT` field on the class.

  * ## Method Details

    * ### rootAgent

public static [LlmAgent](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents") rootAgent()

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents"). Safe to call at class-init time: it only reads [`Settings`](Settings.html "class in com.example.adkspam") accessors that never throw (no `GITHUB_TOKEN` is required to construct the agent), so the `ROOT_AGENT` field and `adk web` agent loaders work without a token configured.

    * ### flagIssueAsSpam

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> flagIssueAsSpam(int itemNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") detectionReason)

Flags an issue as spam by applying the configured spam label and posting one alert comment for maintainers. Mirrors `flag_issue_as_spam` in the Python sample, including the idempotency checks that avoid duplicate labels/comments on re-runs.




* * *

Copyright (C) 1980\. All rights reserved.
