# Application
1.  `python -m uvicorn main:app --reload --port 8001 --app-dir backend`


# How to run the model

1. **-- 8-bit quantization**

``` bash
python -m vllm.entrypoints.openai.api_server \
    --model neuralmagic/DeepSeek-R1-Distill-Qwen-7B-quantized.w8a8 \
    --host 0.0.0.0 \
    --port 8000 \
    --trust-remote-code \
    --gpu-memory-utilization 0.90 \
    --max-model-len 32768


# sample request
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "neuralmagic/DeepSeek-R1-Distill-Qwen-7B-quantized.w8a8",
    "messages": [
      {
        "role": "user",
        "content": "What is the capital of France?"
      }
    ],
    "temperature": 0.7,
    "max_tokens": 512
  }'


```




