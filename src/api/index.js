import axios from "axios";

let host_1 = 'https://gc.caohongchuan.top:8080';
// let host_2 = 'http://gc.caohongchuan.top:7788/';

export const getSearch = (params) => {
    return axios.get(host_1 +`/search/querynews/?query=${params}`)
}
export const updateRecords = (params) => {
    return axios.put(host_1 +`/search/viewrecord`, params)
}

export const register = (params) => {
    return axios.post(host_1 + `/login/register`, params)
}

export const login = (params) => {
    return axios.post(host_1 +`/recommend/renews`, params)
}

export const updateRecommends = () => {
    return axios.get(host_1 + `/recommend/update`)
}
export const getAllCountries = () => {
    return axios.get(host_1 + `/search/getcountry`)
}
export const getAllThemeCountries = () => {
    return axios.get(host_1 + `/search/getcountytheme`)
}
export const getAllTheme = () => {
    return axios.get(host_1 + `/search/gettheme`)
}
