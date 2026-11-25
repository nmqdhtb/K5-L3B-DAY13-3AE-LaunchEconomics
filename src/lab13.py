"""Lab 13 · Chạy từ src/ bằng python lab13.py."""
import math
from statistics import NormalDist

import pandas as pd

GIA_VAO = 26
GIA_RA = 130
GIA_TOOL = 15
LUONG_PHUT = 2000
BASELINE = 12000


def so_lan_chay_ky_vong(p, k=None):
    if k is None:
        return 1 / p if p else math.inf
    return sum((1 - p) ** i for i in range(k))


def ti_le_thanh_cong(p, k=None):
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    values = (so_lan_chay_ky_vong(.8, 2), so_lan_chay_ky_vong(.8),
              he_so_chi_phi_moi_viec_thanh_cong(.8, 3))
    for value, expected in zip(values, (1.20, 1.25, 1.25)):
        assert math.isclose(value, expected)
    print('Ba phép thử đáp án biết trước: ĐẠT', *(f'{v:.2f}' for v in values))


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1, he_so_lam_lai=1, max_lan_chay=None):
    runs = runs[runs.request_id.isin(reqs.request_id)]
    eligible = reqs
    if max_lan_chay is not None:
        runs = runs[runs.attempt <= max_lan_chay]
        eligible = reqs[reqs.so_lan_chay <= max_lan_chay]
    token = (runs.tokens_in * gia_vao + runs.tokens_out * gia_ra) / 1000
    tool = runs.tool_calls * gia_tool
    xem = eligible.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam = eligible.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    total = token.sum() + tool.sum() + xem + lam
    success = eligible.ket_qua.eq('thanh_cong').sum()
    return dict(token=token.sum(), tool=tool.sum(), chay_lai=(token + tool)[runs.attempt > 1].sum(),
                xem_lai=xem, lam_lai=lam, tong=total, thanh_cong=success,
                cps=total / success if success else math.inf,
                hoa_don_moi_yc=(token.sum() + tool.sum()) / len(reqs) if len(reqs) else math.nan)


