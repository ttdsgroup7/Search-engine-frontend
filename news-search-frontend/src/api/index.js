import axios from "axios";
let host_1 = 'http://gc.caohongchuan.top:8080/';
let host_2 = 'http://gc.caohongchuan.top:7788/';

export const getSearch = (params) => {
    return axios.get(host_1 +`search/querynews?query=${params}`)
}
export const getRecords = () => {
    return axios.put(host_1 +`search/viewrecord`)
}

// export const login = (params) => {
//     return axios.post(host_1 + `login/register`, params)
// }
//
export const register = (params) => {
    return axios.post(host_1 + `login/register`, params)
}

export const setRecommends = (params) => {
    return axios.get(host_2 +`recommend/renews`, params)
}

export const updateRecommends = (params) => {
    return axios.post(host_2 + `recommend/update`, params)
}
