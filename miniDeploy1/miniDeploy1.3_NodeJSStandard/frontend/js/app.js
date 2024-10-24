// Import hàm isEmpty từ validators.js
import { isEmpty } from './utils/validators.js';
// Import hàm processPrompt từ openaiApi.js
import { processPrompt } from './api/openaiApi.js';

// Thêm sự kiện click cho nút 'submitBtn'
document.getElementById('submitBtn').addEventListener('click', async () => {
  // Lấy giá trị từ ô nhập systemPrompt
  const systemPrompt = document.getElementById('systemPrompt').value;
  // Lấy giá trị từ ô nhập userInputPrompt
  const userInputPrompt = document.getElementById('userInputPrompt').value;

  // Kiểm tra nếu bất kỳ ô nhập nào bị trống
  if (isEmpty(systemPrompt) || isEmpty(userInputPrompt)) {
    // Hiển thị thông báo lỗi
    alert('System prompt và user input prompt không được để trống.');
    return;
  }

  // Hiển thị thông báo đang xử lý
  document.getElementById('response').innerHTML = 'Đang xử lý...';

  try {
    // Gọi hàm processPrompt để gửi yêu cầu đến backend
    const response = await processPrompt(systemPrompt, userInputPrompt);
    // Hiển thị phản hồi từ OpenAI
    document.getElementById('response').innerText = response;
  } catch (error) {
    // Nếu có lỗi, hiển thị thông báo lỗi
    document.getElementById('response').innerText = 'Đã xảy ra lỗi: ' + error.message;
  }
});
