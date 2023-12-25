"""
百度指数数据获取最佳实践
此脚本完成
1. 清洗关键词
2. 发更少请求获取更多的数据
3. 请求容错
4. 容错后并保留当前已经请求过的数据，并print已请求过的keywords
"""
import datetime
from queue import Queue
from typing import Dict, List
import traceback
import time

import pandas as pd
from qdata.baidu_index import get_search_index
from qdata.baidu_index.common import check_keywords_exists, split_keywords

cookies = """BIDUPSID=2A2F8D1BFD38516904DFEBA3CB96DE9C; PSTM=1687999439; BAIDUID=6EBDC209E475985999504B7CCE070742:SL=0:NR=10:FG=1; H_WISE_SIDS=131862_216850_213357_214792_110085_244718_261724_236312_264478_265615_265881_266366_256303_267072_268593_268706_266186_259642_269233_269831_269749_269904_267066_256739_270460_270520_264423_270547_270315_271171_256958_266028_270102_267807_269627_256151_234295_234208_272278_267596_272465_272655_272764_270141_260335_273119_273140_273241_273300_272500_273399_273380_271157_273451_273474_271146_273671_264170_270186_263619_273165_273957_274139_274209_273788_273043_273594_274301_274385_272560_274440_274617_274766_274759_274793_274853_274857_274847_270158_275070_275095_267547_273922_275167_274333_275147_272331_272317_275771_275383_270538_273492_275007_275865_275993_275941_275970_274784_276090_269610_276062_276120_271120_276250_274502_276196_275629_276338_275908_275171_276424_273945_272168_276510_269286_275691_276586_273520_275589; H_WISE_SIDS_BFESS=131862_216850_213357_214792_110085_244718_261724_236312_264478_265615_265881_266366_256303_267072_268593_268706_266186_259642_269233_269831_269749_269904_267066_256739_270460_270520_264423_270547_270315_271171_256958_266028_270102_267807_269627_256151_234295_234208_272278_267596_272465_272655_272764_270141_260335_273119_273140_273241_273300_272500_273399_273380_271157_273451_273474_271146_273671_264170_270186_263619_273165_273957_274139_274209_273788_273043_273594_274301_274385_272560_274440_274617_274766_274759_274793_274853_274857_274847_270158_275070_275095_267547_273922_275167_274333_275147_272331_272317_275771_275383_270538_273492_275007_275865_275993_275941_275970_274784_276090_269610_276062_276120_271120_276250_274502_276196_275629_276338_275908_275171_276424_273945_272168_276510_269286_275691_276586_273520_275589; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-326%3A; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1695370396,1696724518,1696731506,1697001842; BDUSS=kJ2RnFlTn53WWpzT1kwTWtBWlhUWWhaUXhMN3ZLZnRLRmxWQ01ERnctVnJ3azFsRVFBQUFBJCQAAAAAAAAAAAEAAAC5B~QbwffA4cDhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGs1JmVrNSZlS; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04470153088B7GE9SlLPMUlqOkBJblkoMuioJiXRtTqxjMDwOApqzn%2FabY6UQTiAfaVaboTFKB5U7HassHjgTSUw2TgkvY2rgXmb6Q8VO95fDb4GWfbSK0Z8jUK6L9rtujRPn8nFen%2BA4WL08X7wHyCKGNHm3t6d%2FK4mzo6KjsX4j%2FPD26mTY%2B%2BmFGq3rjOTtSWqjTMlnENPKDFTmvYIEm0b8eiSpOJhvE%2FLiTm5VHNSo33gmeep4tmZnLmJzUBRLI2V1yKe1WvK3MmtMBzAC%2Bj4%2B4xCES6X2c5KqKLd8IxNfek2tFzBcgNYHg%2FzvR1j6sMqnQ1HWNY26702427265331330666369674598524; __cas__rn__=447015308; __cas__st__212=cf34fcedbd7ef55931dcabd26ef3472c7d22b9ac114e6b68f51e7b71b5d6af132168019c162b264d7a139e43; __cas__id__212=50488007; CPTK_212=1734226457; CPID_212=50488007; bdindexid=j65nupmghcssgg0iagl809tng4; BA_HECTOR=812l058hakak20ah8521akac1iicgdu1p; delPer=0; PSINO=2; BAIDUID_BFESS=6EBDC209E475985999504B7CCE070742:SL=0:NR=10:FG=1; ZFY=7mIwgXagVr32DrJU2E4PVvSlpnQbhZxZPgAOP8YiNZ8:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=39329_39368_39447_39399_39396_39420_39413_39480_39307_39478_39466_39234_39406_39486_26350_39219_39427; BCLID=10379782310572468641; BCLID_BFESS=10379782310572468641; BDSFRCVID=RCKOJexroG0i0JJq54KZrIPJkcpWxY5TDYrEOwXPsp3LGJLVFqB6EG0Pts1-dEu-S2EwogKKymOTHuuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=RCKOJexroG0i0JJq54KZrIPJkcpWxY5TDYrEOwXPsp3LGJLVFqB6EG0Pts1-dEu-S2EwogKKymOTHuuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC8-fIvDqTrP-trf5DCShUFsaUJRB2Q-XPoO3KJEhhc_KjonMjLXyJ3Za-JjQ5bk_xbgy4op8P3y0bb2DUA1y4vp0JoGJeTxoUJ2-KDVeh5Gqq-KQJ-ebPRih4r9QgbtLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD89Dj-Ke5PVKgTa54cbb4o2WbCQWRQr8pcN2b5oQT8tD-6Zb6QxK57HaxJF2bO2SPnXjqOUWJDkXpJvQnJjt2JxaqRC3tjIMl5jDh3MKToDb-oteltH36vy0hvcMR6cShnG5fjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDH-OJ6tHfn3aQ5rtKRTffjrnhPF3KpLrXP6-hnjy3bR0opcF-CKMOIT4yq3kMPtQ3p7ktl3Ry6r42-39LPO2hpRjyxv4QR_Yj4oxJpOJ-bCL0p5aHx8Kst3vbURv2tug3-7t-x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC8ytC8KbKvPKITD-tFO5eT22-usMDvm2hcHMPoosIJYDM6kKjQ3yNJHBlOZ2K7j--nwJxbUotoHXnJi0btQDPvxBf7p3j6G_q5TtUJMqIDzbMohqqJXQqJyKMniMCj9-pnablQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDj-WDjJXeaRabK6aKC5bL6rJabC3VlOoXU6q2bDeQN30JUTZ-RIJaMc-WxJkjnOx3n7Zjq0vWq54WbbvLT7johRTWqR4s4jtjxonDh83KNLLKUQtHGAHK43O5hvvJJ6O3M7h5fKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRC8VC-b3H; H_BDCLCKID_SF_BFESS=tRAOoC8-fIvDqTrP-trf5DCShUFsaUJRB2Q-XPoO3KJEhhc_KjonMjLXyJ3Za-JjQ5bk_xbgy4op8P3y0bb2DUA1y4vp0JoGJeTxoUJ2-KDVeh5Gqq-KQJ-ebPRih4r9QgbtLlQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD89Dj-Ke5PVKgTa54cbb4o2WbCQWRQr8pcN2b5oQT8tD-6Zb6QxK57HaxJF2bO2SPnXjqOUWJDkXpJvQnJjt2JxaqRC3tjIMl5jDh3MKToDb-oteltH36vy0hvcMR6cShnG5fjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDH-OJ6tHfn3aQ5rtKRTffjrnhPF3KpLrXP6-hnjy3bR0opcF-CKMOIT4yq3kMPtQ3p7ktl3Ry6r42-39LPO2hpRjyxv4QR_Yj4oxJpOJ-bCL0p5aHx8Kst3vbURv2tug3-7t-x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC8ytC8KbKvPKITD-tFO5eT22-usMDvm2hcHMPoosIJYDM6kKjQ3yNJHBlOZ2K7j--nwJxbUotoHXnJi0btQDPvxBf7p3j6G_q5TtUJMqIDzbMohqqJXQqJyKMniMCj9-pnablQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDj-WDjJXeaRabK6aKC5bL6rJabC3VlOoXU6q2bDeQN30JUTZ-RIJaMc-WxJkjnOx3n7Zjq0vWq54WbbvLT7johRTWqR4s4jtjxonDh83KNLLKUQtHGAHK43O5hvvJJ6O3M7h5fKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRC8VC-b3H; RT="z=1&dm=baidu.com&si=ead82217-e173-4d95-bc67-8c8763070a8f&ss=lnldqt8e&sl=6&tt=6qg&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1697008872; ab_sr=1.0.1_NDhhYzcyZmEwYWZmZmFkZjgwMTJjZTYxOGQ0ZjJmMTE5MjM1NjIxNWU2MThmMjc1YTdkNjMwZWRiMjgyMTk5NjhjYWI4OWE3OTA3YzZjYmY3YjU0NmQyYWQ3YThkOWU1NDdmMWFjZThjMmFiM2Y1NWFiNGY4MjAzNGY5MDg2MmE2YWYxOTQyYTM0ODRlOGYxMTBhZDY1ODMzYzc5N2QwMg==; BDUSS_BFESS=kJ2RnFlTn53WWpzT1kwTWtBWlhUWWhaUXhMN3ZLZnRLRmxWQ01ERnctVnJ3azFsRVFBQUFBJCQAAAAAAAAAAAEAAAC5B~QbwffA4cDhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGs1JmVrNSZlS"""


