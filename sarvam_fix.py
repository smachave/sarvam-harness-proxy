# sarvam-harness-proxy.py
import logging
from litellm.integrations.custom_logger import CustomLogger

logger = logging.getLogger("LiteLLM Proxy")

class StripPartsForSarvam(CustomLogger):
    async def async_pre_call_hook(self, *args, **kwargs):
        logger.info("--- [HOOK TRIGGERED] Intercepting Request Payload ---")
        
        data = kwargs.get("data")
        if data is None and len(args) > 2:
            data = args[2]
            
        if not data:
            logger.info("Hook warning: No request data block found.")
            return kwargs.get("data", {})

        if "messages" in data and isinstance(data["messages"], list):
            for msg in data["messages"]:
                content = msg.get("content")
                
                if isinstance(content, list):
                    logger.info(f"Detected list format in content: {content}")
                    text_parts = []
                    for part in content:
                        if isinstance(part, dict) and "text" in part:
                            text_parts.append(part["text"])
                        elif isinstance(part, str):
                            text_parts.append(part)
                    
                    flattened_str = "\n".join(text_parts)
                    msg["content"] = flattened_str
                    logger.info(f"Successfully flattened array to string: '{flattened_str}'")
                    
        return data

    async def async_post_call_success_hook(self, *args, **kwargs):
        pass

    async def async_post_call_failure_hook(self, *args, **kwargs):
        pass

proxy_handler_instance = StripPartsForSarvam()