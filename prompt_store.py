CLASSIFIER_PROMPT = """
Placeholder
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

    prompt_text = prompt_mapping.get(prompt_name, f"Missing Prompt: {prompt_name}")
    return prompt_text