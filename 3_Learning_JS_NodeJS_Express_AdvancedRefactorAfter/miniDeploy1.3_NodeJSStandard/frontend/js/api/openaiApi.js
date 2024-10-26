// Hàm để gửi yêu cầu đến backend và nhận phản hồi
export async function processPrompt(systemPrompt, userInputPrompt) {
    // Gửi yêu cầu fetch tới endpoint '/api/process-prompt' với phương thức POST
    const response = await fetch('/api/process-prompt', {
      method: 'POST',
      headers: {
        // Đặt loại nội dung là JSON
        'Content-Type': 'application/json'
      },
      // Chuyển đổi dữ liệu thành chuỗi JSON để gửi đi
      body: JSON.stringify({ systemPrompt, userInputPrompt })
    });
  
    // Nếu phản hồi không thành công (mã trạng thái không từ 200-299)
    if (!response.ok) {
      // Lấy dữ liệu lỗi từ phản hồi
      const errorData = await response.json();
      // Ném ra một lỗi mới với thông báo từ errorData
      throw new Error(errorData.error || 'Lỗi trong quá trình gọi API');
    }
  
    // Chuyển đổi phản hồi thành đối tượng JavaScript
    const data = await response.json();
    // Trả về phản hồi từ OpenAI
    return data.response;
  }
  