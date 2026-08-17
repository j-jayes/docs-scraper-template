JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](index.html)
  * [Tree](overview-tree.html)
  * [Deprecated](deprecated-list.html)
  * [Index](index-all.html)
  * [Search](search.html)
  * 


Select Theme

LightDarkSystem Setting




Contents  

  1. Constant Field Values
     1. com.example.*
     2. com.google.*

Hide sidebar  Show sidebar

# Constant Field Values

## com.example.*

  * com.example.adkprtriaging.[AdkPrTriagingAgent](com/example/adkprtriaging/AdkPrTriagingAgent.html "class in com.example.adkprtriaging")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[LABEL_GUIDELINES](com/example/adkprtriaging/AdkPrTriagingAgent.html#LABEL_GUIDELINES)`

`"Label rubric (these are the labels that exist in the google/adk-java\nrepository; apply the single most specific one):\n- \"bug\": A pull request that fixes a reproducible defect, regression, or\n unexpected error in ADK Java behavior.\n- \"enhancement\": A pull request that adds a new feature or improves\n existing functionality.\n- \"documentation\": Changes to docs, READMEs, Javadoc, tutorials, or the\n content of code samples\' documentation.\n- \"testing\": Changes to tests, test utilities, testing infrastructure, or\n code coverage.\n- \"sample\": Changes to the sample apps under contrib/samples or the\n tutorials.\n- \"dependencies\": Dependency upgrades or build dependency changes.\n- \"github\": Changes to GitHub Actions, workflows, or repository\n automation (files under .github/).\n\nGuidance:\n- Apply exactly one label: the single most specific match.\n- Prefer \"bug\" or \"enhancement\" for functional code changes; use a topic\n label (documentation, testing, sample, dependencies, github) when the PR\n is predominantly about that area.\n- If no label clearly applies, do not call the labeling tool.\n"`



  * com.example.adktriaging.[AdkTriagingAgent](com/example/adktriaging/AdkTriagingAgent.html "class in com.example.adktriaging")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[LABEL_GUIDELINES](com/example/adktriaging/AdkTriagingAgent.html#LABEL_GUIDELINES)`

`"Label rubric and disambiguation rules (these are the labels that exist in\nthe google/adk-java repository):\n- \"bug\": A reproducible defect, regression, or unexpected error in ADK\n Java behavior. Apply this to bug reports.\n- \"enhancement\": A new feature request or an improvement to existing\n functionality. Apply this to feature requests.\n- \"documentation\": Issues about docs, READMEs, Javadoc, tutorials, or the\n content of code samples.\n- \"question\": Usage questions or requests for clarification with no\n reproducible defect.\n- \"testing\": Test utilities, testing infrastructure, code coverage, or\n flaky/broken tests.\n- \"sample\": Issues about the sample apps under contrib/samples or the\n tutorials.\n- \"dependencies\": Dependency upgrades, version conflicts, or build-time\n dependency problems.\n- \"github\": GitHub Actions, workflows, or repository automation.\n\nGuidance:\n- Always classify the issue kind: apply \"bug\" for bug reports and\n \"enhancement\" for feature requests.\n- Additionally apply at most one topic label (documentation, question,\n testing, sample, dependencies, github) when one clearly applies.\n- Prefer the most specific match. If no label can be assigned\n confidently, do not call the labeling tool.\n"`




## com.google.*

  * com.google.adk.[Version](com/google/adk/Version.html "class in com.google.adk")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[JAVA_ADK_VERSION](com/google/adk/Version.html#JAVA_ADK_VERSION)`

`"1.7.0"`



  * com.google.adk.a2a.converters.[EventConverter](com/google/adk/a2a/converters/EventConverter.html "class in com.google.adk.a2a.converters")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[ADK_CONTEXT_ID_KEY](com/google/adk/a2a/converters/EventConverter.html#ADK_CONTEXT_ID_KEY)`

`"adk_context_id"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[ADK_TASK_ID_KEY](com/google/adk/a2a/converters/EventConverter.html#ADK_TASK_ID_KEY)`

`"adk_task_id"`

  * com.google.adk.a2a.converters.[PartConverter](com/google/adk/a2a/converters/PartConverter.html "class in com.google.adk.a2a.converters")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[A2A_DATA_PART_END_TAG](com/google/adk/a2a/converters/PartConverter.html#A2A_DATA_PART_END_TAG)`

`"</a2a_datapart_json>"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[A2A_DATA_PART_START_TAG](com/google/adk/a2a/converters/PartConverter.html#A2A_DATA_PART_START_TAG)`

`"<a2a_datapart_json>"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[A2A_DATA_PART_TEXT_MIME_TYPE](com/google/adk/a2a/converters/PartConverter.html#A2A_DATA_PART_TEXT_MIME_TYPE)`

`"text/plain"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[ARGS_KEY](com/google/adk/a2a/converters/PartConverter.html#ARGS_KEY)`

`"args"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[CODE_KEY](com/google/adk/a2a/converters/PartConverter.html#CODE_KEY)`

`"code"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[ID_KEY](com/google/adk/a2a/converters/PartConverter.html#ID_KEY)`

`"id"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[LANGUAGE_KEY](com/google/adk/a2a/converters/PartConverter.html#LANGUAGE_KEY)`

`"language"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[NAME_KEY](com/google/adk/a2a/converters/PartConverter.html#NAME_KEY)`

`"name"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[OUTCOME_KEY](com/google/adk/a2a/converters/PartConverter.html#OUTCOME_KEY)`

`"outcome"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[OUTPUT_KEY](com/google/adk/a2a/converters/PartConverter.html#OUTPUT_KEY)`

`"output"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[PARTIAL_ARGS_KEY](com/google/adk/a2a/converters/PartConverter.html#PARTIAL_ARGS_KEY)`

`"partialArgs"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[PARTS_KEY](com/google/adk/a2a/converters/PartConverter.html#PARTS_KEY)`

`"parts"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[RESPONSE_KEY](com/google/adk/a2a/converters/PartConverter.html#RESPONSE_KEY)`

`"response"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[SCHEDULING_KEY](com/google/adk/a2a/converters/PartConverter.html#SCHEDULING_KEY)`

`"scheduling"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[WILL_CONTINUE_KEY](com/google/adk/a2a/converters/PartConverter.html#WILL_CONTINUE_KEY)`

`"willContinue"`



  * com.google.adk.flows.llmflows.[Functions](com/google/adk/flows/llmflows/Functions.html "class in com.google.adk.flows.llmflows")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[REQUEST_CONFIRMATION_FUNCTION_CALL_NAME](com/google/adk/flows/llmflows/Functions.html#REQUEST_CONFIRMATION_FUNCTION_CALL_NAME)`

`"adk_request_confirmation"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[TOOL_CALL_SECURITY_STATES](com/google/adk/flows/llmflows/Functions.html#TOOL_CALL_SECURITY_STATES)`

`"adk_tool_call_security_states"`



  * com.google.adk.models.[GeminiUtil](com/google/adk/models/GeminiUtil.html "class in com.google.adk.models")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[CONTINUE_OUTPUT_MESSAGE](com/google/adk/models/GeminiUtil.html#CONTINUE_OUTPUT_MESSAGE)`

`"Continue output. DO NOT look at this line. ONLY look at the content before this line and system instruction."`



  * com.google.adk.sessions.[State](com/google/adk/sessions/State.html "class in com.google.adk.sessions")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[APP_PREFIX](com/google/adk/sessions/State.html#APP_PREFIX)`

`"app:"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[TEMP_PREFIX](com/google/adk/sessions/State.html#TEMP_PREFIX)`

`"temp:"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[USER_PREFIX](com/google/adk/sessions/State.html#USER_PREFIX)`

`"user:"`



  * com.google.adk.skills.[SkillSourceException](com/google/adk/skills/SkillSourceException.html "class in com.google.adk.skills")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[RESOURCE_LOAD_ERROR](com/google/adk/skills/SkillSourceException.html#RESOURCE_LOAD_ERROR)`

`"RESOURCE_LOAD_ERROR"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[RESOURCE_NOT_FOUND](com/google/adk/skills/SkillSourceException.html#RESOURCE_NOT_FOUND)`

`"RESOURCE_NOT_FOUND"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[SKILL_FORMAT_ERROR](com/google/adk/skills/SkillSourceException.html#SKILL_FORMAT_ERROR)`

`"SKILL_FORMAT_ERROR"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[SKILL_LOAD_ERROR](com/google/adk/skills/SkillSourceException.html#SKILL_LOAD_ERROR)`

`"SKILL_LOAD_ERROR"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[SKILL_NOT_FOUND](com/google/adk/skills/SkillSourceException.html#SKILL_NOT_FOUND)`

`"SKILL_NOT_FOUND"`



  * com.google.adk.tools.[SetModelResponseTool](com/google/adk/tools/SetModelResponseTool.html "class in com.google.adk.tools")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[NAME](com/google/adk/tools/SetModelResponseTool.html#NAME)`

`"set_model_response"`



  * com.google.adk.utils.[Constants](com/google/adk/utils/Constants.html "class in com.google.adk.utils")

Modifier and Type

Constant Field

Value

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[APP_STATE_COLLECTION](com/google/adk/utils/Constants.html#APP_STATE_COLLECTION)`

`"app-state"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[EVENTS_SUBCOLLECTION_NAME](com/google/adk/utils/Constants.html#EVENTS_SUBCOLLECTION_NAME)`

`"user-event"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_APP_NAME](com/google/adk/utils/Constants.html#KEY_APP_NAME)`

`"appName"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_AUTHOR](com/google/adk/utils/Constants.html#KEY_AUTHOR)`

`"author"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_ID](com/google/adk/utils/Constants.html#KEY_ID)`

`"id"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_MODEL](com/google/adk/utils/Constants.html#KEY_MODEL)`

`"model"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_STATE](com/google/adk/utils/Constants.html#KEY_STATE)`

`"state"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_TIMESTAMP](com/google/adk/utils/Constants.html#KEY_TIMESTAMP)`

`"timestamp"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_UPDATE_TIME](com/google/adk/utils/Constants.html#KEY_UPDATE_TIME)`

`"updateTime"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_USER](com/google/adk/utils/Constants.html#KEY_USER)`

`"user"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[KEY_USER_ID](com/google/adk/utils/Constants.html#KEY_USER_ID)`

`"userId"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[SESSION_COLLECTION_NAME](com/google/adk/utils/Constants.html#SESSION_COLLECTION_NAME)`

`"sessions"`

`public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[USER_STATE_COLLECTION](com/google/adk/utils/Constants.html#USER_STATE_COLLECTION)`

`"user-state"`




* * *

Copyright (C) 1980\. All rights reserved.
