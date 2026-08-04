# GPT-5.5 Size Estimated at 9.7 Trillion Parameters | Kirill A. B. posted on the topic | LinkedIn

_Source: <https://www.linkedin.com/posts/kirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-share-7455363398248271872-H64Y/?utm_medium=ios_app&rcm=ACoAACFnwO0BSM_PUdN56uDdT0mCuYlxq4cK3fc&utm_source=social_share_send&utm_campaign=whatsapp>_

`` `` `` `` `` `` `` [Skip to main content](#main-content) 

#  GPT-5.5 Size Estimated at 9.7 Trillion Parameters

This title was summarized by AI from the post below. <https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [1,750](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [92 Comments](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_social-actions-comments) [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 
<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_comment_actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

Full paper is here [https://arxiv.org/pdf/2604.24827](https://arxiv.org/pdf/2604.24827?trk=public_post_comment-text)

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [13 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  14 Reactions <https://www.linkedin.com/in/dhyey-mavani?trk=public_post_comment_actor-image> [Dhyey Mavani](https://www.linkedin.com/in/dhyey-mavani?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

We gotta stop premature scaling of pre-training. AI labs are incentivised to do it because it lends guaranteed improvements (basics of information theory), but it's local optima. It'd be tragic to win the battle, but lose the war!

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  3 Reactions <https://uk.linkedin.com/in/dio77?trk=public_post_comment_actor-image> [Igor Diev](https://uk.linkedin.com/in/dio77?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

Next step – to estimate how expensive it is to infer it

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  3 Reactions <https://de.linkedin.com/in/davide-mattioli-605ab41b3?trk=public_post_comment_actor-image> [Davide Mattioli](https://de.linkedin.com/in/davide-mattioli-605ab41b3?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

Honestly what bothers me about this paper are the claims in the model table. Saying “GPT-5.5 ≈ 9.7T” looks much more concrete than the method deserves, even though the nominal 90% interval is already 3.2T–28.7T, and a rough 99% interval would be something like 1.7T–54T under the same assumptions. The paper does disclose the 3× interval, but the headline estimates are still easy to overinterpret. With such an huge variance i think the statement is misleading and not fairly presented.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [19 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  20 Reactions <https://sg.linkedin.com/in/georgzoeller?trk=public_post_comment_actor-image> [Georg Zoeller](https://sg.linkedin.com/in/georgzoeller?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

Number of parameters also tells you model economics (although active parameter in MoE can be obscured) and that would be very bad news 

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [4 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  5 Reactions <https://in.linkedin.com/in/sidhant-p-thole-62128aaa?trk=public_post_comment_actor-image> [Sidhant P Thole](https://in.linkedin.com/in/sidhant-p-thole-62128aaa?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

I hope in while gauging size of these models, Model did not have access to the internet, otherwise whole point fails. Also, the questions should be pure factual which could not be derived by just connecting facts. Also, I see model refusals as well, which might be due to external guardrails and not the model.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  3 Reactions <https://pl.linkedin.com/in/ivan-cherepanov?trk=public_post_comment_actor-image> [Ivan Charapanau](https://pl.linkedin.com/in/ivan-cherepanov?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

It looks like it doesn't account for the time of the release. Models of the same size released just two years apart demonstrate drastically different depth and breadth of capability and knowledge

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  3 Reactions <https://no.linkedin.com/in/drcrutch?trk=public_post_comment_actor-image> [Bohdan Krechko](https://no.linkedin.com/in/drcrutch?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

It looks like we've reached a plateau in model performance just by scaling up the number of parameters. I think the next step will be integrating tools directly into the system

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [2 Reactions](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  3 Reactions <https://www.linkedin.com/in/isaac-to?trk=public_post_comment_actor-image> [Isaac To](https://www.linkedin.com/in/isaac-to?trk=public_post_comment_actor-name)  3mo 

- [Report this comment](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=COMMENT&_f=guest-reporting) 

I think another measure e.g. time might be useful. Newer models tend to be more efficient which means that the older models are actually shifting the down a bit. Given how recent models like Kimi K2.6 and DeepSeek V4 are very much above the line, we can similarly infer that GPT5.5 will also be above that line. 9.7T might be overshooting it a bit.

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_like) [Reply](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reply) [1 Reaction](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_comment_reactions)  2 Reactions [See more comments](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_see-more-comments) 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_feed-cta-banner-cta) 

`` 

##  More Relevant Posts 

- <https://www.linkedin.com/posts/valtteri-valo_before-you-go-around-citing-this-information-activity-7455542606320590848-3GTY> <https://fi.linkedin.com/in/valtteri-valo?trk=public_post_feed-actor-image> [Valtteri Valo](https://fi.linkedin.com/in/valtteri-valo?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvaltteri-valo_before-you-go-around-citing-this-information-activity-7455542606320590848-3GTY&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

before you go around citing this information, you might want to keep in mind that the actual 90% PI they give is 3.2T to 28.7T. 

<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-name) 

 Building AI Products • PhD • Product Leader • AI/ML • Cybersecurity • Mentor & Educator • UK Global Talent 

 3mo 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [2](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvaltteri-valo_before-you-go-around-citing-this-information-activity-7455542606320590848-3GTY&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvaltteri-valo_before-you-go-around-citing-this-information-activity-7455542606320590848-3GTY&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvaltteri-valo_before-you-go-around-citing-this-information-activity-7455542606320590848-3GTY&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvaltteri-valo_before-you-go-around-citing-this-information-activity-7455542606320590848-3GTY&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/vincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG> <https://www.linkedin.com/in/vincentg?trk=public_post_feed-actor-image> [Vincent Granville](https://www.linkedin.com/in/vincentg?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

My alternative to deep neural networks has 10k (yes, 10,000). No millions. Not billions. Not trillions. And it does better predictions for my LLM needs than multi-trillion models. A precursor to this model is described at [https://lnkd.in/g9pwr2Ej](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2Fg9pwr2Ej&urlhash=N4xB&trk=public_post-text)

<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-name) 

 Building AI Products • PhD • Product Leader • AI/ML • Cybersecurity • Mentor & Educator • UK Global Talent 

 3mo 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [12](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [3 Comments](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG&trk=public_post_social-actions-comments) [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fvincentg_my-alternative-to-deep-neural-networks-has-activity-7456126514938662912-6wkG&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/falmanna_if-this-is-true-it-means-models-are-not-activity-7455671223742693376-GViT> <https://tr.linkedin.com/in/falmanna?trk=public_post_feed-actor-image> [Feras AlManna](https://tr.linkedin.com/in/falmanna?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ffalmanna_if-this-is-true-it-means-models-are-not-activity-7455671223742693376-GViT&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

'IF' this is true, it means models are not getting smarter, they are just decreasing the compression effect. If we can't do significant improvements without significant model size increase then it's just a saturation game. 

<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-name) 

 Building AI Products • PhD • Product Leader • AI/ML • Cybersecurity • Mentor & Educator • UK Global Talent 

 3mo 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [2](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ffalmanna_if-this-is-true-it-means-models-are-not-activity-7455671223742693376-GViT&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ffalmanna_if-this-is-true-it-means-models-are-not-activity-7455671223742693376-GViT&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ffalmanna_if-this-is-true-it-means-models-are-not-activity-7455671223742693376-GViT&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ffalmanna_if-this-is-true-it-means-models-are-not-activity-7455671223742693376-GViT&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/dhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR> <https://www.linkedin.com/in/dhyey-mavani?trk=public_post_feed-actor-image> [Dhyey Mavani](https://www.linkedin.com/in/dhyey-mavani?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fdhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

We gotta stop premature scaling of pre-training. AI labs are incentivised to do it because it lends guaranteed improvements (basics of information theory), but it's local optima. It'd be tragic to win the battle, but lose the war!

<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-name) 

 Building AI Products • PhD • Product Leader • AI/ML • Cybersecurity • Mentor & Educator • UK Global Talent 

 3mo 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [12](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fdhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [1 Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fdhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR&trk=public_post_social-actions-comments) [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fdhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fdhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fdhyey-mavani_we-gotta-stop-premature-scaling-of-pre-training-activity-7455487392712679426-SoLR&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/khang-doan-249969166_oh-the-author-compiled-1400-questions-activity-7458106120646279168-XReb> <https://vn.linkedin.com/in/khang-doan-249969166?trk=public_post_feed-actor-image> [Khang Doan](https://vn.linkedin.com/in/khang-doan-249969166?trk=public_post_feed-actor-name)  2mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkhang-doan-249969166_oh-the-author-compiled-1400-questions-activity-7458106120646279168-XReb&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

Oh !!! The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts.

<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-name) 

 Building AI Products • PhD • Product Leader • AI/ML • Cybersecurity • Mentor & Educator • UK Global Talent 

 3mo 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [8](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkhang-doan-249969166_oh-the-author-compiled-1400-questions-activity-7458106120646279168-XReb&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkhang-doan-249969166_oh-the-author-compiled-1400-questions-activity-7458106120646279168-XReb&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkhang-doan-249969166_oh-the-author-compiled-1400-questions-activity-7458106120646279168-XReb&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fkhang-doan-249969166_oh-the-author-compiled-1400-questions-activity-7458106120646279168-XReb&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/tcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE> <https://uk.linkedin.com/in/tcreswick?trk=public_post_feed-actor-image> [Tim Creswick](https://uk.linkedin.com/in/tcreswick?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

I've often thought about the fundamental data storage efficiency of these models - didn't think to actually test it this way. Very elegant, and pretty fascinating that the method more or less seems to hold up. Worth a read 🤓 

<https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-image> [Kirill A. B.](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_reshare_feed-actor-name) 

 Building AI Products • PhD • Product Leader • AI/ML • Cybersecurity • Mentor & Educator • UK Global Talent 

 3mo 

GPT-5.5 (likely) has 9.7 trillion (!) parameters. A Chinese researcher simply calculated what OpenAI keeps hidden 😬 I was hooked by a paper on IKP – a benchmark that estimates the size of closed models through their store of factual knowledge. The logic goes like this: factual knowledge can't be distilled or compressed the way reasoning capabilities can – it's bounded by Shannon entropy. The author compiled 1,400 questions about obscure facts, ran them through 89 open models, and found a strong log-linear relationship between scores and parameter counts. For an approach that reads almost like a gamble on first glance, the justification is surprisingly solid. Estimates for closed models (lower bounds due to safety refusals): GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T, Gemini 2.5 Pro ≈ 1.2T. What surprised me most is that GPT-5.5 comes out twice the size of Opus – though this may well be within the margin of error. And there's an open question: how will the method hold up in a world with search use? In theory, external tools should introduce a lot of noise. For now the results look predictable, but the boundary between a model's internal knowledge and the external retrieval loop may turn out to be far from obvious (or we can't guarantee there is no internal knowledge base use). And yes – another interesting AI paper from China, not the US.

- 
`` `` [4](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [1 Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE&trk=public_post_social-actions-comments) [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftcreswick_ive-often-thought-about-the-fundamental-activity-7456435371694862336-IHzE&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/asteris-ai_amel-accumulated-message-effects-on-llm-activity-7464336914939150336-mNlx> <https://www.linkedin.com/company/asteris-ai?trk=public_post_feed-actor-image> [Asteris.ai](https://www.linkedin.com/company/asteris-ai?trk=public_post_feed-actor-name) 

 530 followers 

 2mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fasteris-ai_amel-accumulated-message-effects-on-llm-activity-7464336914939150336-mNlx&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

🧪 YOUR LLM JUDGE MAY BE CARRYING BAGGAGE A lot of AI evaluation pipelines now quietly rely on LLMs as judges. They review code, moderate content, score responses and compare outputs. The assumption is that if the judging prompt is well written, the model will evaluate each item fairly. AMEL challenges that assumption by asking a simple question: does the prior conversation history bias the next judgement? The paper ran 75,898 API calls across 11 models from four providers and found that models shift towards the prevailing tone of the previous conversation. Negative histories created 1.62x more bias than positive histories, and the effect was strongest when the model was uncertain. The practical lesson is not glamorous, but it matters. If you are using an LLM to judge many items, a fresh context per item may be one of the cheapest quality improvements available. This is the kind of issue that does not show up in a demo, but can quietly distort production systems. Has anyone else seen judge models behave differently after a long run of similar examples? Sources: - [https://lnkd.in/eKdbEB2n](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FeKdbEB2n&urlhash=bj0u&trk=public_post-text) [#AIResearch](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fairesearch&trk=public_post-text) [#LLMEvaluation](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fllmevaluation&trk=public_post-text) [#MachineLearning](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fmachinelearning&trk=public_post-text) [#ResponsibleAI](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fresponsibleai&trk=public_post-text)

[AMEL: Accumulated Message Effects on LLM Judgments  arxiv.org](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Farxiv%2Eorg%2Fabs%2F2605%2E22714v1&urlhash=-3Ak&trk=public_post_feed-article-content) `` `` [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fasteris-ai_amel-accumulated-message-effects-on-llm-activity-7464336914939150336-mNlx&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fasteris-ai_amel-accumulated-message-effects-on-llm-activity-7464336914939150336-mNlx&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fasteris-ai_amel-accumulated-message-effects-on-llm-activity-7464336914939150336-mNlx&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/ali-mehdy-b2b335b0_and-yet-gpt-claude-gemini-every-llm-activity-7459854305676816385-Qaqv> 
- <https://www.linkedin.com/posts/courtlinholt_11-tips-to-spend-tokens-smarter-on-gpt-55-activity-7456997168562978816-fi4Q> <https://sg.linkedin.com/in/courtlinholt?trk=public_post_feed-actor-image> [Courtlin Holt-Nguyen](https://sg.linkedin.com/in/courtlinholt?trk=public_post_feed-actor-name)  3mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fcourtlinholt_11-tips-to-spend-tokens-smarter-on-gpt-55-activity-7456997168562978816-fi4Q&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

If GPT-5.5 feels dumber than GPT-4o, the problem isn’t the model. It’s the 400-word prompt you copy-pasted from a 2023 productivity newsletter. GPT-5.5 and Claude Opus 4.7 both shipped with official prompting guides this month. Different solutions, same finding: the verbose, step-by-step prompts that worked on GPT-4o and Claude 3 are now noise. OpenAI is blunt: legacy prompts often over-specify the process because earlier models needed more help staying on track, and with GPT-5.5 that can add noise, narrow the model’s search space, or lead to overly mechanical answers. Anthropic goes the other way: Claude Opus 4.7 interprets prompts more literally and explicitly than Claude Opus 4.6, particularly at lower effort levels. It will not silently generalize an instruction from one item to another, and it will not infer requests you didn’t make. Translation: GPT-5.5 wants you to back off. Opus 4.7 wants you to be precise. Both look dumber if you treat them like a 2023 model. Three things to change with your prompts: 1. Drop unnecessary “always,” “never,” and “must.” Keep them for real non-negotiables, e.g. security, output format. Convert the rest into decision rules: “Ask a clarifying question only when missing info would change the answer.” 2. Tell the model when to stop. New models reason longer than you’d expect. If you don’t define what “done” looks like, they’ll either quit early or chase evidence indefinitely. 3. Re-scope your Claude prompts. If you need Claude to apply an instruction broadly, state the scope explicitly since Opus 4.7 won’t quietly extend “handle item A” to a similar item B. Worth bookmarking: OpenAI’s GPT-5.5 Prompting Guide and Anthropic’s Opus 4.7 migration guide. Both free, both from the people who trained the models, and both contradict half the prompting advice still circulating on LinkedIn. The models got smarter. Your prompts didn’t.

[11 Tips to Spend Tokens Smarter on GPT-5.5 & Claude 4.7  aidisruption.ai](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Faidisruption%2Eai%2Fp%2F11-tips-to-spend-tokens-smarter-on&urlhash=1y4D&trk=public_post_feed-article-content) `` `` [2](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fcourtlinholt_11-tips-to-spend-tokens-smarter-on-gpt-55-activity-7456997168562978816-fi4Q&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fcourtlinholt_11-tips-to-spend-tokens-smarter-on-gpt-55-activity-7456997168562978816-fi4Q&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fcourtlinholt_11-tips-to-spend-tokens-smarter-on-gpt-55-activity-7456997168562978816-fi4Q&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fcourtlinholt_11-tips-to-spend-tokens-smarter-on-gpt-55-activity-7456997168562978816-fi4Q&trk=public_post_feed-cta-banner-cta) 

`` 
- <https://www.linkedin.com/posts/timoselvaraj_searchblox-searchai-mercury-diffusion-llms-activity-7462217810778329088-9xb9> <https://www.linkedin.com/in/timoselvaraj?trk=public_post_feed-actor-image> [Timo Selvaraj](https://www.linkedin.com/in/timoselvaraj?trk=public_post_feed-actor-name)  2mo 

- [Report this post](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftimoselvaraj_searchblox-searchai-mercury-diffusion-llms-activity-7462217810778329088-9xb9&trk=public_post_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=POST&_f=guest-reporting) 

Why "Diffusion" Changes Everything. Old Way: One Word at a Time (Autoregressive) Traditional models (like GPT-4) act like a slow typist. They guess the next word, then the next, in a straight line. This is called "Auto-regressive," and it creates a speed limit you can't break. New Way: The Whole Idea at Once (Diffusion) Diffusion LLMs (dLLMs) are a new class of large language models that produce text through a denoising-based, parallel generation process. Unlike transformer models that generate one token at a time, dLLMs refine entire sequences simultaneously, enabling dramatically faster inference, smoother scaling, and lower computational cost — ideal for enterprise [#GenAI](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fgenai&trk=public_post-text) [#workloads](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fworkloads&trk=public_post-text). The Result: Answers appear instantly, not word-by-word [Inception](https://www.linkedin.com/company/inception-labs-ai?trk=public_post-text) [#LLM](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fllm&trk=public_post-text) [#Diffusion](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fdiffusion&trk=public_post-text) [#AgenticAI](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fagenticai&trk=public_post-text) [https://lnkd.in/eUm4cZrW](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FeUm4cZrW&urlhash=-79T&trk=public_post-text)

[SearchBlox SearchAI + Mercury Diffusion LLMs | SearchBlox | The Search & RAG Platform  searchblox.com](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fwww%2Esearchblox%2Ecom%2Fpartners%2Fsearchai-and-inception-mercury-diffusion-models&urlhash=MnvS&trk=public_post_feed-article-content) `` `` [5](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftimoselvaraj_searchblox-searchai-mercury-diffusion-llms-activity-7462217810778329088-9xb9&trk=public_post_social-actions-reactions) `` `` `` `` `` `` `` [Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftimoselvaraj_searchblox-searchai-mercury-diffusion-llms-activity-7462217810778329088-9xb9&trk=public_post_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftimoselvaraj_searchblox-searchai-mercury-diffusion-llms-activity-7462217810778329088-9xb9&trk=public_post_comment-cta) `` ``  Share 

- Copy 
- LinkedIn 
- Facebook 
- X 

 To view or add a comment, [sign in](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftimoselvaraj_searchblox-searchai-mercury-diffusion-llms-activity-7462217810778329088-9xb9&trk=public_post_feed-cta-banner-cta) 

`` 
![](https://media.licdn.com/dms/image/v2/D4D16AQGz6F6slOZ5_Q/profile-displaybackgroundimage-shrink_200_800/B4DZ6JmloLGYAQ-/0/1780425055361?e=2147483647&v=beta&t=xArvn1KADmdNKXU3evNsetN9VmzYrs65yqaxOSwA3VU) 

 7,288 followers 

- [506 Posts](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fin%2Fkirill-balakhonov%2Frecent-activity%2F&trk=public_post_follow-posts) 
- [5 Articles](https://www.linkedin.com/today/author/kirill-balakhonov?trk=public_post_follow-articles) 
[View Profile](https://uk.linkedin.com/in/kirill-balakhonov?trk=public_post_follow-view-profile) [Connect](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2Fupdate%2Furn%3Ali%3Aactivity%3A7455363399325999104&trk=public_post_follow) 

##  More from this author 

- 

### 

[Audits are a snapshot. Security is a system. Let's build it together  Kirill A. B.  3mo](https://www.linkedin.com/pulse/audits-snapshot-security-system-lets-build-together-balakhonov-ngbae?trk=public_post) 
- 

### 

[Introducing ChaosChain by Nethermind – Where AI Takes Over the Chain  Kirill A. B.  1y](https://www.linkedin.com/pulse/introducing-chaoschain-nethermind-where-ai-takes-over-balakhonov-ymnmf?trk=public_post) 
- 

### 

[n9 (Nine): The First Distributed Agentic Framework by Nethermind  Kirill A. B.  1y](https://www.linkedin.com/pulse/n9-nine-first-distributed-agentic-framework-kirill-balakhonov-rvrbf?trk=public_post) 

##  Explore content categories 

- [Career](https://www.linkedin.com/top-content/career/) 
- [Productivity](https://www.linkedin.com/top-content/productivity/) 
- [Finance](https://www.linkedin.com/top-content/finance/) 
- [Soft Skills & Emotional Intelligence](https://www.linkedin.com/top-content/soft-skills-emotional-intelligence/) 
- [Project Management](https://www.linkedin.com/top-content/project-management/) 
- [Education](https://www.linkedin.com/top-content/education/) 
- [Technology](https://www.linkedin.com/top-content/technology/) 
- [Leadership](https://www.linkedin.com/top-content/leadership/) 
- [Ecommerce](https://www.linkedin.com/top-content/ecommerce/) 
- [User Experience](https://www.linkedin.com/top-content/user-experience/) 
 Show more  Show less 

##  Sign in to view more content 

Create your free account or sign in to continue your search 

`` `` `` `` `` `` `` `` `` `` Sign in with Email 

 or 

 New to LinkedIn? [Join now](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fposts%2Fkirill-balakhonov_gpt-55-likely-has-97-trillion-parameters-activity-7455363399325999104--aZQ&trk=public_post_contextual-sign-in-modal_join-link) 

 By clicking Continue to join or sign in, you agree to LinkedIn’s [User Agreement](/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement), [Privacy Policy](/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy), and [Cookie Policy](/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy). 

``
