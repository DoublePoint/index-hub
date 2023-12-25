import request from '@/utils/index-request.js'

export function getBaiduIndex(keyWords, start_date, end_date) {
    return request({
        url: '/index/baidu/' + keyWords,
        method: "get",
        params:{
            start_date,
            end_date
        }
    }
    )
}