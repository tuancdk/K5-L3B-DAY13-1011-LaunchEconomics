# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

Cả ba phép thử đều ĐẠT.

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 đ | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | token và tool của các lượt có `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 đ | token, tool, xem lại và làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 đ | tổng chi phí chia 978 việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ | tiền token và tool chia 1.200 yêu cầu | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,28 lần hoá đơn token và tool trên mỗi yêu cầu [simulated].
- Chi phí làm lại lớn nhất, chiếm 51,8% tổng chi phí [simulated].

Đối chiếu tiền token trên 1.624 lượt chạy, kể cả lượt lỗi: (5.771.712 × 26 + 734.774 × 130) ÷ 1.000 = 245.585,132 đ, khớp với 245.585 đ khi làm tròn.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại `quoc_te` có chi phí cao hơn mốc 12.000 đ, ở mức 1,88× [simulated]. Tỉ lệ `ok` giảm từ 30,0% ở lần đầu xuống 11,4% ở lần hai và 2,2% ở lần ba, nên lần thử thứ ba mang lại ít thêm kết quả thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Dùng tổng khối lượng yêu cầu làm cơ sở dự báo. Trong mẫu 1.200 yêu cầu, có 900 việc thành công thuộc hai loại trong phạm vi. Nhân khối lượng tháng với 900/1.200 để ước tính số việc thành công, rồi chia 40.000.000 đ/tháng cho số việc đó.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Ở cả hai mức khối lượng, chi phí mỗi việc thành công sau khi cộng phí cố định vẫn dưới 12.000 đ [simulated]. Khi khối lượng giảm một nửa, chi phí cố định mỗi việc tăng từ 1.185 đ lên 2.370 đ.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi so với A2 [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token, giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ, giá tool giữ nguyên | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt có `attempt > 2`, yêu cầu có `so_lan_chay > 2` được chuyển nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Áp dụng cùng cách tính với giới hạn 1 | 4.111 đ | −8,1% |

Đối chiếu trước khi làm tròn [simulated]. Mức giảm khi chia đôi bằng nửa mức tăng khi nhân đôi, lần lượt là 2,8076% so với 5,6152% cho token, 20,3494% so với 40,6989% cho xem lại và 25,8827% so với 51,7653% cho làm lại.

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng tăng gấp đôi đưa chi phí lên 6.543 đ/việc thành công (+46,3%) [simulated].
- Theo các kịch bản tăng trong B1, ba yếu tố ảnh hưởng mạnh nhất là làm lại (+51,8%), xem lại (+40,7%) và lương nhân viên (+23,1%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Mỗi yêu cầu không thành công được tính thêm 12.000 đ khi tính chi phí cả hệ thống.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn 2 lần có chi phí cả hệ thống thấp nhất (6.901.220 đ). Riêng chi phí trợ lý mỗi việc thành công thấp nhất ở giới hạn 1 lần (4.111 đ) [simulated].

## B4 · Nếu phải xem lại tất cả

- Với `noi_dia` và `hang_nang`, kịch bản xem lại 100% ca có lượt chạy `ok` tính 5 phút mỗi ca. Chi phí là 11.743 đ/việc thành công (0,98× mốc 12.000 đ) khi làm lại mất 9 phút/ca, và 12.415 đ (1,03×) khi mất 15,3 phút/ca [simulated].
- Pilot cần đo thời gian xem lại và làm lại. Mốc hòa vốn cho thời gian xem lại giảm từ 5,1 xuống 4,8 phút/ca khi thời gian làm lại tăng từ 9 lên 15,3 phút/ca [simulated].
