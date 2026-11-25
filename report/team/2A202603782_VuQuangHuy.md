# Báo cáo cá nhân — VuQuangHuy-2A202603782

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Huy
- MSSV: 2A202603782
- Email: 26ai.huyvq6@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code ở CP1–CP2, người kiểm số ở CP4

## 2. Phần việc phụ trách

- Phụ trách viết code CP1 (A1–A4) theo [issue #2](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/2). Minhduc7904 phụ trách kiểm số độc lập và điền bảng chi phí.
- Phụ trách viết code phân tích độ nhạy CP2 (B1–B4). Minhduc7904 phụ trách kiểm số độc lập và ghi kết quả vào bảng chi phí. [Issue #3](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/3)

- Kiểm số CP4 sau khi đổi vai với Minhduc7904. Tính tay D1(e), đối chiếu với script và hoàn thiện kế hoạch pilot. [Issue #5](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/5)

## 3. Đóng góp cụ thể

- **A1:** Cài đặt ba hàm tính số lần chạy kỳ vọng, xác suất thành công và hệ số chi phí mỗi việc thành công.
- **A2:** Viết mô hình tính tổng chi phí token, tool, xem lại và làm lại trên dữ liệu; tính riêng chi phí chạy lại đã nằm trong tổng.
- **A3:** In bảng theo bốn loại yêu cầu, gồm tỉ lệ thành công, số lần chạy trung bình, chi phí mỗi việc thành công và tỉ lệ `ok` theo từng lần thử.
- **A4:** Tính chi phí mỗi việc thành công sau khi phân bổ 40 triệu đồng chi phí cố định mỗi tháng cho phạm vi `noi_dia` và `hang_nang` ở hai mức khối lượng.
- **B1–B2:** Dùng lại `mo_hinh` để chạy chín kịch bản đổi từng yếu tố, tính tác động khi giá token và chi phí xem lại cùng tăng gấp đôi, rồi xếp hạng ba yếu tố ảnh hưởng lớn nhất.
- **B3–B4:** So sánh giới hạn 1–3 lần chạy, cộng chi phí nhân viên xử lý các ca chưa thành công, rồi tính chi phí và thời gian xem lại hòa vốn khi xem lại 100% trong phạm vi `noi_dia` và `hang_nang`.

- **D1–D3:** Ghi kết quả cỡ mẫu, năm câu kiểm tra khả năng tách tác động và tỉ lệ mở lại trong 7 ngày vào kế hoạch. Chọn chia ngẫu nhiên theo nhân viên với 20 người mỗi nhóm và viết bốn luật dừng bao quát an toàn, chi phí và mức sử dụng.

## 4. Bằng chứng

- Commit `4c884a3` trong [`src/lab13.py`](../../src/lab13.py).
- Kết quả chạy trên hai CSV của lab: ba phép thử A1 đều đạt (1,20 · 1,25 · 1,25). A2 ghi nhận 978 yêu cầu thành công, với chi phí 4.472 đ/việc thành công (simulated).
- A3 cho thấy yêu cầu quốc tế có tỉ lệ thành công 27,3% và chi phí 22.515 đ/việc thành công (simulated). A4 cho kết quả 4.599 đ/việc thành công ở mức 45.000 yêu cầu/tháng và 5.784 đ ở mức 22.500 yêu cầu/tháng (simulated).
- Commit CP2 `f8aa454` trong [`src/lab13.py`](../../src/lab13.py). Ba tác động lớn nhất đến chi phí mỗi việc thành công là làm lại gấp đôi (+51,8%), xem lại gấp đôi (+40,7%) và lương tăng 25% (+23,1%), đều là kết quả simulated.
- Giới hạn hai lần chạy cho chi phí cả hệ thống thấp nhất, 6.901.220 đ (simulated). Khi xem lại 100%, chi phí là 11.743 đ hoặc 12.415 đ/việc thành công với thời gian làm lại tương ứng 9 hoặc 15,3 phút/ca (simulated).

- Commit CP4 `f9d8207` trong [pilot_plan.yaml](pilot_plan.yaml). Tính tay D1(e): 20m ≥ 859 × (0,98 + 0,02m) ⇒ 2,82m ≥ 841,82 ⇒ m ≥ 298,52. Làm tròn lên 299 yêu cầu mỗi nhân viên, khớp với script của Minhduc7904 và cho 859,20 mẫu hiệu dụng mỗi nhóm (simulated).

## 5. Công cụ AI đã dùng

- Dùng Codex để triển khai và chạy thử phần code A1–A4. Kiểm tra bằng ba phép thử có sẵn và đối chiếu kết quả tính từ hai CSV với [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- Dùng Codex để triển khai và kiểm tra B1–B4 theo [CHECKPOINTS.md](../../CHECKPOINTS.md). Trước khi làm tròn, mức giảm khi chia đôi bằng một nửa mức tăng khi nhân đôi cho cả ba yếu tố token, xem lại và làm lại. Tác động của kịch bản kết hợp bằng tổng hai tác động riêng.

- Dùng Codex để hoàn thiện YAML và kiểm tra bằng `yaml.safe_load`. Đã đối chiếu kết quả D1(e) tính tay với đầu ra của script, kiểm tra hết dấu hỏi và xác nhận cả bốn luật dừng có đủ bốn vế.

## 6. Tự đánh giá

- Mô hình tính chi phí từ mọi lần chạy, kể cả lần lỗi, rồi chia cho số yêu cầu thành công. Khi so với nhân viên tự xử lý, mô hình cộng chi phí xử lý thủ công cho các ca chưa thành công và tính theo mỗi yêu cầu.
- Giới hạn một lần chạy cho chi phí trợ lý trên mỗi việc thành công thấp nhất, còn giới hạn hai lần cho tổng chi phí thấp nhất sau khi cộng phần nhân viên xử lý thay. Khi xem lại toàn bộ, thời gian làm lại có thể đẩy chi phí qua mốc 12.000 đ/việc thành công (simulated).
- Chia theo nhân viên giúp giảm tràn tác động giữa hai nhóm. Với cỡ mẫu đã chọn, pilot nhắm mức chênh 6 điểm phần trăm và chỉ có khoảng 64,2% power nếu mức chênh thực là 5 điểm (simulated).
