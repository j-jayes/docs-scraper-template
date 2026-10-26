[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/TurnCompleteReason

# TurnCompleteReason

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [TurnCompleteReasonSerializer::class](../../../google-adk-kotlin-core/com.google.adk.kt.types/-turn-complete-reason-serializer/index.html))

enum [TurnCompleteReason](index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[TurnCompleteReason](index.html)>

Why a live turn ended.

Absent on an ordinary completion; present when the turn was cut short, most often by a safety filter on either the input or the generated content.

MembersEntries

## Entries

[TURN_COMPLETE_REASON_UNSPECIFIED](-t-u-r-n_-c-o-m-p-l-e-t-e_-r-e-a-s-o-n_-u-n-s-p-e-c-i-f-i-e-d/index.html)

Link copied to clipboard

common

[TURN_COMPLETE_REASON_UNSPECIFIED](-t-u-r-n_-c-o-m-p-l-e-t-e_-r-e-a-s-o-n_-u-n-s-p-e-c-i-f-i-e-d/index.html)

[MALFORMED_FUNCTION_CALL](-m-a-l-f-o-r-m-e-d_-f-u-n-c-t-i-o-n_-c-a-l-l/index.html)

Link copied to clipboard

common

[MALFORMED_FUNCTION_CALL](-m-a-l-f-o-r-m-e-d_-f-u-n-c-t-i-o-n_-c-a-l-l/index.html)

[RESPONSE_REJECTED](-r-e-s-p-o-n-s-e_-r-e-j-e-c-t-e-d/index.html)

Link copied to clipboard

common

[RESPONSE_REJECTED](-r-e-s-p-o-n-s-e_-r-e-j-e-c-t-e-d/index.html)

[NEED_MORE_INPUT](-n-e-e-d_-m-o-r-e_-i-n-p-u-t/index.html)

Link copied to clipboard

common

[NEED_MORE_INPUT](-n-e-e-d_-m-o-r-e_-i-n-p-u-t/index.html)

[PROHIBITED_INPUT_CONTENT](-p-r-o-h-i-b-i-t-e-d_-i-n-p-u-t_-c-o-n-t-e-n-t/index.html)

Link copied to clipboard

common

[PROHIBITED_INPUT_CONTENT](-p-r-o-h-i-b-i-t-e-d_-i-n-p-u-t_-c-o-n-t-e-n-t/index.html)

[IMAGE_PROHIBITED_INPUT_CONTENT](-i-m-a-g-e_-p-r-o-h-i-b-i-t-e-d_-i-n-p-u-t_-c-o-n-t-e-n-t/index.html)

Link copied to clipboard

common

[IMAGE_PROHIBITED_INPUT_CONTENT](-i-m-a-g-e_-p-r-o-h-i-b-i-t-e-d_-i-n-p-u-t_-c-o-n-t-e-n-t/index.html)

[INPUT_TEXT_CONTAIN_PROMINENT_PERSON_PROHIBITED](-i-n-p-u-t_-t-e-x-t_-c-o-n-t-a-i-n_-p-r-o-m-i-n-e-n-t_-p-e-r-s-o-n_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[INPUT_TEXT_CONTAIN_PROMINENT_PERSON_PROHIBITED](-i-n-p-u-t_-t-e-x-t_-c-o-n-t-a-i-n_-p-r-o-m-i-n-e-n-t_-p-e-r-s-o-n_-p-r-o-h-i-b-i-t-e-d/index.html)

[INPUT_IMAGE_CELEBRITY](-i-n-p-u-t_-i-m-a-g-e_-c-e-l-e-b-r-i-t-y/index.html)

Link copied to clipboard

common

[INPUT_IMAGE_CELEBRITY](-i-n-p-u-t_-i-m-a-g-e_-c-e-l-e-b-r-i-t-y/index.html)

[INPUT_IMAGE_PHOTO_REALISTIC_CHILD_PROHIBITED](-i-n-p-u-t_-i-m-a-g-e_-p-h-o-t-o_-r-e-a-l-i-s-t-i-c_-c-h-i-l-d_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[INPUT_IMAGE_PHOTO_REALISTIC_CHILD_PROHIBITED](-i-n-p-u-t_-i-m-a-g-e_-p-h-o-t-o_-r-e-a-l-i-s-t-i-c_-c-h-i-l-d_-p-r-o-h-i-b-i-t-e-d/index.html)

[INPUT_TEXT_NCII_PROHIBITED](-i-n-p-u-t_-t-e-x-t_-n-c-i-i_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[INPUT_TEXT_NCII_PROHIBITED](-i-n-p-u-t_-t-e-x-t_-n-c-i-i_-p-r-o-h-i-b-i-t-e-d/index.html)

[INPUT_OTHER](-i-n-p-u-t_-o-t-h-e-r/index.html)

Link copied to clipboard

common

[INPUT_OTHER](-i-n-p-u-t_-o-t-h-e-r/index.html)

[INPUT_IP_PROHIBITED](-i-n-p-u-t_-i-p_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[INPUT_IP_PROHIBITED](-i-n-p-u-t_-i-p_-p-r-o-h-i-b-i-t-e-d/index.html)

[BLOCKLIST](-b-l-o-c-k-l-i-s-t/index.html)

Link copied to clipboard

common

[BLOCKLIST](-b-l-o-c-k-l-i-s-t/index.html)

[UNSAFE_PROMPT_FOR_IMAGE_GENERATION](-u-n-s-a-f-e_-p-r-o-m-p-t_-f-o-r_-i-m-a-g-e_-g-e-n-e-r-a-t-i-o-n/index.html)

Link copied to clipboard

common

[UNSAFE_PROMPT_FOR_IMAGE_GENERATION](-u-n-s-a-f-e_-p-r-o-m-p-t_-f-o-r_-i-m-a-g-e_-g-e-n-e-r-a-t-i-o-n/index.html)

[GENERATED_IMAGE_SAFETY](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-s-a-f-e-t-y/index.html)

Link copied to clipboard

common

[GENERATED_IMAGE_SAFETY](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-s-a-f-e-t-y/index.html)

[GENERATED_CONTENT_SAFETY](-g-e-n-e-r-a-t-e-d_-c-o-n-t-e-n-t_-s-a-f-e-t-y/index.html)

Link copied to clipboard

common

[GENERATED_CONTENT_SAFETY](-g-e-n-e-r-a-t-e-d_-c-o-n-t-e-n-t_-s-a-f-e-t-y/index.html)

[GENERATED_AUDIO_SAFETY](-g-e-n-e-r-a-t-e-d_-a-u-d-i-o_-s-a-f-e-t-y/index.html)

Link copied to clipboard

common

[GENERATED_AUDIO_SAFETY](-g-e-n-e-r-a-t-e-d_-a-u-d-i-o_-s-a-f-e-t-y/index.html)

[GENERATED_VIDEO_SAFETY](-g-e-n-e-r-a-t-e-d_-v-i-d-e-o_-s-a-f-e-t-y/index.html)

Link copied to clipboard

common

[GENERATED_VIDEO_SAFETY](-g-e-n-e-r-a-t-e-d_-v-i-d-e-o_-s-a-f-e-t-y/index.html)

[GENERATED_CONTENT_PROHIBITED](-g-e-n-e-r-a-t-e-d_-c-o-n-t-e-n-t_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[GENERATED_CONTENT_PROHIBITED](-g-e-n-e-r-a-t-e-d_-c-o-n-t-e-n-t_-p-r-o-h-i-b-i-t-e-d/index.html)

[GENERATED_CONTENT_BLOCKLIST](-g-e-n-e-r-a-t-e-d_-c-o-n-t-e-n-t_-b-l-o-c-k-l-i-s-t/index.html)

Link copied to clipboard

common

[GENERATED_CONTENT_BLOCKLIST](-g-e-n-e-r-a-t-e-d_-c-o-n-t-e-n-t_-b-l-o-c-k-l-i-s-t/index.html)

[GENERATED_IMAGE_PROHIBITED](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[GENERATED_IMAGE_PROHIBITED](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-p-r-o-h-i-b-i-t-e-d/index.html)

[GENERATED_IMAGE_CELEBRITY](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-c-e-l-e-b-r-i-t-y/index.html)

Link copied to clipboard

common

[GENERATED_IMAGE_CELEBRITY](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-c-e-l-e-b-r-i-t-y/index.html)

[GENERATED_IMAGE_PROMINENT_PEOPLE_DETECTED_BY_REWRITER](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-p-r-o-m-i-n-e-n-t_-p-e-o-p-l-e_-d-e-t-e-c-t-e-d_-b-y_-r-e-w-r-i-t-e-r/index.html)

Link copied to clipboard

common

[GENERATED_IMAGE_PROMINENT_PEOPLE_DETECTED_BY_REWRITER](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-p-r-o-m-i-n-e-n-t_-p-e-o-p-l-e_-d-e-t-e-c-t-e-d_-b-y_-r-e-w-r-i-t-e-r/index.html)

[GENERATED_IMAGE_IDENTIFIABLE_PEOPLE](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-i-d-e-n-t-i-f-i-a-b-l-e_-p-e-o-p-l-e/index.html)

Link copied to clipboard

common

[GENERATED_IMAGE_IDENTIFIABLE_PEOPLE](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-i-d-e-n-t-i-f-i-a-b-l-e_-p-e-o-p-l-e/index.html)

[GENERATED_IMAGE_MINORS](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-m-i-n-o-r-s/index.html)

Link copied to clipboard

common

[GENERATED_IMAGE_MINORS](-g-e-n-e-r-a-t-e-d_-i-m-a-g-e_-m-i-n-o-r-s/index.html)

[OUTPUT_IMAGE_IP_PROHIBITED](-o-u-t-p-u-t_-i-m-a-g-e_-i-p_-p-r-o-h-i-b-i-t-e-d/index.html)

Link copied to clipboard

common

[OUTPUT_IMAGE_IP_PROHIBITED](-o-u-t-p-u-t_-i-m-a-g-e_-i-p_-p-r-o-h-i-b-i-t-e-d/index.html)

[GENERATED_OTHER](-g-e-n-e-r-a-t-e-d_-o-t-h-e-r/index.html)

Link copied to clipboard

common

[GENERATED_OTHER](-g-e-n-e-r-a-t-e-d_-o-t-h-e-r/index.html)

[MAX_REGENERATION_REACHED](-m-a-x_-r-e-g-e-n-e-r-a-t-i-o-n_-r-e-a-c-h-e-d/index.html)

Link copied to clipboard

common

[MAX_REGENERATION_REACHED](-m-a-x_-r-e-g-e-n-e-r-a-t-i-o-n_-r-e-a-c-h-e-d/index.html)

## Properties

[entries](entries.html)

Link copied to clipboard

common

val [entries](entries.html): [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)<[TurnCompleteReason](index.html)>

Returns a representation of an immutable list of all enum entries, in the order they're declared.

[name](../-voice-activity-type/-a-c-t-i-v-i-t-y_-e-n-d/index.html#-372974862%2FProperties%2F-1855338903)

Link copied to clipboard

common

val [name](../-voice-activity-type/-a-c-t-i-v-i-t-y_-e-n-d/index.html#-372974862%2FProperties%2F-1855338903): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

[ordinal](../-voice-activity-type/-a-c-t-i-v-i-t-y_-e-n-d/index.html#-739389684%2FProperties%2F-1855338903)

Link copied to clipboard

common

val [ordinal](../-voice-activity-type/-a-c-t-i-v-i-t-y_-e-n-d/index.html#-739389684%2FProperties%2F-1855338903): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

## Functions

[valueOf](value-of.html)

Link copied to clipboard

common

fun [valueOf](value-of.html)(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [TurnCompleteReason](index.html)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

[values](values.html)

Link copied to clipboard

common

fun [values](values.html)(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[TurnCompleteReason](index.html)>

Returns an array containing the constants of this enum type, in the order they're declared.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
