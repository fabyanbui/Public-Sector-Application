# Thứ tự chạy file và tổ chức thư mục

> Cài đặt LM Studio: https://lmstudio.ai/

- Open source models sử dụng LM Studio
- Close source models sử dụng OpenRouter API

## Open-source model selection:
- `llama-3-7b`: https://huggingface.co/christopherBR/Llama-3-7B-Q4_K_M => Llama 3 
- `mistral-7b-instruct-v0.3`: https://huggingface.co/lmstudio-community/Mistral-7B-Instruct-v0.3-GGUF => Mistral instruct v0.3
- `qwen2.5-7b-instruct-1m`: https://huggingface.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF => Qwen 2.5 Instruct 1M
- `vicuna-7b-v1.5`: https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF => Vicuna v1.5
- `c4ai-command-r7b-12-2024-abliterated`: https://huggingface.co/bartowski/c4ai-command-r7b-12-2024-abliterated-GGUF => Command R7B abliterated 

### Vietnamese support model selection:
- `vistral-7b-chat`: https://huggingface.co/uonlp/Vistral-7B-Chat-gguf => Vistral Chat 
- `qwen2.5-7b-instruct-viet-sft`: https://huggingface.co/mradermacher/Qwen2.5-7B-Instruct-Viet-SFT-GGUF => Qwen 2.5 Vietnamese Supervised Fine-tuning 

## Pre-planning: Open-source model (7b)

| URL | Mục đích | Tác giả | Tên model | Tham số | Trạng thái | Lựa chọn |
|-----|----------|---------|-----------|---------|------------|--------|
| [Link](https://huggingface.co/christopherBR/Llama-3-7B-Q4_K_M) | General | christopherBR | Llama-3-7B-Q4_K_M | 7B | Fine | ✅ |
| [Link](https://huggingface.co/MaziyarPanahi/gemma-7b-GGUF) | General | MaziyarPanahi | gemma-7b-GGUF | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/lmstudio-community/Mistral-7B-Instruct-v0.3-GGUF) | General | lmstudio-community | Mistral-7B-Instruct-v0.3-GGUF | 7B | Fine (no system prompt) | ✅ |
| [Link](https://huggingface.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF) | General | lmstudio-community | Qwen2.5-7B-Instruct-1M-GGUF | 7B | Fine | ✅ |
| [Link](https://huggingface.co/tiiuae/falcon-mamba-7b-instruct-Q4_K_M-GGUF) | General | tiiuae | falcon-mamba-7b-instruct-Q4_K_M-GGUF | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF) | General | TheBloke | vicuna-7B-v1.5-GGUF | 7B | Fine (full "Yes") | ✅ |
| [Link](https://huggingface.co/bartowski/c4ai-command-r7b-12-2024-abliterated-GGUF) | General | bartowski | c4ai-command-r7b-12-2024-abliterated-GGUF | 7B | Fine | ✅ |
| [Link](https://huggingface.co/lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF) | General | lmstudio-community | DeepSeek-R1-Distill-Qwen-7B-GGUF | 7B | Reasoning model | ❌ |
| [Link](https://huggingface.co/TheBloke/Llama-2-7B-vietnamese-20k-GGUF) | Vietnamese | TheBloke | Llama-2-7B-vietnamese-20k-GGUF | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/ndthai/ToRoLaMa-7B-GGUF) | Vietnamese | ndthai | ToRoLaMa-7B-GGUF | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/RichardErkhov/vilm_-_vietcuna-7b-v3-gguf) | Vietnamese | RichardErkhov | vilm_-_vietcuna-7b-v3-gguf | 7B | Unable to load | ❌ |
| [Link](https://huggingface.co/uonlp/Vistral-7B-Chat-gguf) | Vietnamese | uonlp | Vistral-7B-Chat-gguf | 7B | Fine | ✅ |
| [Link](https://huggingface.co/RichardErkhov/phongtintruong_-_Mistrava-7B-Instruct-v0.32-3000-gguf) | Vietnamese | RichardErkhov | phongtintruong_-_Mistrava-7B-Instruct-v0.32-3000-gguf | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/nguyenviet/PhoGPT-7B5-Instruct-GGUF) | Vietnamese | nguyenviet | PhoGPT-7B5-Instruct-GGUF | 7.5B | Not Fine | ❌ |
| [Link](https://huggingface.co/tensorblock/SeaLLMs-v3-7B-GGUF) | Vietnamese | tensorblock | SeaLLMs-v3-7B-GGUF | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/chillies/vinallama-7b-legal-chat-final) | Vietnamese | chillies | vinallama-7b-legal-chat-final | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/mradermacher/Qwen2.5-7B-Instruct-Viet-SFT-GGUF) | Vietnamese | mradermacher | Qwen2.5-7B-Instruct-Viet-SFT-GGUF | 7B | Fine | ✅ |
| [Link](https://huggingface.co/tensorblock/vinallama-7b-GGUF) | Vietnamese | tensorblock | vinallama-7b-GGUF | 7B | Not Fine | ❌ |
| [Link](https://huggingface.co/thanhtan2136/GemSUra-7B-Q4_K_M-GGUF) | Vietnamese | thanhtan2136 | GemSUra-7B-Q4_K_M-GGUF | 7B | Not Fine | ❌ |


> Not suitable

- https://huggingface.co/Bachhoang/vbd-llama2-7B-standard-train-chat-GGUF
- https://huggingface.co/mav23/Arcee-VyLinh-GGUF
---
- claude2-alpaca-7b
- mistral-7b-v0.1
- japanese-stablelm-instruct-gamma-7b
