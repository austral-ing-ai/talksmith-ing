# About supervised fine-tuning for Gemini models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

_Source: <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning>_

[Skip to main content](#main-content) ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5be16d8c9f9402e54c2da2ff24cb75c148f5d2bc84c6f8dfc8b9e16ae456160b/clouddocs/images/lockup_full_color.svg) </> [Console](//console.cloud.google.com/) 

- English 
- Deutsch 
- Español – América Latina 
- Français 
- Indonesia 
- Italiano 
- Português – Brasil 
- עברית 
- 中文 – 简体 
- 中文 – 繁體 
- 日本語 
- 한국어 
Sign in ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) <https://docs.cloud.google.com/gemini-enterprise-agent-platform> 

- [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform) 
[Start free](//console.cloud.google.com/freetrial) 

- [Home](https://docs.cloud.google.com/) 
- [Documentation](https://docs.cloud.google.com/docs) 
- [AI and ML](https://docs.cloud.google.com/docs/ai-ml) 
- [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform) 
- [Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models) 
 Send feedback 

#  About supervised fine-tuning for Gemini models  Stay organized with collections  Save and categorize content based on your preferences. 

Supervised fine-tuning is a good option when you have a well-defined task with available labeled data. It's particularly effective for domain-specific applications where the language or content significantly differs from the data the large model was originally trained on. You can tune [text](/gemini-enterprise-agent-platform/models/tuning/text), [image](/gemini-enterprise-agent-platform/models/tuning/image), [audio](/gemini-enterprise-agent-platform/models/tuning/audio), [video](/gemini-enterprise-agent-platform/models/tuning/video), and [document](/gemini-enterprise-agent-platform/models/tuning/document) data types. You can also create Gemini-based applications and agents that can interact with real-time information and services like databases, customer relationship management systems, and document repositories.

Supervised fine-tuning adapts model behavior with a labeled dataset. This process adjusts the model's weights to minimize the difference between its predictions and the actual labels. For example, it can improve model performance for the following types of tasks:

- Classification 
- Summarization 
- Extractive question answering 
- Chat 

For a discussion of the top tuning use cases, check out the blog post [Hundreds of organizations are fine-tuning Gemini models. Here's their favorite use cases](https://cloud.google.com/transform/top-five-gen-ai-tuning-use-cases-gemini-hundreds-of-orgs).

To learn more, see [When to use supervised fine-tuning for Gemini](https://cloud.google.com/blog/products/ai-machine-learning/supervised-fine-tuning-for-gemini-llm?e=48754805).

## Supported models

The following Gemini models support supervised fine-tuning:

#### Click to expand supported models

- [Gemini 3.5 Flash](/gemini-enterprise-agent-platform/models/gemini/3-5-flash) 
- [Gemini 3.1 Flash-Lite](/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite) 
- [Gemini 2.5 Pro](/gemini-enterprise-agent-platform/models/gemini/2-5-pro) 
- [Gemini 2.5 Flash-Lite](/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite) 
- [Gemini 2.5 Flash](/gemini-enterprise-agent-platform/models/gemini/2-5-flash) 

## Limitations

Supervised fine-tuning is not a Covered Service and is excluded from the SLO of any Service Level Agreement.

The following table shows the limitations on supervised fine-tuning datasets:

###  Gemini 3.5 Flash

Specification Value Maximum input and output tokens per training example 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum number of examples in a validation dataset 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, 8, and 16 Supported endpoint for model tuning `us-central1`, and `europe-west4` Supported endpoint for tuned model serving `us` and `eu` multi-region endpoints only CMEK support Not supported 

###  Gemini 3.1 Flash-Lite

Specification Value Maximum input and output tokens per training example 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum number of examples in a validation dataset 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, 8, and 16 Supported endpoint for model tuning `us-central1`, and `europe-west4` Supported endpoint for tuned model serving `us` and `eu` multi-region endpoints only CMEK support Not supported 

### Gemini 2.5 Flash  
Gemini 2.5 Flash-Lite

Specification Value Maximum input and output tokens per training example 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum number of examples in a validation dataset 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, 8, and 16 

### Gemini 2.5 Pro

Specification Value Maximum input and output training tokens 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum validation dataset size 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, and 8 

## Known issues

- Applying [controlled generation](/gemini-enterprise-agent-platform/models/capabilities/control-generated-output) when submitting inference requests to tuned Gemini models can result in decreased model quality due to data misalignment during tuning and inference time. During tuning, controlled generation isn't applied, so the tuned model isn't able to handle controlled generation well at inference time. Supervised fine-tuning effectively customizes the model to generate structured output. Therefore you don't need to apply controlled generation when making inference requests on tuned models. 

## Use cases for using supervised fine-tuning

Foundation models work well when the expected output or task can be clearly and concisely defined in a prompt and the prompt consistently produces the expected output. If you want a model to learn something niche or specific that deviates from general patterns, then you might want to consider tuning that model. For example, you can use model tuning to teach the model the following:

- Specific structures or formats for generating output. 
- Specific behaviors such as when to provide a terse or verbose output. 
- Specific customized outputs for specific types of inputs. 

The following examples are use cases that are difficult to capture with only prompt instructions:

- 

**Classification**: The expected response is a specific word or phrase.

**Prompt:**  Classify the following text into one of the following classes: [business, entertainment]. Text: Diversify your investment portfolio 

**Response:**  business 

Tuning the model can help prevent the model from generating verbose responses.

- 

**Summarization**: The summary follows a specific format. For example, you might need to remove personally identifiable information (PII) in a chat summary.

**Prompt:**  Summarize: Jessica: That sounds great! See you in Times Square! Alexander: See you at 10! 

**Response:**  #Person1 and #Person2 agree to meet at Times Square at 10:00 AM. 

This formatting of replacing the names of the speakers with `#Person1` and `#Person2` is difficult to describe and the foundation model might not naturally produce such a response.

- 

**Extractive question answering**: The question is about a context and the answer is a substring of the context.

**Prompt:**  Context: There is evidence that there have been significant changes in Amazon rainforest vegetation over the last 21,000 years through the Last Glacial Maximum (LGM) and subsequent deglaciation. Question: What does LGM stand for? 

**Response:**  Last Glacial Maximum 

The response "Last Glacial Maximum" is a specific phrase from the context.

- 

**Chat**: You need to customize model response to follow a persona, role, or character.

**Prompt:**  User: What's the weather like today? 

**Response:**  Assistant: As the virtual shopkeeper of Example Organization, I can only help you with the purchases and shipping. 

You can also tune a model in the following situations:

- Prompts are not producing the expected results consistently enough. 
- The task is too complicated to define in a prompt. For example, you want the model to do behavior cloning for a behavior that's hard to articulate in a prompt. 
- You have complex intuitions about a task that are difficult to formalize in a prompt. 
- You want to reduce the context length by removing the few-shot examples. 

## Configure a tuning job region

User data, such as the transformed dataset and the tuned model, is stored in the tuning job region. During tuning, computation could be offloaded to other `US` or `EU` regions for available accelerators. The offloading is transparent to users.

- 

If you use the Vertex AI SDK, you can specify the region at initialization. For example:

```
import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
[vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(project='myproject', location='us-central1')

```

- 

If you create a supervised fine-tuning job by sending a POST request using the ``[tuningJobs.create](/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tuningJobs/create) method, then you use the URL to specify the region where the tuning job runs. For example, in the following URL, you specify a region by replacing both instances of `TUNING_JOB_REGION` with the region where the job runs.

```
 https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs

```

- 

If you use the [Google Cloud console](/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning#create_a_text_model_supervised_tuning_job), you can select the region name in the **Region** drop-down field on the **Model details** page. This is the same page where you select the base model and a tuned model name.

## Evaluating tuned models

You can evaluate tuned models in the following ways:

- 

**Tuning and validation metrics**: [Evaluate the tuned model](/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning#evaluate_the_tuned_model) using [tuning and validation metrics](/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning#tuning-metrics) after the tuning job completes.

- 

**Integrated evaluation with Gen AI evaluation service** (Preview): [Configure tuning jobs](/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning#create_a_text_model_supervised_tuning_job) to automatically run evaluations using the [Gen AI evaluation service](/gemini-enterprise-agent-platform/models/evaluation-overview) during tuning. The following interfaces, models, and regions are supported for the tuning integration with Gen AI evaluation service:

- 

**Supported interfaces**: Google Gen AI SDK and REST API.

- 

**Supported models**: `gemini-2.5-pro`, `gemini-2.5-flash`, and `gemini-2.5-flash-lite`.

- 

**Supported regions**: For a list of supported regions, see [Supported regions](/gemini-enterprise-agent-platform/models/evaluation-overview#supported-regions).

## Quota

Quota is enforced on the number of concurrent tuning jobs. Every project comes with a default quota to run at least one tuning job. This is a global quota, shared across all available regions and supported models. If you want to run more jobs concurrently, you need to [request additional quota](/docs/quota_detail/view_manage#requesting_higher_quota) for `Global concurrent tuning jobs`.

If you configure the [Gen AI evaluation service](/gemini-enterprise-agent-platform/models/evaluation-overview) to run evaluations automatically during tuning, see the [Gen AI evaluation service quotas](/gemini-enterprise-agent-platform/models/quotas#eval-quotas).

## Pricing

Pricing for Gemini supervised fine-tuning can be found here: [Gemini Enterprise Agent Platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing).

The number of training tokens is calculated by multiplying the number of tokens in your training dataset by the number of epochs. After tuning, inference (prediction request) costs for the tuned model still apply. Inference pricing is the same for each stable version of Gemini. For more information, see [Available Gemini stable model versions](/gemini-enterprise-agent-platform/models/model-versions#stable-versions-available).

If you configure the Gen AI evaluation service to run automatically during tuning, evaluations are charged as batch prediction jobs. For more information, see [Pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#prediction-prices).

## What's next

- Learn about [supervised fine-tuning](/gemini-enterprise-agent-platform/models/gemini-supervised-tuning). 
- Learn about [deploying a tuned Gemini model](/gemini-enterprise-agent-platform/models/deploy/overview#deploy_a_tuned_model). 
 Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

 Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]]
