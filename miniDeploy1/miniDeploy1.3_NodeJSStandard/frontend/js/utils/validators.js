// Hàm để kiểm tra xem một chuỗi có rỗng hay không
export function isEmpty(str) {
    // Nếu chuỗi không tồn tại hoặc sau khi loại bỏ khoảng trắng mà độ dài bằng 0
    return (!str || str.trim().length === 0);
  }
  