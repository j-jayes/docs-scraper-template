JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/AdkStaleAgent.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkstale](package-summary.html)
  2. [AdkStaleAgent](AdkStaleAgent.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. ROOT_AGENT
  5. Method Details
     1. rootAgent()
     2. getIssueState(int)
     3. addLabelToIssue(int, String)
     4. removeLabelFromIssue(int, String)
     5. addStaleLabelAndComment(int)
     6. alertMaintainerOfEdit(int)
     7. closeAsStale(int)

Hide sidebar  Show sidebar

# Class AdkStaleAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkstale.AdkStaleAgent

* * *

public final class AdkStaleAgent extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

ADK Stale Issue Auditor for `google/adk-java`. 

This is the Java port of the Python `adk_stale_agent/agent.py`. Unlike a timestamp-only "stale bot", it reconstructs each issue's **Unified History Trace** from a single GraphQL query (comments, body edits, title renames, reopens, label events) and uses Gemini to reason about the _intent_ of the last action: 

  * If the author/user acted last -> the issue is ACTIVE: the `stale` label is removed (and, for a silent description edit GitHub does not notify on, maintainers are alerted). 
  * If a maintainer asked a question and the inactivity threshold has passed -> the issue is marked `stale`; after a further threshold it is closed. 
  * If a maintainer gave a status update (or is talking to another maintainer) -> no action. 


Reads (the GraphQL history, maintainer list) go through `GitHubStaleClient`; writes (comments, labels, closing) go through the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github") so the dry-run and target-repository guards are applied uniformly. Tool methods are exposed as [`FunctionTool`](../../google/adk/tools/FunctionTool.html "class in com.google.adk.tools")s using `snake_case` via [`Annotations.Schema`](../../google/adk/tools/Annotations.Schema.html "annotation interface in com.google.adk.tools") so the function declarations seen by the model match the Python implementation, and each returns a `{"status": "success" | "error", ...}` envelope.

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

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`addLabelToIssue(int itemNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") labelName)`

 

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`addStaleLabelAndComment(int itemNumber)`

 

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`alertMaintainerOfEdit(int itemNumber)`

 

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`closeAsStale(int itemNumber)`

 

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`getIssueState(int itemNumber)`

 

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`removeLabelFromIssue(int itemNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") labelName)`

 

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

Builds the [`LlmAgent`](../../google/adk/agents/LlmAgent.html "class in com.google.adk.agents"). Safe to call at class-init time: it only reads [`Settings`](Settings.html "class in com.example.adkstale") accessors that never throw (no `GITHUB_TOKEN` is required to construct the agent), so the `ROOT_AGENT` field and `adk web` agent loaders work without a token configured.

    * ### getIssueState

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> getIssueState(int itemNumber)

    * ### addLabelToIssue

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> addLabelToIssue(int itemNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") labelName)

    * ### removeLabelFromIssue

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> removeLabelFromIssue(int itemNumber, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") labelName)

    * ### addStaleLabelAndComment

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> addStaleLabelAndComment(int itemNumber)

    * ### alertMaintainerOfEdit

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> alertMaintainerOfEdit(int itemNumber)

    * ### closeAsStale

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> closeAsStale(int itemNumber)




* * *

Copyright (C) 1980\. All rights reserved.
