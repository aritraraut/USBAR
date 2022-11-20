# USBAR
. Abstract :::

Purpose ->
Existing task-oriented virtual agents can assist users with simple tasks like ticket
booking, hotel reservations, etc., effectively and with high confidence. These virtual
assistants, however, assume specific, predictable end-user behavior, such as
predefined/servable objectives, which results in conversation failures in challenging
situations, such as when goals are unavailable.

Methodology ->
Inspired by the practice and its efficacy, we propose an end-to-end framework for
task-oriented persuasive dialogue generation that combines pre-training and
reinforcement learning for generating context-aware persuasive responses. We utilize
four novel rewards to improve consistency and repetitiveness in generated responses.
Additionally, a meta-learning strategy has also been utilized to make the model
parameters better for domain adaptation. Furthermore, we also curate a personalized
persuasive dialogue (PPD) corpus, which contains utterance-level intent, slot, sentiment,
and persuasion strategy annotation.

Findings ->
The obtained results and detailed analysis firmly establish the effectiveness of the
proposed persuasive virtual assistant over traditional task-oriented virtual assistants.
The proposed framework considerably increases the quality of dialogue generation in
terms of consistency and repetitiveness. Additionally, our experiment with a few shot
and zero-shot settings proves that our meta-learned model learns to quickly adopt new
domains with a few or even zero no. of training epochs. It outperforms the
non-meta-learning-based approaches keeping the base model constant.

Originality ->
To the best of our knowledge, this is the first effort to improve a task-oriented virtual
agent’s persuasiveness and domain adaptation.
