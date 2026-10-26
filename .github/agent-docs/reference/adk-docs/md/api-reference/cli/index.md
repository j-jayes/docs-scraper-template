# ADK CLI documentation¶

This page contains the auto-generated command-line reference for ADK 2.12.0.

  * adk

    * api_server

    * conformance

    * create

    * deploy

    * eval

    * eval_set

    * migrate

    * optimize

    * run

    * telemetry

    * test

    * web




## adk¶

Agent Development Kit CLI tools.

Usage
    
    
    adk [OPTIONS] COMMAND [ARGS]...
    

Options

\--version¶
    

Show the version and exit.

### api_server¶

Starts a FastAPI server for agents.

AGENTS_DIR: The directory of agents (where each subdirectory is a single agent containing agent.py, __init__.py, or root_agent.yaml) or a path pointing directly to a single agent folder.

This server’s endpoints are unauthenticated. Run it on a trusted network only, and put it behind your own authentication and authorization layer before exposing it to untrusted or public networks or serving multiple users.

Example:

> adk api_server –session_service_uri=[uri] –port=[port] path/to/agents_dir

Usage
    
    
    adk api_server [OPTIONS] [AGENTS_DIR]
    

Options

\--enable_features <enable_features>¶
    

Optional. Comma-separated list of feature names to enable. This provides an alternative to environment variables for enabling experimental features. Example: –enable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--disable_features <disable_features>¶
    

Optional. Comma-separated list of feature names to disable. This provides an alternative to environment variables for disabling features. Example: –disable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--host <host>¶
    

Optional. The binding host of the server

Default:
    

`'127.0.0.1'`

\--port <port>¶
    

Optional. The port of the server

\--allow_origins <allow_origins>¶
    

