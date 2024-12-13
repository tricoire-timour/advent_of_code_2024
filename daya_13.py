import re
from typing import Dict


def parse_claw_machine(machinestring: str, part2: bool = False) -> Dict[str, int]:
    regex_A = r"Button A: X\+(\d+), Y\+(\d+)"
    regex_B = r"Button B: X\+(\d+), Y\+(\d+)"
    regex_S = r"Prize: X=(\d+), Y=(\d+)"
    # print(regex_A)
    a_search = re.search(regex_A, machinestring)
    b_search = re.search(regex_B, machinestring)
    s_search = re.search(regex_S, machinestring)

    return {
        "ax": int(a_search.group(1)),
        "ay": int(a_search.group(2)),
        "bx": int(b_search.group(1)),
        "by": int(b_search.group(2)),
        "sx": int(s_search.group(1)) + 10000000000000 * part2,
        "sy": int(s_search.group(2)) + 10000000000000 * part2,
    }


def solve_machine(ax: int, ay: int, bx: int, by: int, sx: int, sy: int):
    det = 1 / (ax * by - bx * ay)
    a = det * (by * sx - bx * sy)
    b = det * (ax * sy - ay * sx)

    return a, b



def main():
    input: str = """
Button A: X+24, Y+19
Button B: X+32, Y+86
Prize: X=1072, Y=2062

Button A: X+70, Y+12
Button B: X+11, Y+43
Prize: X=3400, Y=3872

Button A: X+48, Y+77
Button B: X+34, Y+12
Prize: X=6510, Y=1583

Button A: X+76, Y+60
Button B: X+29, Y+88
Prize: X=5506, Y=6300

Button A: X+16, Y+75
Button B: X+68, Y+20
Prize: X=17148, Y=13490

Button A: X+46, Y+13
Button B: X+33, Y+63
Prize: X=15572, Y=9644

Button A: X+21, Y+79
Button B: X+44, Y+32
Prize: X=2433, Y=5147

Button A: X+13, Y+45
Button B: X+36, Y+11
Prize: X=4612, Y=19164

Button A: X+28, Y+60
Button B: X+53, Y+22
Prize: X=16217, Y=18514

Button A: X+35, Y+12
Button B: X+21, Y+34
Prize: X=4631, Y=17148

Button A: X+15, Y+48
Button B: X+60, Y+13
Prize: X=12755, Y=355

Button A: X+86, Y+21
Button B: X+11, Y+64
Prize: X=4706, Y=15186

Button A: X+53, Y+17
Button B: X+44, Y+81
Prize: X=4451, Y=3294

Button A: X+13, Y+43
Button B: X+94, Y+86
Prize: X=2299, Y=2881

Button A: X+74, Y+19
Button B: X+24, Y+76
Prize: X=7178, Y=9259

Button A: X+28, Y+67
Button B: X+39, Y+13
Prize: X=10019, Y=17169

Button A: X+30, Y+11
Button B: X+44, Y+61
Prize: X=7878, Y=8640

Button A: X+97, Y+44
Button B: X+16, Y+60
Prize: X=9823, Y=6460

Button A: X+30, Y+96
Button B: X+94, Y+53
Prize: X=3112, Y=6737

Button A: X+17, Y+51
Button B: X+40, Y+22
Prize: X=7630, Y=8490

Button A: X+60, Y+29
Button B: X+13, Y+48
Prize: X=7070, Y=6922

Button A: X+25, Y+83
Button B: X+62, Y+13
Prize: X=11211, Y=3085

Button A: X+77, Y+11
Button B: X+20, Y+24
Prize: X=7131, Y=1801

Button A: X+12, Y+44
Button B: X+68, Y+22
Prize: X=8684, Y=14092

Button A: X+59, Y+16
Button B: X+16, Y+62
Prize: X=19148, Y=17858

Button A: X+14, Y+67
Button B: X+74, Y+44
Prize: X=3388, Y=5359

Button A: X+15, Y+44
Button B: X+60, Y+17
Prize: X=10145, Y=16182

Button A: X+41, Y+26
Button B: X+18, Y+39
Prize: X=16245, Y=19737

Button A: X+78, Y+18
Button B: X+72, Y+99
Prize: X=8592, Y=5031

Button A: X+37, Y+11
Button B: X+40, Y+79
Prize: X=15777, Y=9199

Button A: X+22, Y+53
Button B: X+50, Y+12
Prize: X=14676, Y=9212

Button A: X+54, Y+81
Button B: X+38, Y+14
Prize: X=1088, Y=5435

Button A: X+15, Y+55
Button B: X+53, Y+22
Prize: X=7906, Y=16259

Button A: X+28, Y+69
Button B: X+58, Y+18
Prize: X=11098, Y=15851

Button A: X+23, Y+61
Button B: X+51, Y+15
Prize: X=5789, Y=17117

Button A: X+55, Y+13
Button B: X+39, Y+76
Prize: X=10884, Y=14021

Button A: X+16, Y+64
Button B: X+41, Y+15
Prize: X=8377, Y=10591

Button A: X+51, Y+78
Button B: X+77, Y+19
Prize: X=9631, Y=6236

Button A: X+18, Y+39
Button B: X+53, Y+20
Prize: X=9001, Y=11458

Button A: X+52, Y+70
Button B: X+32, Y+13
Prize: X=19604, Y=2193

Button A: X+68, Y+22
Button B: X+25, Y+67
Prize: X=2995, Y=1001

Button A: X+47, Y+69
Button B: X+39, Y+18
Prize: X=4025, Y=5595

Button A: X+19, Y+95
Button B: X+25, Y+20
Prize: X=1708, Y=1925

Button A: X+93, Y+31
Button B: X+59, Y+88
Prize: X=9880, Y=7735

Button A: X+22, Y+82
Button B: X+50, Y+26
Prize: X=5002, Y=7258

Button A: X+23, Y+12
Button B: X+17, Y+54
Prize: X=797, Y=8306

Button A: X+60, Y+12
Button B: X+14, Y+66
Prize: X=10262, Y=8498

Button A: X+97, Y+12
Button B: X+18, Y+39
Prize: X=5116, Y=780

Button A: X+57, Y+12
Button B: X+23, Y+70
Prize: X=14382, Y=5998

Button A: X+55, Y+17
Button B: X+12, Y+43
Prize: X=10392, Y=989

Button A: X+15, Y+58
Button B: X+74, Y+11
Prize: X=13688, Y=9512

Button A: X+66, Y+18
Button B: X+79, Y+80
Prize: X=9011, Y=7660

Button A: X+52, Y+20
Button B: X+38, Y+72
Prize: X=16614, Y=10572

Button A: X+62, Y+23
Button B: X+63, Y+90
Prize: X=3542, Y=1847

Button A: X+67, Y+16
Button B: X+19, Y+65
Prize: X=12129, Y=12930

Button A: X+29, Y+43
Button B: X+66, Y+13
Prize: X=4534, Y=2310

Button A: X+86, Y+36
Button B: X+40, Y+89
Prize: X=4066, Y=7338

Button A: X+84, Y+25
Button B: X+29, Y+89
Prize: X=7772, Y=3599

Button A: X+13, Y+53
Button B: X+43, Y+19
Prize: X=19353, Y=16657

Button A: X+42, Y+19
Button B: X+17, Y+34
Prize: X=2814, Y=3483

Button A: X+35, Y+79
Button B: X+80, Y+11
Prize: X=2875, Y=5811

Button A: X+38, Y+14
Button B: X+25, Y+41
Prize: X=15533, Y=13869

Button A: X+60, Y+14
Button B: X+14, Y+38
Prize: X=3774, Y=2652

Button A: X+42, Y+13
Button B: X+22, Y+73
Prize: X=370, Y=7555

Button A: X+94, Y+30
Button B: X+36, Y+59
Prize: X=11974, Y=8335

Button A: X+48, Y+13
Button B: X+17, Y+53
Prize: X=17226, Y=13807

Button A: X+36, Y+94
Button B: X+53, Y+20
Prize: X=1576, Y=3168

Button A: X+13, Y+41
Button B: X+62, Y+13
Prize: X=5670, Y=10213

Button A: X+49, Y+23
Button B: X+16, Y+75
Prize: X=3597, Y=4253

Button A: X+67, Y+32
Button B: X+26, Y+54
Prize: X=9852, Y=18406

Button A: X+64, Y+19
Button B: X+18, Y+64
Prize: X=17750, Y=4281

Button A: X+91, Y+23
Button B: X+14, Y+33
Prize: X=4480, Y=1751

Button A: X+46, Y+14
Button B: X+12, Y+26
Prize: X=1956, Y=11264

Button A: X+59, Y+15
Button B: X+61, Y+64
Prize: X=3283, Y=1756

Button A: X+18, Y+66
Button B: X+38, Y+17
Prize: X=3268, Y=4765

Button A: X+12, Y+89
Button B: X+31, Y+35
Prize: X=761, Y=3500

Button A: X+77, Y+34
Button B: X+23, Y+71
Prize: X=5262, Y=5244

Button A: X+27, Y+11
Button B: X+25, Y+46
Prize: X=9480, Y=900

Button A: X+53, Y+96
Button B: X+82, Y+28
Prize: X=6588, Y=3496

Button A: X+91, Y+91
Button B: X+12, Y+53
Prize: X=7616, Y=8764

Button A: X+18, Y+62
Button B: X+90, Y+73
Prize: X=7542, Y=10099

Button A: X+98, Y+43
Button B: X+30, Y+52
Prize: X=6912, Y=5130

Button A: X+33, Y+94
Button B: X+96, Y+28
Prize: X=6855, Y=2590

Button A: X+80, Y+14
Button B: X+18, Y+79
Prize: X=18962, Y=9367

Button A: X+25, Y+39
Button B: X+94, Y+44
Prize: X=1877, Y=2107

Button A: X+94, Y+57
Button B: X+32, Y+99
Prize: X=7894, Y=8289

Button A: X+23, Y+51
Button B: X+60, Y+32
Prize: X=10153, Y=5421

Button A: X+72, Y+16
Button B: X+26, Y+31
Prize: X=974, Y=393

Button A: X+43, Y+57
Button B: X+74, Y+28
Prize: X=6291, Y=3643

Button A: X+52, Y+26
Button B: X+13, Y+95
Prize: X=2912, Y=4996

Button A: X+51, Y+21
Button B: X+21, Y+40
Prize: X=11606, Y=5563

Button A: X+17, Y+47
Button B: X+39, Y+20
Prize: X=1239, Y=9144

Button A: X+66, Y+48
Button B: X+35, Y+97
Prize: X=2981, Y=6103

Button A: X+44, Y+78
Button B: X+56, Y+27
Prize: X=4604, Y=6138

Button A: X+78, Y+17
Button B: X+28, Y+62
Prize: X=5814, Y=2441

Button A: X+50, Y+12
Button B: X+28, Y+67
Prize: X=11480, Y=11750

Button A: X+65, Y+42
Button B: X+38, Y+94
Prize: X=3716, Y=7054

Button A: X+62, Y+12
Button B: X+19, Y+72
Prize: X=7707, Y=16700

Button A: X+13, Y+31
Button B: X+62, Y+38
Prize: X=6220, Y=4624

Button A: X+56, Y+16
Button B: X+30, Y+94
Prize: X=2978, Y=2474

Button A: X+94, Y+34
Button B: X+28, Y+98
Prize: X=5764, Y=5424

Button A: X+62, Y+11
Button B: X+22, Y+79
Prize: X=14984, Y=3092

Button A: X+99, Y+23
Button B: X+59, Y+56
Prize: X=9449, Y=5917

Button A: X+19, Y+42
Button B: X+64, Y+29
Prize: X=8395, Y=5312

Button A: X+12, Y+31
Button B: X+37, Y+18
Prize: X=10180, Y=17381

Button A: X+29, Y+57
Button B: X+51, Y+12
Prize: X=1838, Y=2289

Button A: X+55, Y+22
Button B: X+27, Y+80
Prize: X=4782, Y=2328

Button A: X+85, Y+39
Button B: X+32, Y+66
Prize: X=6870, Y=5718

Button A: X+59, Y+23
Button B: X+36, Y+98
Prize: X=6052, Y=5466

Button A: X+62, Y+24
Button B: X+18, Y+39
Prize: X=10738, Y=13433

Button A: X+52, Y+21
Button B: X+15, Y+55
Prize: X=12810, Y=18835

Button A: X+21, Y+81
Button B: X+55, Y+13
Prize: X=10967, Y=12335

Button A: X+26, Y+54
Button B: X+58, Y+20
Prize: X=17800, Y=12084

Button A: X+48, Y+22
Button B: X+38, Y+59
Prize: X=2020, Y=18720

Button A: X+38, Y+60
Button B: X+89, Y+16
Prize: X=6495, Y=1912

Button A: X+13, Y+38
Button B: X+43, Y+17
Prize: X=3164, Y=3814

Button A: X+19, Y+79
Button B: X+99, Y+97
Prize: X=2264, Y=4694

Button A: X+55, Y+30
Button B: X+17, Y+48
Prize: X=13997, Y=1718

Button A: X+52, Y+17
Button B: X+12, Y+67
Prize: X=13200, Y=13640

Button A: X+22, Y+39
Button B: X+49, Y+15
Prize: X=19399, Y=2297

Button A: X+19, Y+45
Button B: X+60, Y+31
Prize: X=19412, Y=15586

Button A: X+19, Y+37
Button B: X+78, Y+37
Prize: X=3793, Y=2331

Button A: X+80, Y+85
Button B: X+16, Y+73
Prize: X=5792, Y=6546

Button A: X+43, Y+12
Button B: X+39, Y+85
Prize: X=4207, Y=3694

Button A: X+46, Y+82
Button B: X+46, Y+15
Prize: X=9576, Y=8815

Button A: X+12, Y+23
Button B: X+34, Y+15
Prize: X=1812, Y=2655

Button A: X+54, Y+20
Button B: X+24, Y+67
Prize: X=4622, Y=15596

Button A: X+67, Y+17
Button B: X+14, Y+38
Prize: X=9207, Y=18557

Button A: X+45, Y+13
Button B: X+25, Y+46
Prize: X=18195, Y=14322

Button A: X+34, Y+86
Button B: X+77, Y+15
Prize: X=9920, Y=9632

Button A: X+46, Y+22
Button B: X+34, Y+61
Prize: X=13246, Y=6391

Button A: X+69, Y+25
Button B: X+22, Y+70
Prize: X=10124, Y=13980

Button A: X+22, Y+97
Button B: X+41, Y+13
Prize: X=4414, Y=3020

Button A: X+13, Y+81
Button B: X+43, Y+43
Prize: X=1722, Y=3082

Button A: X+73, Y+17
Button B: X+35, Y+79
Prize: X=2952, Y=900

Button A: X+61, Y+22
Button B: X+28, Y+62
Prize: X=5420, Y=9566

Button A: X+94, Y+89
Button B: X+69, Y+13
Prize: X=5199, Y=1835

Button A: X+49, Y+11
Button B: X+19, Y+77
Prize: X=4403, Y=6557

Button A: X+13, Y+35
Button B: X+56, Y+16
Prize: X=5234, Y=3310

Button A: X+31, Y+55
Button B: X+79, Y+31
Prize: X=4261, Y=4285

Button A: X+77, Y+30
Button B: X+12, Y+59
Prize: X=4151, Y=15807

Button A: X+24, Y+33
Button B: X+93, Y+30
Prize: X=6117, Y=2049

Button A: X+56, Y+16
Button B: X+28, Y+79
Prize: X=5996, Y=8999

Button A: X+36, Y+48
Button B: X+62, Y+22
Prize: X=6140, Y=2848

Button A: X+19, Y+81
Button B: X+92, Y+73
Prize: X=1937, Y=4108

Button A: X+34, Y+43
Button B: X+71, Y+14
Prize: X=8182, Y=2920

Button A: X+88, Y+17
Button B: X+23, Y+76
Prize: X=8572, Y=4232

Button A: X+43, Y+14
Button B: X+48, Y+62
Prize: X=3715, Y=3760

Button A: X+64, Y+31
Button B: X+15, Y+28
Prize: X=4831, Y=3356

Button A: X+20, Y+78
Button B: X+59, Y+16
Prize: X=18135, Y=18436

Button A: X+34, Y+82
Button B: X+67, Y+50
Prize: X=7082, Y=10608

Button A: X+27, Y+52
Button B: X+35, Y+16
Prize: X=13420, Y=14496

Button A: X+63, Y+16
Button B: X+17, Y+45
Prize: X=11797, Y=7522

Button A: X+59, Y+32
Button B: X+22, Y+42
Prize: X=2576, Y=2630

Button A: X+72, Y+19
Button B: X+11, Y+65
Prize: X=11493, Y=12456

Button A: X+28, Y+50
Button B: X+44, Y+17
Prize: X=3376, Y=4243

Button A: X+12, Y+26
Button B: X+40, Y+15
Prize: X=6240, Y=8820

Button A: X+95, Y+90
Button B: X+24, Y+92
Prize: X=3109, Y=8902

Button A: X+54, Y+85
Button B: X+29, Y+13
Prize: X=5304, Y=8153

Button A: X+89, Y+30
Button B: X+37, Y+63
Prize: X=4498, Y=3891

Button A: X+64, Y+26
Button B: X+28, Y+65
Prize: X=12672, Y=15304

Button A: X+59, Y+13
Button B: X+30, Y+68
Prize: X=2106, Y=11186

Button A: X+67, Y+38
Button B: X+15, Y+54
Prize: X=2451, Y=2118

Button A: X+90, Y+64
Button B: X+38, Y+85
Prize: X=8508, Y=9007

Button A: X+15, Y+49
Button B: X+79, Y+66
Prize: X=4691, Y=6873

Button A: X+69, Y+36
Button B: X+30, Y+70
Prize: X=8784, Y=8496

Button A: X+50, Y+27
Button B: X+24, Y+54
Prize: X=13606, Y=12005

Button A: X+93, Y+20
Button B: X+60, Y+82
Prize: X=9540, Y=6612

Button A: X+16, Y+37
Button B: X+44, Y+25
Prize: X=11072, Y=4649

Button A: X+15, Y+72
Button B: X+67, Y+64
Prize: X=5435, Y=9344

Button A: X+82, Y+20
Button B: X+58, Y+85
Prize: X=7080, Y=4065

Button A: X+46, Y+16
Button B: X+25, Y+30
Prize: X=2728, Y=2568

Button A: X+44, Y+21
Button B: X+16, Y+25
Prize: X=9076, Y=7755

Button A: X+18, Y+73
Button B: X+65, Y+52
Prize: X=3257, Y=2840

Button A: X+96, Y+88
Button B: X+88, Y+19
Prize: X=8304, Y=3542

Button A: X+43, Y+66
Button B: X+82, Y+34
Prize: X=4003, Y=2286

Button A: X+38, Y+49
Button B: X+56, Y+20
Prize: X=4954, Y=4143

Button A: X+78, Y+13
Button B: X+13, Y+76
Prize: X=5528, Y=13048

Button A: X+59, Y+17
Button B: X+20, Y+59
Prize: X=1181, Y=5537

Button A: X+47, Y+16
Button B: X+21, Y+52
Prize: X=17705, Y=1120

Button A: X+53, Y+80
Button B: X+32, Y+12
Prize: X=12796, Y=12368

Button A: X+99, Y+49
Button B: X+49, Y+96
Prize: X=8502, Y=5930

Button A: X+44, Y+11
Button B: X+42, Y+75
Prize: X=4310, Y=1307

Button A: X+34, Y+41
Button B: X+35, Y+11
Prize: X=2088, Y=1020

Button A: X+66, Y+34
Button B: X+16, Y+55
Prize: X=7012, Y=10115

Button A: X+95, Y+23
Button B: X+31, Y+59
Prize: X=5358, Y=3254

Button A: X+99, Y+60
Button B: X+25, Y+84
Prize: X=7177, Y=11028

Button A: X+50, Y+54
Button B: X+66, Y+14
Prize: X=10886, Y=6258

Button A: X+81, Y+71
Button B: X+19, Y+56
Prize: X=6295, Y=8154

Button A: X+42, Y+90
Button B: X+87, Y+11
Prize: X=4329, Y=4189

Button A: X+12, Y+35
Button B: X+91, Y+41
Prize: X=9190, Y=5709

Button A: X+19, Y+63
Button B: X+63, Y+13
Prize: X=13162, Y=5892

Button A: X+94, Y+22
Button B: X+57, Y+67
Prize: X=5085, Y=1995

Button A: X+33, Y+57
Button B: X+54, Y+23
Prize: X=4505, Y=10885

Button A: X+44, Y+94
Button B: X+97, Y+41
Prize: X=5347, Y=6935

Button A: X+85, Y+32
Button B: X+31, Y+69
Prize: X=4575, Y=2009

Button A: X+25, Y+47
Button B: X+47, Y+11
Prize: X=19108, Y=11486

Button A: X+52, Y+20
Button B: X+36, Y+63
Prize: X=7292, Y=7081

Button A: X+16, Y+60
Button B: X+37, Y+12
Prize: X=1666, Y=776

Button A: X+87, Y+55
Button B: X+12, Y+65
Prize: X=1536, Y=1660

Button A: X+78, Y+17
Button B: X+12, Y+46
Prize: X=9200, Y=5592

Button A: X+70, Y+33
Button B: X+51, Y+91
Prize: X=7679, Y=6901

Button A: X+26, Y+50
Button B: X+41, Y+12
Prize: X=12582, Y=12894

Button A: X+64, Y+61
Button B: X+16, Y+95
Prize: X=6640, Y=13586

Button A: X+31, Y+70
Button B: X+58, Y+13
Prize: X=13263, Y=9321

Button A: X+19, Y+34
Button B: X+39, Y+14
Prize: X=5655, Y=13370

Button A: X+12, Y+98
Button B: X+22, Y+20
Prize: X=1958, Y=5612

Button A: X+27, Y+77
Button B: X+57, Y+11
Prize: X=17351, Y=13817

Button A: X+15, Y+40
Button B: X+80, Y+56
Prize: X=11650, Y=360

Button A: X+15, Y+65
Button B: X+43, Y+15
Prize: X=4148, Y=12300

Button A: X+67, Y+20
Button B: X+14, Y+39
Prize: X=13161, Y=11201

Button A: X+49, Y+87
Button B: X+87, Y+30
Prize: X=6930, Y=5334

Button A: X+45, Y+23
Button B: X+30, Y+47
Prize: X=11225, Y=10035

Button A: X+88, Y+93
Button B: X+13, Y+60
Prize: X=5964, Y=6858

Button A: X+26, Y+16
Button B: X+18, Y+49
Prize: X=15688, Y=1078

Button A: X+18, Y+62
Button B: X+32, Y+13
Prize: X=9468, Y=7487

Button A: X+58, Y+23
Button B: X+22, Y+41
Prize: X=17842, Y=4467

Button A: X+64, Y+30
Button B: X+13, Y+54
Prize: X=7290, Y=19154

Button A: X+48, Y+15
Button B: X+20, Y+67
Prize: X=4212, Y=3574

Button A: X+34, Y+72
Button B: X+61, Y+20
Prize: X=18848, Y=9472

Button A: X+13, Y+67
Button B: X+68, Y+21
Prize: X=3277, Y=5697

Button A: X+71, Y+19
Button B: X+23, Y+69
Prize: X=15376, Y=14536

Button A: X+28, Y+95
Button B: X+99, Y+81
Prize: X=2060, Y=2911

Button A: X+63, Y+67
Button B: X+99, Y+18
Prize: X=9783, Y=5778

Button A: X+67, Y+31
Button B: X+14, Y+40
Prize: X=7952, Y=15880

Button A: X+76, Y+21
Button B: X+11, Y+58
Prize: X=13336, Y=18613

Button A: X+41, Y+13
Button B: X+44, Y+71
Prize: X=11068, Y=15033

Button A: X+52, Y+12
Button B: X+11, Y+71
Prize: X=14703, Y=12923

Button A: X+15, Y+62
Button B: X+63, Y+21
Prize: X=7070, Y=17662

Button A: X+54, Y+22
Button B: X+28, Y+59
Prize: X=4372, Y=1446

Button A: X+39, Y+16
Button B: X+36, Y+54
Prize: X=15797, Y=3828

Button A: X+69, Y+28
Button B: X+15, Y+51
Prize: X=17381, Y=14738

Button A: X+62, Y+87
Button B: X+76, Y+12
Prize: X=4348, Y=5628

Button A: X+69, Y+26
Button B: X+37, Y+55
Prize: X=2549, Y=2028

Button A: X+13, Y+62
Button B: X+71, Y+24
Prize: X=8269, Y=18356

Button A: X+43, Y+15
Button B: X+28, Y+65
Prize: X=1909, Y=13695

Button A: X+98, Y+20
Button B: X+91, Y+82
Prize: X=11683, Y=7522

Button A: X+15, Y+52
Button B: X+40, Y+11
Prize: X=9010, Y=9870

Button A: X+59, Y+85
Button B: X+68, Y+28
Prize: X=2809, Y=3767

Button A: X+47, Y+12
Button B: X+19, Y+84
Prize: X=4558, Y=4488

Button A: X+33, Y+82
Button B: X+55, Y+14
Prize: X=17392, Y=15744

Button A: X+72, Y+11
Button B: X+80, Y+81
Prize: X=4136, Y=1526

Button A: X+44, Y+70
Button B: X+43, Y+19
Prize: X=10317, Y=6549

Button A: X+20, Y+56
Button B: X+37, Y+14
Prize: X=4504, Y=4624

Button A: X+83, Y+52
Button B: X+13, Y+37
Prize: X=6478, Y=4477

Button A: X+16, Y+64
Button B: X+74, Y+54
Prize: X=4768, Y=5520

Button A: X+33, Y+16
Button B: X+28, Y+48
Prize: X=17063, Y=736

Button A: X+58, Y+12
Button B: X+37, Y+84
Prize: X=9214, Y=16484

Button A: X+66, Y+26
Button B: X+18, Y+55
Prize: X=8768, Y=16881

Button A: X+87, Y+21
Button B: X+68, Y+80
Prize: X=4422, Y=3738

Button A: X+77, Y+18
Button B: X+12, Y+58
Prize: X=7308, Y=5572

Button A: X+12, Y+56
Button B: X+80, Y+38
Prize: X=6432, Y=3860

Button A: X+53, Y+11
Button B: X+15, Y+53
Prize: X=10981, Y=19595

Button A: X+46, Y+29
Button B: X+17, Y+35
Prize: X=7679, Y=8850

Button A: X+24, Y+81
Button B: X+64, Y+13
Prize: X=17472, Y=10578

Button A: X+88, Y+69
Button B: X+13, Y+42
Prize: X=1742, Y=2829

Button A: X+32, Y+69
Button B: X+91, Y+29
Prize: X=6884, Y=7486

Button A: X+54, Y+35
Button B: X+21, Y+47
Prize: X=12746, Y=7205

Button A: X+39, Y+29
Button B: X+20, Y+67
Prize: X=3081, Y=6357

Button A: X+34, Y+64
Button B: X+49, Y+12
Prize: X=2492, Y=6360

Button A: X+73, Y+39
Button B: X+11, Y+45
Prize: X=14329, Y=19055

Button A: X+16, Y+40
Button B: X+63, Y+29
Prize: X=17398, Y=1826

Button A: X+17, Y+38
Button B: X+62, Y+38
Prize: X=12659, Y=3236

Button A: X+21, Y+47
Button B: X+70, Y+40
Prize: X=1421, Y=2247

Button A: X+78, Y+20
Button B: X+23, Y+68
Prize: X=8360, Y=7236

Button A: X+28, Y+61
Button B: X+91, Y+64
Prize: X=3717, Y=4473

Button A: X+72, Y+83
Button B: X+57, Y+14
Prize: X=2736, Y=1913

Button A: X+24, Y+54
Button B: X+50, Y+23
Prize: X=3560, Y=248

Button A: X+61, Y+12
Button B: X+21, Y+60
Prize: X=11872, Y=2000

Button A: X+85, Y+53
Button B: X+30, Y+62
Prize: X=1310, Y=1726

Button A: X+42, Y+97
Button B: X+99, Y+59
Prize: X=9915, Y=8140

Button A: X+23, Y+50
Button B: X+50, Y+13
Prize: X=13729, Y=7516

Button A: X+13, Y+27
Button B: X+95, Y+29
Prize: X=8284, Y=3404

Button A: X+88, Y+33
Button B: X+42, Y+75
Prize: X=6990, Y=8013

Button A: X+45, Y+23
Button B: X+21, Y+37
Prize: X=15869, Y=19355

Button A: X+11, Y+35
Button B: X+47, Y+14
Prize: X=9187, Y=16573

Button A: X+99, Y+29
Button B: X+70, Y+92
Prize: X=5883, Y=6013

Button A: X+29, Y+43
Button B: X+31, Y+15
Prize: X=8625, Y=5987

Button A: X+49, Y+39
Button B: X+25, Y+80
Prize: X=1776, Y=2856

Button A: X+27, Y+11
Button B: X+17, Y+46
Prize: X=13003, Y=7114

Button A: X+54, Y+14
Button B: X+11, Y+76
Prize: X=16886, Y=4026

Button A: X+34, Y+18
Button B: X+16, Y+40
Prize: X=7878, Y=10310

Button A: X+14, Y+57
Button B: X+77, Y+15
Prize: X=7826, Y=5595

Button A: X+19, Y+50
Button B: X+70, Y+43
Prize: X=692, Y=16327

Button A: X+51, Y+11
Button B: X+27, Y+80
Prize: X=19598, Y=7460

Button A: X+86, Y+46
Button B: X+24, Y+95
Prize: X=10030, Y=13499

Button A: X+85, Y+61
Button B: X+27, Y+60
Prize: X=8478, Y=8481

Button A: X+16, Y+23
Button B: X+82, Y+30
Prize: X=4332, Y=2888

Button A: X+51, Y+14
Button B: X+18, Y+59
Prize: X=15431, Y=9761

Button A: X+19, Y+58
Button B: X+48, Y+15
Prize: X=13183, Y=3940

Button A: X+29, Y+99
Button B: X+87, Y+60
Prize: X=6090, Y=7044

Button A: X+34, Y+11
Button B: X+12, Y+40
Prize: X=18710, Y=1065

Button A: X+17, Y+46
Button B: X+44, Y+13
Prize: X=4698, Y=3273

Button A: X+76, Y+86
Button B: X+59, Y+19
Prize: X=9951, Y=9111

Button A: X+12, Y+30
Button B: X+60, Y+44
Prize: X=15416, Y=19276

Button A: X+50, Y+14
Button B: X+21, Y+73
Prize: X=2127, Y=7059

Button A: X+37, Y+68
Button B: X+55, Y+18
Prize: X=16182, Y=18552

Button A: X+16, Y+59
Button B: X+62, Y+32
Prize: X=2728, Y=4554

Button A: X+91, Y+25
Button B: X+56, Y+80
Prize: X=4032, Y=2400

Button A: X+54, Y+17
Button B: X+30, Y+69
Prize: X=8828, Y=15418

Button A: X+21, Y+47
Button B: X+46, Y+13
Prize: X=4247, Y=3836

Button A: X+43, Y+15
Button B: X+20, Y+71
Prize: X=10222, Y=2796

Button A: X+50, Y+72
Button B: X+69, Y+19
Prize: X=1047, Y=463

Button A: X+12, Y+47
Button B: X+87, Y+41
Prize: X=6288, Y=5444

Button A: X+27, Y+65
Button B: X+41, Y+17
Prize: X=8972, Y=14008

Button A: X+13, Y+60
Button B: X+90, Y+44
Prize: X=2050, Y=3148

Button A: X+19, Y+44
Button B: X+62, Y+39
Prize: X=14606, Y=17376

Button A: X+44, Y+73
Button B: X+88, Y+39
Prize: X=10384, Y=7170

Button A: X+17, Y+51
Button B: X+61, Y+26
Prize: X=4865, Y=18025

Button A: X+18, Y+58
Button B: X+92, Y+17
Prize: X=8214, Y=2994

Button A: X+61, Y+29
Button B: X+25, Y+51
Prize: X=17234, Y=7118

Button A: X+82, Y+39
Button B: X+17, Y+26
Prize: X=5753, Y=3614

Button A: X+31, Y+58
Button B: X+48, Y+16
Prize: X=2723, Y=12770

Button A: X+11, Y+57
Button B: X+70, Y+15
Prize: X=13033, Y=19721

Button A: X+51, Y+28
Button B: X+18, Y+84
Prize: X=3027, Y=8036

Button A: X+87, Y+64
Button B: X+12, Y+86
Prize: X=3813, Y=9982

Button A: X+97, Y+94
Button B: X+12, Y+71
Prize: X=4516, Y=7523

Button A: X+29, Y+66
Button B: X+67, Y+29
Prize: X=3515, Y=14148

Button A: X+54, Y+17
Button B: X+20, Y+39
Prize: X=19206, Y=10999

Button A: X+53, Y+31
Button B: X+15, Y+83
Prize: X=2225, Y=5755
    """.strip()

    PART_2 = True

    machines = [parse_claw_machine(machine, PART_2) for machine in input.split("\n\n")]
    print(machines[0])

    print(solve_machine(**machines[0]))
    attempts = [solve_machine(**machine) for machine in machines]

    costs = [3 * round(a) + round(b) for a, b in attempts if is_reasonable_int(a) and is_reasonable_int(b)]
    
    tokens = sum(costs)

    print(tokens)


def is_reasonable_int(n):
    integer = round(n)
    return abs(n - round(n)) < 0.01


if __name__ == "__main__":
    main()