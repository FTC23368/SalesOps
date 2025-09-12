CLASSIFIER_PROMPT = """
You are a message classifier. Your job is to classify user messages into exactly one category.

Analyze the user's message and return ONLY the category name. Do not provide explanations or additional text.

Categories:
- **smalltalk**: Greetings, general conversation, casual comments
- **clarify**: Unclear requests that need more information  
- **policy**: Questions related to policy
- **quota**: Questions related to quota setting
- **segmentation**: Questions related to customer segments
- **stardt**: Questions related to territory setting

Examples:
- "Hi there" → smalltalk
- "How are you?" → smalltalk  
- "I need help" → clarify

Return only one word: smalltalk, clarify, policy, quota, segmentation, stardt.
"""

SMALLTALK_PROMPT = """
Placeholder
"""

CLARIFY_PROMPT = """
Placeholder
"""

POLICY_PROMPT = """
Placeholder
"""

QUOTA_PROMPT = """
Placeholder
"""

SEGMENTATION_PROMPT = """
Placeholder
"""

STARDT_PROMPT = """
Placeholder
"""

def get_prompt(prompt_name):
    prompt_mapping = {
        "classifier": CLASSIFIER_PROMPT,
        "smalltalk": SMALLTALK_PROMPT,
        "clarify": CLARIFY_PROMPT,
        "policy": POLICY_PROMPT,
        "quota": QUOTA_PROMPT,
        "segmentation": SEGMENTATION_PROMPT,
        "stardt": STARDT_PROMPT,
    }

    prompt_text = prompt_mapping.get(prompt_name, f"Missing prompt: {prompt_name}")
    return prompt_text