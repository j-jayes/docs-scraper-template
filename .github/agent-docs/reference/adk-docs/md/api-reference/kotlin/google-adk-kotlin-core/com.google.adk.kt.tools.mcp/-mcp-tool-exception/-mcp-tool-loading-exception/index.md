toggle menu

[ google-adk-kotlin ](../../../../index.html)

0.2.0 

jvm

switch theme

search in API

[google-adk-kotlin-core](../../../index.html)/[com.google.adk.kt.tools.mcp](../../index.html)/[McpToolException](../index.html)/McpToolLoadingException

# McpToolLoadingException

jvm

class [McpToolLoadingException](index.html)(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [McpToolException](../index.html)

Exception thrown when there's an error during MCP tools loading/initialization.

Members

## Constructors

[McpToolLoadingException](-mcp-tool-loading-exception.html)

Link copied to clipboard

jvm

constructor(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)? = null)

## Properties

[cause](../-mcp-tool-execution-exception/index.html#-654012527%2FProperties%2F-1959370187)

Link copied to clipboard

jvm

open val [cause](../-mcp-tool-execution-exception/index.html#-654012527%2FProperties%2F-1959370187): [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)?

[message](../-mcp-tool-execution-exception/index.html#1824300659%2FProperties%2F-1959370187)

Link copied to clipboard

jvm

open val [message](../-mcp-tool-execution-exception/index.html#1824300659%2FProperties%2F-1959370187): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?

## Functions

[addSuppressed](../-mcp-tool-execution-exception/index.html#282858770%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

fun [addSuppressed](../-mcp-tool-execution-exception/index.html#282858770%2FFunctions%2F-1959370187)(p0: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html))

[fillInStackTrace](../-mcp-tool-execution-exception/index.html#-1102069925%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [fillInStackTrace](../-mcp-tool-execution-exception/index.html#-1102069925%2FFunctions%2F-1959370187)(): [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)

[getLocalizedMessage](../-mcp-tool-execution-exception/index.html#1043865560%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [getLocalizedMessage](../-mcp-tool-execution-exception/index.html#1043865560%2FFunctions%2F-1959370187)(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[getStackTrace](../-mcp-tool-execution-exception/index.html#2050903719%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [getStackTrace](../-mcp-tool-execution-exception/index.html#2050903719%2FFunctions%2F-1959370187)(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html)<[StackTraceElement](https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html)>

[getSuppressed](../-mcp-tool-execution-exception/index.html#672492560%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

fun [getSuppressed](../-mcp-tool-execution-exception/index.html#672492560%2FFunctions%2F-1959370187)(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html)<[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)>

[initCause](../-mcp-tool-execution-exception/index.html#-418225042%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [initCause](../-mcp-tool-execution-exception/index.html#-418225042%2FFunctions%2F-1959370187)(p0: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)): [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)

[printStackTrace](../-mcp-tool-execution-exception/index.html#-1769529168%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [printStackTrace](../-mcp-tool-execution-exception/index.html#-1769529168%2FFunctions%2F-1959370187)()

open fun [printStackTrace](../-mcp-tool-execution-exception/index.html#1841853697%2FFunctions%2F-1959370187)(p0: [PrintStream](https://developer.android.com/reference/kotlin/java/io/PrintStream.html))

open fun [printStackTrace](../-mcp-tool-execution-exception/index.html#1175535278%2FFunctions%2F-1959370187)(p0: [PrintWriter](https://developer.android.com/reference/kotlin/java/io/PrintWriter.html))

[setStackTrace](../-mcp-tool-execution-exception/index.html#2135801318%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [setStackTrace](../-mcp-tool-execution-exception/index.html#2135801318%2FFunctions%2F-1959370187)(p0: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html)<[StackTraceElement](https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html)>)

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
