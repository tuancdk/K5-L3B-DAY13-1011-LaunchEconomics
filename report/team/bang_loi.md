# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phùng Văn Thanh Cao · Người gắn nhãn 2: Lê Anh Tuấn (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Giới hạn hệ thống | Không | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Giới hạn hệ thống | Không | Do người dùng |
| 10 | Ngữ cảnh | Giới hạn hệ thống | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Ngầm | Không | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngầm | Không | Ngữ cảnh |
| 17 | Ngầm | Hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Do người dùng | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Ngầm | Hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** 10 / 20 = 50%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

**Định nghĩa đã viết lại** (đồng thuận 50%, dưới 80%). Xét theo thứ tự, dừng ở câu đầu tiên trả lời "có":

1. **Ngầm:** không khách nào báo, không cảnh báo nào kích hoạt, chỉ lộ ra khi kiểm tra mẫu. Có người phản ánh, mở lại hoặc nhìn thấy là lỗi đã lộ, không phải Ngầm.
2. **Do người dùng:** đầu vào hoặc thao tác của khách sai. Nếu đầu vào đúng thì trợ lý vẫn làm được. Trợ lý xử lý chưa khéo thì ghi ở cột khắc phục, không đổi nhãn.
3. **Giới hạn hệ thống:** đầu vào đúng nhưng trợ lý vẫn không làm được, vì thiếu dữ liệu, ngoài phạm vi hoặc dạng đầu vào không xử lý được.
4. **Hệ thống:** trợ lý làm trái thiết kế hoặc chính sách, và lỗi đã lộ ra.
5. **Ngữ cảnh:** trợ lý làm đúng thiết kế và chính sách, nhưng giả định không khớp với hoàn cảnh hay kỳ vọng của khách.

**Quy tắc cho từng ca không trùng:**

- Ca 1 · Do người dùng: khách nhập thiếu số tài khoản. Có số đúng thì trợ lý hoàn được, nên đây không phải giới hạn.
- Ca 3 · Ngữ cảnh: hoàn về ví đúng thiết kế, chỉ có kỳ vọng "tiền về ngân hàng" của khách là khác. Trợ lý không làm sai thiết kế nên không phải Hệ thống.
- Ca 9 · Do người dùng: gốc lỗi là khách nhập mã đơn của sàn thay vì mã vận đơn. Việc trợ lý không gợi ý là điểm cần cải thiện, không phải nhãn.
- Ca 10 · Ngữ cảnh: từ chối đúng điều khoản bất khả kháng, khách thấy vô lý vì app vẫn hiện "cam kết 24 giờ". Trợ lý vẫn làm được việc nên không phải Giới hạn.
- Ca 13 · Giới hạn hệ thống: yêu cầu ngoài phạm vi thì gắn Giới hạn, kể cả khi trợ lý báo giới hạn đó kém.
- Ca 14 · Do người dùng: khách bấm nhầm "đã nhận tiền". Khách sẽ tự phát hiện vì chưa nhận tiền, nên không phải Ngầm.
- Ca 16 · Ngữ cảnh: gửi lúc 2:14 sáng đúng thiết kế "gửi ngay". Khách đã phản ánh nên lỗi đã lộ, không phải Ngầm.
- Ca 17 · Ngầm: lệch bảng giá trên 212 đơn trong 9 ngày mà không ai mở lại hay nhận ra. Sai chính sách nhưng chưa lộ, nên không phải Hệ thống.
- Ca 18 · Ngữ cảnh: số tiền đúng chính sách, khách hiểu sai vì tin nhắn thiếu cách tính. Khách không nhập sai nên không phải Do người dùng.
- Ca 20 · Hệ thống: hoàn hai lần do thiếu khoá chống trùng là vi phạm thiết kế, sổ cái ghi hai lệnh nên lỗi đã lộ, không phải Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (reason = ma_khong_hop_le, trace_id); đếm hằng ngày, cảnh báo khi > 2% số yêu cầu trong ngày | Nhận diện mã đơn sàn TMĐT và tra sang mã vận đơn; không tra được thì hỏi lại khách kèm ảnh hướng dẫn chỗ lấy mã | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: hai bản ghi `refund_ledger_write` cùng request_id (trace_id); ngưỡng 0 ca, có 1 ca là cảnh báo ngay | Thêm khoá chống trùng (idempotency_key theo request_id) trước khi ghi sổ; yêu cầu gửi lại thì trả trạng thái của lệnh đầu | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` (reason = so_tien, trace_id) mà kiểm tra lại thấy số tiền đúng, theo tuần; ngưỡng > 1% số yêu cầu đã đóng | Mẫu tin nhắn luôn ghi cách tính (30.000 đ × 50% = 15.000 đ) và điều khoản áp dụng | Trưởng nhóm CSKH |
| 13 | Giới hạn hệ thống | Event `handoff_to_staff` (reason = ngoai_pham_vi, trace_id) theo chủ đề, mỗi tuần; lấy mẫu 50 hội thoại/tuần đếm ca ngoài phạm vi mà trợ lý không chuyển, ngưỡng 0 ca | Nhận diện yêu cầu bảo hiểm hàng hoá, nói rõ trợ lý không xử lý được, chuyển đầu mối đối tác kèm tóm tắt | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`, trace_id) so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace; liên hệ khách của 212 đơn bị ảnh hưởng | Kế toán trưởng |
