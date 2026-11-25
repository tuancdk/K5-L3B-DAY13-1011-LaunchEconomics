# Báo cáo cá nhân — 2A202603751_NguyenMinhDuc

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Đức
- MSSV: 2A202603751
- Email: nmduc7904@gmail.com
- Vai trong nhóm: Kiểm số CP1–CP2, viết code CP4 sau khi đổi vai với Vũ Quang Huy.

## 2. Phần việc phụ trách

- CP1 và CP2: đối chiếu đầu ra của `src/lab13.py` và ghi kết quả A1–A4, B1–B4 vào bảng chi phí.
- CP4: triển khai phần tính cỡ mẫu D1 a–e và tỷ lệ mở lại trong 7 ngày cho toàn mẫu và phạm vi pilot.

## 3. Đóng góp cụ thể

- CP1: cộng token từ 1.624 lượt chạy, kể cả lượt lỗi. Kết quả 245.585,132 đ khớp dòng chi phí token sau khi làm tròn.
- CP2: đối chiếu ba cặp kịch bản nhân đôi và chia đôi trước khi làm tròn. Ghi lại giới hạn chạy rẻ nhất cho hệ thống và kết quả độ nhạy khi xem lại toàn bộ ca có lượt chạy thành công.
- CP4: thêm công thức xác định ngưỡng 299 yêu cầu mỗi nhân viên để đạt 859 mẫu hiệu dụng mỗi nhóm. Tính tỷ lệ mở lại từ dữ liệu lab, lần lượt là 4,25% và 3,97% [simulated].

## 4. Bằng chứng

- [PR #12](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/pull/12) gồm bảng CP1 và phép tính đối chiếu tiền token.
- [Bảng chi phí B1–B4](bang_chi_phi.md#b1--đổi-từng-yếu-tố) ghi kết quả CP2 theo [issue #3](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/3).
- [PR #13](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/pull/13) gồm code tính cỡ mẫu và tỷ lệ mở lại cho CP4.

## 5. Công cụ AI đã dùng

- Dùng Codex để hỗ trợ viết code D1, chạy chương trình và điền bảng từ kết quả chạy.
- Cách kiểm tra kết quả: tính lại tiền token trực tiếp từ CSV, so sánh thay đổi CP2 trước khi làm tròn và thay 298, 299 vào công thức cỡ mẫu hiệu dụng để kiểm tra ngưỡng D1e.

## 6. Tự đánh giá

- CP2 cho thấy giới hạn chạy phải được đánh giá trên chi phí toàn hệ thống vì các yêu cầu chuyển nhân viên vẫn phát sinh chi phí.
- Với CP4, việc chia theo cụm làm giảm cỡ mẫu hiệu dụng. Phương án 20 người mỗi nhóm chỉ đạt mục tiêu của bài khi chấp nhận chênh lệch 6 điểm phần trăm và đủ khối lượng trên mỗi người.