Optional. Origins to allow for CORS. Can be literal origins (e.g., ‘<https://example.com>’) or regex patterns prefixed with ‘regex:’ (e.g., ‘regex:https://.*.example.com’).

\--trace_to_cloud¶
    

Optional. Whether to enable cloud trace for telemetry.

Default:
    

`False`

\--otel_to_cloud¶
    

Optional. Whether to write OTel data to Google Cloud Observability services - Cloud Trace and Cloud Logging.

Default:
    

`False`

\--reload, \--no-reload¶
    

Optional. Whether to enable auto reload for server. Not supported for Cloud Run.

\--a2a¶
    

Optional. Whether to enable A2A endpoint.

Default:
    

`False`

\--reload_agents¶
    

Optional. Whether to enable live reload for agents changes.

Default:
    

`False`

\--eval_storage_uri <eval_storage_uri>¶
    

Optional. The evals storage URI to store agent evals, supported URIs: gs://<bucket name>.

\--extra_plugins <extra_plugins>¶
    

Optional. Comma-separated list of extra plugin classes or instances to enable (e.g., my.module.MyPluginClass or my.module.my_plugin_instance).

\--url_prefix <url_prefix>¶
    

Optional. URL path prefix when the application is mounted behind a reverse proxy or API gateway (e.g., ‘/api/v1’, ‘/adk’). This ensures generated URLs and redirects work correctly when the app is not served at the root path. Must start with ‘/’ if provided.

\--avatar_config <avatar_config>¶
    

Optional. AvatarConfig as an inline JSON object or a path to a JSON file. Applied only to /run_live sessions whose client requests video output (modalities=VIDEO); other live sessions ignore it. If unset, video sessions use the pre-built ‘Kai’ avatar.

\--max_llm_calls <max_llm_calls>¶
    

Optional. Maximum number of LLM calls allowed for each agent run. Values less than or equal to zero disable the limit.

\--trigger_sources <trigger_sources>¶
    

Optional. Comma-separated list of trigger sources to enable (e.g., ‘pubsub,eventarc’). Registers /apps/{app_name}/trigger/* endpoints for batch and event-driven agent invocations.

\--trigger_oidc_audience <trigger_oidc_audience>¶
    

Optional. Expected audience for Google-signed OIDC bearer tokens on /apps/{app_name}/trigger/* endpoints. When set, requests without a valid token matching this audience are rejected with 401.

\--trigger_oidc_service_accounts <trigger_oidc_service_accounts>¶
    

Optional. Comma-separated list of allowed service account emails for Google-signed OIDC tokens on /apps/{app_name}/trigger/* endpoints. Requires –trigger_oidc_audience.

-v, \--verbose¶
    

Enable verbose (DEBUG) logging. Shortcut for –log_level DEBUG.

Default:
    

`False`

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`True`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

\--auto_create_session¶
    

Automatically create a session if it doesn’t exist when calling /run.

\--with_ui¶
    

Serve ADK Web UI if set.

\--gemini_enterprise_app_name <gemini_enterprise_app_name>¶
    

The app_name to register with Gemini Enterprise via <https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent>

\--express_mode¶
    

Whether or not to initialize the server in express mode. This is only supported when gemini_enterprise_app_name is set. Defaults to False.

Arguments

AGENTS_DIR¶
    

Optional argument

### conformance¶

Conformance testing tools for ADK.

Usage
    
    
    adk conformance [OPTIONS] COMMAND [ARGS]...
    

#### record¶

Generate ADK conformance test recordings from spec.yaml files.

NOTE: this is work in progress.

This command reads TestSpec specifications from spec.yaml files, executes the specified test cases against agents, and writes the recorded agent interactions next to each spec.yaml.

Expected directory structure: category/name/spec.yaml (TestSpec) -> category/name/generated-recordings.yaml and category/name/generated-session.yaml (‘-sse’ suffix in sse mode)

PATHS: One or more directories containing test case specifications. If no paths are provided, defaults to ‘tests/’ directory.

STREAMING_MODE: The streaming mode to record in: none or sse.

Examples:

Use default directory: adk conformance record none

Custom directories: adk conformance record tests/core tests/tool sse

Usage
    
    
    adk conformance record [OPTIONS] [PATHS]... {none|sse|bidi}
    

Arguments

PATHS¶
    

Optional argument(s)

STREAMING_MODE¶
    

Required argument

#### test¶

Run conformance tests to verify agent behavior consistency.

Validates that agents produce consistent outputs by comparing against recorded interactions or evaluating live execution results.

PATHS can be any number of folder paths. Each folder can either: \- Contain a spec.yaml file directly (single test case) \- Contain subdirectories with spec.yaml files (multiple test cases)

If no paths are provided, defaults to searching for the ‘tests’ folder.

TEST MODES:

replay : Verifies agent interactions match previously recorded behaviors

exactly. Compares LLM requests/responses and tool calls/results.

live : Runs evaluation-based verification (not yet implemented)

DIRECTORY STRUCTURE:

Test cases must follow this structure:

category/

test_name/

spec.yaml # Test specification

generated-recordings.yaml # Recorded interactions (replay mode)

generated-session.yaml # Session data (replay mode)

generated-recordings-sse.yaml # Recorded SSE interactions (replay mode)

generated-session-sse.yaml # SSE Session data (replay mode)

REPORT GENERATION:

Use –generate_report to create a Markdown report of test results. Use –report_dir to specify where the report should be saved.

EXAMPLES:

# Run all tests in current directory’s ‘tests’ folder

adk conformance test

# Run tests from specific folders

adk conformance test tests/core tests/tool

# Run a single test case

adk conformance test tests/core/sys_instruction_001

# Run in live mode (when available)

adk conformance test –mode=live tests/core

# Generate a test report

adk conformance test –generate_report

# Generate a test report in a specific directory

adk conformance test –generate_report –report_dir=reports

Usage
    
    
    adk conformance test [OPTIONS] [PATHS]...
    

Options

\--mode <mode>¶
    

Test mode: ‘replay’ verifies against recorded interactions, ‘live’ runs evaluation-based verification.

Default:
    

`'replay'`

Options:
    

replay | live

\--generate_report¶
    

Optional. Whether to generate a Markdown report of the test results.

Default:
    

`False`

\--report_dir <report_dir>¶
    

Optional. Directory to store the generated report. Defaults to current directory.

\--streaming-mode <streaming_mode>¶
    

Options:
    

None | sse | bidi

Arguments

PATHS¶
    

Optional argument(s)

### create¶

Creates a new app in the current folder with prepopulated agent template.

APP_NAME: required, the folder of the agent source code.

Example:

> adk create path/to/my_app

Usage
    
    
    adk create [OPTIONS] APP_NAME
    

Options

\--model <model>¶
    

Optional. The model used for the root agent.

\--api_key <api_key>¶
    

Optional. The API Key needed to access the model, e.g. Google AI API Key.

\--project <project>¶
    

Optional. The Google Cloud Project for using VertexAI as backend.

\--region <region>¶
    

Optional. The Google Cloud Region for using VertexAI as backend.

\--type <type>¶
    

EXPERIMENTAL Optional. Type of agent to create: ‘config’ or ‘code’. ‘config’ is not ready for use so it defaults to ‘code’. It may change later once ‘config’ is ready for use.

Default:
    

`'CODE'`

Options:
    

CODE | CONFIG

Arguments

APP_NAME¶
    

Required argument

### deploy¶

Deploys agent to hosted environments.

Usage
    
    
    adk deploy [OPTIONS] COMMAND [ARGS]...
    

#### agent_engine¶

Deploys an agent to Agent Engine.

Example:

>  # With Express Mode API Key adk deploy agent_engine –api_key=[api_key] my_agent
> 
>  # With Google Cloud Project and Region adk deploy agent_engine –project=[project] –region=[region]
>
>> –display_name=[app_name] my_agent
> 
>  # With a private Cloud Build worker pool (VPC-SC / private network) adk deploy agent_engine –project=[project] –region=[region]
>
>> –worker_pool=projects/[project]/locations/[region]/workerPools/[pool] my_agent
> 
>  # With a custom runtime service account adk deploy agent_engine –project=[project] –region=[region]
>
>> –service_account=my-agent@[project].iam.gserviceaccount.com my_agent

Usage
    
    
    adk deploy agent_engine [OPTIONS] AGENT
    

Options

\--api_key <api_key>¶
    

Optional. The API key to use for Express Mode. If not provided, the API key from the GOOGLE_API_KEY environment variable will be used. It will only be used if GOOGLE_GENAI_USE_ENTERPRISE is true. (It will override GOOGLE_API_KEY in the .env file if it exists.)

\--project <project>¶
    

Optional. Google Cloud project to deploy the agent. It will override GOOGLE_CLOUD_PROJECT in the .env file (if it exists). It will be ignored if api_key is set.

\--region <region>¶
    

Optional. Google Cloud region to deploy the agent. It will override GOOGLE_CLOUD_LOCATION in the .env file (if it exists). It will be ignored if api_key is set.

\--staging_bucket <staging_bucket>¶
    

Deprecated. This argument is no longer required or used.

\--agent_engine_id <agent_engine_id>¶
    

Optional. ID of the Agent Engine instance to update if it exists (default: None, which means a new instance will be created). If project and region are set, this should be the resource ID, and the corresponding resource name in Agent Engine will be: projects/{project}/locations/{region}/reasoningEngines/{agent_engine_id}. If api_key is set, then agent_engine_id is required to be the full resource name (i.e. projects/*/locations/*/reasoningEngines/*).

\--trace_to_cloud, \--no-trace_to_cloud¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--otel_to_cloud¶
    

Optional. Whether to enable OpenTelemetry for Agent Engine.

\--display_name <display_name>¶
    

Optional. Display name of the agent in Agent Engine.

Default:
    

`''`

\--description <description>¶
    

Optional. Description of the agent in Agent Engine.

Default:
    

`''`

\--adk_app <adk_app>¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--temp_folder <temp_folder>¶
    

Optional. Temp folder for the generated Agent Engine source files. If the folder already exists, its contents will be removed. (default: a timestamped folder in the current working directory).

\--adk_app_object <adk_app_object>¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--env_file <env_file>¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--requirements_file <requirements_file>¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--absolutize_imports <absolutize_imports>¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--agent_engine_config_file <agent_engine_config_file>¶
    

Optional. The filepath to the .agent_engine_config.json file to use. The values in this file will be overridden by the values set by other flags. (default: the .agent_engine_config.json file in the agent directory, if any.)

\--validate-agent-import, \--no-validate-agent-import¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--skip-agent-import-validation¶
    

NOTE: This flag is deprecated and will be removed in the future.

\--trigger_sources <trigger_sources>¶
    

Optional. Comma-separated list of trigger sources to enable (e.g., ‘pubsub,eventarc’). Registers /trigger/* endpoints for batch and event-driven agent invocations.

\--trigger_oidc_audience <trigger_oidc_audience>¶
    

Optional. Expected audience for Google-signed OIDC bearer tokens on /apps/{app_name}/trigger/* endpoints.

\--trigger_oidc_service_accounts <trigger_oidc_service_accounts>¶
    

Optional. Comma-separated list of allowed service account emails for Google-signed OIDC tokens on /apps/{app_name}/trigger/* endpoints.

\--adk_version <adk_version>¶
    

Optional. The ADK version used in Agent Engine deployment. (default: the version in the dev environment)

Default:
    

`'2.12.0'`

\--extra_packages <extra_packages>¶
    

Optional. Additional local package paths (a file or directory) to stage and deploy alongside the agent, and make importable in the deployed image. Each entry is placed at /app/<basename> and /app is added to PYTHONPATH, so a top-level name that matches an installed dependency will shadow it at runtime; pick distinct names. Repeatable.

\--worker_pool <worker_pool>¶
    

Optional. Cloud Build private worker pool resource name used to build the Agent Engine container image. Format: projects/{project}/locations/{location}/workerPools/{pool}. Required for VPC-SC / private-network environments that cannot use the default public Cloud Build pool. Overrides worker_pool or build_config.worker_pool in .agent_engine_config.json.

\--service_account <service_account>¶
    

Optional. Google Cloud service account email used as the Agent Engine runtime identity (e.g. [my-agent@my-project.iam.gserviceaccount.com](mailto:my-agent%40my-project.iam.gserviceaccount.com)). Overrides GOOGLE_CLOUD_SERVICE_ACCOUNT in the .env file and service_account in .agent_engine_config.json. When omitted, Agent Engine uses its default service agent.

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`False`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

Arguments

AGENT¶
    

Required argument

#### cloud_run¶

Deploys an agent to Cloud Run.

AGENT: The path to the agent source code folder.

Use ‘–’ to separate gcloud arguments from adk arguments.

Examples:

> adk deploy cloud_run –project=[project] –region=[region] path/to/my_agent
> 
> adk deploy cloud_run –project=[project] –region=[region] path/to/my_agent
>     
> 
> – –no-allow-unauthenticated –min-instances=2

Usage
    
    
    adk deploy cloud_run [OPTIONS] AGENT
    

Options

\--project <project>¶
    

Required. Google Cloud project to deploy the agent. When absent, default project from gcloud config is used.

\--region <region>¶
    

Required. Google Cloud region to deploy the agent. When absent, gcloud run deploy will prompt later.

\--otel_to_cloud¶
    

Optional. Whether to enable OpenTelemetry export to GCP for Cloud Run deployments.

Default:
    

`False`

\--trigger_sources <trigger_sources>¶
    

Optional. Comma-separated list of trigger sources to enable (e.g., ‘pubsub,eventarc’). Registers /trigger/* endpoints for batch and event-driven agent invocations.

\--trigger_oidc_audience <trigger_oidc_audience>¶
    

Optional. Expected audience for Google-signed OIDC bearer tokens on /apps/{app_name}/trigger/* endpoints.

\--trigger_oidc_service_accounts <trigger_oidc_service_accounts>¶
    

Optional. Comma-separated list of allowed service account emails for Google-signed OIDC tokens on /apps/{app_name}/trigger/* endpoints.

\--with_cloud_run_sandbox¶
    

Optional. Whether to enable the Cloud Run sandbox for code execution. Requires the ‘gcloud beta run deploy’ release track.

Default:
    

`False`

\--extra_packages <extra_packages>¶
    

Optional. Additional local package paths (a file or directory) to stage and deploy alongside the agent, and make importable in the deployed image. Each entry is placed at /app/<basename> and /app is added to PYTHONPATH, so a top-level name that matches an installed dependency will shadow it at runtime; pick distinct names. Repeatable.

\--allow_origins <allow_origins>¶
    

Optional. Origins to allow for CORS. Can be literal origins (e.g., ‘<https://example.com>’) or regex patterns prefixed with ‘regex:’ (e.g., ‘regex:https://.*.example.com’).

\--a2a¶
    

Optional. Whether to enable A2A endpoint.

Default:
    

`False`

\--adk_version <adk_version>¶
    

Optional. The ADK version used in deployment. (default: the version in the dev environment)

Default:
    

`'2.12.0'`

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--temp_folder <temp_folder>¶
    

Optional. Temp folder for the generated source files (default: a timestamped folder in the system temp directory).

\--with_ui¶
    

Optional. Deploy ADK Web UI if set. (default: deploy ADK API server only)

Default:
    

`False`

\--trace_to_cloud¶
    

Optional. Whether to enable cloud tracing for deployment.

Default:
    

`False`

\--port <port>¶
    

Optional. The port of the ADK API server (default: 8000).

\--app_name <app_name>¶
    

Optional. App name of the ADK API server (default: the folder name of the AGENT source code).

\--provider-args <provider_args>¶
    

Optional. Additional flags passed through to the provider’s deployment tool (e.g. gcloud or docker).

\--env <env>¶
    

Optional. Environment variables as multiple –env key=value pairs. –env GOOGLE_GENAI_USE_ENTERPRISE=1

\--service_name <service_name>¶
    

Optional. The service name to use in target environment (default: ‘adk-default-service-name’).

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`False`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

Arguments

AGENT¶
    

Required argument

#### docker¶

Deploys an agent to a local Docker container.

Usage
    
    
    adk deploy docker [OPTIONS] AGENT
    

Options

\--allow_origins <allow_origins>¶
    

Optional. Origins to allow for CORS. Can be literal origins (e.g., ‘<https://example.com>’) or regex patterns prefixed with ‘regex:’ (e.g., ‘regex:https://.*.example.com’).

\--a2a¶
    

Optional. Whether to enable A2A endpoint.

Default:
    

`False`

\--adk_version <adk_version>¶
    

Optional. The ADK version used in deployment. (default: the version in the dev environment)

Default:
    

`'2.12.0'`

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--temp_folder <temp_folder>¶
    

Optional. Temp folder for the generated source files (default: a timestamped folder in the system temp directory).

\--with_ui¶
    

Optional. Deploy ADK Web UI if set. (default: deploy ADK API server only)

Default:
    

`False`

\--trace_to_cloud¶
    

Optional. Whether to enable cloud tracing for deployment.

Default:
    

`False`

\--port <port>¶
    

Optional. The port of the ADK API server (default: 8000).

\--app_name <app_name>¶
    

Optional. App name of the ADK API server (default: the folder name of the AGENT source code).

\--provider-args <provider_args>¶
    

Optional. Additional flags passed through to the provider’s deployment tool (e.g. gcloud or docker).

\--env <env>¶
    

Optional. Environment variables as multiple –env key=value pairs. –env GOOGLE_GENAI_USE_ENTERPRISE=1

\--service_name <service_name>¶
    

Optional. The service name to use in target environment (default: ‘adk-default-service-name’).

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`True`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

Arguments

AGENT¶
    

Required argument

#### gke¶

Deploys an agent to GKE.

AGENT: The path to the agent source code folder.

Example:

> adk deploy gke –project=[project] –region=[region]
>     
> 
> –cluster_name=[cluster_name] path/to/my_agent

Usage
    
    
    adk deploy gke [OPTIONS] AGENT
    

Options

\--project <project>¶
    

Required. Google Cloud project to deploy the agent. When absent, default project from gcloud config is used.

\--region <region>¶
    

Required. Google Cloud region to deploy the agent. When absent, gcloud run deploy will prompt later.

\--cluster_name <cluster_name>¶
    

Required. The name of the GKE cluster.

\--service_name <service_name>¶
    

Optional. The service name to use in GKE (default: ‘adk-default-service-name’).

\--app_name <app_name>¶
    

Optional. App name of the ADK API server (default: the folder name of the AGENT source code).

\--port <port>¶
    

Optional. The port of the ADK API server (default: 8000).

\--trace_to_cloud¶
    

Optional. Whether to enable Cloud Trace for GKE.

Default:
    

`False`

\--otel_to_cloud¶
    

Optional. Whether to enable OpenTelemetry for GKE.

Default:
    

`False`

\--with_ui¶
    

Optional. Deploy ADK Web UI if set. (default: deploy ADK API server only). WARNING: The web UI is for development and testing only — do not use in production.

Default:
    

`False`

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--service_type <service_type>¶
    

Optional. The Kubernetes Service type for the deployed agent. ClusterIP (default) keeps the service cluster-internal; use LoadBalancer to expose a public IP.

Default:
    

`'ClusterIP'`

Options:
    

ClusterIP | LoadBalancer

\--temp_folder <temp_folder>¶
    

Optional. Temp folder for the generated GKE source files (default: a timestamped folder in the system temp directory).

\--adk_version <adk_version>¶
    

Optional. The ADK version used in GKE deployment. (default: the version in the dev environment)

Default:
    

`'2.12.0'`

\--trigger_sources <trigger_sources>¶
    

Optional. Comma-separated list of trigger sources to enable (e.g., ‘pubsub,eventarc’). Registers /trigger/* endpoints for batch and event-driven agent invocations.

\--trigger_oidc_audience <trigger_oidc_audience>¶
    

Optional. Expected audience for Google-signed OIDC bearer tokens on /apps/{app_name}/trigger/* endpoints.

\--trigger_oidc_service_accounts <trigger_oidc_service_accounts>¶
    

Optional. Comma-separated list of allowed service account emails for Google-signed OIDC tokens on /apps/{app_name}/trigger/* endpoints.

\--extra_packages <extra_packages>¶
    

Optional. Additional local package paths (a file or directory) to stage and deploy alongside the agent, and make importable in the deployed image. Each entry is placed at /app/<basename> and /app is added to PYTHONPATH, so a top-level name that matches an installed dependency will shadow it at runtime; pick distinct names. Repeatable.

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`False`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

Arguments

AGENT¶
    

Required argument

### eval¶

Evaluates an agent given the eval sets.

AGENT_MODULE_FILE_PATH: The path to the agent folder, whose __init__.py imports a module by the name “agent”. “agent” module contains a root_agent.

EVAL_SET_FILE_PATH_OR_ID: You can specify one or more eval set file paths or eval set id.

Mixing of eval set file paths with eval set ids is not allowed.

_Eval Set File Path_ For each file, all evals will be run by default.

If you want to run only specific evals from an eval set, first create a comma separated list of eval names and then add that as a suffix to the eval set file name, demarcated by a :.

For example, we have sample_eval_set_file.json file that has following the eval cases: sample_eval_set_file.json:

> |……. eval_1 |……. eval_2 |……. eval_3 |……. eval_4 |……. eval_5

sample_eval_set_file.json:eval_1,eval_2,eval_3

This will only run eval_1, eval_2 and eval_3 from sample_eval_set_file.json.

_Eval Set ID_ For each eval set, all evals will be run by default.

If you want to run only specific evals from an eval set, first create a comma separated list of eval names and then add that as a suffix to the eval set file name, demarcated by a :.

For example, we have sample_eval_set_id that has following the eval cases: sample_eval_set_id:

> |……. eval_1 |……. eval_2 |……. eval_3 |……. eval_4 |……. eval_5

If we did:
    

sample_eval_set_id:eval_1,eval_2,eval_3

This will only run eval_1, eval_2 and eval_3 from sample_eval_set_id.

CONFIG_FILE_PATH: The path to config file.

PRINT_DETAILED_RESULTS: Prints detailed results on the console.

Usage
    
    
    adk eval [OPTIONS] AGENT_MODULE_FILE_PATH [EVAL_SET_FILE_PATH_OR_ID]...
    

Options

\--enable_features <enable_features>¶
    

Optional. Comma-separated list of feature names to enable. This provides an alternative to environment variables for enabling experimental features. Example: –enable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--disable_features <disable_features>¶
    

Optional. Comma-separated list of feature names to disable. This provides an alternative to environment variables for disabling features. Example: –disable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--config_file_path <config_file_path>¶
    

Optional. The path to config file.

\--print_detailed_results¶
    

Optional. Whether to print detailed results on console or not.

Default:
    

`False`

\--eval_storage_uri <eval_storage_uri>¶
    

Optional. The evals storage URI to store agent evals, supported URIs: gs://<bucket name>.

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

Arguments

AGENT_MODULE_FILE_PATH¶
    

Required argument

EVAL_SET_FILE_PATH_OR_ID¶
    

Optional argument(s)

### eval_set¶

Manage Eval Sets.

Usage
    
    
    adk eval_set [OPTIONS] COMMAND [ARGS]...
    

#### add_eval_case¶

Adds eval cases to the given eval set.

There are several ways that an eval case can be created, for now this method only supports adding one using a conversation scenarios file.

If an eval case for the generated id already exists, then we skip adding it.

Usage
    
    
    adk eval_set add_eval_case [OPTIONS] AGENT_MODULE_FILE_PATH EVAL_SET_ID
    

Options

\--scenarios_file <scenarios_file>¶
    

**Required** A path to file containing JSON serialized ConversationScenarios.

\--session_input_file <session_input_file>¶
    

**Required** Path to session file containing SessionInput in JSON format.

\--eval_storage_uri <eval_storage_uri>¶
    

Optional. The evals storage URI to store agent evals, supported URIs: gs://<bucket name>.

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

Arguments

AGENT_MODULE_FILE_PATH¶
    

Required argument

EVAL_SET_ID¶
    

Required argument

#### create¶

Creates an empty EvalSet given the agent_module_file_path and eval_set_id.

Usage
    
    
    adk eval_set create [OPTIONS] AGENT_MODULE_FILE_PATH EVAL_SET_ID
    

Options

\--eval_storage_uri <eval_storage_uri>¶
    

Optional. The evals storage URI to store agent evals, supported URIs: gs://<bucket name>.

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

Arguments

AGENT_MODULE_FILE_PATH¶
    

Required argument

EVAL_SET_ID¶
    

Required argument

#### generate_eval_cases¶

Generates eval cases dynamically and adds them to the given eval set.

Uses Vertex AI Eval SDK to generate conversation scenarios based on an Agent’s info and definitions. It will automatically create the empty eval_set if it has not been created in advance.

Args:
    

agent_module_file_path: The path to the agent folder. eval_set_id: The id of the eval set to generate cases for. user_simulation_config_file: The path to the user simulation config file. eval_storage_uri: The eval storage uri. log_level: The log level.

Usage
    
    
    adk eval_set generate_eval_cases [OPTIONS] AGENT_MODULE_FILE_PATH EVAL_SET_ID
    

Options

\--user_simulation_config_file <user_simulation_config_file>¶
    

**Required** A path to file containing JSON serialized UserScenarioGenerationConfig dict.

\--eval_storage_uri <eval_storage_uri>¶
    

Optional. The evals storage URI to store agent evals, supported URIs: gs://<bucket name>.

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

Arguments

AGENT_MODULE_FILE_PATH¶
    

Required argument

EVAL_SET_ID¶
    

Required argument

### migrate¶

ADK migration commands.

Usage
    
    
    adk migrate [OPTIONS] COMMAND [ARGS]...
    

#### session¶

Migrates a session database to the latest schema version.

Usage
    
    
    adk migrate session [OPTIONS]
    

Options

\--source_db_url <source_db_url>¶
    

**Required** SQLAlchemy URL of source database in database session service, e.g. sqlite:///source.db.

\--dest_db_url <dest_db_url>¶
    

**Required** SQLAlchemy URL of destination database in database session service, e.g. sqlite:///dest.db.

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--allow-unsafe-unpickling, \--allow_unsafe_unpickling¶
    

Optional. Allow unsafe pickle loading for trusted legacy session databases.

### optimize¶

Optimizes the root agent instructions using the GEPA optimizer.

AGENT_MODULE_FILE_PATH: The path to the agent folder, whose __init__.py imports a module by the name “agent”. “agent” module contains a root_agent.

SAMPLER_CONFIG_FILE_PATH: The path to the config for the LocalEvalSampler, which contains the eval config and the eval sets to use for training and validation during optimization.

OPTIMIZER_CONFIG_FILE_PATH: Optional. The path to the config for the GEPARootAgentPromptOptimizer. If not provided, the default config will be used.

PRINT_DETAILED_RESULTS: Optional. Enables printing detailed results exposed by the GEPA optimizer to the console.

LOG_LEVEL: Optional. Set the logging level.

Usage
    
    
    adk optimize [OPTIONS] AGENT_MODULE_FILE_PATH
    

Options

\--sampler_config_file_path <sampler_config_file_path>¶
    

**Required** The path to the local eval sampler config file.

\--optimizer_config_file_path <optimizer_config_file_path>¶
    

Optional. The path to the GEPA optimizer config file. If not provided, the default config will be used.

\--print_detailed_results¶
    

Optional. Set to enable detailed printing of GEPA optimization results to the console.

Default:
    

`False`

\--log_level <log_level>¶
    

Optional. Set the logging level

Default:
    

`'INFO'`

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

Arguments

AGENT_MODULE_FILE_PATH¶
    

Required argument

### run¶

Runs an agent. If no query is provided, enters interactive mode.

AGENT: The path to the agent source code folder. QUERY: Optional. The user message to send to the agent for a single-step run.

Example:

> adk run path/to/my_agent adk run path/to/my_agent “hello”

Usage
    
    
    adk run [OPTIONS] AGENT [QUERY]
    

Options

\--enable_features <enable_features>¶
    

Optional. Comma-separated list of feature names to enable. This provides an alternative to environment variables for enabling experimental features. Example: –enable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--disable_features <disable_features>¶
    

Optional. Comma-separated list of feature names to disable. This provides an alternative to environment variables for disabling features. Example: –disable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`True`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

-v, \--verbose¶
    

Enable verbose (DEBUG) logging. Shortcut for –log_level DEBUG.

Default:
    

`False`

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--save_session¶
    

Optional. Whether to save the session to a json file on exit.

Default:
    

`False`

\--session_id <session_id>¶
    

Optional. The session ID to save the session to on exit when –save_session is set to true. User will be prompted to enter a session ID if not set.

\--replay <replay>¶
    

The json file that contains the initial state of the session and user queries. A new session will be created using this state. And user queries are run against the newly created session. Users cannot continue to interact with the agent.

\--resume <resume>¶
    

The json file that contains a previously saved session (by –save_session option). The previous session will be re-displayed. And user can continue to interact with the agent.

\--state <state>¶
    

Optional. Initial state for the run as a JSON string.

\--state_file <state_file>¶
    

Optional. Path to a JSON file containing initial state for the run.

\--timeout <timeout>¶
    

Optional. Timeout for a single turn or query (e.g., 30s, 5m).

\--in_memory¶
    

Optional. Do not persist session data (use in-memory storage).

\--jsonl¶
    

Optional. Output structured JSONL instead of human-readable text.

\--default_llm_model <default_llm_model>¶
    

Optional. Sets the default LLM model used when the agent does not set a model explicitly.

Arguments

AGENT¶
    

Required argument

QUERY¶
    

Optional argument

### telemetry¶

Manage telemetry settings.

Usage
    
    
    adk telemetry [OPTIONS] COMMAND [ARGS]...
    

#### disable¶

Disable telemetry collection.

Usage
    
    
    adk telemetry disable [OPTIONS]
    

#### enable¶

Enable telemetry collection.

Usage
    
    
    adk telemetry enable [OPTIONS]
    

#### status¶

Show telemetry collection status.

Usage
    
    
    adk telemetry status [OPTIONS]
    

### test¶

Runs pytest on agent test JSON files under the specified folder.

FOLDER: The path to the folder containing agents and tests. Defaults to the current directory if not specified.

Example:
    

adk test path/to/agents

Usage
    
    
    adk test [OPTIONS] [FOLDER]
    

Options

\--rebuild¶
    

Rebuild test files by running the real agent with user messages.

Arguments

FOLDER¶
    

Optional argument

### web¶

Starts a FastAPI server with Web UI for agents.

AGENTS_DIR: The directory of agents (where each subdirectory is a single agent containing agent.py, __init__.py, or root_agent.yaml) or a path pointing directly to a single agent folder.

This server is intended for local development. Its endpoints are unauthenticated, so run it on a trusted network only and do not expose it to untrusted or public networks.

Example:

> adk web –session_service_uri=[uri] –port=[port] path/to/agents_dir

Usage
    
    
    adk web [OPTIONS] [AGENTS_DIR]
    

Options

\--enable_features <enable_features>¶
    

Optional. Comma-separated list of feature names to enable. This provides an alternative to environment variables for enabling experimental features. Example: –enable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--disable_features <disable_features>¶
    

Optional. Comma-separated list of feature names to disable. This provides an alternative to environment variables for disabling features. Example: –disable_features=JSON_SCHEMA_FOR_FUNC_DECL,PROGRESSIVE_SSE_STREAMING

\--host <host>¶
    

Optional. The binding host of the server

Default:
    

`'127.0.0.1'`

\--port <port>¶
    

Optional. The port of the server

\--allow_origins <allow_origins>¶
    

Optional. Origins to allow for CORS. Can be literal origins (e.g., ‘<https://example.com>’) or regex patterns prefixed with ‘regex:’ (e.g., ‘regex:https://.*.example.com’).

\--trace_to_cloud¶
    

Optional. Whether to enable cloud trace for telemetry.

Default:
    

`False`

\--otel_to_cloud¶
    

Optional. Whether to write OTel data to Google Cloud Observability services - Cloud Trace and Cloud Logging.

Default:
    

`False`

\--reload, \--no-reload¶
    

Optional. Whether to enable auto reload for server. Not supported for Cloud Run.

\--a2a¶
    

Optional. Whether to enable A2A endpoint.

Default:
    

`False`

\--reload_agents¶
    

Optional. Whether to enable live reload for agents changes.

Default:
    

`False`

\--eval_storage_uri <eval_storage_uri>¶
    

Optional. The evals storage URI to store agent evals, supported URIs: gs://<bucket name>.

\--extra_plugins <extra_plugins>¶
    

Optional. Comma-separated list of extra plugin classes or instances to enable (e.g., my.module.MyPluginClass or my.module.my_plugin_instance).

\--url_prefix <url_prefix>¶
    

Optional. URL path prefix when the application is mounted behind a reverse proxy or API gateway (e.g., ‘/api/v1’, ‘/adk’). This ensures generated URLs and redirects work correctly when the app is not served at the root path. Must start with ‘/’ if provided.

\--avatar_config <avatar_config>¶
    

Optional. AvatarConfig as an inline JSON object or a path to a JSON file. Applied only to /run_live sessions whose client requests video output (modalities=VIDEO); other live sessions ignore it. If unset, video sessions use the pre-built ‘Kai’ avatar.

\--max_llm_calls <max_llm_calls>¶
    

Optional. Maximum number of LLM calls allowed for each agent run. Values less than or equal to zero disable the limit.

\--trigger_sources <trigger_sources>¶
    

Optional. Comma-separated list of trigger sources to enable (e.g., ‘pubsub,eventarc’). Registers /apps/{app_name}/trigger/* endpoints for batch and event-driven agent invocations.

\--trigger_oidc_audience <trigger_oidc_audience>¶
    

Optional. Expected audience for Google-signed OIDC bearer tokens on /apps/{app_name}/trigger/* endpoints. When set, requests without a valid token matching this audience are rejected with 401.

\--trigger_oidc_service_accounts <trigger_oidc_service_accounts>¶
    

Optional. Comma-separated list of allowed service account emails for Google-signed OIDC tokens on /apps/{app_name}/trigger/* endpoints. Requires –trigger_oidc_audience.

-v, \--verbose¶
    

Enable verbose (DEBUG) logging. Shortcut for –log_level DEBUG.

Default:
    

`False`

\--log_level <log_level>¶
    

Optional. Set the logging level

Options:
    

DEBUG | INFO | WARNING | ERROR | CRITICAL

\--logo-text <logo_text>¶
    

Optional. The text to display in the logo of the web UI.

\--logo-image-url <logo_image_url>¶
    

Optional. The URL of the image to display in the logo of the web UI.

\--session_service_uri <session_service_uri>¶
    

Optional. The URI of the session service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Sessions when

an Agent Platform environment is detected. Otherwise, it chooses a

default session service (see –use_local_storage).

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘memory://’ to run with the in-memory session service.

\- Use ‘sqlite://<path_to_sqlite_file>’ to connect to a SQLite DB.

\- See <https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls>

for supported database URIs.

\--artifact_service_uri <artifact_service_uri>¶
    

Optional. The URI of the artifact service. If set, ADK uses this service.

If unset, ADK chooses a default artifact service (see

–use_local_storage).

\- Use ‘gs://<bucket_name>’ to connect to the GCS artifact service.

\- Use ‘memory://’ to force the in-memory artifact service.

\- Use ‘[file:/](file:/)/<path>’ to store artifacts in a custom local directory.

\--use_local_storage, \--no_use_local_storage¶
    

Optional. Whether to use local .adk storage when explicit service URIs are unset, and an Agent Platform environment is not detected. Cannot be combined with explicit service URIs. When the agents directory isn’t writable (common in Cloud Run/Kubernetes), ADK falls back to in-memory unless overridden by ADK_FORCE_LOCAL_STORAGE=1 or ADK_DISABLE_LOCAL_STORAGE=1.

Default:
    

`True`

\--memory_service_uri <memory_service_uri>¶
    

Optional. The URI of the memory service. If set, ADK uses this service.

If unset, ADK automatically connects to Agent Platform Memory Bank

when an Agent Platform environment is detected. Otherwise, it uses

the default memory service.

\- Use ‘rag://<rag_corpus_id>’ to connect to Vertex AI Rag Memory Service.

\- Use ‘agentengine://<agent_engine>’ to connect to Agent Engine

sessions. <agent_engine> can either be the full qualified resource

name ‘projects/abc/locations/us-central1/reasoningEngines/123’ or

the resource id ‘123’.

\- Use ‘sqlite:///<relative_path>’ / ‘sqlite:////<absolute_path>’ to connect to SQLite memory service.

\- Use ‘memory://’ to force the in-memory memory service.

\--default_llm_model <default_llm_model>¶
    

Optional. Sets the default LLM model used when the agent does not set a model explicitly.

Arguments

AGENTS_DIR¶
    

Optional argument

### Quick search

(C)2026, Google. | Powered by [Sphinx 9.1.0](https://www.sphinx-doc.org/) & [Alabaster 1.0.0](https://alabaster.readthedocs.io) | [Page source](_sources/index.rst.txt)