def get_clear_keywords_list(keywords_list: List[List[str]]) -> List[List[str]]:
    q = Queue(-1)

    cur_keywords_list = []
    for keywords in keywords_list:
        cur_keywords_list.extend(keywords)

    # 先找到所有未收录的关键词
    for start in range(0, len(cur_keywords_list), 15):
        q.put(cur_keywords_list[start:start + 15])

    not_exist_keyword_set = set()
    while not q.empty():
        keywords = q.get()
        try:
            check_result = check_keywords_exists(keywords, cookies)
            time.sleep(5)
        except:
            traceback.print_exc()
            q.put(keywords)
            time.sleep(90)

        for keyword in check_result["not_exists_keywords"]:
            not_exist_keyword_set.add(keyword)

    # 在原有的keywords_list拎出没有收录的关键词
    new_keywords_list = []
    for keywords in keywords_list:
        not_exists_count = len([None for keyword in keywords if keyword in not_exist_keyword_set])
        if not_exists_count == 0:
            new_keywords_list.append(keywords)

    return new_keywords_list


def save_to_excel(datas: List[Dict]):
    pd.DataFrame(datas).to_excel("index.xlsx")


def get_search_index_demo(keywords_list: List[List[str]],start_date: str,end_date:str):
    """
        1. 先清洗keywords数据，把没有收录的关键词拎出来
        2. 然后split_keywords关键词正常请求
        3. 数据存入excel
    """
    print("开始清洗关键词")
    requested_keywords = []
    keywords_list = get_clear_keywords_list(keywords_list)
    q = Queue(-1)

    for splited_keywords_list in split_keywords(keywords_list):
        q.put(splited_keywords_list)

    print("开始请求百度指数")
    datas = []
    while not q.empty():
        cur_keywords_list = q.get()
        try:
            print(f"开始请求: {cur_keywords_list}")
            for index in get_search_index(
                    keywords_list=cur_keywords_list,
                    start_date= start_date,
                    end_date=end_date,
                    cookies=cookies
            ):
                index["keyword"] = ",".join(index["keyword"])
                datas.append(index)
            requested_keywords.extend(cur_keywords_list)
            print(f"请求完成: {cur_keywords_list}")
            time.sleep(10)
        except:
            traceback.print_exc()
            print(f"请求出错, requested_keywords: {requested_keywords}")
            # save_to_excel(datas)
            q.put(cur_keywords_list)
            time.sleep(180)

    return datas


if __name__ == "__main__":
    keywords_list = [
        ["任正非"],
    ]
    get_search_index_demo(keywords_list)