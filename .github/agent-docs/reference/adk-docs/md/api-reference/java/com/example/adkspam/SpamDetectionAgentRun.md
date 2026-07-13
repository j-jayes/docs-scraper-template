JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/SpamDetectionAgentRun.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkspam](package-summary.html)
  2. [SpamDetectionAgentRun](SpamDetectionAgentRun.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. main(String[])

Hide sidebar  Show sidebar

# Class SpamDetectionAgentRun

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkspam.SpamDetectionAgentRun

* * *

public final class SpamDetectionAgentRun extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Entry point for the ADK Java issue monitoring (spam detection) agent. Mirrors `main.py` in the Python sample, and follows the `*Run` entry-point convention of the ADK Issue Triaging Agent and ADK Docs Release Analyzer samples. 

The runtime mode is selected by environment variables: 

  * **GitHub Actions workflow mode** (set `INTERACTIVE=0`): one-shot run. 
    * If `EVENT_NAME=issues` and `ISSUE_NUMBER` is set -> audit that single issue. 
    * Otherwise -> sweep open issues. With `INITIAL_FULL_SCAN=1` the whole open backlog is audited; otherwise only issues updated in the last 24 hours. 
  * **Interactive console mode** (default; `INTERACTIVE=1`): a Scanner-based REPL. The system instruction tells the agent to ask for confirmation before flagging. For a richer UI, the `google-adk-maven-plugin`'s `web` goal can serve this agent (see this module's README for the exact command). 


Following the Python design, cost-saving pre-filtering (skip maintainer/bot authors, strip code blocks, truncate, idempotency) happens here in code; the LLM is invoked only for threads that actually contain reviewable non-maintainer text. All GitHub access (reads and writes) goes through the shared [`GitHubTools`](../github/GitHubTools.html "class in com.example.github"), whose [`GitHubTools.dryRun`](../github/GitHubTools.html#dryRun)/[`GitHubTools.writeRepoOwner`](../github/GitHubTools.html#writeRepoOwner) /[`GitHubTools.writeRepoName`](../github/GitHubTools.html#writeRepoName) guards are configured here so untrusted issue content cannot redirect writes to another repository.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")[] args)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### main

public static void main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")[] args)




* * *

Copyright (C) 1980\. All rights reserved.
