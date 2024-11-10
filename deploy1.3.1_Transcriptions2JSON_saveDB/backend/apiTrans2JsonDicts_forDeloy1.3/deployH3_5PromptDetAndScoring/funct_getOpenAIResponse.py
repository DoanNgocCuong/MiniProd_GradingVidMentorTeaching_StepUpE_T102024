import requests
import logging
from typing import Optional
import json



def get_openai_response(
    system_prompt: str, 
    user_input_prompt: str, 
    api_key: str,
    model: str = 'gpt-4o-mini', 
    max_tokens: int = 2048,        # Thêm max_tokens
    temperature: float = 0       # Thêm temperature để control randomness
) -> str:
    """
    Hàm để gửi yêu cầu tới OpenAI API và trả về phản hồi.

    Args:
        system_prompt (str): Nội dung system prompt
        user_input_prompt (str): Nội dung user input prompt
        api_key (str): API key của bạn
        model (str, optional): Model GPT để sử dụng. Defaults to 'gpt-4o-mini'

    Returns:
        str: Phản hồi từ mô hình OpenAI

    Raises:
        ValueError: Khi system prompt hoặc user input prompt rỗng
        Exception: Khi có lỗi trong quá trình gọi API
    """
    # Kiểm tra input
    if not system_prompt or not user_input_prompt:
        raise ValueError('System prompt và user input prompt không được rỗng.')

    url = 'https://api.openai.com/v1/chat/completions'

    # Chuẩn bị payload
    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input_prompt}
        ], 
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {
            "type": "json_object"
        }
    }

    # Chuẩn bị headers
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        # Gửi request
        response = requests.post(
            url=url,
            headers=headers,
            json=payload  # requests sẽ tự động chuyển dict thành JSON
        )

        # Kiểm tra status code
        if response.status_code != 200:
            error_msg = f'Yêu cầu API thất bại với trạng thái {response.status_code}: {response.text}'
            logging.error(error_msg)
            raise Exception(error_msg)

        # Parse response
        result = response.json()['choices'][0]['message']['content']
        
        logging.info(f'Phản hồi từ OpenAI: {result}')
        return result

    except requests.exceptions.RequestException as e:
        error_msg = f'Lỗi kết nối trong quá trình gọi API: {str(e)}'
        logging.error(error_msg)
        raise

    except (KeyError, json.JSONDecodeError) as e:
        error_msg = f'Lỗi xử lý phản hồi từ API: {str(e)}'
        logging.error(error_msg)
        raise

    except Exception as e:
        error_msg = f'Lỗi không xác định trong quá trình gọi API: {str(e)}'
        logging.error(error_msg)
        raise

# Cấu hình logging cơ bản
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ví dụ sử dụng:
if __name__ == "__main__":
    try:
        response = get_openai_response(
            system_prompt="You are a helpful assistant.",
            user_input_prompt="What is the capital of France?",
            api_key="your-api-key-here"
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")