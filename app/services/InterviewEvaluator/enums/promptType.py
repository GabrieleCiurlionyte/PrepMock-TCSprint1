from enum import Enum

class PromptType(str, Enum):
    ZERO_SHOT = "zero_shot"
    FEW_SHOT_WITH_GENERIC_EXAMPLES = "few_shot_generic"
    FEW_SHOT_WITH_DIFFICULTY_EXAMPLES = "few_shot_difficulty_specific"
    CHAIN_OF_THOUGHT = "chain_of_thought"
    SIMPLE = "simple"
    