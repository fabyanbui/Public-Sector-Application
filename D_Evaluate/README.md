# Thứ tự chạy file và tổ chức thư mục

> Cài đặt LM Studio: https://lmstudio.ai/

- Open source models sử dụng LM Studio
- Close source models sử dụng OpenRouter API

## Pre-planning: Open-source model (7b)

| Model   | URL                                                                             | Params | Name                                   | Note                          |
|---------|-----------------------------------------------------------------------------------------------|------|----------------------------------------------|---------------------------------|
| Llama   | [Link](https://huggingface.co/christopherBR/Llama-3-7B-Q4_K_M)                                | 7B   | Llama-3-7B-Q4_K_M                             | Fine                            |
| Gemma   | [Link](https://huggingface.co/MaziyarPanahi/gemma-7b-GGUF)                                    | 7B   | gemma-7b-GGUF                                 | Not Fine                        |
| Mistral | [Link](https://huggingface.co/lmstudio-community/Mistral-7B-Instruct-v0.3-GGUF)               | 7B   | Mistral-7B-Instruct-v0.3-GGUF                 | Fine, but without system prompt |
| Qwen    | [Link](https://huggingface.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF)                 | 7B   | Qwen2.5-7B-Instruct-1M-GGUF                   | Fine                            |
| Falcon  | [Link](https://huggingface.co/tiiuae/falcon-mamba-7b-instruct-Q4_K_M-GGUF)                    | 7B   | falcon-mamba-7b-instruct-Q4_K_M-GGUF          | Not Fine                        |
| Vicuna  | [Link](https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF)                                   | 7B   | vicuna-7B-v1.5-GGUF                           | Fine, but full "Yes"           |

## Vietnamese support models recommendation

- https://huggingface.co/TheBloke/Llama-2-7B-vietnamese-20k-GGUF
- https://huggingface.co/nguyenviet/PhoGPT-7B5-Instruct-GGUF
- https://huggingface.co/RichardErkhov/vilm_-_vietcuna-7b-v3-gguf
- https://huggingface.co/ndthai/ToRoLaMa-7B-GGUF
- https://huggingface.co/mav23/Arcee-VyLinh-GGUF
- https://huggingface.co/uonlp/Vistral-7B-Chat-gguf
- https://huggingface.co/RichardErkhov/phongtintruong_-_Mistrava-7B-Instruct-v0.32-3000-gguf
- https://huggingface.co/Bachhoang/vbd-llama2-7B-standard-train-chat-GGUF
- https://huggingface.co/parinzee/SeaLLM-7B-Chat-GGUF