# Báo cáo cá nhân — VuQuangHuy-2A202603782

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Huy
- MSSV: 2A202603782
- Email: 26ai.huyvq6@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

- Phụ trách viết code CP1 (A1–A4) theo [issue #2](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/2). Minhduc7904 phụ trách kiểm số độc lập và điền bảng chi phí.

## 3. Đóng góp cụ thể

- **A1:** Cài đặt ba hàm tính số lần chạy kỳ vọng, xác suất thành công và hệ số chi phí mỗi việc thành công.
- **A2:** Viết mô hình tính tổng chi phí token, tool, xem lại và làm lại trên dữ liệu; tính riêng chi phí chạy lại đã nằm trong tổng.
- **A3:** In bảng theo bốn loại yêu cầu, gồm tỉ lệ thành công, số lần chạy trung bình, chi phí mỗi việc thành công và tỉ lệ `ok` theo từng lần thử.
- **A4:** Tính chi phí mỗi việc thành công sau khi phân bổ 40 triệu đồng chi phí cố định mỗi tháng cho phạm vi `noi_dia` và `hang_nang` ở hai mức khối lượng.

## 4. Bằng chứng

- Commit `4c884a3` trong [`src/lab13.py`](../../src/lab13.py).
- Kết quả chạy trên hai CSV của lab: ba phép thử A1 đều đạt (1,20 · 1,25 · 1,25). A2 ghi nhận 978 yêu cầu thành công, với chi phí 4.472 đ/việc thành công (simulated).
- A3 cho thấy yêu cầu quốc tế có tỉ lệ thành công 27,3% và chi phí 22.515 đ/việc thành công (simulated). A4 cho kết quả 4.599 đ/việc thành công ở mức 45.000 yêu cầu/tháng và 5.784 đ ở mức 22.500 yêu cầu/tháng (simulated).

## 5. Công cụ AI đã dùng

- Dùng Codex để triển khai và chạy thử phần code A1–A4. Kiểm tra bằng ba phép thử có sẵn và đối chiếu kết quả tính từ hai CSV với [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## 6. Tự đánh giá

- Mô hình tính chi phí từ mọi lần chạy, kể cả lần lỗi, rồi chia cho số yêu cầu thành công. Khi so với nhân viên tự xử lý, mô hình cộng chi phí xử lý thủ công cho các ca chưa thành công và tính theo mỗi yêu cầu.