def bao_cao_chi_phi(runs, reqs):
    base = mo_hinh(runs, reqs)
    print('A2 · Khoản có giờ nhân viên và các tỷ số tương ứng: simulated')
    for name, value in base.items():
        print(f'{name:18} {value:,.2f}')
    print('CPS / hóa đơn:', base['cps'] / base['hoa_don_moi_yc'])
    print('Tỷ trọng làm lại:', base['lam_lai'] / base['tong'])
    fallback = len(reqs) - base['thanh_cong']
    system_per_request = (base['tong'] + BASELINE * fallback) / len(reqs)
    print('Chi phí hệ thống/yêu cầu (simulated):', round(system_per_request),
          f'{system_per_request / BASELINE:.2f}× mức tự làm')
    print('A3 · Loại | số yêu cầu | thành công | lần/yêu cầu | CPS và tỷ số (simulated)')
    for name, group in reqs.groupby('loai'):
        model = mo_hinh(runs, group)
        print(name, len(group), f"{model['thanh_cong']/len(group):.1%}",
              f"{group.so_lan_chay.mean():.2f}", round(model['cps']), f"{model['cps']/BASELINE:.2f}")
    intl = runs[runs.request_id.isin(reqs.loc[reqs.loai == 'quoc_te', 'request_id'])]
    print('Quốc tế, tỷ lệ ok theo lần:', intl.status.eq('ok').groupby(intl.attempt).mean().to_dict())
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    pilot = mo_hinh(runs, scope)
    print('A4 · Lượng | số thành công | cố định/việc | CPS gồm cố định và tỷ số (simulated)')
    for volume in (45000, 22500):
        solved = volume * pilot['thanh_cong'] / len(reqs)
        fixed = 40000000 / solved
        cps = pilot['cps'] + fixed
        print(volume, solved, round(fixed), round(cps), f'{cps/BASELINE:.2f}')

    scenarios = {
        'Token ×2': dict(gia_vao=52, gia_ra=260), 'Token ×0,5': dict(gia_vao=13, gia_ra=65),
        'Xem lại ×2': dict(he_so_xem_lai=2), 'Xem lại ×0,5': dict(he_so_xem_lai=.5),
        'Làm lại ×2': dict(he_so_lam_lai=2), 'Làm lại ×0,5': dict(he_so_lam_lai=.5),
        'Lương +25%': dict(luong_phut=2500), 'Tối đa 2 lần': dict(max_lan_chay=2),
        'Tối đa 1 lần': dict(max_lan_chay=1),
        'B2 · Token và xem lại ×2': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    print('B1–B2 · CPS và thay đổi (simulated)')
    for name, params in scenarios.items():
        cps = mo_hinh(runs, reqs, **params)['cps']
        print(name, round(cps), f"{cps/base['cps']-1:+.1%}")
    print('B3 · Giới hạn | tổng trợ lý | chưa thành công | tổng hệ thống | CPS (tiền simulated)')
    for limit in (1, 2, 3):
        model = mo_hinh(runs, reqs, max_lan_chay=limit)
        remaining = len(reqs) - model['thanh_cong']
        system = model['tong'] + remaining * BASELINE
        print(limit, round(model['tong']), remaining, round(system), round(model['cps']))
    ok = runs.loc[runs.status.eq('ok') & runs.request_id.isin(scope.request_id), 'request_id'].nunique()
    rework = scope.ket_qua.eq('lam_lai').sum()
    mean_minutes = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print('B4 · Yêu cầu có run OK, ca làm lại trong phạm vi:', ok, rework)
    print('B4 · Phút làm lại | CPS | tỷ số | phút xem lại hòa vốn (simulated)')
    for minutes in (9, round(mean_minutes, 1)):
        other = pilot['token'] + pilot['tool'] + rework * minutes * LUONG_PHUT
        cps = (other + ok * 5 * LUONG_PHUT) / pilot['thanh_cong']
        max_minutes = (BASELINE * pilot['thanh_cong'] - other) / (ok * LUONG_PHUT)
        print(minutes, round(cps), f'{cps/BASELINE:.2f}', f'{max_minutes:.2f}')
    print('Tỷ lệ mở lại, toàn mẫu và phạm vi:', reqs.mo_lai_trong_7_ngay.mean(),
          scope.mo_lai_trong_7_ngay.mean())


def co_mau(p1, p2, alpha=.05, power=.80):
    normal = NormalDist()
    mean = (p1 + p2) / 2
    null_term = normal.inv_cdf(1 - alpha / 2) * math.sqrt(2 * mean * (1 - mean))
    alt_term = normal.inv_cdf(power) * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((null_term + alt_term) / (p2 - p1)) ** 2)


def bao_cao_co_mau():
    icc = .02
    n = co_mau(.70, .75)
    de = 1 + (75 - 1) * icc
    print('D1a · Yêu cầu mỗi nhánh:', n)
    print('D1b · DE, số yêu cầu và nhân viên mỗi nhánh:', de, math.ceil(n * de), math.ceil(n * de / 75))
    print('D1c,d · Trần mẫu hiệu dụng với 20 nhân viên hoặc 6 depot:', 20 / icc, 6 / icc)
    target = 859  # Cỡ mẫu hiệu dụng mỗi nhánh cho sẵn trong câu D1e.
    m = math.ceil(target * (1 - icc) / (20 - target * icc))
    print('D1e · Yêu cầu/nhân viên, DE:', m, 1 + (m - 1) * icc)


def bao_cao_chi_so(reqs):
    reviewed = reqs[reqs.duoc_xem_lai.eq(1)]
    reopened = reqs.mo_lai_trong_7_ngay.eq(1)
    metrics = {
        'Đóng trong 24h, không mở lại trong 7 ngày': reqs.dong_trong_24h.eq(1) & ~reopened,
        'Sửa hoặc bỏ trong số đã xem': reviewed.quyet_dinh_xem_lai.isin(['sua', 'bo']),
        'Mở lại trong 7 ngày': reopened,
    }
    print('E1 · Chỉ số trong đợt chạy thử')
    for name, observed in metrics.items():
        result = f'{observed.mean():.2%}' if len(observed) else 'chưa có mẫu'
        print(f'{name}: {observed.sum()}/{len(observed)} ({result})')


if __name__ == '__main__':
    kiem_tra_dap_an_biet_truoc()
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    bao_cao_chi_phi(runs, reqs)
    bao_cao_co_mau()
    bao_cao_chi_so(reqs)
