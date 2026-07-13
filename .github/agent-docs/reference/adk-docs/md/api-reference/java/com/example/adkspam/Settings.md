JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/Settings.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkspam](package-summary.html)
  2. [Settings](Settings.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. githubToken()
     2. hasGithubToken()
     3. owner()
     4. repo()
     5. model()
     6. spamLabel()
     7. botName()
     8. botAlertSignature()
     9. isInitialFullScan()
     10. issueScanLimit()
     11. eventName()
     12. issueNumber()
     13. issueTitle()
     14. issueBody()
     15. isInteractive()
     16. isDryRun()
     17. parseNumberString(String, int)

Hide sidebar  Show sidebar

# Class Settings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkspam.Settings

* * *

public final class Settings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration read from environment variables. Mirrors `settings.py` in the Python ADK issue monitoring (spam detection) agent. 

Values are exposed as **accessor methods** (read lazily on each call) rather than ` static final` fields. This keeps the class loadable in unit tests and `adk web` agent loaders without a `GITHUB_TOKEN` present -- only `githubToken()` throws when the token is actually required (i.e. right before a network call). 

Required variables: 

  * `GITHUB_TOKEN` -- GitHub Personal Access Token (or the Actions built-in token) with `issues:write` permission. Required for both interactive and workflow modes. 
  * `GOOGLE_API_KEY` -- Gemini API key. Required for both modes (or set up Vertex AI credentials and `GOOGLE_GENAI_USE_VERTEXAI=TRUE`). 


Optional variables: 

  * `OWNER` -- defaults to `google`. 
  * `REPO` -- defaults to `adk-java`. 
  * `MODEL` -- Gemini model used for moderation. Defaults to ` gemini-flash-latest` (a Flash model favors latency/cost for this high-volume scan, matching the Python sample's `gemini-2.5-flash`). Overridable without a code change. 
  * `SPAM_LABEL_NAME` -- label applied to flagged issues. Defaults to `spam`. 
  * `BOT_NAME` -- GitHub handle of the official bot whose content is never scanned. Defaults to `adk-bot`. 
  * `BOT_ALERT_SIGNATURE` -- signature prefix the agent writes in its alert comment; also used as the idempotency marker so the agent never double-posts. Defaults to a fixed alert banner. 
  * `INITIAL_FULL_SCAN` -- `1`/`true` audits every open issue; otherwise only issues updated in the last 24 hours are audited. Defaults to off (daily sweep). 
  * `ISSUE_SCAN_LIMIT` -- safety cap on how many open issues a single sweep processes. Defaults to `100`. 
  * `INTERACTIVE` -- `1`/`true` for interactive mode (asks for confirmation before flagging), `0`/`false` for unattended workflow mode. Defaults to interactive when unset. 
  * `DRY_RUN` -- `1`/`true` logs intended labels/comments without calling the GitHub mutation endpoints. Lets you verify the full pipeline (incl. Gemini) without modifying any real issue. Defaults to off. 
  * `EVENT_NAME` -- the GitHub event that triggered the workflow (`issues`, `schedule`, etc.). Drives single-issue vs. sweep behavior in [`SpamDetectionAgentRun`](SpamDetectionAgentRun.html "class in com.example.adkspam"). 
  * `ISSUE_NUMBER`, `ISSUE_TITLE`, `ISSUE_BODY` -- populated by the GitHub Actions workflow when the trigger is an issue event. 


  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`botAlertSignature()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`botName()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`eventName()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`githubToken()`

Returns the GitHub token, throwing a clear error if it is not configured.

`static boolean`

`hasGithubToken()`

Returns true if a `GITHUB_TOKEN` is configured, without throwing.

`static boolean`

`isDryRun()`

 

`static boolean`

`isInitialFullScan()`

 

`static boolean`

`isInteractive()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueBody()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueNumber()`

 

`static int`

`issueScanLimit()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueTitle()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model()`

Returns the Gemini model used for moderation.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`owner()`

 

`static int`

`parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)`

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`repo()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`spamLabel()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### githubToken

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") githubToken()

Returns the GitHub token, throwing a clear error if it is not configured.

    * ### hasGithubToken

public static boolean hasGithubToken()

Returns true if a `GITHUB_TOKEN` is configured, without throwing.

    * ### owner

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") owner()

    * ### repo

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") repo()

    * ### model

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model()

Returns the Gemini model used for moderation. Defaults to `gemini-flash-latest` (a Flash model favors latency/cost for this high-volume scan) and is overridable via the `MODEL` environment variable, so it can be changed without editing source.

    * ### spamLabel

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") spamLabel()

    * ### botName

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") botName()

    * ### botAlertSignature

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") botAlertSignature()

    * ### isInitialFullScan

public static boolean isInitialFullScan()

    * ### issueScanLimit

public static int issueScanLimit()

    * ### eventName

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventName()

    * ### issueNumber

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueNumber()

    * ### issueTitle

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueTitle()

    * ### issueBody

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueBody()

    * ### isInteractive

public static boolean isInteractive()

    * ### isDryRun

public static boolean isDryRun()

    * ### parseNumberString

public static int parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input. Mirrors `parse_number_string` in the Python utils.




* * *

Copyright (C) 1980\. All rights reserved.
