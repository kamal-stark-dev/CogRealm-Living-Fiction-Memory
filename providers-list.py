# import cognee.infrastructure.llm.config as config
#
# print(dir(config))

# from cognee.infrastructure.llm.config import LLMConfig
#
# print(LLMConfig.model_json_schema())

from cognee.infrastructure.llm.config import get_llm_config

config = get_llm_config()

print(config)
