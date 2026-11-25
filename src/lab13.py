"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí theo yêu cầu và chi phí mỗi việc thành công.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - chay_lai: phần token và tool của các lần thử sau lần đầu, đã nằm trong tổng.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs['ket_qua'].eq('thanh_cong').sum()
    return {
        'token': token,
        'tool': tool,
        'chay_lai': (tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.inf,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


def in_ket_qua_cp1(runs, reqs):
    """In bảng A2–A4 để đối chiếu với báo cáo chi phí."""
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí từ trace (đồng, trừ số việc thành công)')
    for ten, gia_tri in ket_qua.items():
        nhan = ' [simulated]' if ten in ('xem_lai', 'lam_lai', 'tong', 'cps') else ''
        so_le = 1 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:16s} {gia_tri:>14,.{so_le}f}{nhan}')
    print(f"CPS / hóa đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f}× [simulated]")
    ca_khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong = (ket_qua['tong'] + ca_khong_thanh_cong * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống: {chi_phi_he_thong:,.0f} đ/yêu cầu '
          f'({chi_phi_he_thong / BASELINE:.2f}× chi phí tự làm) [simulated]')

    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f'{"Loại":12s} {"Số YC":>6s} {"Thành công":>12s} {"Lần/YC":>8s} '
          f'{"CPS [simulated]":>17s} {"CPS/12.000 [simulated]":>23s}')
    for loai, nhom in reqs.groupby('loai', sort=False):
        ket_qua_nhom = mo_hinh(runs, nhom)
        cps = ket_qua_nhom['cps']
        print(f'{loai:12s} {len(nhom):6d} {ket_qua_nhom["thanh_cong"] / len(nhom):12.1%} '
              f'{nhom["so_lan_chay"].mean():8.2f} {cps:17,.0f} {cps / BASELINE:22.2f}×')

    runs_theo_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ti_le_ok = runs_theo_loai.assign(ok=runs_theo_loai['status'].eq('ok')).pivot_table(
        index='loai', columns='attempt', values='ok'
    )
    print('\nTỉ lệ ok theo lần thử')
    print(ti_le_ok.to_string(float_format=lambda ti_le: f'{ti_le:.1%}'))

    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua_pham_vi = mo_hinh(runs, pham_vi)
    ti_le_thanh_cong_trong_mau = ket_qua_pham_vi['thanh_cong'] / len(reqs)
    for khoi_luong in (45_000, 22_500):
        so_viec_thanh_cong = khoi_luong * ti_le_thanh_cong_trong_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / so_viec_thanh_cong
        cps = ket_qua_pham_vi['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} yêu cầu/tháng → {so_viec_thanh_cong:,.0f} việc thành công/tháng, '
              f'cố định {co_dinh_moi_viec:,.0f} đ/việc, '
              f'CPS {cps:,.0f} đ ({cps / BASELINE:.2f}×) [simulated]')


def in_ket_qua_cp2(runs, reqs):
    """In bảng độ nhạy B1–B4 từ cùng mô hình chi phí A2."""
    cps_goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print('\nB1 · Đổi từng yếu tố [simulated]')
    print(f'{"Gốc (A2)":26s} {cps_goc:>8,.0f} đ')
    thay_doi = {}
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi[ten] = cps / cps_goc - 1
        print(f'{ten:26s} {cps:>8,.0f} đ {thay_doi[ten]:+7.1%}')

    print('\nB2 · Đổi một cặp và xếp hạng [simulated]')
    cps_cap = mo_hinh(runs, reqs, **kich_ban['Giá token gấp đôi'],
                     **kich_ban['Xem lại gấp đôi'])['cps']
    print(f'Token và xem lại cùng gấp đôi: {cps_cap:,.0f} đ ({cps_cap / cps_goc - 1:+.1%})')
    tac_dong = {ten: muc for ten, muc in thay_doi.items() if muc > 0}
    hang = sorted(tac_dong, key=tac_dong.get, reverse=True)
    print('Ba tác động lớn nhất: ' + ' · '.join(f'{ten} ({tac_dong[ten]:+.1%})' for ten in hang[:3]))

    print('\nB3 · Giới hạn chạy lại [chi phí simulated]')
    print(f'{"Giới hạn":>9s} {"Tổng trợ lý":>14s} {"Không thành công":>18s} '
          f'{"Cả hệ thống":>14s} {"CPS":>8s}')
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        tong_he_thong = ket_qua['tong'] + khong_thanh_cong * BASELINE
        print(f'{gioi_han:9d} {ket_qua["tong"]:14,.0f} {khong_thanh_cong:18d} '
              f'{tong_he_thong:14,.0f} {ket_qua["cps"]:8,.0f}')

    print('\nB4 · Xem lại 100% trong phạm vi noi_dia + hang_nang [simulated]')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    yeu_cau_ok = runs.loc[runs['status'].eq('ok'), 'request_id']
    can_xem_lai = pham_vi['request_id'].isin(yeu_cau_ok)
    can_lam_lai = pham_vi['ket_qua'].eq('lam_lai')
    pham_vi['phut_xem_lai_simulated'] = can_xem_lai.astype(int) * 5
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    print(f'{len(pham_vi)} yêu cầu, {can_xem_lai.sum()} ca xem lại, {can_lam_lai.sum()} ca làm lại')
    for phut_lam_lai in (9, round(phut_lam_lai_tb, 1)):
        pham_vi['phut_lam_lai_simulated'] = can_lam_lai.astype(int) * phut_lam_lai
        ket_qua = mo_hinh(runs, pham_vi)
        ngan_sach_xem_lai = BASELINE * ket_qua['thanh_cong'] - (ket_qua['tong'] - ket_qua['xem_lai'])
        phut_hoa_von = ngan_sach_xem_lai / (can_xem_lai.sum() * LUONG_PHUT)
        print(f'{phut_lam_lai:g} phút làm lại/ca → CPS {ket_qua["cps"]:,.0f} đ '
              f'({ket_qua["cps"] / BASELINE:.2f}×), hòa vốn ở {phut_hoa_von:.1f} phút xem lại/ca')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_ket_qua_cp1(runs, reqs)
    in_ket_qua_cp2(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
