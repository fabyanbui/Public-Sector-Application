# Hướng dẫn chạy file và kiểm tra chính tả

| Tên file          | Nội dung                     | Người kiểm tra     |
|-------------------|------------------------------|---------------------|
| `first_link.csv`    | Nửa đầu bộ dữ liệu câu hỏi & câu trả lời      | Bùi Đình Bảo        |
| `second_link.csv`    | Nửa cuối bộ dữ liệu câu hỏi & câu trả lời | Nguyễn Tiến Nhật          |
| `first_tthc.csv`  | Nửa đầu bộ dữ liệu kiến thức liên quan (TTHC)        | Bùi Đình Bảo            |
| `second_tthc.csv`       | Nửa cuối bộ dữ liệu kiến thức liên quan (TTHC)       | Nguyễn Tiến Nhật          |

---
- Mở terminal với thư mục BH_Annotate
- Chạy `streamlit run app.py`
- Chọn tab tương ứng

## Chú ý:

- Tự thay đổi API trong `app.py` khi hết quota

- **Nhấn `Generate` nhiều lần để gen ra đầy đủ (đối với TTHC) vì có thể hết quota giữa chừng**

- **Warning sau có thể bỏ qua trong UI của streamlit** (có thể setting lại trong local config của streamlit lib)

> The widget with key `<something>` was created with a default value but also had its value set via the Session State API.